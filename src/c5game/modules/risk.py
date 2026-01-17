"""Risk scoring module."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .analysis import RecipeCandidate


@dataclass(frozen=True)
class RiskScore:
    recipe: RecipeCandidate
    score: float
    half_kelly: float
    sortino: float
    roi: float


class RiskScorer:
    def __init__(self, min_score: float = 0.0) -> None:
        self.min_score = min_score

    def score(self, candidates: List[RecipeCandidate], expected_returns: List[float]) -> List[RiskScore]:
        scored: List[RiskScore] = []
        for candidate, expected_return in zip(candidates, expected_returns, strict=False):
            roi = expected_return / max(candidate.total_cost, 1e-9)
            half_kelly = max(0.0, roi / 2.0)
            sortino = roi / max(candidate.wear_gap, 1e-6)
            composite = 0.5 * roi + 0.3 * sortino + 0.2 * half_kelly
            scored.append(RiskScore(recipe=candidate, score=composite, half_kelly=half_kelly, sortino=sortino, roi=roi))
        return [item for item in scored if item.score >= self.min_score]

    def rank(self, scores: List[RiskScore]) -> List[RiskScore]:
        return sorted(scores, key=lambda s: s.score, reverse=True)
