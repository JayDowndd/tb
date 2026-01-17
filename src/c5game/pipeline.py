"""Pipeline orchestrating all modules."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from .api_client import ApiClient
from .config import AccountConfig, StrategyConfig, SystemConfig
from .rate_limit import RateLimiter
from .modules.analysis import GreedyOptimizer, LinearPlanner, WearNormalizer
from .modules.data_collection import DataCollector
from .modules.inventory import InventoryManager
from .modules.risk import RiskScorer
from .modules.trading import Trader


@dataclass
class AccountRuntime:
    account: AccountConfig
    api_client: ApiClient
    inventory: InventoryManager
    trader: Trader
    collector: DataCollector
    limiter: RateLimiter


class Pipeline:
    def __init__(self, config: SystemConfig) -> None:
        self.config = config
        self.accounts = self._build_accounts()
        self.normalizer = WearNormalizer()
        self.greedy = GreedyOptimizer()
        self.planner = LinearPlanner()

    def _build_accounts(self) -> Dict[str, AccountRuntime]:
        runtimes: Dict[str, AccountRuntime] = {}
        for account in self.config.accounts:
            limiter = RateLimiter(default_qps=account.default_qps, endpoint_qps=account.endpoint_qps)
            api_client = ApiClient(base_url=account.base_url, app_key=account.app_key, limiter=limiter)
            runtime = AccountRuntime(
                account=account,
                api_client=api_client,
                inventory=InventoryManager(api_client, self.config.inventory_endpoint),
                trader=Trader(api_client, self.config.order_endpoint),
                collector=DataCollector(api_client, self.config.material_endpoint),
                limiter=limiter,
            )
            runtimes[account.name] = runtime
        return runtimes

    def run_strategy(self, account_name: str, strategy: StrategyConfig) -> List[dict]:
        runtime = self.accounts[account_name]
        materials = runtime.collector.fetch_materials()
        normalized = self.normalizer.normalize(materials)
        greedy_candidate = self.greedy.build_candidate(normalized, strategy.target_wear, strategy.recipe_size)
        refined = self.planner.refine(greedy_candidate, normalized)
        expected_returns = [refined.total_cost * 0.05]
        scorer = RiskScorer(min_score=strategy.min_score)
        scored = scorer.rank(scorer.score([refined], expected_returns))
        if not scored:
            return []
        recipes = [score.recipe for score in scored]
        results = runtime.trader.submit_batch(recipes)
        return [{"success": result.success, "response": result.response} for result in results]
