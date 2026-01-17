"""Automated trading module."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List

from ..api_client import ApiClient
from .analysis import RecipeCandidate


@dataclass(frozen=True)
class TradeResult:
    recipe: RecipeCandidate
    success: bool
    response: Dict[str, Any]


class Trader:
    def __init__(self, api_client: ApiClient, order_endpoint: str) -> None:
        self.api_client = api_client
        self.order_endpoint = order_endpoint

    def submit_recipe(self, recipe: RecipeCandidate, extra_payload: Dict[str, Any] | None = None) -> TradeResult:
        payload = {
            "materials": [m.material_id for m in recipe.materials],
            "targetWear": recipe.target_wear,
            "totalCost": recipe.total_cost,
        }
        if extra_payload:
            payload.update(extra_payload)
        response = self.api_client.post(self.order_endpoint, payload)
        success = bool(response.get("success", False))
        return TradeResult(recipe=recipe, success=success, response=response)

    def submit_batch(self, recipes: List[RecipeCandidate]) -> List[TradeResult]:
        results = []
        for recipe in recipes:
            results.append(self.submit_recipe(recipe))
        return results
