"""Inventory management module."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from ..api_client import ApiClient


@dataclass
class InventoryState:
    items: Dict[str, int]
    raw: Dict[str, Any]


class InventoryManager:
    def __init__(self, api_client: ApiClient, inventory_endpoint: str) -> None:
        self.api_client = api_client
        self.inventory_endpoint = inventory_endpoint

    def refresh(self) -> InventoryState:
        response = self.api_client.get(self.inventory_endpoint)
        data = response.get("data", {}) or {}
        items = {str(item.get("id", "")): int(item.get("count", 0)) for item in data.get("items", [])}
        return InventoryState(items=items, raw=data)

    def reserve(self, state: InventoryState, material_id: str, amount: int) -> bool:
        current = state.items.get(material_id, 0)
        if current < amount:
            return False
        state.items[material_id] = current - amount
        return True
