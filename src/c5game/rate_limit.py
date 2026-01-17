"""Token bucket rate limiter with per-endpoint overrides."""

from dataclasses import dataclass
import time


@dataclass
class TokenBucket:
    capacity: float
    refill_rate: float
    tokens: float
    last_refill: float

    def refill(self) -> None:
        now = time.monotonic()
        elapsed = now - self.last_refill
        if elapsed <= 0:
            return
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now

    def consume(self, amount: float = 1.0) -> bool:
        self.refill()
        if self.tokens >= amount:
            self.tokens -= amount
            return True
        return False


class RateLimiter:
    def __init__(self, default_qps: float, endpoint_qps: dict[str, float] | None = None) -> None:
        self.default_qps = default_qps
        self.endpoint_qps = endpoint_qps or {}
        self.buckets: dict[str, TokenBucket] = {}

    def _bucket_for(self, endpoint: str) -> TokenBucket:
        if endpoint in self.buckets:
            return self.buckets[endpoint]
        qps = self.endpoint_qps.get(endpoint, self.default_qps)
        bucket = TokenBucket(capacity=qps, refill_rate=qps, tokens=qps, last_refill=time.monotonic())
        self.buckets[endpoint] = bucket
        return bucket

    def wait_for_slot(self, endpoint: str, amount: float = 1.0, sleep_s: float = 0.05) -> None:
        bucket = self._bucket_for(endpoint)
        while not bucket.consume(amount):
            time.sleep(sleep_s)
