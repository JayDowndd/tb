# C5GAME OpenDoc System Design (Public Info Based)

## Public doc constraints & integration notes

The publicly visible guide indicates the following integration constraints:

- All requests require an `app-key` in the query string. Example usage is shown as `https://openapi.c5game.com?app-key=appkey-example`. The `app-key` is obtained from the user center API management page. (Doc guide, “前提条件”)
- Default rate limit is **50 QPS**, with some interfaces having their own special limits (“限流说明”).
- A notice on the doc page shows a temporary stricter QPS limit for “在售列表查询”: normal users 1 request per 300s, whitelisted users 10 requests per 10s.
- Service base URL: `https://openapi.c5game.com` with HTTPS-only communication; requests are GET/POST depending on endpoint; UTF-8 encoding; no signature mechanism is currently required.

**Reference text excerpted from the public guide (for traceability):**

```
前提条件: app-key ...  https://openapi.c5game.com?app-key=appkey-example
限流说明: 默认限流次数为50qps
通知: 在售列表查询 qps 限流 ... 普通用户 300s 1 次 ... 白名单用户 10s 10次
服务地址: https://openapi.c5game.com
通信协议: HTTPS
请求方式: GET / POST
字符编码: UTF-8
签名机制: 目前无
```

## Public doc pages (from sitemap)

The public sitemap lists 2 doc pages:

- https://opendoc.c5game.com/doc-3014376
- https://opendoc.c5game.com/doc-5007280

## Public API page list (from sitemap)

The public sitemap lists 30 API pages. These represent the accessible API documentation surface:

- https://opendoc.c5game.com/api-104138428
- https://opendoc.c5game.com/api-104138430
- https://opendoc.c5game.com/api-104138431
- https://opendoc.c5game.com/api-104138441
- https://opendoc.c5game.com/api-111917012
- https://opendoc.c5game.com/api-111917782
- https://opendoc.c5game.com/api-111917784
- https://opendoc.c5game.com/api-112234466
- https://opendoc.c5game.com/api-125914570
- https://opendoc.c5game.com/api-153195179
- https://opendoc.c5game.com/api-161954984
- https://opendoc.c5game.com/api-181496279
- https://opendoc.c5game.com/api-181508072
- https://opendoc.c5game.com/api-184817384
- https://opendoc.c5game.com/api-184827891
- https://opendoc.c5game.com/api-206715572
- https://opendoc.c5game.com/api-211629706
- https://opendoc.c5game.com/api-220748356
- https://opendoc.c5game.com/api-220765280
- https://opendoc.c5game.com/api-221209660
- https://opendoc.c5game.com/api-225781321
- https://opendoc.c5game.com/api-237960928
- https://opendoc.c5game.com/api-304298359
- https://opendoc.c5game.com/api-304306656
- https://opendoc.c5game.com/api-319091711
- https://opendoc.c5game.com/api-319094040
- https://opendoc.c5game.com/api-347610797
- https://opendoc.c5game.com/api-354331322
- https://opendoc.c5game.com/api-354375293
- https://opendoc.c5game.com/api-354392712

## Public schema pages (from sitemap)

The public sitemap lists 106 schema pages. These represent the documented data models:

