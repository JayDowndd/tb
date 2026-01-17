"""Configuration models for accounts and strategies."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(frozen=True)
class AccountConfig:
    name: str
    app_key: str
    base_url: str = "https://openapi.c5game.com"
    default_qps: float = 50.0
    endpoint_qps: Dict[str, float] = field(default_factory=dict)


@dataclass(frozen=True)
class StrategyConfig:
    name: str
    target_wear: float
    max_cost: Optional[float] = None
    min_score: float = 0.0
    recipe_size: int = 10


@dataclass(frozen=True)
class SystemConfig:
    accounts: List[AccountConfig]
    strategies: List[StrategyConfig]
    material_endpoint: str
    order_endpoint: str
    inventory_endpoint: str
