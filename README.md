# tb

Starter implementation for a C5GAME OpenAPI automation pipeline.

## Structure

- `src/c5game/modules/data_collection.py`: pulls market material data through OpenAPI.
- `src/c5game/modules/analysis.py`: normalizes wear values and computes recipe candidates.
- `src/c5game/modules/risk.py`: half-Kelly, Sortino, and ROI composite scoring.
- `src/c5game/modules/trading.py`: submits recipes via OpenAPI.
- `src/c5game/modules/inventory.py`: inventory refresh and reservation.
- `src/c5game/pipeline.py`: orchestration across modules, accounts, and strategies.

## Quick start (skeleton)

```bash
PYTHONPATH=src python - <<'PY'
from c5game import AccountConfig, StrategyConfig, SystemConfig, Pipeline

config = SystemConfig(
    accounts=[
        AccountConfig(
            name="primary",
            app_key="YOUR_APP_KEY",
            endpoint_qps={
                "/market/listing": 0.0033,  # example: 1 request / 300s
            },
        )
    ],
    strategies=[
        StrategyConfig(name="target_wear_0.12", target_wear=0.12, min_score=0.5),
    ],
    material_endpoint="/market/materials",
    order_endpoint="/orders/create",
    inventory_endpoint="/inventory/list",
)

pipeline = Pipeline(config)
results = pipeline.run_strategy("primary", config.strategies[0])
print(results)
PY
```

> Replace endpoints with the concrete ones from the OpenDoc API pages.
