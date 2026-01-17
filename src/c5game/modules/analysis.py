"""Data analysis and pairing module."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence

from .data_collection import MarketMaterial


@dataclass(frozen=True)
class RecipeCandidate:
    materials: List[MarketMaterial]
    total_cost: float
    mean_wear: float
    target_wear: float

    @property
    def wear_gap(self) -> float:
        return abs(self.target_wear - self.mean_wear)


class WearNormalizer:
    def normalize(self, materials: Sequence[MarketMaterial]) -> List[MarketMaterial]:
        if not materials:
            return []
        wears = [m.wear for m in materials]
        min_wear = min(wears)
        max_wear = max(wears)
        span = max(max_wear - min_wear, 1e-9)
        normalized = []
        for material in materials:
            normalized_wear = (material.wear - min_wear) / span
            normalized.append(
                MarketMaterial(
                    material_id=material.material_id,
                    name=material.name,
                    price=material.price,
                    wear=normalized_wear,
                    extra=material.extra,
                )
            )
        return normalized


class GreedyOptimizer:
    def build_candidate(self, materials: Sequence[MarketMaterial], target_wear: float, recipe_size: int) -> RecipeCandidate:
        sorted_materials = sorted(materials, key=lambda m: abs(m.wear - target_wear))
        selected = list(sorted_materials[:recipe_size])
        if not selected:
            return RecipeCandidate(materials=[], total_cost=0.0, mean_wear=0.0, target_wear=target_wear)
        total_cost = sum(m.price for m in selected)
        mean_wear = sum(m.wear for m in selected) / len(selected)
        return RecipeCandidate(materials=selected, total_cost=total_cost, mean_wear=mean_wear, target_wear=target_wear)


class LinearPlanner:
    """Placeholder optimizer that refines the greedy candidate.

    The implementation uses a simple local swap search to avoid external solver dependencies.
    """

    def refine(self, base: RecipeCandidate, pool: Sequence[MarketMaterial]) -> RecipeCandidate:
        if not base.materials:
            return base
        best = base
        for candidate in pool:
            for idx, current in enumerate(best.materials):
                if candidate.price > current.price and abs(candidate.wear - best.target_wear) >= abs(current.wear - best.target_wear):
                    continue
                swapped = list(best.materials)
                swapped[idx] = candidate
                total_cost = sum(m.price for m in swapped)
                mean_wear = sum(m.wear for m in swapped) / len(swapped)
                refined = RecipeCandidate(materials=swapped, total_cost=total_cost, mean_wear=mean_wear, target_wear=best.target_wear)
                if refined.total_cost < best.total_cost or refined.wear_gap < best.wear_gap:
                    best = refined
        return best
