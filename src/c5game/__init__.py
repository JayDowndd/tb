"""Core package for C5GAME automation pipeline."""

from .config import AccountConfig, StrategyConfig, SystemConfig
from .pipeline import Pipeline

__all__ = ["AccountConfig", "StrategyConfig", "SystemConfig", "Pipeline"]
