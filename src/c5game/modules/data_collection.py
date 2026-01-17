"""Market data ingestion module."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List

from ..api_client import ApiClient


@dataclass(frozen=True)
class MarketMaterial:
    material_id: str
    name: str
    price: float
    wear: float
    extra: Dict[str, Any]


class DataCollector:
    def __init__(self, api_client: ApiClient, endpoint: str) -> None:
        self.api_client = api_client
        self.endpoint = endpoint

    def fetch_materials(self, params: Dict[str, Any] | None = None) -> List[MarketMaterial]:
        response = self.api_client.get(self.endpoint, params=params)
        data = response.get("data", []) or []
        return [self._to_material(item) for item in data]

    def _to_material(self, item: Dict[str, Any]) -> MarketMaterial:
        return MarketMaterial(
            material_id=str(item.get("id", "")),
            name=str(item.get("name", "")),
            price=float(item.get("price", 0.0)),
            wear=float(item.get("wear", 0.0)),
            extra={k: v for k, v in item.items() if k not in {"id", "name", "price", "wear"}},
        )

    def flatten_batches(self, batches: Iterable[List[MarketMaterial]]) -> List[MarketMaterial]:
        materials: List[MarketMaterial] = []
        for batch in batches:
            materials.extend(batch)
        return materials
