"""Minimal HTTP client for C5GAME OpenAPI calls."""

from __future__ import annotations

import json
from typing import Any, Dict, Optional
from urllib import parse, request

from .rate_limit import RateLimiter


class ApiClient:
    def __init__(self, base_url: str, app_key: str, limiter: RateLimiter) -> None:
        self.base_url = base_url.rstrip("/")
        self.app_key = app_key
        self.limiter = limiter

    def _build_url(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> str:
        params = params or {}
        params["app-key"] = self.app_key
        query = parse.urlencode(params)
        return f"{self.base_url}{endpoint}?{query}"

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        self.limiter.wait_for_slot(endpoint)
        url = self._build_url(endpoint, params)
        with request.urlopen(url, timeout=30) as response:
            payload = response.read().decode("utf-8")
        return json.loads(payload)

    def post(self, endpoint: str, payload: Dict[str, Any], params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        self.limiter.wait_for_slot(endpoint)
        url = self._build_url(endpoint, params)
        data = json.dumps(payload).encode("utf-8")
        req = request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with request.urlopen(req, timeout=30) as response:
            body = response.read().decode("utf-8")
        return json.loads(body)