- https://opendoc.c5game.com/schema-57203592
- https://opendoc.c5game.com/schema-57203593
- https://opendoc.c5game.com/schema-57203594
- https://opendoc.c5game.com/schema-57203595
- https://opendoc.c5game.com/schema-57203596
- https://opendoc.c5game.com/schema-57203597
- https://opendoc.c5game.com/schema-57203598
- https://opendoc.c5game.com/schema-57203599
- https://opendoc.c5game.com/schema-57203600
- https://opendoc.c5game.com/schema-57203601
- https://opendoc.c5game.com/schema-57203602
- https://opendoc.c5game.com/schema-57203603
- https://opendoc.c5game.com/schema-57203604
- https://opendoc.c5game.com/schema-57203605
- https://opendoc.c5game.com/schema-57203606
- https://opendoc.c5game.com/schema-57203607
- https://opendoc.c5game.com/schema-57203608
- https://opendoc.c5game.com/schema-57203609
- https://opendoc.c5game.com/schema-57203610
- https://opendoc.c5game.com/schema-57203611
- https://opendoc.c5game.com/schema-57203612
- https://opendoc.c5game.com/schema-57203613
- https://opendoc.c5game.com/schema-57203614
- https://opendoc.c5game.com/schema-57203615
- https://opendoc.c5game.com/schema-57203616
- https://opendoc.c5game.com/schema-57203617
- https://opendoc.c5game.com/schema-57203618
- https://opendoc.c5game.com/schema-57203619
- https://opendoc.c5game.com/schema-57203620
- https://opendoc.c5game.com/schema-57203621
- https://opendoc.c5game.com/schema-57203622
- https://opendoc.c5game.com/schema-57203623
- https://opendoc.c5game.com/schema-57203624
- https://opendoc.c5game.com/schema-57203625
- https://opendoc.c5game.com/schema-57203626
- https://opendoc.c5game.com/schema-57203627
- https://opendoc.c5game.com/schema-57203628
- https://opendoc.c5game.com/schema-57203629
- https://opendoc.c5game.com/schema-57203630
- https://opendoc.c5game.com/schema-57203631
- https://opendoc.c5game.com/schema-57203632
- https://opendoc.c5game.com/schema-57203633
- https://opendoc.c5game.com/schema-57203634
- https://opendoc.c5game.com/schema-57203635
- https://opendoc.c5game.com/schema-57203636
- https://opendoc.c5game.com/schema-57203637
- https://opendoc.c5game.com/schema-57203638
- https://opendoc.c5game.com/schema-57203639
- https://opendoc.c5game.com/schema-57203640
- https://opendoc.c5game.com/schema-57203641
- https://opendoc.c5game.com/schema-57203642
- https://opendoc.c5game.com/schema-57203643
- https://opendoc.c5game.com/schema-57203644
- https://opendoc.c5game.com/schema-57203645
- https://opendoc.c5game.com/schema-57203646
- https://opendoc.c5game.com/schema-57203647
- https://opendoc.c5game.com/schema-57203648
- https://opendoc.c5game.com/schema-57203649
- https://opendoc.c5game.com/schema-57203650
- https://opendoc.c5game.com/schema-57203651
- https://opendoc.c5game.com/schema-57203652
- https://opendoc.c5game.com/schema-57203653
- https://opendoc.c5game.com/schema-57203654
- https://opendoc.c5game.com/schema-57203655
- https://opendoc.c5game.com/schema-57203656
- https://opendoc.c5game.com/schema-57203657
- https://opendoc.c5game.com/schema-57203658
- https://opendoc.c5game.com/schema-57203659
- https://opendoc.c5game.com/schema-57203660
- https://opendoc.c5game.com/schema-57203661
- https://opendoc.c5game.com/schema-57203662
- https://opendoc.c5game.com/schema-57203663
- https://opendoc.c5game.com/schema-57203664
- https://opendoc.c5game.com/schema-57203665
- https://opendoc.c5game.com/schema-57203666
- https://opendoc.c5game.com/schema-57203667
- https://opendoc.c5game.com/schema-57203668
- https://opendoc.c5game.com/schema-57203669
- https://opendoc.c5game.com/schema-57203670
- https://opendoc.c5game.com/schema-57203671
- https://opendoc.c5game.com/schema-57203672
- https://opendoc.c5game.com/schema-57203673
- https://opendoc.c5game.com/schema-57203674
- https://opendoc.c5game.com/schema-57203675
- https://opendoc.c5game.com/schema-57203676
- https://opendoc.c5game.com/schema-57203677
- https://opendoc.c5game.com/schema-57203678
- https://opendoc.c5game.com/schema-57203679
- https://opendoc.c5game.com/schema-57203680
- https://opendoc.c5game.com/schema-57203681
- https://opendoc.c5game.com/schema-57203682
- https://opendoc.c5game.com/schema-57203683
- https://opendoc.c5game.com/schema-57203684
- https://opendoc.c5game.com/schema-57203685
- https://opendoc.c5game.com/schema-57203686
- https://opendoc.c5game.com/schema-57203687
- https://opendoc.c5game.com/schema-61702561
- https://opendoc.c5game.com/schema-61702562
- https://opendoc.c5game.com/schema-61702563
- https://opendoc.c5game.com/schema-61702564
- https://opendoc.c5game.com/schema-61702565
- https://opendoc.c5game.com/schema-61702566
- https://opendoc.c5game.com/schema-61705710
- https://opendoc.c5game.com/schema-61705711
- https://opendoc.c5game.com/schema-61705712
- https://opendoc.c5game.com/schema-61877965

## System design overview (multi-strategy + multi-account)

### Module 1: Data Collection
**Goal:** Pull market material data through OpenAPI and normalize it for downstream use.

- **Input:** Market material endpoints (from the public API list above).
- **Output:** Cleaned material dataset with timestamps and quality signals.
- **Key constraints:** Rate limits (default 50 QPS) and endpoint-specific limits (e.g., in-sale list QPS reduction).
- **Implementation notes:**
  - Per-account throttling and shared global throttling.
  - Snapshot storage for backtests and drift detection.

### Module 2: Data Analysis & Pairing
**Goal:** Create a normalized “wear” library and compute minimum-cost recipes.

- **Normalization:** Convert raw wear values into a standardized 0–1 scale.
- **Optimization:**
  - **Greedy search** to generate candidate recipes quickly.
  - **Linear programming** to compute minimum cost for target wear output.
- **Outputs:** Candidate recipe list with material composition, cost, and target wear match score.

### Module 3: Automated Trading
**Goal:** Execute qualified recipes via OpenAPI.

- **Inputs:** Approved recipes from the risk control module.
- **Execution flow:**
  - Validate inventory & balance.
  - Place order(s) through API.
  - Monitor order status; retry or rollback on failure.
- **Safety:** Idempotent requests, account-level order locks, and max-spend guards.

### Module 4: Risk Control
**Goal:** Score recipes and filter candidates before execution.

- **Metrics:** Half-Kelly sizing, Sortino ratio, ROI-weighted scoring.
- **Decision logic:**
  - Compute composite score per recipe.
  - Apply thresholds by account & strategy.
  - Send only top-ranked recipes to trading.

### Module 5: Inventory Management
**Goal:** Maintain safe, consistent asset state across accounts.

- **Functions:**
  - Real-time inventory refresh.
  - Asset reservation for pending orders.
  - Reconciliation with trading outcomes.

## Multi-strategy & multi-account architecture

- **Account abstraction:** Each account has its own API key, limits, balances, and risk profile.
- **Strategy isolation:** Strategy runner processes operate independently but publish to a shared event bus.
- **Scheduler:** Weighted fair queue that respects per-account QPS limits and per-endpoint caps.
- **Security:** Encrypted API key storage, short-lived access tokens for runtime, audit logging for each API call.

## Recommended next steps

1. Map each required function to the specific API pages above (e.g., material list, listings, order create, order status, inventory).
2. Confirm all endpoint-specific QPS caps for high-frequency calls.
3. Provide target wear calculation rules to finalize normalization and LP formulation.
