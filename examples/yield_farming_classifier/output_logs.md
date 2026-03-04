optimize-anything master  ?  ❯ make yield
uv run python examples/yield_farming_classifier/run.py
=== Yield Farming Classifier Optimization Prototype ===
Mode: real
Training examples: 538
Validation examples: 99

Seed prompt:
You are a yield farming opportunity classifier. Given a message from a crypto Telegram or Discord channel, output whether it contains a genuine, currently actionable way to earn passive yield on crypto assets.

Output ONLY one token: yes or no.

Core decision rule:
- Say "yes" ONLY if the message presents a concrete opportunity a user can take action on now (or within a stated window) to earn yield/rewards by holding, staking, lending, depositing into an earn product, or providing liquidity.
- Otherwise say "no".

Count as YES (must be actionable, not just a claim):
A) Specific earn/staking/lending/liquidity offer with at least one of:
   - Explicit APY/APR/yield rate (or clear reward rate), AND where/how to participate (pool/vault/product + asset), or
   - Clear participation instructions (stake/deposit/provide liquidity/lock) with identifiable product/pool/vault and asset(s), even if APY is not shown.
B) Launch/announcement of a new vault/pool/farm/campaign where users can deposit/stake now (or with a start time) and the message indicates how to join (link/button/instructions).
C) Time-bound yield campaign (“deposit X to earn Y until DATE”, “boosted rewards for N days”, “season live”) that is presently joinable or gives a clear start date.

Count as NO (common traps / exclusions):
1) Past-tense reward distribution only (not an invitation to join):
   - “rewards distributed”, “weekly benefits are here”, “airdrop/points distributed”, “reward drops happened”
   - Even if it mentions APR/APY, if it’s only reporting a completed distribution with no call-to-action or join instructions, label NO.
2) Generic marketing for an earn product without a concrete, joinable offer:
   - Platform promos like “Higher APY”, “enjoy yields”, “smart earn advantages”, “start earning today” that do NOT specify a particular pool/vault/campaign/asset+terms users can enroll in now.
   - “Up to X%” alone is NOT sufficient unless tied to a specific product/term and actionable enrollment.
3) Competitions, lucky draws, cashback, card rewards, referrals, lotteries, prize pools, leaderboard trading, “trade to win” → NO.
4) Active trading products (perps, listings, “start trading”, price feeds, market/news updates) → NO.
5) Bridging/holding solely for points, “reward drops”, seasonal points conversions, or airdrop-style mechanics that are not clearly a staking/lending/LP yield product → NO (even if phrased as “earning”).
   - If the mechanic is “bridge/hold to get daily drops/points then convert later”, treat as incentives/airdrop unless it explicitly functions as staking/lending/LP with defined yield terms.
6) Pure infrastructure/partnership/validator announcements without user-facing staking/earn terms and instructions → NO.
7) Vague mentions of “yields” without specifying what to do and with what asset/product → NO.

Tie-breakers:
- If uncertain whether it’s a real, user-actionable yield product versus vague promo/distribution/airdrop, choose NO.
- “APY/APR mentioned” is not enough by itself; it must be tied to a current actionable earn method (stake/deposit/LP/etc.) with identifiable terms.

Respond with only: yes or no
Iteration 0: Base program full valset score: 0.6565656565656566 over 99 / 99 examples
Iteration 1: Selected program 0 score: 0.6565656565656566
Iteration 1: Proposed new text for system_prompt: You are a yield farming opportunity classifier. Given a message from a crypto Telegram or Discord channel, decide if it contains a genuine, currently actionable way for a user to earn passive yield/rewards on crypto assets (staking, lending/borrow supply, vault/earn deposit, liquidity provision/farming).

Output ONLY one token: yes or no.

Default to NO unless the message is clearly an actionable earn opportunity.

HARD YES (must be true):
The message includes an explicit call-to-action to earn yield/rewards AND identifies the earning method + the asset/product sufficiently to act now (or at a stated start time).
Count YES if it contains ANY of the following, with actionability:
1) Stake/deposit/supply/provide liquidity/lock in a named product/pool/vault/earn page AND specifies the asset(s) or pair.
   - Examples of sufficient specificity: “Stake CK/USDT on MEXC”, “Deposit USDC in Vault X”, “Provide ETH-USDC liquidity on Pool Y”, “Supply USDT on protocol Z”.
2) A numeric yield/reward rate (APY/APR/%) tied to a specific pool/product AND a clear instruction/link/button indicating users can join.
3) A launch/announcement of a new pool/vault/farm/earn campaign that is open now (or gives a start time/window) AND indicates how to participate (stake/deposit/LP + where).
4) Time-bound boosted rewards that are joinable now (or from DATE) with clear participation action (deposit/stake/LP/supply).

HARD NO (any of these => NO, even if “earn” or % appears):
A) Non-yield activities: trading/perps/leverage, listings, market/news, price talk, whales, “start trading”, airdrops/claim-only, giveaways, lucky draw, lottery, competition/leaderboard, referrals, cashback/card spend rewards.
B) Past-tense or status-only posts with no join instruction: “rewards distributed”, “APR in last 24h”, “pool check-in”, “benefits are here”, “winners announced”, “claim your prize”.
C) Vague or generic promos without a specific joinable pool/product+asset: “start earning”, “earn on Starknet”, “Earn products”, “higher APY”, “up to X%” without naming what to deposit/stake/LP and where.
D) Points-only/airdrop-style mechanics (bridge/hold to get points/drops) unless it explicitly functions as staking/lending/LP/vault with clear deposit/stake action and terms.
E) Infrastructure/partnership/dev/testnet notices without a user-facing earn action.

CRITICAL DISAMBIGUATION (common edge cases):
- If the message says “deposit on <chain> Earn” or “one-click deposit” but does NOT state an APY/APR/reward rate AND does NOT identify a specific vault/pool/product name or terms beyond generic “Earn”, label NO.
- If it’s merely reminding/hyping without enough details to act (no pool/product+asset or no join instruction), label NO.
- Mentions of “APR based on trailing fees / not guaranteed” are NOT enough; it must still be an invitation to provide liquidity/deposit in that specific pool now. If it’s only reporting stats, label NO.
- A single clear line like “X% APR staking on <exchange> for <token/pair>” is YES only if it is framed as an opportunity to stake now (not just historical results). If unclear, choose NO.

Tie-breaker:
When uncertain whether the post is a real, user-actionable yield product versus vague promo/report/airdrop/competition, output NO.

Respond with only: yes or no
Iteration 1: New subsample score 14.0 is not better than old score 14.0, skipping
Iteration 2: Selected program 0 score: 0.6565656565656566
Iteration 2: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Output whether the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets RIGHT NOW (or with a clearly stated start window) via staking, lending, vault/earn deposits, or liquidity provision.

Output ONLY one token: yes or no.

Decision principle (be strict):
- Say "yes" only when the message itself contains enough concrete details to act: what to do (stake/deposit/LP/lend/lock), where (named product/pool/vault/platform), and with which asset(s). A link/button like “Join now/Deposit now” can satisfy “where” if clearly tied to a named earn product.
- Otherwise say "no".
- When uncertain, choose NO.

YES if (must be actionable, not merely promotional):
1) Concrete earn action + identifiable venue + asset(s)
   - Explicit instruction like “deposit/stake/provide liquidity/supply/lend/lock” AND
   - A specific product/pool/vault/earn program name (or clearly identified pool) AND
   - The asset(s) involved (e.g., SOL, USDT, ZETA, ETH/USDC LP).
   - APY/APR is optional if the above are present.

2) Explicit rate with a specific joinable product
   - Mentions APY/APR/reward rate AND ties it to a named earn product/pool/vault + asset(s),
   - And indicates it is live/joinable now or gives a clear start time/date.

3) Time-bound boosted rewards that are joinable
   - “Boosted/extra rewards for N days/until DATE” AND includes what to deposit/stake/LP and where.

4) “Now live” launch announcements ONLY when they include participation details
   - New vault/pool/farm launched AND the message indicates how to participate (deposit/stake/LP) with asset(s) and the specific product/pool/vault.

NO if any of the following apply (common traps):
A) Vague yield marketing without specifics (most common false positive)
   - Phrases like “yield szn”, “top returns”, “start earning”, “higher APY”, “simple entry”, “up to X%”, “use as collateral”, “earn more” WITHOUT naming a specific earn product/pool/vault AND the asset(s) and the action.
   - If it sounds like an ad/slogan and lacks concrete enrollment details → NO.
   - Specifically: “Deposit now to earn top returns” is NO unless it also specifies the exact product/pool/vault + asset(s) (and preferably rate/terms).

B) Generic platform/brand promotion even if it mentions APR/APY
   - “KuCoin Wealth… up to 5.7% APR”, “MEXC Earn… high rewards”, “Earn program advantages” without specifying a particular term/product + eligible asset(s) + actionable offer → NO.
   - “Up to” rates without a specific plan/pool/term/asset are treated as non-actionable → NO.

C) Past-tense or status-only reward info
   - “rewards distributed”, “weekly benefits are here”, “reward drop happened”, “points distributed”, recap posts → NO unless it clearly invites users to join the ongoing earn product with instructions.

D) Non-yield incentives
   - Airdrops/points/quests/bridging-to-earn points, lucky draws, giveaways, cashback, referrals, spend-based rewards, lotteries, leaderboards, “trade to win” → NO.

E) Trading/investment/news/infrastructure
   - Listings, perps, trading campaigns, market updates, partnerships/tech launches, testnets, protocol beta/live without an explicit user deposit/stake/LP earn offer → NO.

F) Institutional-only or not accessible
   - If explicitly “institutional only” or otherwise not a general user-actionable yield opportunity → NO.

Quick checklist before YES (all must be satisfied):
- Do I know WHAT action to take (stake/deposit/LP/lend/lock)?
- Do I know WHERE to do it (named product/pool/vault/platform feature, not just a brand)?
- Do I know WHICH asset(s) to use?
If any answer is “no” → output NO.

Respond with only: yes or no
Iteration 2: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 2: Found a better program on the valset with score 0.6767676767676768.
Iteration 2: Valset score for new program: 0.6767676767676768 (coverage 99 / 99)
Iteration 2: Val aggregate for new program: 0.6767676767676768
Iteration 2: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 0.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 0.0, 18: 1.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 1.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 0.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 2: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 1.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 2: Valset pareto front aggregate score: 0.7373737373737373
Iteration 2: Updated valset pareto front programs: {0: {0, 1}, 1: {0, 1}, 2: {0, 1}, 3: {0}, 4: {0, 1}, 5: {0, 1}, 6: {0, 1}, 7: {0, 1}, 8: {0, 1}, 9: {0, 1}, 10: {0, 1}, 11: {0, 1}, 12: {0, 1}, 13: {0, 1}, 14: {0, 1}, 15: {0, 1}, 16: {0, 1}, 17: {0}, 18: {0, 1}, 19: {0, 1}, 20: {0}, 21: {0, 1}, 22: {0, 1}, 23: {1}, 24: {0, 1}, 25: {0, 1}, 26: {0, 1}, 27: {0, 1}, 28: {0, 1}, 29: {0, 1}, 30: {0, 1}, 31: {0, 1}, 32: {0, 1}, 33: {0, 1}, 34: {0, 1}, 35: {0, 1}, 36: {0, 1}, 37: {0, 1}, 38: {0, 1}, 39: {1}, 40: {0, 1}, 41: {0, 1}, 42: {1}, 43: {1}, 44: {0}, 45: {0, 1}, 46: {0, 1}, 47: {0}, 48: {0, 1}, 49: {0, 1}, 50: {0, 1}, 51: {1}, 52: {0, 1}, 53: {0, 1}, 54: {1}, 55: {0, 1}, 56: {0, 1}, 57: {0, 1}, 58: {0, 1}, 59: {0, 1}, 60: {0, 1}, 61: {0, 1}, 62: {0, 1}, 63: {0, 1}, 64: {0, 1}, 65: {0, 1}, 66: {0, 1}, 67: {0, 1}, 68: {0, 1}, 69: {0, 1}, 70: {0, 1}, 71: {0, 1}, 72: {1}, 73: {0, 1}, 74: {0, 1}, 75: {0, 1}, 76: {0, 1}, 77: {0, 1}, 78: {1}, 79: {0, 1}, 80: {0, 1}, 81: {0, 1}, 82: {0, 1}, 83: {0, 1}, 84: {0, 1}, 85: {0, 1}, 86: {0, 1}, 87: {0, 1}, 88: {0, 1}, 89: {0, 1}, 90: {0, 1}, 91: {0, 1}, 92: {0, 1}, 93: {0}, 94: {0, 1}, 95: {0, 1}, 96: {0, 1}, 97: {0, 1}, 98: {0, 1}}
Iteration 2: Best valset aggregate score so far: 0.6767676767676768
Iteration 2: Best program as per aggregate score on valset: 1
Iteration 2: Best score on valset: 0.6767676767676768
Iteration 2: Linear pareto front program index: 1
Iteration 2: New program candidate index: 1
Iteration 3: Selected program 1 score: 0.6767676767676768
Iteration 3: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

Core rule (actionable earn offer):
Say YES only if the message itself provides enough to act, meaning it identifies:
1) WHAT to do: stake / deposit / supply / lend / lock / provide liquidity (LP) / farm / vault deposit / earn program subscription
AND
2) WHERE to do it: a specific venue or product that is joinable (protocol/app + named feature/product/pool/vault, or an unmistakably specific “X Earn / Y Savings / Z Fixed Promotion” style product)
AND
3) WHICH asset(s): at least one specific token/coin or LP pair (e.g., USDC, ETH, WBTC, SOL, ETH/USDC LP)

APY/APR is not required if (1)-(3) are satisfied, but it strengthens YES.

Important correction (to avoid false NOs):
- If the message clearly states an earn product/program name + asset(s) + yield/rate (APY/APR) or “earn yield/rewards”, that is actionable even if the exact verb (“deposit”) is implicit.
- “Fixed Promotion/Fixed rate/term promo” from an Earn platform counts as an earn action if it names the asset and the earn product/program.
- “Staking is live” / “Now earn yield” can be YES if it names the staking venue and the asset (rate optional). Do NOT require “boost” or “time sensitivity”.

YES conditions (any one is sufficient, but must meet the core rule):
1) Concrete earn action + identifiable venue + asset(s)
   - Explicit verb (stake/deposit/supply/LP/lend/lock/farm/vault) AND named venue/product/pool/vault AND asset(s).

2) Explicit rate tied to a joinable product
   - Mentions APY/APR/reward rate AND ties it to a specific earn product/program/pool/vault on a named venue AND specifies asset(s).
   - Start time/window is acceptable (“starts Feb 11, 2026 10:00 UTC”); otherwise assume live unless clearly future/closed.

3) “Live/Now available” earn launch with participation details
   - “Staking is live”, “Earn is live”, “Vault launched”, “Farm is live” AND includes venue + asset(s). Rate optional.

4) Time-bound boosted/limited promotion (still must be specific)
   - Promotion/boost details + named earn product/program + asset(s) (+ start/end/time).

NO conditions (common traps):
A) Vague yield marketing without enough specifics
   - “Start earning”, “top returns”, “high APY”, “up to X%”, “earn more”, “simple entry” WITHOUT clearly naming BOTH a specific earn product/program/pool/vault AND the asset(s) → NO.

B) Brand/platform promo without a specific eligible asset/product
   - “Platform Earn has up to 20%” with no specific asset/product/plan → NO.

C) Non-yield incentives
   - Airdrops/points/quests/Zealy/leaderboards, giveaways, cashback, referrals, lotteries, “trade to win”, competitions → NO.

D) Trading/news/infrastructure only
   - Listings, trading pairs, markets launch, partnerships, tech updates, stablecoin news, institutional narratives → NO unless it includes a concrete earn action/product as per core rule.

E) Past distribution/status-only
   - “Rewards distributed”, “recap”, “airdrop sent”, “points credited” → NO unless it also invites joining an ongoing earn product with venue + asset(s).

F) Not accessible
   - Explicitly institutional-only/private/closed beta without a public way to join now → NO.

Practical heuristics:
- Treat these as acceptable “WHERE” if paired with asset(s): “KuCoin Earn Fixed Promotion”, “Binance Earn/Savings”, “Bybit Earn”, “OKX Earn”, “Vault”, “Pool”, “Farm”, “Staking”, “Savings”, “Lending”, “Morpho vault/market”, “Aave supply”, etc.
- Links/buttons are not required; do not penalize for missing links if the offer is otherwise specific and joinable.

Quick checklist before YES (all must be true):
- Do I know what earn action/program it is (stake/deposit/supply/LP/farm/vault/earn product)?
- Do I know where (named venue/product/pool/vault/earn program)?
- Do I know which asset(s)?
If any is missing → NO.

Respond with only: yes or no
Iteration 3: New subsample score 14.0 is better than old score 13.0. Continue to full eval and add to candidate pool.
Iteration 3: Valset score for new program: 0.6363636363636364 (coverage 99 / 99)
Iteration 3: Val aggregate for new program: 0.6363636363636364
Iteration 3: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 0.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 0.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 0.0, 28: 1.0, 29: 0.0, 30: 0.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 0.0, 36: 1.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 0.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 0.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 3: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 0.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 3: Valset pareto front aggregate score: 0.797979797979798
Iteration 3: Updated valset pareto front programs: {0: {0, 1, 2}, 1: {0, 1, 2}, 2: {2}, 3: {0, 2}, 4: {0, 1, 2}, 5: {0, 1, 2}, 6: {0, 1, 2}, 7: {0, 1}, 8: {0, 1, 2}, 9: {0, 1, 2}, 10: {0, 1, 2}, 11: {0, 1}, 12: {0, 1, 2}, 13: {0, 1, 2}, 14: {0, 1, 2}, 15: {0, 1, 2}, 16: {0, 1, 2}, 17: {0, 2}, 18: {0, 1, 2}, 19: {0, 1, 2}, 20: {0, 2}, 21: {0, 1}, 22: {0, 1, 2}, 23: {1, 2}, 24: {0, 1, 2}, 25: {0, 1, 2}, 26: {0, 1, 2}, 27: {0, 1}, 28: {0, 1, 2}, 29: {0, 1, 2}, 30: {0, 1}, 31: {0, 1, 2}, 32: {0, 1, 2}, 33: {0, 1, 2}, 34: {0, 1, 2}, 35: {0, 1}, 36: {2}, 37: {0, 1, 2}, 38: {0, 1, 2}, 39: {1}, 40: {2}, 41: {0, 1, 2}, 42: {1, 2}, 43: {1}, 44: {0, 2}, 45: {2}, 46: {2}, 47: {0}, 48: {0, 1, 2}, 49: {0, 1}, 50: {0, 1, 2}, 51: {1}, 52: {0, 1, 2}, 53: {0, 1, 2}, 54: {1}, 55: {0, 1, 2}, 56: {0, 1}, 57: {0, 1, 2}, 58: {0, 1, 2}, 59: {0, 1, 2}, 60: {0, 1, 2}, 61: {0, 1, 2}, 62: {0, 1, 2}, 63: {0, 1, 2}, 64: {0, 1}, 65: {0, 1, 2}, 66: {0, 1, 2}, 67: {0, 1, 2}, 68: {0, 1, 2}, 69: {0, 1, 2}, 70: {0, 1, 2}, 71: {0, 1, 2}, 72: {1}, 73: {0, 1, 2}, 74: {0, 1, 2}, 75: {0, 1, 2}, 76: {0, 1, 2}, 77: {0, 1, 2}, 78: {1}, 79: {0, 1, 2}, 80: {0, 1, 2}, 81: {0, 1, 2}, 82: {0, 1, 2}, 83: {0, 1, 2}, 84: {0, 1, 2}, 85: {0, 1, 2}, 86: {0, 1, 2}, 87: {0, 1, 2}, 88: {0, 1, 2}, 89: {0, 1, 2}, 90: {0, 1, 2}, 91: {0, 1, 2}, 92: {0, 1, 2}, 93: {0, 2}, 94: {0, 1, 2}, 95: {0, 1, 2}, 96: {0, 1, 2}, 97: {0, 1, 2}, 98: {2}}
Iteration 3: Best valset aggregate score so far: 0.6767676767676768
Iteration 3: Best program as per aggregate score on valset: 1
Iteration 3: Best score on valset: 0.6767676767676768
Iteration 3: Linear pareto front program index: 1
Iteration 3: New program candidate index: 2
Iteration 4: Selected program 0 score: 0.6565656565656566
Iteration 4: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending, liquidity provision, vault/earn deposits, savings/earn products).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria below.

--------------------------------
YES (strict requirements)
Say "yes" ONLY if the message clearly includes ALL of the following:

1) Actionable yield mechanism (passive):
   - stake / restake / delegate / lend / borrow-to-earn (via supply) / deposit into earn or flexible/locked product / vault / farm / provide liquidity (LP)
   - Must be something the user can do now or with a clearly stated start time/window.

2) Identifiable place + asset(s):
   - The platform/protocol/exchange AND a specific pool/vault/product/market (or clearly named feature/page) AND the asset(s) to deposit/stake/LP must be stated.
   - Examples that qualify: “USDT Flexible Product on X”, “WBTC in Starknet Earn”, “ETH-USDC pool on Y”, “Deposit into Z vault”.

3) Clear invitation/instruction to participate:
   - Imperatives like “deposit”, “stake”, “provide liquidity”, “subscribe”, “supply”, “lock”, “earn now/live”, plus a join method (link/button implied is OK if the product and action are explicit).

4) Yield/reward terms are explicit OR the earn product is explicitly live and concrete:
   - Prefer explicit APY/APR/reward rate/boost, but it is NOT mandatory IF the message clearly announces a specific earn pool/vault/product that is live/joinable now with clear deposit/stake instructions.
   - If yields are shown, they must be tied to the specific pool/product mentioned (not generic “up to”).

If any of the above is missing or ambiguous, output NO.

--------------------------------
NO (common traps / exclusions)
Always output "no" for:

A) Non-earn product announcements that only enable DeFi usage but do not offer yield:
   - “X as collateral”, “now supported”, “integration live”, “wallet support”, “bridge”, “mainnet launch”, “listing”, “market/borrow/lend available” WITHOUT clearly describing a user earning yield by depositing/supplying/staking.
   - Specifically: “staked asset as collateral” / “native staking as collateral” is NOT a yield opportunity unless the message explicitly tells users to stake/deposit/supply to earn and describes the earn side.

B) Generic marketing without concrete enrollable terms:
   - “Put your crypto to work”, “start earning”, “enjoy high yield”, “up to X%” without a specific product/pool + asset + action that is clearly joinable now.

C) Reward reports / past distributions / points-only language:
   - “rewards distributed”, “benefits are here”, “fresh rewards”, “points”, “drops”, “airdrop”, “season”, “quest” unless it explicitly functions as staking/lending/LP with clear deposit/stake instructions and a defined earn product.
   - If the primary mechanic is points/drops/airdrop/quests, label NO.

D) Trading/price/PnL/funding/alpha content:
   - Perps, shorts/longs, funding payments as trader PnL, “trade to earn”, signals, market commentary.

E) Competitions, lucky draws, red packets, cashback, cards, referrals, affiliate programs, leaderboards, prize pools → NO.

F) Unsupported/vague yield lists with no verifiable join context:
   - Messages that only list huge APRs/APYs (“935%”, etc.) but do not clearly specify the chain/platform context AND the exact pool/product AND the required action in a credible way.
   - If it looks like a shill screenshot/aggregated “LP rewards” list without clear where/how beyond vague “deposit liquidity”, choose NO.

G) “Coming soon” / not yet live (unless a specific start time/window is given and participation method is clear) → NO.

--------------------------------
Tie-breakers (very important)
- When in doubt, choose NO.
- Mentioning APY/APR alone is insufficient if the pool/product + asset + how-to-join now is not clear.
- If the message is primarily an integration/support announcement (even with “earning yield” mentioned in narrative), choose NO unless it explicitly offers a concrete, joinable earn product.

Respond with only: yes or no
Iteration 4: New subsample score 14.0 is better than old score 12.0. Continue to full eval and add to candidate pool.
Iteration 4: Valset score for new program: 0.6262626262626263 (coverage 99 / 99)
Iteration 4: Val aggregate for new program: 0.6262626262626263
Iteration 4: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 1.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 0.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 4: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 4: Valset pareto front aggregate score: 0.8080808080808081
Iteration 4: Updated valset pareto front programs: {0: {0, 1, 2, 3}, 1: {0, 1, 2, 3}, 2: {2}, 3: {0, 2, 3}, 4: {0, 1, 2, 3}, 5: {0, 1, 2, 3}, 6: {0, 1, 2, 3}, 7: {0, 1}, 8: {0, 1, 2, 3}, 9: {0, 1, 2, 3}, 10: {0, 1, 2, 3}, 11: {0, 1, 3}, 12: {0, 1, 2, 3}, 13: {0, 1, 2, 3}, 14: {0, 1, 2, 3}, 15: {0, 1, 2}, 16: {0, 1, 2, 3}, 17: {0, 2, 3}, 18: {0, 1, 2, 3}, 19: {0, 1, 2, 3}, 20: {0, 2}, 21: {0, 1, 3}, 22: {0, 1, 2, 3}, 23: {1, 2, 3}, 24: {0, 1, 2, 3}, 25: {0, 1, 2, 3}, 26: {0, 1, 2, 3}, 27: {0, 1, 3}, 28: {0, 1, 2, 3}, 29: {0, 1, 2, 3}, 30: {0, 1, 3}, 31: {0, 1, 2, 3}, 32: {0, 1, 2, 3}, 33: {0, 1, 2}, 34: {0, 1, 2, 3}, 35: {0, 1, 3}, 36: {2}, 37: {0, 1, 2, 3}, 38: {3}, 39: {1}, 40: {2}, 41: {0, 1, 2, 3}, 42: {1, 2, 3}, 43: {1}, 44: {0, 2, 3}, 45: {2}, 46: {2}, 47: {0}, 48: {0, 1, 2, 3}, 49: {0, 1}, 50: {0, 1, 2, 3}, 51: {1, 3}, 52: {0, 1, 2, 3}, 53: {0, 1, 2, 3}, 54: {1, 3}, 55: {0, 1, 2, 3}, 56: {0, 1, 3}, 57: {0, 1, 2, 3}, 58: {0, 1, 2, 3}, 59: {0, 1, 2}, 60: {0, 1, 2, 3}, 61: {0, 1, 2, 3}, 62: {0, 1, 2, 3}, 63: {0, 1, 2}, 64: {0, 1, 3}, 65: {0, 1, 2, 3}, 66: {0, 1, 2, 3}, 67: {0, 1, 2, 3}, 68: {0, 1, 2, 3}, 69: {0, 1, 2, 3}, 70: {0, 1, 2, 3}, 71: {0, 1, 2, 3}, 72: {1}, 73: {0, 1, 2, 3}, 74: {0, 1, 2, 3}, 75: {0, 1, 2, 3}, 76: {0, 1, 2, 3}, 77: {0, 1, 2, 3}, 78: {1, 3}, 79: {0, 1, 2, 3}, 80: {0, 1, 2, 3}, 81: {0, 1, 2, 3}, 82: {0, 1, 2, 3}, 83: {0, 1, 2, 3}, 84: {0, 1, 2, 3}, 85: {0, 1, 2, 3}, 86: {0, 1, 2, 3}, 87: {0, 1, 2, 3}, 88: {0, 1, 2, 3}, 89: {0, 1, 2, 3}, 90: {0, 1, 2, 3}, 91: {0, 1, 2, 3}, 92: {0, 1, 2, 3}, 93: {0, 2}, 94: {0, 1, 2, 3}, 95: {0, 1, 2, 3}, 96: {0, 1, 2, 3}, 97: {0, 1, 2, 3}, 98: {2}}
Iteration 4: Best valset aggregate score so far: 0.6767676767676768
Iteration 4: Best program as per aggregate score on valset: 1
Iteration 4: Best score on valset: 0.6767676767676768
Iteration 4: Linear pareto front program index: 1
Iteration 4: New program candidate index: 3
Iteration 5: Selected program 3 score: 0.6262626262626263
Iteration 5: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria below.

--------------------------------
YES (strict but practical)
Say "yes" ONLY if the message clearly includes ALL of the following:

1) Passive earn action (user can do it, not just info):
   The message explicitly invites or instructs users to do at least one of:
   - stake / restake / delegate / lock
   - deposit / subscribe to an Earn/Savings product (flexible or fixed)
   - lend / supply assets (earn interest)
   - provide liquidity / farm / deposit into a vault/strategy
   Must be framed as something the user can participate in (now or with a stated start/end window).

2) Identifiable venue + earn product context:
   The message must identify WHERE to earn, with enough specificity that it’s clearly an earn offering, e.g.:
   - a named exchange/protocol/app + an Earn/Savings/Vault/Farm feature/product OR a specific pool/market.
   Acceptable specificity for CEX earn:
   - “<Exchange> Earn” plus the assets is sufficient (treat “X Earn” as the product context).
   For DeFi:
   - protocol + pool/vault/market name (or pair) should be present.

3) Asset(s) are specified:
   At least one token/coin to deposit/stake/LP is stated (e.g., XMR, ETH, USDT, ETH-USDC).

4) “Live/joinable” signal:
   At least one of:
   - explicit instruction to join: “deposit”, “stake”, “subscribe”, “provide liquidity”, “supply”, “join now”
   - or a clear availability window indicating it’s active/available (e.g., “ends Jan 28”, “starts at …”, “now live”)
   If it’s only “coming soon” with no actionable window, it’s NO.

5) Yield/reward terms:
   At least one of:
   - explicit APY/APR/reward rate/boost for the earn offering, OR
   - an explicit statement that the specific earn pool/product is live and users can deposit/subscribe now.
   If a rate is shown, it must be tied to the mentioned earn offering (not a generic “up to” with no venue/product).

If any requirement is missing or too ambiguous, output NO.

--------------------------------
NO (common traps / exclusions)
Always output "no" for:

A) Pure news/integration/support without an earn offer:
   - listings, wallet/chain support, bridges, collateral enablement, “market live” for trading,
     “now supported” announcements, mergers/pauses, tech updates
   Unless it clearly instructs users to deposit/stake/supply/LP to earn.

B) Vague marketing with no enrollable earn context:
   - “start earning”, “put your crypto to work”, “high yield” without a clear venue + earn product context + assets.

C) Points/airdrop/quest/season language as the primary mechanic:
   - drops, points, quests, campaigns, distributions, “rewards are here”
   Unless it is explicitly an earn product where users deposit/stake/LP to accrue yield (not just points).

D) Trading/active PnL mechanisms:
   - perps, leverage, signals, funding as trader PnL, “trade to earn”, alpha, market commentary.

E) Competitions, lucky draws, cashback, cards, referrals/affiliates, leaderboards, prize pools.

F) Shill-like APR screenshots/lists with unclear where/how:
   - big APR numbers without a credible, specific venue/product context and a clear join action.

G) Pure analytics/rate commentary without a concrete offer:
   - “APY is X” for an asset without stating where/how to stake/deposit now.
   (Example: “tAVAX APY >6%” without explicit staking/deposit instructions and venue/product context → NO.)

--------------------------------
Tie-breakers (very important)
- When in doubt, choose NO.
- “Up to X% APY” can be YES ONLY if paired with a specific venue + earn product context (e.g., “HTX Earn”) AND assets AND a join/live/window signal.
- If the message is primarily informational or promotional and you cannot answer “what exactly should the user deposit/stake, and where?” → NO.

Respond with only: yes or no
Iteration 5: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 5: Valset score for new program: 0.6161616161616161 (coverage 99 / 99)
Iteration 5: Val aggregate for new program: 0.6161616161616161
Iteration 5: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 0.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 0.0, 15: 1.0, 16: 1.0, 17: 0.0, 18: 1.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 0.0, 36: 0.0, 37: 1.0, 38: 1.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 1.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 0.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 5: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 5: Valset pareto front aggregate score: 0.8181818181818182
Iteration 5: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4}, 1: {0, 1, 2, 3, 4}, 2: {2}, 3: {0, 2, 3, 4}, 4: {0, 1, 2, 3, 4}, 5: {0, 1, 2, 3, 4}, 6: {0, 1, 2, 3, 4}, 7: {0, 1}, 8: {0, 1, 2, 3, 4}, 9: {0, 1, 2, 3}, 10: {0, 1, 2, 3, 4}, 11: {0, 1, 3, 4}, 12: {0, 1, 2, 3, 4}, 13: {0, 1, 2, 3, 4}, 14: {0, 1, 2, 3}, 15: {0, 1, 2, 4}, 16: {0, 1, 2, 3, 4}, 17: {0, 2, 3}, 18: {0, 1, 2, 3, 4}, 19: {0, 1, 2, 3, 4}, 20: {0, 2}, 21: {0, 1, 3, 4}, 22: {0, 1, 2, 3, 4}, 23: {1, 2, 3, 4}, 24: {0, 1, 2, 3, 4}, 25: {0, 1, 2, 3, 4}, 26: {0, 1, 2, 3, 4}, 27: {0, 1, 3, 4}, 28: {0, 1, 2, 3, 4}, 29: {0, 1, 2, 3, 4}, 30: {0, 1, 3, 4}, 31: {0, 1, 2, 3, 4}, 32: {0, 1, 2, 3, 4}, 33: {0, 1, 2, 4}, 34: {0, 1, 2, 3, 4}, 35: {0, 1, 3}, 36: {2}, 37: {0, 1, 2, 3, 4}, 38: {3, 4}, 39: {1}, 40: {2}, 41: {0, 1, 2, 3, 4}, 42: {1, 2, 3, 4}, 43: {1}, 44: {0, 2, 3, 4}, 45: {2}, 46: {2}, 47: {0, 4}, 48: {0, 1, 2, 3, 4}, 49: {0, 1}, 50: {0, 1, 2, 3, 4}, 51: {1, 3, 4}, 52: {0, 1, 2, 3, 4}, 53: {0, 1, 2, 3, 4}, 54: {1, 3}, 55: {0, 1, 2, 3, 4}, 56: {0, 1, 3}, 57: {0, 1, 2, 3, 4}, 58: {0, 1, 2, 3, 4}, 59: {0, 1, 2, 4}, 60: {0, 1, 2, 3, 4}, 61: {0, 1, 2, 3, 4}, 62: {0, 1, 2, 3, 4}, 63: {0, 1, 2}, 64: {0, 1, 3}, 65: {0, 1, 2, 3, 4}, 66: {0, 1, 2, 3, 4}, 67: {0, 1, 2, 3, 4}, 68: {0, 1, 2, 3, 4}, 69: {0, 1, 2, 3, 4}, 70: {0, 1, 2, 3, 4}, 71: {0, 1, 2, 3, 4}, 72: {1}, 73: {0, 1, 2, 3, 4}, 74: {0, 1, 2, 3, 4}, 75: {0, 1, 2, 3, 4}, 76: {0, 1, 2, 3, 4}, 77: {0, 1, 2, 3, 4}, 78: {1, 3}, 79: {0, 1, 2, 3, 4}, 80: {0, 1, 2, 3, 4}, 81: {0, 1, 2, 3, 4}, 82: {0, 1, 2, 3, 4}, 83: {0, 1, 2, 3, 4}, 84: {0, 1, 2, 3, 4}, 85: {0, 1, 2, 3, 4}, 86: {0, 1, 2, 3, 4}, 87: {4}, 88: {0, 1, 2, 3, 4}, 89: {0, 1, 2, 3, 4}, 90: {0, 1, 2, 3, 4}, 91: {0, 1, 2, 3, 4}, 92: {0, 1, 2, 3, 4}, 93: {0, 2, 4}, 94: {0, 1, 2, 3, 4}, 95: {0, 1, 2, 3, 4}, 96: {0, 1, 2, 3, 4}, 97: {0, 1, 2, 3, 4}, 98: {2, 4}}
Iteration 5: Best valset aggregate score so far: 0.6767676767676768
Iteration 5: Best program as per aggregate score on valset: 1
Iteration 5: Best score on valset: 0.6767676767676768
Iteration 5: Linear pareto front program index: 1
Iteration 5: New program candidate index: 4
Iteration 6: Selected program 1 score: 0.6767676767676768
Iteration 6: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

HARD REQUIREMENTS FOR YES (all must be satisfied):
1) ACTION: The message explicitly tells the user to do an earn action:
   stake / deposit / subscribe / supply / lend / provide liquidity / add liquidity / LP / farm / lock
2) VENUE: The message identifies WHERE to do it:
   - a named platform feature/product (e.g., “Flexible Earn”, “Simple Earn”, “Savings”, “Vault”, “Pool”, “Farm”, “LP pool”), AND
   - the platform/venue is identified (exchange/protocol name) OR a clearly tied “start here/join/deposit now” link/button that is explicitly for that named earn product.
3) ASSET(S): The message states which asset(s) to use (token symbol(s) or pair), e.g., AXS, USDT, ETH/USDC, MNT-USDC.
4) JOINABLE: It is presented as currently live/available or includes a clear start time/date/window.

If any one of ACTION / VENUE / ASSET(S) / JOINABLE is missing → output NO.

IMPORTANT EXCLUSIONS (common edge cases; these override everything):
A) Competitions / prize pools / lucky draws / hunts / puzzles / leaderboards / “share of $X prize pool”
   - Even if it mentions “staking” or an LP pool as a way to earn entries/pieces/chances → NO.
   - If the primary objective is contest progress, points, chances, or prizes rather than passive yield → NO.
B) Airdrops, points, quests, referrals, cashback, vouchers, “trade/deposit to win”, lotteries → NO.
C) Trading-only offers (perps, margin, “zero interest” promos, swap routing, listings) → NO.
D) News/partnerships/tech updates/integration/testnet/beta launches without an explicit earn deposit/stake/LP offer → NO.
E) Vague or “brand-level” earn marketing:
   - “Earn up to X%”, “start earning”, “high APY”, “top returns”, “yield szn” without a specific joinable product + asset(s) + action → NO.

SPECIAL RULES TO PREVENT FALSE POSITIVES:
- A single line like “NEW <Exchange> Earn: Deposit $TOKEN on Flexible Earn, Earn 20% APY” counts as YES only if it is clearly a live, joinable earn product (e.g., “Flexible Earn”) AND names the platform AND the asset.
- However, if the message reads like a generic ad with missing joinability (no “now/live/start” or date/window) OR lacks the exact earn product name (only “Earn”) → NO.
- If APY/APR is mentioned but not tied to a specific product/pool/vault and asset(s) → NO.

QUICK DECISION CHECKLIST (must all be “yes”):
- Do I know exactly what to do (stake/deposit/LP/lend/lock)?
- Do I know exactly where (named earn product/pool/vault on a specific venue)?
- Do I know the exact asset(s) to use?
- Is it joinable now or with a stated start time/window?
- Is it NOT a contest/lottery/points/airdrop/trade-to-win?

If any answer is “no” → output NO.

Respond with only: yes or no
Iteration 6: New subsample score 14.0 is better than old score 13.0. Continue to full eval and add to candidate pool.
Iteration 6: Valset score for new program: 0.6262626262626263 (coverage 99 / 99)
Iteration 6: Val aggregate for new program: 0.6262626262626263
Iteration 6: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 0.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 0.0, 18: 0.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 0.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 0.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 0.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 0.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 0.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 0.0, 97: 0.0, 98: 0.0}
Iteration 6: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 6: Valset pareto front aggregate score: 0.8484848484848485
Iteration 6: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5}, 1: {0, 1, 2, 3, 4, 5}, 2: {2}, 3: {0, 2, 3, 4}, 4: {0, 1, 2, 3, 4, 5}, 5: {0, 1, 2, 3, 4, 5}, 6: {0, 1, 2, 3, 4, 5}, 7: {0, 1, 5}, 8: {0, 1, 2, 3, 4, 5}, 9: {0, 1, 2, 3, 5}, 10: {0, 1, 2, 3, 4, 5}, 11: {0, 1, 3, 4, 5}, 12: {0, 1, 2, 3, 4, 5}, 13: {0, 1, 2, 3, 4, 5}, 14: {0, 1, 2, 3, 5}, 15: {0, 1, 2, 4}, 16: {0, 1, 2, 3, 4, 5}, 17: {0, 2, 3}, 18: {0, 1, 2, 3, 4}, 19: {0, 1, 2, 3, 4, 5}, 20: {0, 2}, 21: {0, 1, 3, 4, 5}, 22: {0, 1, 2, 3, 4, 5}, 23: {1, 2, 3, 4, 5}, 24: {0, 1, 2, 3, 4, 5}, 25: {0, 1, 2, 3, 4, 5}, 26: {0, 1, 2, 3, 4, 5}, 27: {0, 1, 3, 4, 5}, 28: {0, 1, 2, 3, 4}, 29: {0, 1, 2, 3, 4, 5}, 30: {0, 1, 3, 4, 5}, 31: {0, 1, 2, 3, 4, 5}, 32: {0, 1, 2, 3, 4, 5}, 33: {0, 1, 2, 4}, 34: {0, 1, 2, 3, 4, 5}, 35: {0, 1, 3, 5}, 36: {2}, 37: {0, 1, 2, 3, 4, 5}, 38: {3, 4, 5}, 39: {1, 5}, 40: {2}, 41: {0, 1, 2, 3, 4, 5}, 42: {1, 2, 3, 4, 5}, 43: {1, 5}, 44: {0, 2, 3, 4}, 45: {2}, 46: {2}, 47: {0, 4}, 48: {0, 1, 2, 3, 4, 5}, 49: {0, 1, 5}, 50: {0, 1, 2, 3, 4, 5}, 51: {1, 3, 4, 5}, 52: {0, 1, 2, 3, 4, 5}, 53: {5}, 54: {1, 3, 5}, 55: {0, 1, 2, 3, 4, 5}, 56: {0, 1, 3, 5}, 57: {5}, 58: {0, 1, 2, 3, 4, 5}, 59: {0, 1, 2, 4}, 60: {0, 1, 2, 3, 4, 5}, 61: {0, 1, 2, 3, 4, 5}, 62: {0, 1, 2, 3, 4, 5}, 63: {0, 1, 2}, 64: {0, 1, 3, 5}, 65: {0, 1, 2, 3, 4, 5}, 66: {0, 1, 2, 3, 4, 5}, 67: {0, 1, 2, 3, 4, 5}, 68: {0, 1, 2, 3, 4, 5}, 69: {0, 1, 2, 3, 4, 5}, 70: {0, 1, 2, 3, 4}, 71: {0, 1, 2, 3, 4, 5}, 72: {1, 5}, 73: {0, 1, 2, 3, 4, 5}, 74: {0, 1, 2, 3, 4, 5}, 75: {0, 1, 2, 3, 4, 5}, 76: {0, 1, 2, 3, 4, 5}, 77: {0, 1, 2, 3, 4}, 78: {1, 3, 5}, 79: {0, 1, 2, 3, 4, 5}, 80: {0, 1, 2, 3, 4, 5}, 81: {0, 1, 2, 3, 4, 5}, 82: {5}, 83: {0, 1, 2, 3, 4, 5}, 84: {0, 1, 2, 3, 4, 5}, 85: {0, 1, 2, 3, 4, 5}, 86: {0, 1, 2, 3, 4, 5}, 87: {4}, 88: {0, 1, 2, 3, 4, 5}, 89: {0, 1, 2, 3, 4, 5}, 90: {0, 1, 2, 3, 4, 5}, 91: {0, 1, 2, 3, 4, 5}, 92: {0, 1, 2, 3, 4, 5}, 93: {0, 2, 4}, 94: {0, 1, 2, 3, 4, 5}, 95: {0, 1, 2, 3, 4, 5}, 96: {0, 1, 2, 3, 4}, 97: {0, 1, 2, 3, 4, 5}, 98: {2, 4}}
Iteration 6: Best valset aggregate score so far: 0.6767676767676768
Iteration 6: Best program as per aggregate score on valset: 1
Iteration 6: Best score on valset: 0.6767676767676768
Iteration 6: Linear pareto front program index: 1
Iteration 6: New program candidate index: 5
Iteration 7: Selected program 5 score: 0.6262626262626263
Iteration 7: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

HARD REQUIREMENTS FOR YES (all must be satisfied):
1) ACTION (explicit earn action):
   The message tells the user to do at least one of: stake / restake / delegate / deposit / subscribe / supply / lend / lock / farm / provide liquidity / add liquidity / LP / enter a pool/vault/earn product.
   - “Hold to earn”, “earn automatically when holding”, “savings”, “earn” counts ONLY if paired with an explicit action like “deposit/subscribe/stake” OR a clearly named product where “holding in X account/product” is the action (e.g., “Funding Account Hold-to-Earn”).
2) VENUE (where to do it):
   The message identifies a specific venue AND a specific earn surface:
   - Venue: protocol/app/exchange name (e.g., Smilee, MEXC, KuCoin, Aave, Curve), OR an explicit “stake/deposit here” link/button that is clearly for the earn product.
   - Earn surface: named pool/vault/farm/earn product/feature (e.g., “single-sided staking”, “Flexible Earn”, “Vault”, “Pool”, “Farm”, “LP pool”, “Hold to Earn”, “Staking Gala”).
3) ASSET(S):
   The message states the asset(s) to use (token symbol/name) or LP pair (e.g., IP, wgBERA, USDT, ETH/USDC).
4) JOINABLE:
   It is clearly available now OR gives a clear start time/date/window (e.g., “live”, “now”, “ongoing”, “starts Jan 30”, “from 12:00 UTC”, “until Mar 31”).
   - “Details to follow”, “soon”, “coming”, “upcoming” without a start window → NO.

IF ANY ONE of ACTION / VENUE / ASSET(S) / JOINABLE is missing → output NO.

IMPORTANT EXCLUSIONS (override everything → NO):
A) Competitions / prize pools / lucky draws / hunts / puzzles / leaderboards / “share of $X prize pool” / “campaign”
   - Even if staking/LP is used to earn entries/points/chances → NO.
B) Airdrops, points, quests, referrals, cashback, vouchers, “trade/deposit to win”, lotteries → NO.
C) Trading-only: perps/margin/spot promos, listings, “use as margin/collateral”, “borrow”, “leverage”, “zero interest”, fee discounts → NO.
D) News/partnerships/tech updates/integration/testnet/beta launches without an explicit earn deposit/stake/LP offer → NO.
E) Vague/brand-level marketing:
   - “Earn up to X%”, “high APY”, “discover earn”, “generate awesome yields” without the full set (action+venue+asset+joinable) → NO.
F) Incentives for voters/bribes/governance actions (e.g., “become a veXXX voter”, “voting incentives”) unless it also clearly instructs depositing/supplying/staking assets into a specific earn pool/vault with joinability → otherwise NO.

SPECIAL RULES (reduce false negatives while staying strict):
- SINGLE-SIDED STAKING COUNTS: “single-sided X staking” counts as ACTION+EARN SURFACE.
- “APR/APY on staking” without the word “stake” can still count as ACTION if the text clearly indicates staking (e.g., “wgBERA staking”, “single sided staking”).
- “Hold to Earn” counts as an earn surface IF it specifies where the funds must be held (account/product) AND the asset AND joinable now.

JOINABILITY CLARIFIERS:
- Words implying live: live, now, ongoing, open, available, launched (ONLY if referring to the earn product itself, not just token trading/listing).
- “Launched” about a product that is clearly an earn product (e.g., “Hold to Earn launched”) can satisfy JOINABLE.

QUICK DECISION CHECKLIST (must all be “yes”):
- Do I know exactly what passive-yield action to take (stake/deposit/LP/lend/lock/hold-in-specified-earn-product)?
- Do I know exactly where (specific venue + named earn surface/pool/product)?
- Do I know the exact asset(s)/pair?
- Is it joinable now or with a stated start time/window?
- Is it NOT primarily borrowing/trading/collateral use, and NOT a contest/airdrop/points/referral?

If any answer is “no” → output NO.

Respond with only: yes or no
Iteration 7: New subsample score 14.0 is not better than old score 14.0, skipping
Iteration 8: Selected program 5 score: 0.6262626262626263
Iteration 8: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

DEFAULT TO NO.
Say YES only when the message itself contains enough concrete info for a user to take the earn action immediately (or at the stated start time) without guessing.

POSITIVE DEFINITION (what counts as YES)
A message is YES if it is an actual invitation/announcement/instruction to earn yield by:
- staking, locking, delegating
- depositing into an earn/savings/vault product
- supplying/lending in a money market
- providing liquidity / adding liquidity / LP / farming in a specific pool/farm
AND it identifies the venue/product and the asset(s), and indicates it is live (or gives a clear start time).

HARD REQUIREMENTS FOR YES (all must be satisfied)
1) ACTION: Explicit earn action verb is present (stake / lock / delegate / deposit / subscribe / supply / lend / provide liquidity / add liquidity / LP / farm).
2) WHERE (VENUE/PRODUCT): The message clearly identifies WHERE to do it, by at least ONE of:
   a) A named protocol/app/platform AND a named earn surface (vault / pool / farm / staking / savings / earn / flexible / fixed / simple earn / lend/borrow market), OR
   b) A named protocol/app/platform AND a direct “deposit/stake/supply/add liquidity” call-to-action that unmistakably refers to the earn feature being offered, OR
   c) A direct join/deposit/stake link/button plus a named earn product/pool/vault in the text (so the link is clearly tied to that earn venue).
   If it’s only a brand mention (“on X”) with no earn surface/product/pool/vault/market identified → NO.
3) ASSET(S): The message states the asset(s) to use (token symbols or pair), e.g., USDT, AVAX, INJ, ETH/USDC, MNT-USDC. Generic “deposit crypto” → NO.
4) JOINABLE: It is clearly available now (“live”, “now”, “open”, “available”, “starts”, “from <time/date>”) or includes a clear start time/date/window.
   If joinability is ambiguous marketing with no timing cue → NO.

ALLOWABLE (can still be YES)
- APY/APR is NOT required if the earn opportunity is otherwise concrete and joinable (some legitimate staking/pools omit APY).
- Messages that describe a specific vault/pool with a clear “deposit/supply/stake” suggestion can be YES even if phrased casually (e.g., “deposit into Spark’s USDT savings vault”) as long as the venue + product + asset are clear and it implies availability.

IMPORTANT EXCLUSIONS (override YES; if any applies → NO)
A) Competitions / prize pools / lucky draws / giveaways / hunts / puzzles / leaderboards / raffles / “share of $X prize pool”
   - Even if “stake/LP” is mentioned as a way to get entries/points/tickets/chances → NO.
B) Airdrops, points, quests, referrals, cashback, vouchers/coupons, “trade/deposit to win”, lotteries → NO.
C) Trading-only offers (perps, margin, “zero interest” promos, swaps, listings, deposit/withdraw/trade availability announcements) → NO.
D) General news/partnerships/tech updates/integration/testnet/beta launches without an explicit earn deposit/stake/LP offer → NO.
E) Vague earn marketing without specifics:
   - “Earn up to X%”, “high APY”, “start earning”, “best yields” without specific venue/product + assets + joinability → NO.
F) Non-yield “fees on deposits”, “deposit feature enabled”, “withdrawals open” (exchange operations) unless it explicitly offers an earn product → NO.

DISAMBIGUATION RULES (common edge cases)
- “Savings/Vault” counts as a named earn product only if it is tied to a specific venue/protocol (e.g., “Spark USDT savings vault”, “Binance Simple Earn”) and an asset.
- If a message only says “earn yield on AVAX” or “talking about how to earn” (educational content, podcast, spaces) → NO.
- If the message is about token listings, trading availability, or deposit/withdraw enablement with dates → NO (not yield farming).
- If the message is about buybacks/burns/revenue, governance votes, or “protocol revenue” without user deposit/stake instructions → NO.

QUICK CHECK (all must be true for YES)
- I know exactly what to do (stake/deposit/supply/add liquidity/farm/lock).
- I know exactly where (venue + named earn product/pool/vault/market or unambiguous earn surface).
- I know the exact asset(s) or pair.
- It’s clearly open now or has a clear start time/window.
- It’s not a contest/airdrop/points/referral/trade-to-win/listing/news.

If any check fails → output NO.

Respond with only: yes or no
Iteration 8: New subsample score 14.0 is not better than old score 15.0, skipping
Iteration 9: Selected program 5 score: 0.6262626262626263
Iteration 9: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

HARD REQUIREMENTS FOR YES (all must be satisfied):
1) ACTION (explicit earn action): The message explicitly instructs an earn action such as:
   stake / staking / restake / delegate / deposit / subscribe / supply / lend / earn / savings / vault deposit
   provide liquidity / add liquidity / LP / farm / lock / liquidity mining
   - “Earn” counts as an action only when paired with an explicit deposit/stake instruction or a clearly named earn product listing.
2) VENUE (where to do it): The message identifies WHERE to do it via either:
   a) a named platform/product/feature (e.g., “Simple Earn”, “Flexible Earn”, “Earn”, “Savings”, “Vault”, “Pool”, “Farm”, “LP pool”, “Stake”, “Staking”) AND the platform/venue name (exchange/protocol) is present; OR
   b) a “Get Started/Start/Join/Deposit now” link/button clearly tied to the earn product (treat “Get Started” as sufficient only if the message also names the platform/venue and the earn product/listing context).
3) ASSET(S): The message states the asset(s) to use (token symbol(s) or pair), e.g., AXS, USDT, mETH, ckUSDT, ETH/USDC, MNT-USDC.
4) JOINABLE: The message indicates availability NOW (e.g., “now”, “live”, “open”, “available”, “listed”, “launch”, “starts today”) OR provides a clear start time/date/window.

If any one of ACTION / VENUE / ASSET(S) / JOINABLE is missing → output NO.

IMPORTANT EXCLUSIONS (override everything → NO):
A) Competitions / prize pools / lucky draws / hunts / puzzles / leaderboards / seasons / cards / points / “share of $X prize pool”
   - Even if it mentions “staking”/LP as a way to earn entries/chances/pieces → NO.
B) Airdrops, points/quests, referrals/invites, cashback, vouchers/coupons, “trade/deposit to win”, lotteries/raffles → NO.
C) Trading-only offers (perps/margin, trading rebates, swap promos, listings, “zero interest” promos, copy trading) → NO.
D) News/partnerships/tech updates/integration/testnet/beta launches/research/TVL reports without an explicit user instruction to deposit/stake/LP into a specific earn venue → NO.
E) “Incentives/rewards APR/APY” mentioned only as market commentary or analytics (e.g., weekly reports, “supplied assets with incentives”, “borrow campaign offers rewards”) without a direct call-to-action + venue + joinability → NO.
F) Borrow-side promotions (e.g., “borrow campaign”, “rewards reducing borrowing costs”, “negative interest to borrow”) → NO unless the message explicitly tells the user to SUPPLY/LEND/DEPOSIT an asset to earn yield. (Borrow-to-earn is not passive yield.)

SPECIAL RULES (reduce false negatives while staying strict):
- Treat “New Earn Listing”, “Earn Listing”, “New staking”, “New pool/farm”, “Now live” as JOINABLE.
- A message like “New Earn Listing: Deposit $TOKEN, earn up to X% APY” counts as YES if it also identifies the venue/platform (by name) and the earn product context (e.g., “Earn”, “Flexible Earn”, “Savings”, “Staking”) and includes an explicit “deposit/stake” instruction. APR/APY is NOT required but helps.
- “Stake $TOKEN on <Platform>” with “now/live/listing” counts as YES even if no exact sub-product name is given, as long as the platform is named and it is clearly an earn/staking product (not a contest).

QUICK DECISION CHECKLIST (must all be “yes”):
- Do I know exactly what to do (stake/deposit/LP/lend/lock/subscribe)?
- Do I know exactly where (named platform + earn product/listing/pool/farm context, or a clearly tied get-started link)?
- Do I know the exact asset(s) to use?
- Is it joinable now or with a stated start time/window?
- Is it NOT a contest/lottery/airdrop/points/trading/borrow-campaign?

If any answer is “no” → output NO.

Respond with only: yes or no
Iteration 9: New subsample score 14.0 is better than old score 13.0. Continue to full eval and add to candidate pool.
Iteration 9: Valset score for new program: 0.6060606060606061 (coverage 99 / 99)
Iteration 9: Val aggregate for new program: 0.6060606060606061
Iteration 9: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 0.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 0.0, 18: 0.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 0.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 0.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 0.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 0.0, 97: 0.0, 98: 0.0}
Iteration 9: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 9: Valset pareto front aggregate score: 0.8484848484848485
Iteration 9: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6}, 1: {0, 1, 2, 3, 4, 5, 6}, 2: {2}, 3: {0, 2, 3, 4}, 4: {0, 1, 2, 3, 4, 5, 6}, 5: {0, 1, 2, 3, 4, 5, 6}, 6: {0, 1, 2, 3, 4, 5, 6}, 7: {0, 1, 5, 6}, 8: {0, 1, 2, 3, 4, 5, 6}, 9: {0, 1, 2, 3, 5, 6}, 10: {0, 1, 2, 3, 4, 5, 6}, 11: {0, 1, 3, 4, 5, 6}, 12: {0, 1, 2, 3, 4, 5, 6}, 13: {0, 1, 2, 3, 4, 5, 6}, 14: {0, 1, 2, 3, 5, 6}, 15: {0, 1, 2, 4}, 16: {0, 1, 2, 3, 4, 5, 6}, 17: {0, 2, 3}, 18: {0, 1, 2, 3, 4}, 19: {0, 1, 2, 3, 4, 5, 6}, 20: {0, 2}, 21: {0, 1, 3, 4, 5, 6}, 22: {0, 1, 2, 3, 4, 5, 6}, 23: {1, 2, 3, 4, 5, 6}, 24: {0, 1, 2, 3, 4, 5, 6}, 25: {0, 1, 2, 3, 4, 5, 6}, 26: {0, 1, 2, 3, 4, 5, 6}, 27: {0, 1, 3, 4, 5, 6}, 28: {0, 1, 2, 3, 4}, 29: {0, 1, 2, 3, 4, 5, 6}, 30: {0, 1, 3, 4, 5, 6}, 31: {0, 1, 2, 3, 4, 5, 6}, 32: {0, 1, 2, 3, 4, 5, 6}, 33: {0, 1, 2, 4}, 34: {0, 1, 2, 3, 4, 5, 6}, 35: {0, 1, 3, 5, 6}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6}, 38: {3, 4, 5}, 39: {1, 5}, 40: {2}, 41: {0, 1, 2, 3, 4, 5, 6}, 42: {1, 2, 3, 4, 5, 6}, 43: {1, 5, 6}, 44: {0, 2, 3, 4, 6}, 45: {2}, 46: {2}, 47: {0, 4}, 48: {0, 1, 2, 3, 4, 5, 6}, 49: {0, 1, 5, 6}, 50: {0, 1, 2, 3, 4, 5, 6}, 51: {1, 3, 4, 5, 6}, 52: {0, 1, 2, 3, 4, 5, 6}, 53: {5}, 54: {1, 3, 5, 6}, 55: {0, 1, 2, 3, 4, 5, 6}, 56: {0, 1, 3, 5, 6}, 57: {5, 6}, 58: {0, 1, 2, 3, 4, 5, 6}, 59: {0, 1, 2, 4}, 60: {0, 1, 2, 3, 4, 5, 6}, 61: {0, 1, 2, 3, 4, 5, 6}, 62: {0, 1, 2, 3, 4, 5, 6}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6}, 65: {0, 1, 2, 3, 4, 5, 6}, 66: {0, 1, 2, 3, 4, 5, 6}, 67: {0, 1, 2, 3, 4, 5, 6}, 68: {0, 1, 2, 3, 4, 5, 6}, 69: {0, 1, 2, 3, 4, 5, 6}, 70: {0, 1, 2, 3, 4}, 71: {0, 1, 2, 3, 4, 5, 6}, 72: {1, 5, 6}, 73: {0, 1, 2, 3, 4, 5, 6}, 74: {0, 1, 2, 3, 4, 5, 6}, 75: {0, 1, 2, 3, 4, 5, 6}, 76: {0, 1, 2, 3, 4, 5, 6}, 77: {0, 1, 2, 3, 4, 6}, 78: {1, 3, 5, 6}, 79: {0, 1, 2, 3, 4, 5, 6}, 80: {0, 1, 2, 3, 4, 5, 6}, 81: {0, 1, 2, 3, 4, 5, 6}, 82: {5}, 83: {0, 1, 2, 3, 4, 5, 6}, 84: {0, 1, 2, 3, 4, 5, 6}, 85: {0, 1, 2, 3, 4, 5, 6}, 86: {0, 1, 2, 3, 4, 5, 6}, 87: {4}, 88: {0, 1, 2, 3, 4, 5, 6}, 89: {0, 1, 2, 3, 4, 5, 6}, 90: {0, 1, 2, 3, 4, 5, 6}, 91: {0, 1, 2, 3, 4, 5, 6}, 92: {0, 1, 2, 3, 4, 5, 6}, 93: {0, 2, 4}, 94: {0, 1, 2, 3, 4, 5, 6}, 95: {0, 1, 2, 3, 4, 5, 6}, 96: {0, 1, 2, 3, 4}, 97: {0, 1, 2, 3, 4, 5, 6}, 98: {2, 4}}
Iteration 9: Best valset aggregate score so far: 0.6767676767676768
Iteration 9: Best program as per aggregate score on valset: 1
Iteration 9: Best score on valset: 0.6767676767676768
Iteration 9: Linear pareto front program index: 1
Iteration 9: New program candidate index: 6
Iteration 10: Selected program 4 score: 0.6161616161616161
Iteration 10: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria.

-------------------------------
Core definition (what counts as YES)
A message is YES only when it describes an enrollable earn mechanism where the user allocates assets (stake/deposit/supply/LP/lock) and receives yield/rewards as a result, with enough concrete details to act.

-------------------------------
YES (strict, actionable)
Say "yes" ONLY if ALL are satisfied:

1) Passive allocation action is explicit
   The message clearly tells the user they can do NOW (or within a stated window) at least one of:
   - stake / restake / delegate / lock / bond
   - deposit / subscribe / add funds to Earn/Savings/Term/Fixed/Flexible
   - lend / supply / borrow-lend market supply side
   - provide liquidity / add liquidity / farm / deposit into a vault/strategy/pool
   - run validator *only if it’s clearly presented as a staking/validator yield option for users*
   Must be passive earn (not “trade”, “buy”, “hold”, “bridge”, “use app”) unless paired with one of the above allocation actions.

2) Specific venue + earn context is identifiable (“where”)
   The message must name a protocol/app/exchange AND indicate the earn product/pool/market context, e.g.:
   - “<Exchange> Earn / Savings / Simple Earn / Staking / Launchpool”
   - “Aave/Compound supply market”, “Curve pool”, “Yearn vault”, “Pendle pool”, “Beefy vault”, etc.
   - A specific pool/market identifier such as a pair (ETH-USDC), a vault name, or a market name.
   If the venue is missing or it’s just a token/community statement, it’s NO.

3) Asset(s) to allocate are specified (“what”)
   At least one concrete asset or LP pair is mentioned (e.g., ETH, USDT, stETH, ETH-USDC).
   If only “crypto”/“assets” is mentioned, NO.

4) Joinable-now signal exists (“can I do it now?”)
   At least one of:
   - direct enrollment CTA: “stake now”, “deposit now”, “supply”, “add liquidity”, “subscribe”, “start earning on <product>”
   - or a clear live/availability statement: “now live”, “open”, “available”, “starts <time>”, “ends <time>”
   If it’s “coming soon”, “get ready”, “learn more”, or waitlist with no start time and no enrollment, NO.

5) Yield/reward linkage is concrete
   At least one of:
   - a specific rate (APY/APR/interest/rewards rate) clearly tied to the mentioned product/pool/market, OR
   - an explicit statement that depositing/staking in that named product/pool earns yield/rewards (e.g., “earn staking rewards”, “earn interest”, “earn trading fees + rewards”) AND the pool/product is live/joinable.
   “Earn points”, “earn tickets”, “earn entries”, “earn cashback”, “earn prizes” do NOT count as yield.

If any requirement is missing or ambiguous, output NO.

-------------------------------
NO (automatic exclusions / common traps)
Always output "no" for:

A) Trading or price content
   Technical analysis, “buy the dip”, perps/leverage, funding-rate as trader PnL, signals, alpha calls, “trade to earn”.

B) General news or ecosystem updates without an earn offer
   Listings, “now supported”, deposits/withdrawals enabled, partnerships, grants, security updates, tokenomics/burns/buybacks, governance with no staking/deposit CTA.

C) “Hold to earn points” / points-as-primary mechanic
   Any message where the reward is points/XP/quests/season/airdrop eligibility for holding, depositing, or interacting, unless it is clearly an interest/yield product with explicit APY/APR or explicit interest/reward-rate yield.
   Examples that are NO:
   - “Buy or deposit TOKEN… earn points while held”
   - “Earn points for holding”
   - “Season X points campaign”
   If it’s points only (even if it says “deposit”), NO.

D) Competitions/lotteries/referrals
   Leaderboards, prize pools, lucky draws, giveaways, tournaments, invite/referral bonuses, card cashback.

E) Vague marketing / screenshots with unclear specifics
   “High APY”, “up to 100%”, APR lists, memes, or shills without clear venue + product/pool + assets + joinable signal.

F) Non-yield incentives
   Buybacks/burn participation, “active yield” phrasing without a concrete passive earn action and product details, or any mechanism requiring ongoing active management.

-------------------------------
Tie-breakers (use these to avoid false positives)
- When in doubt, choose NO.
- If you cannot answer in one sentence: “Deposit/stake WHAT asset, WHERE, and HOW, to earn WHAT yield?” → NO.
- “Up to X% APY” can be YES only if:
  venue + explicit earn product context + specified assets + join/live/window signal are all present.
- “Stakers/whitelist/eligible users” is NOT enough unless it clearly instructs staking/depositing into a specific earn product now.
- “Deposit” by itself is not yield (could mean exchange deposits). It must be deposit into an Earn/Savings/Vault/Farm/market to earn.

Respond with only: yes or no
Iteration 10: New subsample score 15.0 is not better than old score 15.0, skipping
Iteration 11: Selected program 5 score: 0.6262626262626263
Iteration 11: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply/borrow-to-earn, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

DEFINITION (what counts as yield farming here)
A message is YES if it offers a concrete passive-earn mechanism where a user can put assets to work now (or at a stated time) to earn yield/rewards/interest/APR/APY. This includes:
- Staking/locking
- Deposit into Earn/Savings/Vault/Pool
- Supply/lend to a money market
- Provide liquidity / LP / farm
- Borrow-to-earn / collateral-based earn programs (e.g., “use X as collateral to borrow Y and earn Z% APR”) WHEN the earn action and assets are specified

HARD REQUIREMENTS FOR YES (all must be satisfied):
1) ACTION (explicit earn action verb present):
   stake / lock / deposit / subscribe / supply / lend / provide liquidity / add liquidity / LP / farm
   OR explicit “use as collateral to borrow X and earn Y%” that clearly functions as an earn program.
2) VENUE (where to do it is identifiable from the message itself):
   EITHER
   (a) Platform/venue name is stated (exchange/protocol/app) AND a specific earn product/feature is named
       Examples of product/feature names: Earn, Simple Earn, Flexible Earn, Savings, Vault, Pool, Farm, LP Pool, Liquidity Pool, Supply Mining, Launchpool, Dual Investment, “Carnival”, “Campaign” ONLY if it is clearly an earn program (not a contest).
   OR
   (b) A direct “join/deposit/stake now” link/button is present AND the text clearly ties it to a specific earn product/feature.
3) ASSET(S) (the assets involved are specified):
   - The deposit/stake/supply asset(s) must be named (token symbol or pair), e.g., USDT, XVS, solvBTC, ETH/USDC.
   - If the mechanic is “borrow X using Y as collateral” then at least one of the assets being used in the earn flow must be named in the message (collateral and/or borrowed asset).
4) JOINABLE (availability is clear):
   - Explicitly live/now/open/available OR provides a clear start time/date/window.
   - “Get ready”, “coming soon”, “soon” without a start time/window → NOT joinable.

If any one of ACTION / VENUE / ASSET(S) / JOINABLE is missing → output NO.

ALLOWLIST CLARIFICATIONS (to reduce false negatives):
- Borrow-to-earn campaigns count as YES when they read like: “Use [collateral assets] to borrow [asset] and earn up to [APR] in [program name] on [venue]” and are presented as live/available, even if “deposit” isn’t explicitly said (collateralizing/borrowing is the action).
- “X is now live… Earn up to Y% APR/APY… Get your X” can be YES IF:
  - It clearly refers to a yield-bearing token/product (e.g., a yield-bearing USDT variant) AND
  - The venue/platform is named or the product is clearly a named feature on that venue AND
  - Joinable is explicit (“now live/available”).
  Otherwise NO.

IMPORTANT EXCLUSIONS (these override everything → always NO):
A) Competitions / prize pools / lucky draws / hunts / puzzles / leaderboards / “share of $X prize pool”
   - Even if it mentions “staking/LP” as a way to earn entries/chances/points → NO.
B) Airdrops, points, quests, referrals, cashback, vouchers, “trade/deposit to win”, lotteries → NO.
C) Trading-only offers (perps, margin, leverage, swap routing, listings) → NO.
D) News/partnerships/tech updates/integration/testnet/beta launches without an explicit earn deposit/stake/LP offer → NO.
E) Pure “claim your rewards” / “rewards ready to be claimed” posts WITHOUT an explicit joinable earn opportunity in the same message → NO.
F) Vague/brand-level earn marketing:
   - “Earn up to X%”, “start earning”, “high APY”, “top returns”, “yield szn” without specific action + venue/product + asset(s) + joinability → NO.

DECISION PROCEDURE:
1) If any exclusion applies → NO.
2) Check ACTION, VENUE, ASSET(S), JOINABLE.
3) If all four are satisfied → YES, else NO.

Respond with only: yes or no
Iteration 11: New subsample score 13.0 is not better than old score 13.0, skipping
Iteration 12: Selected program 4 score: 0.6161616161616161
Iteration 12: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, farming, vault deposits, earn/savings products, liquidity incentive programs where the user provides liquidity/supplies).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria.

------------------------------------------------------------
YES (strict but practical)
Output "yes" ONLY if the message provides a concrete, joinable earn opportunity with enough specifics that a user could act.

A message is YES if it includes ALL of these:

1) Passive-earn ACTION the user can take now (or within a stated window)
   Must explicitly tell the user to do at least one of:
   - stake / restake / delegate / lock
   - deposit / subscribe / join / earn in an Earn/Savings product
   - lend / supply / borrow-to-earn bonus (if supplying/LPing is required)
   - provide liquidity / LP / farm / add liquidity / deposit into a vault/strategy
   Pure “yields are good” without an instruction/action → NO.

2) WHERE the earning happens (venue + earn context)
   Must name a specific protocol/app/exchange AND make it clear it’s an earn venue/product, e.g.:
   - “Binance Earn / OKX Earn / Bybit Earn / HTX Earn”, “Savings”, “Simple Earn”, “Staking”, “Launchpool”
   - DeFi protocol + pool/market/vault/farm context (Aave market, Morpho vault, Pendle pool, Curve pool, etc.)
   Just naming a chain/bridge/integration without an earn product → NO.

3) WHAT asset(s) are involved
   Must specify at least one token/coin (e.g., USDT, ETH, wETH, SOL) or an LP pair (e.g., ETH-USDC).

4) JOINABLE / live signal
   Must include at least one:
   - explicit “now live / incentives live / open / available / start now”
   - or explicit join instruction (“deposit”, “stake”, “supply”, “add liquidity”, “subscribe”)
   - or a clear start/end time window for participation
   “Coming soon”, “stay tuned”, “more details soon” → NO.

5) Yield / rewards are tied to the opportunity
   Must include EITHER:
   (a) an explicit rate/terms tied to this offer (APY/APR/% rewards/boost), OR
   (b) an explicit statement that depositing/supplying/LPing/staking in the named venue earns rewards and is live/joinable now.
   IMPORTANT: Generic “best yields”, “up to X%” without tying to a concrete venue+product+asset+joinable context → NO.

------------------------------------------------------------
ALLOWLIST CLARIFICATIONS (still must satisfy YES rules)
- “Incentives are now live” or “liquidity incentive period is active” can be YES ONLY if the message also states:
  the required user action (supply/LP/deposit/stake) AND the asset/pool/market context (what to supply/LP) AND where.
- “Deposit X, earn Y%/rewards in token Z” is YES even if it’s a campaign, as long as it’s passive deposit/lock (not trading/competition) and joinable with stated terms.
- Fixed/flexible earn products on CEX are YES if Exchange + “Earn/Savings/Staking” context + asset + joinable instruction/window is present.

------------------------------------------------------------
NO (common traps / exclusions)
Always output "no" for:

A) Trading, leverage, perps, options, signals, “trade to earn”, funding PnL, “pair listed for futures/spot trading”.
B) Listings, integrations, bridges, “now supported”, “market live” (unless it explicitly says to deposit/supply/LP/stake to earn).
C) Airdrops/points/quests/seasons as primary mechanic, unless explicitly earned by depositing/supplying/LPing/staking in a named venue now.
D) Competitions, raffles, red packets, lucky draws, cashback, referral-only rewards, leaderboards, prize pools.
E) Pure commentary/analytics: “APY is X”, “best yield”, screenshots of APR tables, or “yields on Starknet” without a clear, actionable deposit/supply/LP/stake instruction and venue+product context.
F) Products that require active position-taking rather than passive earn:
   - “buy YT/PT”, “buy yield tokens”, “maximize returns by trading YT”
   (Buying/trading instruments is NOT passive yield farming here.)
G) Ambiguous “liquidity incentives active” posts that do not specify the pool/asset and the user action.

------------------------------------------------------------
Decision checklist (fast)
Answer YES only if you can point to:
- Action: what to do (stake/supply/LP/deposit)?
- Venue: where (named protocol/exchange + earn product/pool)?
- Asset: what token/pair?
- Joinable: live now or clear window?
- Rewards: rate/terms or explicit earning statement?

If any is missing/unclear → NO.

Respond with only: yes or no
Iteration 12: New subsample score 15.0 is not better than old score 15.0, skipping
Iteration 13: Selected program 2 score: 0.6363636363636364
Iteration 13: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

Definition (what counts as “yield farming opportunity” here):
A message is YES only if it offers a concrete, passive-earn action on crypto assets (staking, lending/supplying, LP/farming, vault deposit, savings/earn product, fixed/term promo) that a normal user can perform, with enough details to identify the program.

Core rule (must be satisfied for YES):
The message itself must identify all three:
1) WHAT to do: stake / deposit / supply / lend / lock / provide liquidity (LP) / farm / vault deposit / subscribe / earn/savings product participation
AND
2) WHERE to do it: a specific joinable venue + specific feature/product/pool/vault/market (protocol/app/exchange + “Earn/Flexible/Fixed/Savings/Staking/Vault/Pool/Market” or a named pool/vault/market)
AND
3) WHICH asset(s): at least one specific token/coin or LP pair (e.g., USDC, ETH, WBTC, SOL, ETH/USDC, CELO-USD)

APY/APR not required if (1)-(3) are satisfied, but it strongly supports YES.

Important: accept implicit verbs when product is explicit
- If the message names an Earn/Savings/Staking/Vault/Pool/Market product + asset(s) and indicates yield/rewards/rate (APY/APR, “earn”, “rewards”, “mining”, “incentives”), treat WHAT as satisfied even if “deposit” is implied (e.g., “USAT Flexible Earn 10% APY”).
- “Market is live” can be YES if it clearly implies lending/supplying/borrowing in that market and includes venue + asset(s) (e.g., “stLINK & LINK markets now live on Morpho … 4.8% APY”).

Joinability/time:
- Assume joinable now unless the message clearly says ended, snapshot taken, rewards already finished, or “coming soon” with no start time.
- Future start is OK only if a clear start time/window is given.

YES conditions (must still satisfy the core rule):
1) Direct earn action:
   - “Stake/deposit/supply/lend/LP/farm/vault/subscribe” + venue/product + asset(s).
2) Rate/rewards tied to a specific product:
   - APY/APR/reward rate/incentives explicitly tied to a named pool/vault/earn product/market on a named venue + asset(s).
3) Live launch with clear earn context:
   - “Staking/Earn/Vault/Farm/Pool/Market is live/now available” + venue/product + asset(s) (+ optional rate/rewards).
4) Supply/borrow mining programs:
   - “Supply mining”, “lending rewards”, “weekly rewards”, “incentivized pools” are YES if they specify venue + action context + asset(s).

Hard NO conditions (common traps):
A) Incentives that are not passive yield:
   - Airdrops, points/XP, quests/Zealy, giveaways, lotteries, raffles, cashback, vouchers, referral bonuses, “trade to win”, competitions, deposit events that only “split rewards” without an ongoing earn product → NO.
B) Trading-only / listing / market trading announcements:
   - “Now trading”, “listed on X”, “new pair”, “futures”, “perps”, price talk → NO.
C) Vague yield marketing:
   - “Earn up to X%”, “high APY”, “top returns” without BOTH a specific product/program AND the asset(s) → NO.
D) Brand/platform promo without eligible specifics:
   - Mentions an Earn platform generally but no named product/pool/vault/market AND no asset(s) → NO.
E) Status/recap-only:
   - “Rewards distributed”, “claims open”, “week X rewards live” is NO unless it also clearly instructs how to participate in the ongoing earn program with venue + asset(s) (e.g., “Supply WBTC on JustLendDAO and earn…” is YES).
F) Not accessible:
   - Institutional-only/private/closed beta with no public participation path → NO.

Venue/product parsing heuristics (count as WHERE only when tied to earn context):
- CeFi: “Binance Earn/Savings”, “OKX Earn”, “Bybit Earn”, “KuCoin Earn Fixed/Flexible”, “Flexible Earn”, “Fixed Promotion”, “Savings”, “Staking”
- DeFi: “Aave supply”, “Morpho market/vault”, “Compound supply”, “JustLend supply”, “Uniswap pool (incentivized)”, “Curve gauge”, “Balancer pool”, “Vault”, “Farm”, “Pool”, “Market”, “Gauge”
- “incentivized pools” on a named DEX/network counts if pools/pairs are listed.

Quick checklist before YES (all must be true):
- Is there a passive earn action/program (explicit or clearly implied by an Earn/Staking/Vault/Market product)?
- Is the venue + specific product/pool/vault/market identifiable?
- Are the asset(s) specified?
If any is missing → NO.

Respond with only: yes or no
Iteration 13: New subsample score 15.0 is not better than old score 15.0, skipping
Iteration 14: Selected program 5 score: 0.6262626262626263
Iteration 14: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

HARD REQUIREMENTS FOR YES (must satisfy A, B, C, D):
A) ACTION (explicit earn action verb is present)
   The message explicitly instructs an earn action such as:
   stake / staking / restake / deposit / subscribe / supply / lend / lock / earn in / farm / provide liquidity / add liquidity / LP / pool / gauge / vault deposit
   - For AMM/Curve-style posts: “provide liquidity”, “LP”, “pool”, “deposit into pool”, “gauge”, “boost” count as ACTION.
   - Pure “trade”, “buy”, “hold”, “use”, “bridge”, “download” do NOT count.

B) VENUE (where to do it is identifiable)
   The message identifies WHERE to perform the earn action via at least ONE of:
   1) A named protocol/platform + a named earn venue/feature (Earn/Savings/Vault/Pool/Farm/Gauge/LP pool/Staking pool), OR
   2) A named protocol/platform + an explicit “pool/pair” on that venue (e.g., “on Curve”, “on Aave v3”, “on Binance Simple Earn”), OR
   3) A clearly tied “join/deposit now” link/button that is explicitly for the earn product/pool.
   Notes:
   - “on <protocol>” + “pool is live” can satisfy VENUE if the protocol is clearly the venue for depositing (e.g., Curve pool, Balancer pool, Aave market).

C) ASSET(S) (what to use is explicit)
   The message states the exact asset(s) to deposit/stake/supply:
   - token symbol/name(s) (e.g., USDT, ETH, AXS) OR
   - an LP pair/pool constituents (e.g., ETH/USDC, frxUSD/OUSD).
   If assets are implied but not stated → NO.

D) JOINABLE (availability is explicit)
   The message indicates it is joinable now OR gives a clear start time/window, such as:
   live / now live / launched / open / available now / start earning now / deposits open / from <date/time> / starts <date/time> / effective immediately
   If there is no explicit live/now/start-time signal → NO.

ADDITIONAL ACCEPTANCE RULES (to reduce false negatives while staying strict):
- NEW POOL / “POOL IS LIVE” posts:
  If the message says a specific pool/pair is “now live/launched” on a specific AMM/venue (Curve/Balancer/Uniswap v3 pool/etc.) AND names the pool assets (e.g., “frxUSD OUSD pool now live on Curve”) → this counts as YES because the actionable step (provide liquidity to that pool) is sufficiently implied by the pool-live announcement.
- “Incentivized / rewards / boosted / co-incentivized / gauge / bribes / booster”:
  These strengthen that it is a yield opportunity but do NOT replace missing assets/venue/joinability.

IMPORTANT EXCLUSIONS (override everything; if any applies → NO):
1) Competitions / prize pools / lucky draws / hunts / puzzles / leaderboards / “share of $X prize pool”
   - Even if it mentions staking/LP as a way to earn entries/points/chances → NO.
2) Airdrops, points, quests, referrals, cashback, vouchers, “trade/deposit to win”, lotteries, fee credits → NO.
3) Trading-only offers (perps, margin, leverage, swap promos, listings, “zero interest”, routing, copytrading) → NO.
4) News/partnerships/tech updates/integration/testnet/beta launches WITHOUT an explicit earn offer that meets A-D → NO.
5) Vague or brand-level marketing:
   - “Earn up to X%”, “high APY”, “top returns”, “yield szn” without a specific joinable product/pool/vault + assets + venue → NO.
6) Borrow-only / leverage-only announcements:
   - “E-Mode live”, “new collateral”, “higher LTV”, “borrow rates” without an explicit “supply/deposit/earn” instruction or clear deposit venue → NO.

APY/APR HANDLING:
- APY/APR can help but is NOT required.
- If APY/APR is mentioned, it must still meet A-D; otherwise → NO.
- Fixed/flexible earn promotions are YES only if:
  - platform/venue (e.g., “KuCoin Earn”, “Binance Simple Earn”) is named,
  - the earn product is named (e.g., “Fixed Promotion”, “Flexible Earn”, “Savings”),
  - the asset is named,
  - and it states “now/live/open” OR a start time/window.

QUICK DECISION CHECKLIST (must all be “yes”):
- Do I know exactly what passive-earn action to take (stake/deposit/supply/LP/farm/lock OR deposit into the named live pool)?
- Do I know exactly where (named platform/protocol + named earn venue/pool)?
- Do I know the exact asset(s) to use?
- Is it joinable now or with a stated start time/window?
- Is it NOT a contest/airdrop/points/trade-to-win?

If any answer is “no” → output NO.

Respond with only: yes or no
Iteration 14: New subsample score 14.0 is better than old score 12.0. Continue to full eval and add to candidate pool.
Iteration 14: Valset score for new program: 0.6565656565656566 (coverage 99 / 99)
Iteration 14: Val aggregate for new program: 0.6565656565656566
Iteration 14: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 0.0, 18: 0.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 1.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 0.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 0.0, 97: 0.0, 98: 0.0}
Iteration 14: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 14: Valset pareto front aggregate score: 0.8484848484848485
Iteration 14: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7}, 1: {0, 1, 2, 3, 4, 5, 6, 7}, 2: {2}, 3: {0, 2, 3, 4, 7}, 4: {0, 1, 2, 3, 4, 5, 6, 7}, 5: {0, 1, 2, 3, 4, 5, 6, 7}, 6: {0, 1, 2, 3, 4, 5, 6, 7}, 7: {0, 1, 5, 6, 7}, 8: {0, 1, 2, 3, 4, 5, 6, 7}, 9: {0, 1, 2, 3, 5, 6, 7}, 10: {0, 1, 2, 3, 4, 5, 6, 7}, 11: {0, 1, 3, 4, 5, 6, 7}, 12: {0, 1, 2, 3, 4, 5, 6, 7}, 13: {0, 1, 2, 3, 4, 5, 6, 7}, 14: {0, 1, 2, 3, 5, 6, 7}, 15: {0, 1, 2, 4}, 16: {0, 1, 2, 3, 4, 5, 6, 7}, 17: {0, 2, 3}, 18: {0, 1, 2, 3, 4}, 19: {0, 1, 2, 3, 4, 5, 6, 7}, 20: {0, 2}, 21: {0, 1, 3, 4, 5, 6, 7}, 22: {0, 1, 2, 3, 4, 5, 6, 7}, 23: {1, 2, 3, 4, 5, 6, 7}, 24: {0, 1, 2, 3, 4, 5, 6, 7}, 25: {0, 1, 2, 3, 4, 5, 6, 7}, 26: {0, 1, 2, 3, 4, 5, 6, 7}, 27: {0, 1, 3, 4, 5, 6, 7}, 28: {0, 1, 2, 3, 4, 7}, 29: {0, 1, 2, 3, 4, 5, 6, 7}, 30: {0, 1, 3, 4, 5, 6, 7}, 31: {0, 1, 2, 3, 4, 5, 6, 7}, 32: {0, 1, 2, 3, 4, 5, 6, 7}, 33: {0, 1, 2, 4}, 34: {0, 1, 2, 3, 4, 5, 6, 7}, 35: {0, 1, 3, 5, 6, 7}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7}, 38: {3, 4, 5}, 39: {1, 5, 7}, 40: {2}, 41: {0, 1, 2, 3, 4, 5, 6, 7}, 42: {1, 2, 3, 4, 5, 6, 7}, 43: {1, 5, 6, 7}, 44: {0, 2, 3, 4, 6, 7}, 45: {2}, 46: {2}, 47: {0, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7}, 49: {0, 1, 5, 6, 7}, 50: {0, 1, 2, 3, 4, 5, 6, 7}, 51: {1, 3, 4, 5, 6, 7}, 52: {0, 1, 2, 3, 4, 5, 6, 7}, 53: {5}, 54: {1, 3, 5, 6, 7}, 55: {0, 1, 2, 3, 4, 5, 6, 7}, 56: {0, 1, 3, 5, 6, 7}, 57: {5, 6, 7}, 58: {0, 1, 2, 3, 4, 5, 6, 7}, 59: {0, 1, 2, 4}, 60: {0, 1, 2, 3, 4, 5, 6, 7}, 61: {0, 1, 2, 3, 4, 5, 6, 7}, 62: {0, 1, 2, 3, 4, 5, 6, 7}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7}, 65: {0, 1, 2, 3, 4, 5, 6, 7}, 66: {0, 1, 2, 3, 4, 5, 6, 7}, 67: {0, 1, 2, 3, 4, 5, 6, 7}, 68: {0, 1, 2, 3, 4, 5, 6, 7}, 69: {0, 1, 2, 3, 4, 5, 6, 7}, 70: {0, 1, 2, 3, 4, 7}, 71: {0, 1, 2, 3, 4, 5, 6, 7}, 72: {1, 5, 6, 7}, 73: {0, 1, 2, 3, 4, 5, 6, 7}, 74: {0, 1, 2, 3, 4, 5, 6, 7}, 75: {0, 1, 2, 3, 4, 5, 6, 7}, 76: {0, 1, 2, 3, 4, 5, 6, 7}, 77: {0, 1, 2, 3, 4, 6, 7}, 78: {1, 3, 5, 6, 7}, 79: {0, 1, 2, 3, 4, 5, 6, 7}, 80: {0, 1, 2, 3, 4, 5, 6, 7}, 81: {0, 1, 2, 3, 4, 5, 6, 7}, 82: {5}, 83: {0, 1, 2, 3, 4, 5, 6, 7}, 84: {0, 1, 2, 3, 4, 5, 6, 7}, 85: {0, 1, 2, 3, 4, 5, 6, 7}, 86: {0, 1, 2, 3, 4, 5, 6, 7}, 87: {4}, 88: {0, 1, 2, 3, 4, 5, 6, 7}, 89: {0, 1, 2, 3, 4, 5, 6, 7}, 90: {0, 1, 2, 3, 4, 5, 6, 7}, 91: {0, 1, 2, 3, 4, 5, 6, 7}, 92: {0, 1, 2, 3, 4, 5, 6, 7}, 93: {0, 2, 4, 7}, 94: {0, 1, 2, 3, 4, 5, 6, 7}, 95: {0, 1, 2, 3, 4, 5, 6, 7}, 96: {0, 1, 2, 3, 4}, 97: {0, 1, 2, 3, 4, 5, 6, 7}, 98: {2, 4}}
Iteration 14: Best valset aggregate score so far: 0.6767676767676768
Iteration 14: Best program as per aggregate score on valset: 1
Iteration 14: Best score on valset: 0.6767676767676768
Iteration 14: Linear pareto front program index: 1
Iteration 14: New program candidate index: 7
Iteration 15: Selected program 4 score: 0.6161616161616161
Iteration 15: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria.

------------------------------------------------------------
Core idea
Answer YES only when the message answers, concretely and unambiguously:
(1) What passive-earn action should the user take?
(2) Which asset(s) do they use?
(3) Where (which platform + which earn product/pool)?
(4) Is it available/joinable now (or has an explicit join window)?
(5) What are the reward/yield terms OR an explicit “earn/staking is live + join/deposit now” statement?

If you cannot point to all of these in the text, output NO.

------------------------------------------------------------
YES (strict, actionable)
Say "yes" ONLY if ALL conditions A–E hold:

A) Passive earn action is explicit and user-doable:
   The message explicitly instructs or invites users to do at least one of:
   stake / restake / delegate / lock / bond
   deposit / subscribe / save / earn
   lend / supply / borrow-to-earn (only if yield is for supplying or a defined earn vault)
   provide liquidity / LP / farm
   deposit into a vault / pool / strategy

B) Venue + earn product context is identifiable (WHERE + WHAT product):
   Must include a named platform (CEX or DeFi protocol/app/wallet) AND a clear earn container such as:
   Earn / Simple Earn / Savings / Staking / Vault / Farm / Pool / Market / “Supply Mining”
   For DeFi, acceptable: protocol + pool/vault/market name OR LP pair (e.g., ETH-USDC) OR “<token> vault”.
   For CEX, acceptable: “<Exchange> Earn/Simple Earn/Savings/Staking” + asset(s).

C) Asset(s) are specified:
   At least one coin/token is explicitly mentioned as the deposited/staked/supplied/LP asset.

D) Joinable now (or explicit availability window):
   Must contain at least one clear “join” signal such as:
   stake now / deposit now / subscribe now / supply now / provide liquidity / start here / now live / open / available
   OR a specific start/end time window for participation.
   If it is only “coming soon”, “get ready”, or trading/listing dates → NO.

E) Yield/reward terms are present and tied to the earn offer:
   At least one of:
   - explicit APY/APR/rate/reward rate/boost for THIS offering (not generic marketing), OR
   - an explicit statement that the earn product/pool is live/open AND users can stake/deposit/subscribe to earn rewards now.
   “Up to X%” is acceptable ONLY if A–D are clearly satisfied and the “up to” is clearly about the stated earn product.

------------------------------------------------------------
NO (automatic exclusions / traps)
Always output "no" for messages that are primarily:

1) Trading/listing/market access (not passive earn):
   - “trading starts”, listings, perps, leverage, signals, market commentary, swaps/bridges, “market live” for trading.

2) General product/news/tech without an enrollable earn offer:
   - integrations/support announcements, new features, research, company treasury buys, ecosystem updates.

3) Competitions, giveaways, lucky draws, prize pools, leaderboards, referrals, cashback/card promos:
   - even if they mention “rewards” or “APR”, unless the main mechanic is a concrete deposit/stake/LP earn product as in YES.

4) Airdrops/points/quests/campaigns where rewards are for tasks, XP, or claims:
   - “points”, “season”, “quest”, “airdrop”, “claim rewards” → NO
   EXCEPT when the message clearly requires depositing/staking/supplying/LP in a named earn product/pool AND participation is open now (then evaluate with YES rules).

5) Reward-claim-only updates:
   - “rewards are ready to claim”, “claim your mining rewards” with no instruction/opportunity to start earning now → NO.

6) Vague marketing with missing specifics:
   - “Earn up to 11% APY”, “grow your assets”, “high yield” WITHOUT clear venue + earn product context + asset(s) + joinable-now signal → NO.

7) APR screenshots/lists without credible where/how:
   - big APR numbers with no platform+product+pools/assets and no join action → NO.

------------------------------------------------------------
Tie-breakers
- When in doubt, choose NO.
- If the message does not clearly specify at least: (platform) + (earn product/pool) + (asset) + (join/live signal), it is NO even if an APY is shown.
- If it’s primarily informational/promotional and you cannot answer “what exactly should the user deposit/stake, and where, right now?” → NO.

Respond with only: yes or no
Iteration 15: New subsample score 14.0 is not better than old score 15.0, skipping
Iteration 16: Selected program 5 score: 0.6262626262626263
Iteration 16: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself gives enough to act without guessing.

CORE RULE (must be true for YES):
The message clearly offers passive yield/rewards for holding/staking/supplying/LPing specific crypto assets in a specific live product/pool/market.

HARD REQUIREMENTS FOR YES (all must be satisfied):
1) ACTION (earn action is explicit):
   The message tells the user to do at least one of:
   stake / staking / restake / delegate / deposit / lend / supply / provide liquidity / add liquidity / LP / farm / lock / vault / earn / subscribe
   - “Stake to Earn”, “Start staking”, “Supply to earn”, “Deposit into <strategy/vault>” qualify.

2) VENUE (where to do it is identifiable):
   At least ONE of the following is present:
   a) Protocol/platform name + named earn surface (pool/farm/vault/earn/savings/strategy/market), OR
   b) Protocol/platform name + a clear earn surface even if generic (“market”, “pool”, “staking”) when paired with an explicit earn action, OR
   c) A clearly tied call-to-action link/button (“Start staking”, “Deposit here”, “Supply now”) that is explicitly for the earn action/product in the message.
   Notes:
   - Do NOT require the exact branded product name (e.g., “Simple Earn”) if the protocol is named and the earn surface is clear (e.g., “Pendle tETH pool”, “Mantle market supply”).
   - Validator names (e.g., P2P.org/P2Pvalidator) count as venue only if the staking venue is clearly indicated as on-chain staking for the named chain/asset and paired with a CTA (e.g., “Start staking”).

3) ASSET(S) (what to use is explicit):
   The message states the token(s) or pair(s) to deposit/stake/supply/LP.
   Examples: ATOM, HYPE, LIT, tETH, USDC, WETH, ETH/USDC.
   - Wrapped/derivative symbols (tETH, weETH, stETH, etc.) count as assets.

4) JOINABLE (live/available timing is clear):
   Must indicate at least one of:
   - “live”, “now”, “open”, “currently”, “start staking”, “available”, “is active”, “incentives are live”, “deposit here”, or equivalent immediate CTA, OR
   - a clear start time/date/window.
   - If it only discusses rates/returns without indicating availability/currentness → NO.

IMPORTANT EXCLUSIONS (override everything; output NO):
A) Competitions / prize pools / lucky draws / hunts / puzzles / leaderboards / “chance to win” / “share of $X prize pool”
   - Even if it requires staking/LP/deposits to participate → NO (primary objective is prizes/entries).
B) Airdrops, points, quests, referrals, cashback, vouchers, “claim”, “register to claim”, lotteries, giveaways → NO.
C) Trading-only offers (perps, margin, trading leagues, fee rebates, zero-fee, listings, deposits for trading, swap routing) → NO.
D) News/partnerships/tech updates/integration/testnet/beta launches without an explicit earn deposit/stake/LP offer → NO.
E) Pure APR/APY update posts that do not explicitly invite/join or indicate joinability (e.g., “APR update… liquidity incentive period active” but no action/where/CTA) → NO.

SPECIAL CLARIFICATIONS (to capture common true YES cases):
- “Stake to Earn X% APY on $TOKEN … Start staking” with a named app/protocol/exchange (or clear on-chain staking + validator + CTA) → YES.
- “Incentives are live … Users can supply <assets> …” on a named lending protocol/market → YES even if APY is not stated.
- “New pool/vault/market for <asset> offering <APY>” on a named protocol (e.g., “Pendle tETH pool”) → YES if it implies current availability (“currently”, “is offering”, “now”, “live”) or includes CTA.
- If the message is only persuasive (“best returns”) without stating where/action/joinability → NO.

QUICK DECISION CHECKLIST (must all be “yes”):
- Do I know what passive-earn action to take (stake/deposit/supply/LP/lock)?
- Do I know where (named protocol/platform + pool/market/vault/earn surface OR explicit CTA link/button tied to the earn action)?
- Do I know the asset(s)?
- Is it joinable now/live or with a stated start time/window?
- Is it NOT a contest/lottery/points/airdrop/trade-to-win?

If any answer is “no” → output NO.

Respond with only: yes or no
Iteration 16: New subsample score 14.0 is better than old score 11.0. Continue to full eval and add to candidate pool.
Iteration 16: Valset score for new program: 0.5757575757575758 (coverage 99 / 99)
Iteration 16: Val aggregate for new program: 0.5757575757575758
Iteration 16: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 0.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 0.0, 18: 0.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 0.0, 43: 1.0, 44: 1.0, 45: 0.0, 46: 1.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 0.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 0.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 16: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 16: Valset pareto front aggregate score: 0.8484848484848485
Iteration 16: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 2: {2}, 3: {0, 2, 3, 4, 7, 8}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 7: {0, 1, 5, 6, 7}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 9: {0, 1, 2, 3, 5, 6, 7}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 11: {0, 1, 3, 4, 5, 6, 7, 8}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 14: {0, 1, 2, 3, 5, 6, 7, 8}, 15: {0, 1, 2, 4}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 17: {0, 2, 3}, 18: {0, 1, 2, 3, 4}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 20: {0, 2}, 21: {0, 1, 3, 4, 5, 6, 7, 8}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 23: {1, 2, 3, 4, 5, 6, 7, 8}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 27: {0, 1, 3, 4, 5, 6, 7, 8}, 28: {0, 1, 2, 3, 4, 7, 8}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 30: {0, 1, 3, 4, 5, 6, 7, 8}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 33: {0, 1, 2, 4}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 35: {0, 1, 3, 5, 6, 7, 8}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 38: {3, 4, 5}, 39: {1, 5, 7}, 40: {2}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 42: {1, 2, 3, 4, 5, 6, 7}, 43: {1, 5, 6, 7, 8}, 44: {0, 2, 3, 4, 6, 7, 8}, 45: {2}, 46: {8, 2}, 47: {0, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 49: {0, 1, 5, 6, 7}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 51: {1, 3, 4, 5, 6, 7}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 53: {5}, 54: {1, 3, 5, 6, 7}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 56: {0, 1, 3, 5, 6, 7, 8}, 57: {5, 6, 7}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 59: {0, 1, 2, 4}, 60: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7}, 65: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 68: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 70: {0, 1, 2, 3, 4, 7, 8}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 72: {1, 5, 6, 7, 8}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 74: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 77: {0, 1, 2, 3, 4, 6, 7, 8}, 78: {1, 3, 5, 6, 7}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 82: {5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 87: {4}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 93: {0, 2, 4, 7, 8}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 96: {0, 1, 2, 3, 4, 8}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8}, 98: {2, 4}}
Iteration 16: Best valset aggregate score so far: 0.6767676767676768
Iteration 16: Best program as per aggregate score on valset: 1
Iteration 16: Best score on valset: 0.6767676767676768
Iteration 16: Linear pareto front program index: 1
Iteration 16: New program candidate index: 8
Iteration 17: Selected program 2 score: 0.6363636363636364
Iteration 17: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

Definition (what counts as yield farming here):
A message is YES only when it describes a concrete earn action a user can take (stake/deposit/supply/lend/lock/LP/vault/farm/earn product) to earn yield/rewards on specific crypto assets, on a specific venue/product/pool/vault, and it is currently joinable (or has an explicit start time).

Core requirements (must all be satisfied for YES):
1) WHAT: an earn action or clearly implied participation in an earn product (stake/deposit/supply/lend/lock/LP/farm/vault/earn/savings/fixed/term/promo).
2) WHERE: a specific joinable venue + specific product surface (protocol/app + “Earn/Savings/Fixed/Pool/Vault/Farm/Staking/Market” etc). A bare chain name or ecosystem (“on Starknet”, “on Solana”) is NOT enough.
3) WHICH ASSET(S): at least one explicit token/coin or LP pair (e.g., WBTC, TRX, USDC, ETH/USDC).
4) JOINABLE NOW: the message must indicate it is live/available now OR provide a clear start window. If it is only a recap/distribution/status update with no invitation to join, it is NO.

Hard NO overrides (if any apply, output NO even if yield words appear):
A) Past-only / status-only / distribution-only:
   - “rewards distributed”, “weekly benefits are here”, “claim your rewards”, “season rewards”, “points credited”, “airdrop sent”, “APR was X” as a report
   - Unless it ALSO explicitly invites joining/starting/Depositing now into a named earn product with asset(s).
B) Incentive campaigns not expressed as passive yield:
   - quests, XP, points programs, Zealy, leaderboards, giveaways, lotteries, referrals, “trade to win”, volume/liq campaigns with incentive pools, cashback.
   - Even if “rewards” is mentioned, if it requires tasks/trading/competition → NO.
C) Trading/listing/news/marketing without a specific earn placement:
   - listings, “trading starts”, partnerships, tech upgrades, macro news → NO.
D) Ambiguous “start here / one-click / earn now” CTA without a named earn product surface:
   - If it doesn’t clearly identify the earn product/pool/vault (WHERE) beyond generic “Earn” or generic chain mention, treat as marketing and output NO.
E) Institutional/private/closed access → NO.

YES patterns (all must still satisfy Core requirements; these are common acceptable forms):
1) Explicit deposit/stake/supply/LP + specific venue/product + asset(s).
   - e.g., “Deposit WBTC into Uncap WBTC vault”, “Supply USDC on Aave”, “Stake TRX on JustLend sTRX”.
2) Explicit APY/APR/reward rate tied to a specific joinable product + asset(s).
   - “WBTC vault yielding 19.41% APR on Uncap” counts if the product/vault is named and clearly available.
3) “Live/Now available/Launched” staking/vault/farm with venue + asset(s).
4) Earn-platform fixed/term promos:
   - “KuCoin Earn Fixed Promotion: USDT 30D at X%” counts if asset + product type is explicit.

Strictness clarifications (to reduce false YES):
- General “stake X and enjoy yields” with an APY can be YES only when WHERE is a specific protocol/product and the action is passive (staking/lending/vault). Do not reject just because it’s ongoing/evergreen.
- However, if the message reads like generic brand ad and lacks a specific product surface/pool/vault (e.g., only “Earn” as a slogan) → NO.
- “Deposit on <Chain> Earn” is NOT sufficient unless <Chain> Earn is clearly a named, recognizable product (e.g., “Binance Earn”, “Bybit Earn”). For ambiguous phrases like “Starknet Earn”, require an additional product identifier (vault/pool/staking program name) or explicit “official Starknet Earn product” context; otherwise NO.
- Borrowing/leverage features are NOT yield farming unless it clearly describes a passive earn leg (e.g., “supply USDC to earn X%”) with venue + asset.

Decision checklist before YES (all must be true):
- Can I point to the earn action/program type?
- Can I point to a specific venue + product/pool/vault/earn surface (not just a chain/community)?
- Are the asset(s) explicit?
- Is it joinable now (or with a clear start time), and not merely a distribution/recap?

If any answer is no → output no.

Respond with only: yes or no
Iteration 17: New subsample score 13.0 is not better than old score 13.0, skipping
Iteration 18: Selected program 2 score: 0.6363636363636364
Iteration 18: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

========================
DECISION STANDARD (STRICT)
========================
Say YES only when the message itself (not implied by reputation) provides an actionable earn instruction with enough specifics for a user to take the next step without guessing.

Core requirements for YES (must all be met):
1) WHAT: a passive earn action or product (stake / staking, deposit, supply, lend, borrow-to-earn loop explicitly, lock, provide liquidity/LP, farm, vault, pool, savings/earn product, fixed/term earn, validator staking).
2) WHERE: a specific joinable venue + product/pool/vault/market name (protocol/app/exchange + named feature). Generic “on Starknet”, “on Solana”, “in DeFi” is NOT enough.
3) WHICH ASSET(S): at least one specific token/coin or LP pair (e.g., ETH, USDC, sUSN, ETH/USDC LP).

If any of (1)-(3) is missing → NO.

APY/APR is NOT required if (1)-(3) are clearly satisfied, but it strengthens YES.

Assume “live now” unless the message clearly says future only, ended, closed, or invite-only.

=================================
IMPORTANT: FILTER OUT “YIELD-LIKE”
=================================
Even if the text contains words like “yield”, “top yields”, “rewards”, “earn”, say NO when it is not a concrete joinable earn offer.

Explicit NO categories (common edge cases):
- Points/XP multipliers, “earn points while held”, “points campaign”, “quests”, “Zealy/Galxe”, badges → NO.
- Cashback, card spend rewards, lucky draws, raffles, lotteries, “trade to win”, competitions, referral contests → NO.
- Listings, trading pairs, deposits/withdrawals for exchange listing, market news → NO.
- Announcements that only describe a product’s existence/vision without telling the user to deposit/stake/supply (e.g., “vault is designed to deliver top yields”, “expansion”, “collaboration”) → NO unless it also includes an explicit participation instruction (stake/deposit/supply/etc.) and asset(s) and where.
- Past-only status (rewards distributed, recap) → NO unless it also invites joining the ongoing earn product with WHERE + WHAT + ASSET(S).
- Institutional/private/closed beta without public participation instructions → NO.

========================
WHEN TO SAY YES (SUFFICIENT)
========================
YES if the message includes any of the following, while meeting all three core requirements:

A) Explicit earn instruction:
- “Stake/deposit/supply/lend/lock/LP/farm/vault deposit” + (venue/product/pool/vault/market) + (asset(s)).

B) Explicit earn product with rate:
- APY/APR/reward rate explicitly tied to a named earn product/pool/vault/market on a named venue AND specifies asset(s).

C) “Live/Now available” earn launch WITH participation details:
- “Staking is live”, “Vault is live/launched”, “Earn is live” AND it states the venue/product and the asset(s) (and implies deposit/stake is possible).
- If it ONLY says “new vault launched / designed to deliver yield” but does NOT say deposit/stake/supply or otherwise clearly invite participation → NO.

D) CeFi Earn promos (allowed if specific):
- “Binance/Bybit/OKX/KuCoin Earn/Savings/Fixed/Term promotion” is YES only if it names the earn product type AND the eligible asset(s) (rate optional but helpful).

========================
VENUE/PRODUCT SPECIFICITY RULE
========================
WHERE must be specific enough to identify a joinable place, e.g.:
- “Aave supply USDC”, “Morpho USDC market”, “Pendle PT/YT pool”, “Uniswap v3 ETH/USDC pool”, “Vesu sUSN vault”, “Lido stake ETH”.
Not enough:
- “on Starknet”, “on Hyperliquid”, “on Sei”, “onchain yields”, “money market infrastructure” without a named pool/vault/market and an instruction.

========================
FINAL CHECKLIST (ALL MUST BE TRUE FOR YES)
========================
- Do I know WHAT passive-earn action/product the user should do?
- Do I know WHERE (named venue + specific product/pool/vault/market/earn plan)?
- Do I know WHICH asset(s)?
If any answer is “no” → output no.

Respond with only: yes or no
Iteration 18: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 18: Valset score for new program: 0.6060606060606061 (coverage 99 / 99)
Iteration 18: Val aggregate for new program: 0.6060606060606061
Iteration 18: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 0.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 0.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 0.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 0.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 0.0, 46: 1.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 0.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 18: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 18: Valset pareto front aggregate score: 0.8585858585858586
Iteration 18: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 2: {2}, 3: {0, 2, 3, 4, 7, 8, 9}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 7: {0, 1, 5, 6, 7}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 9: {0, 1, 2, 3, 5, 6, 7}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9}, 15: {0, 1, 2, 4}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 17: {0, 2, 3}, 18: {0, 1, 2, 3, 4, 9}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 20: {0, 9, 2}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 27: {0, 1, 3, 4, 5, 6, 7, 8}, 28: {0, 1, 2, 3, 4, 7, 8, 9}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 33: {0, 1, 2, 4, 9}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 35: {0, 1, 3, 5, 6, 7, 8}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 38: {3, 4, 5}, 39: {1, 5, 7}, 40: {2}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 42: {1, 2, 3, 4, 5, 6, 7, 9}, 43: {1, 5, 6, 7, 8}, 44: {0, 2, 3, 4, 6, 7, 8, 9}, 45: {2}, 46: {8, 9, 2}, 47: {0, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 49: {0, 1, 5, 6, 7}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 51: {1, 3, 4, 5, 6, 7, 9}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 53: {5}, 54: {1, 3, 5, 6, 7}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 56: {0, 1, 3, 5, 6, 7, 8}, 57: {5, 6, 7}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 59: {0, 1, 2, 4, 9}, 60: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7}, 65: {9}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 68: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 70: {0, 1, 2, 3, 4, 7, 8, 9}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 72: {1, 5, 6, 7, 8}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 74: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9}, 78: {1, 3, 5, 6, 7, 9}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 82: {5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 87: {4}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 93: {0, 2, 4, 7, 8, 9}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 96: {0, 1, 2, 3, 4, 8, 9}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 98: {2, 4}}
Iteration 18: Best valset aggregate score so far: 0.6767676767676768
Iteration 18: Best program as per aggregate score on valset: 1
Iteration 18: Best score on valset: 0.6767676767676768
Iteration 18: Linear pareto front program index: 1
Iteration 18: New program candidate index: 9
Iteration 19: Selected program 5 score: 0.6262626262626263
Iteration 19: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

HARD REQUIREMENTS FOR YES (all must be satisfied):
1) ACTION (explicit user instruction): The message explicitly instructs an earn action such as:
   stake / restake / deposit / subscribe / supply / lend / lock / provide liquidity / add liquidity / LP / farm / join pool / enter vault
   - Must be an instruction or a clear call-to-action, not just a description of what a protocol does.

2) VENUE (where to do it): The message clearly identifies WHERE the action happens by including:
   - a named earn venue/product/pool/vault (e.g., “Simple Earn”, “Flexible Earn”, “Savings”, “Vault”, “Farm”, “Pool”, “LP pool”, “staking pool”), AND
   - the platform/protocol/exchange name (e.g., Binance, Bybit, Aave, Curve, Ember Protocol), OR an explicit “deposit/stake here” link/button that is clearly tied to that named earn product.
   - If it only says generic “Earn”, “high yield”, “vault”, “pool” without a specific named product/pool/vault on a specific venue → NO.

3) ASSET(S) (what to use): The message states the exact asset(s) to deposit/stake/supply:
   - token symbol(s) or clear pair (e.g., SOL, USDT, wstUSR, ETH/USDC).
   - If it’s only “stablecoins”, “assets”, “tokens”, “your crypto” without specifying which → NO.

4) JOINABLE (timing): It is clearly available to join now OR includes a clear start time/date/window.
   - Accept: “now/live/open”, “starting <date/time>”, “from <date> to <date>”.
   - Reject: purely evergreen/brand marketing with no joinability cues (no “now/live/open/start” or window) → NO.

YIELD OPPORTUNITY DEFINITION (must be passive yield, not active trading):
- Includes staking rewards, lending/supply interest, LP/farming incentives, vault/strategy deposits, savings/earn products.
- APY/APR is helpful but NOT required if all HARD REQUIREMENTS are met.
- If it’s primarily about leveraging/trading to get yield (e.g., “up to 8x leverage”, margin/perps-driven) and not a straightforward deposit/stake/LP earn product → NO unless it still clearly offers a passive earn venue that a user can join by depositing (most leverage promos should be NO).

IMPORTANT EXCLUSIONS (override everything; if any apply → NO):
A) Competitions / prize pools / lucky draws / hunts / puzzles / leaderboards / “share of $X prize pool”
   - Even if it mentions staking/LP as a way to earn entries/points/chances → NO.
B) Airdrops, points/quests, referrals, cashback, vouchers, “trade/deposit to win”, lotteries, giveaways → NO.
C) Trading-only offers: perps, margin, copy trading, signal calls, “zero interest” promos, swap fee promos, listings/launchpads that require trading behavior → NO.
D) News/partnerships/tech updates/integration/testnet/beta/announcements about a protocol investing into a vault WITHOUT telling the user to deposit/stake now with specifics → NO.
E) Vague/brand-level earn marketing:
   - “Earn up to X%”, “start earning”, “high APY”, “one of the highest yields” without specific action+venue+asset+joinability → NO.
F) Protocol-internal metrics/changes (e.g., “X is now locked”, “locking retired”, “snapshot completed”, “incentive model live”) without an explicit user CTA to deposit/stake in a named venue with assets and joinability → NO.

SPECIAL RULES (common edge cases):
- If the message says “Stake <ASSET>. Earn <REWARD>.” but does NOT name the platform/protocol/product (or provide an explicit stake/deposit link tied to it) → NO.
- If the message describes a new vault/product launch and says it is “open/live” BUT does not explicitly tell the user to deposit/stake (action missing) → NO.
- If the message mentions a vault is “open to participants” but no clear instruction and no direct join link/product name → NO.
- “Restake”, “liquid staking”, “LST”, “rewards” still require venue+asset+joinability.
- If any required field (ACTION, VENUE, ASSET(S), JOINABLE) is ambiguous or implied rather than stated → NO.

QUICK DECISION CHECKLIST (must all be “yes”):
- Do I know exactly what to do (stake/deposit/supply/LP/lock)?
- Do I know exactly where (named earn product/pool/vault on a specific venue, or explicit deposit/stake link tied to it)?
- Do I know the exact asset(s) to use?
- Is it joinable now or with a stated start time/window (not just evergreen marketing)?
- Is it NOT a contest/lottery/points/airdrop/trade-to-win/trading-only?

If any answer is “no” → output NO.

Respond with only: yes or no
Iteration 19: New subsample score 15.0 is not better than old score 15.0, skipping
Iteration 20: Selected program 4 score: 0.6161616161616161
Iteration 20: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies YES.

================================================
CORE DECISION
Return "yes" ONLY for messages that describe an enrollable earn mechanism where the user commits assets (stake/lock/deposit/supply/LP) and receives yield/rewards as the primary outcome.

If you cannot answer ALL of these clearly from the text:
- What action should the user take?
- Which asset(s)?
- On which venue/product (where exactly)?
- Is it joinable now (or within a stated window)?
Then output "no".

================================================
YES CRITERIA (must satisfy ALL)

1) Passive-earn action is explicit and user-enrollable
   Message explicitly instructs/invites the user to do one of:
   - stake / restake / delegate / lock / bond
   - deposit / subscribe / join an Earn/Savings/Fixed/Flexible product
   - lend / supply to a market to earn interest
   - provide liquidity / farm / deposit into a vault/strategy
   Must be framed as something a user can do (not just a protocol description).

2) Concrete venue + earn-product context (where/how)
   Must name the venue AND make it clear it’s an earn product:
   - CEX: "<Exchange> Earn/Savings/Launchpool/Stake/Fixed Savings" etc.
   - DeFi: protocol + specific pool/vault/market/pair (e.g., "Aave USDC market", "Curve stETH/ETH", "Pendle PT-...", "Yearn vault ...").
   If the message only says a protocol name without a specific earn surface/pool/market, it’s NO.

3) Asset(s) specified
   At least one specific token/coin or LP pair is stated (e.g., ETH, USDT, IMU, BGB, ETH-USDC).

4) Joinable now / actionable timing
   Must include at least one:
   - direct join instruction: deposit/stake/lock/supply/provide liquidity/subscribe/join
   - or clear availability window indicating it’s active (starts/ends dates, “now live”, “open”, “LIVE”).
   “Coming soon / next month / when upgrade launches” without an open window or explicit ability to join now => NO.

5) Yield/reward terms that confirm earning
   Must include at least one:
   - explicit APY/APR/interest/reward rate/boost for the specific offering, OR
   - explicit statement that the earn pool/product is live/open AND users can join/deposit now.
   (If there is neither a rate nor an explicit “earn product is open/live to deposit”, output NO.)

================================================
SPECIAL HANDLING (reduce false positives)

A) Launchpool / Launchpad / “lock to share rewards”
Treat as YES ONLY if it is clearly a passive lock/stake program on a venue (e.g., “Bitget Launchpool”) WITH:
- assets to lock,
- a stated window or “now live/join,” AND
- explicit earning language (e.g., “earn/share X tokens,” “APR/APY,” “rewards” tied to locking).
If it looks like a promotion/airdrop/points campaign without clear lock/deposit mechanics or join window, => NO.

B) Generic “Stake your ETH with <protocol>” ads
If it’s only promotional with no concrete earn terms (no APY/APR/reward rate and no specific live/open product detail beyond generic staking), default NO.
Only say YES if it clearly presents an actionable staking/deposit AND either a rate OR a clearly-defined open product/pool context (e.g., “Rocket Pool rETH staking is open; mint rETH; earn staking yield”).

C) “Claim your rewards”
Claiming, distributions, retroactive rewards, airdrops, points, quests, seasons => NO
UNLESS the same message also clearly offers an enrollable deposit/stake/supply/LP mechanism to earn yield going forward (then evaluate with YES criteria).

D) Trading and market availability
Anything about “trade now”, swaps, listings, “market live”, leverage/perps, signals, funding-as-trader-PnL => NO.

E) Infrastructure/news/integration/support/collateral announcements
“Now supported”, “collateralized”, “available”, “integration”, “protocol update”, “tokenized assets”, “new LST exists” => NO
UNLESS it explicitly invites the user to supply/deposit/LP/stake in a specific market/pool to earn.

F) “Up to X%”
“Up to X% APY/APR” can be YES only if paired with:
- a specific venue + earn product context,
- specific asset(s),
- and a joinable/live signal.

================================================
TIE-BREAKERS
- When in doubt, output NO.
- If the message is primarily informational/promotional and not a concrete enrollable earn offer, output NO.
- Prefer precision over recall: avoid labeling “yes” unless the opportunity is clearly actionable and passive.

Respond with only: yes or no
Iteration 20: New subsample score 14.0 is not better than old score 14.0, skipping
Iteration 21: Selected program 5 score: 0.6262626262626263
Iteration 21: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

HARD REQUIREMENTS FOR YES (all must be satisfied):
1) ACTION: The message explicitly instructs an earn action, e.g. stake / deposit / subscribe / supply / lend / provide liquidity / add liquidity / LP / farm / lock / earn in a specific product.
2) VENUE (WHERE): The message identifies the exact venue/product:
   - a named earn product/pool/vault/farm (e.g., “Flexible Earn”, “Simple Earn”, “Savings”, “Vault”, “Pool”, “Farm”, “LP pool”, “Staking”), AND
   - the platform/protocol/exchange name is explicitly stated (e.g., Binance, Bybit, Aave, Curve) OR a clearly tied “start/join/deposit now” link/button that is explicitly for that named earn product.
3) ASSET(S): The message explicitly states the asset(s) (token symbol(s) or LP pair), e.g., BTC, USDT, AXS, ETH/USDC, MNT-USDC.
4) JOINABLE WINDOW: The message clearly indicates it is available now/live/open OR provides a clear start time/date/window (and not merely a duration/lock term).

If any one of ACTION / VENUE / ASSET(S) / JOINABLE WINDOW is missing → output NO.

CRITICAL EXCLUSIONS (override everything; if any apply → NO):
A) Competitions / prize pools / lucky draws / hunts / puzzles / leaderboards / “share of $X prize pool”
   - Even if “staking/LP” is used to earn entries/points/chances.
B) Airdrops, points systems, “reward drops”, seasons, quests, referrals, cashback, vouchers, “trade/deposit to win”, lotteries.
C) Trading-only offers (spot/perps/margin), listings, “start trading”, fee promos, routing, “zero interest”.
D) General news/partnerships/integrations/validators/tech updates/testnet/beta, unless it contains a concrete, joinable earn offer meeting ALL hard requirements.

TIME/STATUS RULES (to prevent false positives):
- PAST/STATUS-ONLY UPDATES → NO:
  If the message is primarily reporting distribution, payouts, “rewards have been distributed”, “week N benefits”, “APR was X%”, “campaign ended/closed”, “snapshot taken”, without an explicit “deposit/stake now” or a future start window → NO.
- GENERIC PRODUCT MARKETING → NO:
  If it says “earn up to X%”, “higher APY”, “max APY”, “enjoy yields”, “get started” but does NOT specify a particular pool/vault/earn product + asset(s) + joinable now/start time → NO.
- DURATION ≠ JOINABLE:
  “30-day”, “lock 30 days”, “fixed term”, “phase 3” does NOT count as joinable unless it explicitly says “live/open now” or gives a start date/time.

POSITIVE CLARIFICATIONS (when to say YES):
- “Deposit/Supply/Stake [ASSET] in/on [NAMED PRODUCT] at [VENUE] to earn [APY/APR] — live now/open” → YES.
- “LP/farm [PAIR] on [PROTOCOL] [POOL/FARM NAME] — rewards/APR shown — available now” → YES.
- A single concise line is sufficient IF it contains: action + venue/product + asset(s) + joinable now/start time, and is not excluded.

QUICK DECISION CHECKLIST (must all be “yes”):
- Do I know exactly what to do (stake/deposit/supply/lend/LP/farm/lock) from the text alone?
- Do I know exactly where (venue + named earn product/pool/vault/farm)?
- Do I know the exact asset(s) to use?
- Is it explicitly joinable now/open/live or with a clear start time/window (not just a lock duration)?
- Is it NOT distribution-only, NOT a contest/lottery/points/airdrop/seasonal drops, and NOT trading-only?

If any answer is “no” → output NO.

Respond with only: yes or no
Iteration 21: New subsample score 15.0 is not better than old score 15.0, skipping
Iteration 22: Selected program 4 score: 0.6161616161616161
Iteration 22: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, specific, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria below.

================================================
Core principle (what counts as a YES)
A message is YES only when it describes a specific earn opportunity a user can actually join (or a clearly scheduled opening) with enough concrete details to answer:
- WHAT asset(s) do I put in?
- WHERE exactly do I put them (product/pool/market)?
- HOW do I join (stake/deposit/supply/LP)?
- WHAT do I earn (rate or explicit rewards mechanics)?
- WHEN is it available (live now or explicit window)?

If you cannot answer these from the text, output NO.

================================================
YES criteria (strict)
Output "yes" ONLY if ALL conditions 1–5 are met:

1) Concrete passive-earn action is instructed or enabled
   The message explicitly tells users they can do at least one NOW (or at a stated opening time):
   - stake / restake / delegate / lock
   - deposit / subscribe / flexible or fixed savings/earn
   - lend / supply / borrow-lend “supply” side earning
   - provide liquidity / farm / deposit into a vault/strategy
   Generic suggestions like “you can stake”, “put it to work”, “earn more” without a specific offering → NO.

2) Specific venue + specific earn product context (not just a brand)
   Must name a concrete venue AND the actual earn surface:
   - CEX: “<Exchange> Earn”, “Savings”, “Simple Earn”, “Fixed Savings”, “Staking”, plus a specific product/event/pool page context.
   - DeFi: protocol + specific pool/vault/market/pair (e.g., “Aave USDC market”, “Uniswap ETH/USDC pool”, “Pendle PT… pool”).
   If it only says “on <chain>”, “on Movement”, “in our app”, or “on DeFi” with no named product/pool/market → NO.

3) Asset(s) are specified
   At least one deposit/stake/LP asset or pair is explicitly mentioned (token symbol/name).
   If only “your tokens”, “crypto”, “stablecoins” (no tickers) → NO.

4) Joinable availability signal
   Must clearly indicate the opportunity is joinable:
   - explicit CTA: “stake now”, “deposit now”, “subscribe”, “supply now”, “LP now”, “join now”
   OR
   - explicit availability window: start/end time/date, “now live”, “subscriptions open”, “opens at …”.
   “Coming soon”, “announced”, “ongoing” without any enroll/join instruction → NO.

5) Earn terms are concrete and tied to the offering
   At least one must be present and clearly associated with the venue/product in (2):
   - explicit APY/APR/reward rate, OR
   - explicit statement of rewards for that specific pool/product (e.g., “earn X token rewards”, “points per day for deposits”, “boosted rewards”), OR
   - explicit statement that deposits/staking in that specific product will earn yield/rewards (not just generic “earn rewards”).
   “Up to X%” is acceptable ONLY if it’s clearly for the named product and assets, and there is a joinable signal.

================================================
Hard NO rules (high-precision exclusions)
Always output "no" for any of the following, even if they mention “stake/earn”:

A) Generic marketing / evergreen promos without a specific offering
   - Broad ads like “Your favorite tokens can earn more”, “Fixed Savings available”, “Earn up to X%” that do NOT specify a particular pool/term/product instance, start/end window, or newly opened subscription.
   Treat these as non-actionable promotional copy → NO.

B) “You can stake/deposit/LP on <chain>” style guidance
   - Messages that list possible actions (stake, lend, provide liquidity) but do not name a specific protocol/product/pool and do not provide concrete earn terms → NO.

C) News, support, listings, integrations, governance, infra updates
   - ETF/news, protocol partnerships, validator infra, upgrades, queued proposals, “now supported”, “market live for trading”, collateral enablement, bridge support → NO unless it explicitly offers a specific earn product to join.

D) Trading/active PnL, competitions, lotteries, referrals, cashback
   - perps/leverage/trading signals, “trade to earn”, contests, leaderboards, prize pools, lucky draws, referral bonuses, card cashback → NO.

E) Airdrop/points/quest campaigns as the main mechanic
   - “season”, “quests”, “missions”, “claim rewards”, “points campaign” → NO
   EXCEPT when it is explicitly a deposit/stake/LP-based earn product with clear venue/product + assets + join instructions (still must satisfy YES criteria 1–5).

F) Pure rate commentary / analytics
   - “APY is X” without where/how to deposit now → NO.

================================================
Tie-breakers
- When in doubt, output NO.
- If the message reads like an advertisement that could be posted any day and lacks a specific pool/term/window, output NO.
- “Ongoing” or “campaign” is NOT sufficient by itself; it must still specify the exact earn product and how to enroll now.
- If the venue is a CEX and the message only says “Earn/Fixed Savings” + assets + “up to APR” but gives no term, pool instance, or enrollment context beyond generic ad copy, output NO.

Respond with only: yes or no
Iteration 22: New subsample score 15.0 is better than old score 13.0. Continue to full eval and add to candidate pool.
Iteration 22: Valset score for new program: 0.6464646464646465 (coverage 99 / 99)
Iteration 22: Val aggregate for new program: 0.6464646464646465
Iteration 22: Individual valset scores for new program: {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 0.0, 18: 0.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 0.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 0.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 0.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 0.0, 97: 0.0, 98: 0.0}
Iteration 22: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 22: Valset pareto front aggregate score: 0.8686868686868687
Iteration 22: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 2: {2}, 3: {0, 2, 3, 4, 7, 8, 9}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 7: {0, 1, 5, 6, 7, 10}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 9: {0, 1, 2, 3, 5, 6, 7, 10}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10}, 15: {0, 1, 2, 4}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 17: {0, 2, 3}, 18: {0, 1, 2, 3, 4, 9}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 20: {0, 9, 2}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10}, 28: {0, 1, 2, 3, 4, 7, 8, 9}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 33: {0, 1, 2, 4, 9}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 35: {0, 1, 3, 5, 6, 7, 8, 10}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 38: {10, 3, 4, 5}, 39: {1, 10, 5, 7}, 40: {2}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10}, 43: {1, 5, 6, 7, 8, 10}, 44: {0, 2, 3, 4, 6, 7, 8, 9}, 45: {2}, 46: {8, 9, 2}, 47: {0, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 49: {0, 1, 5, 6, 7, 10}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 51: {1, 3, 4, 5, 6, 7, 9, 10}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 53: {10, 5}, 54: {1, 3, 5, 6, 7, 10}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 56: {0, 1, 3, 5, 6, 7, 8, 10}, 57: {10, 5, 6, 7}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 59: {0, 1, 2, 4, 9}, 60: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10}, 65: {9}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 68: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 72: {1, 5, 6, 7, 8, 10}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 74: {10}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10}, 78: {1, 3, 5, 6, 7, 9, 10}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 82: {10, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 87: {4}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 93: {0, 2, 4, 7, 8, 9}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 96: {0, 1, 2, 3, 4, 8, 9}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 98: {2, 4}}
Iteration 22: Best valset aggregate score so far: 0.6767676767676768
Iteration 22: Best program as per aggregate score on valset: 1
Iteration 22: Best score on valset: 0.6767676767676768
Iteration 22: Linear pareto front program index: 1
Iteration 22: New program candidate index: 10
Iteration 23: Selected program 2 score: 0.6363636363636364
Iteration 23: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

Definition (what counts as “yield farming opportunity” here):
A message is YES only when it offers (or announces as live/upcoming with clear timing) a passive-earn action such as staking, lending/supplying, vault deposit, LP providing/farming, savings/earn product subscription, or lockup/term deposit—where a normal user can take that action.

Core rule (must be satisfied for YES):
The message itself must identify all three:
1) WHAT to do (earn action/program): stake / deposit / supply / lend / lock / provide liquidity (LP) / farm / vault / savings/earn product.
2) WHERE to do it: a specific joinable venue + product/pool/vault/earn plan (protocol/app/exchange + named feature like “Earn”, “Savings”, “Fixed”, “Vault”, “Pool”, “Farm”, “Staking”, “Lending market”).
3) WHICH asset(s): at least one specific token/coin or LP pair (e.g., USDC, ETH, SOL, WBTC, $U, ETH/USDC LP).

If any of (1)-(3) is missing → NO.

Joinable timing rule:
- Assume joinable NOW unless the message clearly says it is in the past, ended, closed, waitlist-only, or institutional/private.
- If it’s future, it can still be YES only if a clear start time/date/window is stated AND (1)-(3) are satisfied.

YES (any case that meets Core rule):
A) Explicit earn action + venue/product + asset(s)
   - “Stake X on Y”, “Deposit X into Y Vault”, “Supply X on Y”, “Provide liquidity to X/Y on Z”, etc.

B) Earn product announcement with implicit action
   - If the message names a specific earn product/plan + asset(s) and indicates earning (APY/APR/rewards/interest), treat the action as “deposit/subscribe” even if not spelled out.
   - Examples of acceptable WHERE phrases when paired with assets: “Binance Earn”, “OKX Earn”, “Bybit Earn”, “KuCoin Earn Fixed Promotion”, “Savings”, “Simple Earn”, “Fixed/Term”, “Launchpool” (only if it’s staking/locking), “Vault”, “Farm”, “Pool”, “Staking”.

C) Explicit APY/APR (or fixed rate) tied to a specific product for a specific asset
   - “16% APY on $U deposits via Binance Wallet into Lista Vault” → YES.

D) “Live/Now available” earn launch
   - “Staking is live” / “Vault launched” is YES only if venue/product + asset(s) are present.

Hard NO (common traps):
1) Vague yield marketing
   - “Earn up to X%”, “high APY”, “top returns”, “start earning” without BOTH a specific product/venue AND specific asset(s) → NO.

2) Trading-only or market announcements
   - Listings, new trading pairs, perps, leverage, “trade now”, spot/contract launch, ETFs, price talk → NO.

3) Non-yield incentives
   - Airdrops/claims, points, quests, Zealy, referrals, giveaways, lotteries, “trade to win”, competitions, cashback → NO (even if “rewards” is mentioned).

4) News/partnerships/tech/infrastructure
   - Integrations, standards, protocol updates, hires, AMAs, institutional narratives → NO unless it clearly contains a joinable earn product per Core rule.

5) Mining profitability / active work
   - PoW/CPU/GPU mining returns, “profitability reports” → NO.

6) Not accessible
   - Institutional-only/private/closed beta/no public participation path → NO.

Disambiguation rules:
- “Rewards distributed/recap” alone → NO.
- “Borrow” is NOT passive yield; it’s typically a cost. Only say YES if the user is being told to supply/deposit/LP to earn yield (borrowing mentioned as a strategy is fine only if deposit/earn is explicit and meets Core rule).
- “Staking” for governance/security with no venue/product or no asset named → NO.

Output format:
Respond with only one token: yes or no.
Iteration 23: New subsample score 15.0 is not better than old score 15.0, skipping
Iteration 24: Selected program 9 score: 0.6060606060606061
Iteration 24: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

========================
DECISION STANDARD (STRICT)
========================
Say YES only when the message itself provides enough actionable details for a user to participate without guessing the earn action, the venue, or the asset(s).

Core requirements for YES (must all be met):
1) WHAT: a passive earn action/product is clearly indicated:
   - stake/staking, deposit, supply/lend, lock, provide liquidity/LP, farm, vault, pool, gauge, savings/earn, fixed/term earn, validator staking
   - OR a pool/vault/market clearly implies deposit/LP to earn incentives (e.g., “pool is live”, “vault live”, “market supplying earns X%”)
2) WHERE: a specific joinable venue AND a specific product/pool/vault/market name (or uniquely identifying feature):
   - Venue examples: Aave, Morpho, Curve, Convex, Uniswap, Pendle, Frax, Origin, Binance Earn, OKX Earn, Bybit Earn, etc.
   - Product examples: “PegKeeper pool”, “USDC market”, “ETH/USDC v3 0.05%”, “OUSD vault”, “Flexible Savings”, etc.
   - NOT enough: only a chain/ecosystem (“on Starknet/Solana/Sei”), or only a generic “earn on our app” without a named pool/vault/market.
3) WHICH ASSET(S): at least one specific token/coin or LP pair is named (e.g., frxUSD, OUSD, USDC, ETH/USDC LP).

If any of (1)-(3) is missing → NO.

APY/APR is not required if (1)-(3) are clearly satisfied, but it strengthens YES.

Assume “live now” unless the message clearly indicates future-only, ended, closed, waitlist, or invite-only.

=========================================
IMPORTANT: DO NOT ADD EXTRA REQUIREMENTS
=========================================
Do NOT require that the opportunity is “limited time”, “boosted”, “early”, or “outsized rewards”.
If the message advertises a standard staking/earn product that is joinable now and meets WHAT+WHERE+ASSET(S) → YES.

=================================
IMPORTANT: FILTER OUT “YIELD-LIKE”
=================================
Even if the text contains words like “yield”, “rewards”, “earn”, say NO when it is not a concrete joinable earn offer.

Explicit NO categories:
- Points/XP multipliers, points campaigns, quests, Zealy/Galxe tasks, badges → NO.
- Cashback, card spend rewards, lucky draws, raffles, lotteries, giveaways, referral contests → NO.
- Trading-only: listings, new pairs, “trade now”, perps, leverage trading, fee discounts, airdrop for trading → NO.
- Pure news/product vision/tech updates without participation instruction or clear joinable pool/vault/market + asset(s) → NO.
- Past-only: “rewards distributed”, “recap”, “congrats to stakers” with no ongoing join invitation/details → NO.
- Institutional/private/closed beta without public participation instructions → NO.

=============================================
YES SIGNALS (SUFFICIENT WHEN CORE REQS MET)
=============================================
Say YES when core requirements are met via any of these patterns:

A) Explicit instruction:
- “Stake/deposit/supply/lend/lock/LP/farm” + named venue/product/pool/vault/market + asset(s).

B) Pool/vault/market live / launched (implied deposit) with assets:
- “X pool/vault/market is live/launched” on a named venue AND it specifies the asset(s).
  Example: “A new frxUSD PegKeeper pool with OriginProtocol OUSD is live” → YES.

C) Rates tied to a specific product with assets:
- “Earn 12% APR on [asset] in [named product] on [venue]” → YES.

D) “Get started” / link CTA is OPTIONAL:
- If the offer is otherwise specific, absence of a link does not block YES.

========================================
HANDLING “LISTS / OVERVIEWS” EDGE CASE
========================================
Sometimes messages mention multiple strategies/pools without listing each one.
Treat as YES if ALL are true:
- It clearly states there are one or more active “strategies/vaults/pools/markets” earning yield on a named venue/app,
- It specifies the asset class or asset(s) (e.g., “USD-based strategies”, “USDC strategies”, “ETH vaults”) AND this is sufficient to know what you would deposit,
- It indicates they exist now (e.g., “currently earning”, “live now”).
If it only says “we will launch soon” or is purely promotional with no current joinable product → NO.

========================
FINAL CHECKLIST (ALL MUST BE TRUE FOR YES)
========================
- Do I know WHAT passive-earn action/product is offered (explicitly or clearly implied by pool/vault/market)?
- Do I know WHERE (named venue + specific product/pool/vault/market)?
- Do I know WHICH asset(s) to deposit/stake/LP?
If any answer is “no” → output no.

Respond with only: yes or no
Iteration 24: New subsample score 15.0 is better than old score 13.0. Continue to full eval and add to candidate pool.
Iteration 24: Valset score for new program: 0.6262626262626263 (coverage 99 / 99)
Iteration 24: Val aggregate for new program: 0.6262626262626263
Iteration 24: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 1.0, 18: 0.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 0.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 0.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 0.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 0.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 24: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 24: Valset pareto front aggregate score: 0.8686868686868687
Iteration 24: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11}, 2: {2}, 3: {0, 2, 3, 4, 7, 8, 9, 11}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 7: {0, 1, 5, 6, 7, 10}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11}, 15: {0, 1, 2, 4}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 17: {0, 11, 2, 3}, 18: {0, 1, 2, 3, 4, 9}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 20: {0, 9, 2}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 33: {0, 1, 2, 4, 9}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 35: {0, 1, 3, 5, 6, 7, 8, 10}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 38: {10, 3, 4, 5}, 39: {1, 10, 5, 7}, 40: {2}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11}, 43: {1, 5, 6, 7, 8, 10, 11}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11}, 45: {2, 11}, 46: {8, 9, 2, 11}, 47: {0, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 49: {0, 1, 5, 6, 7, 10, 11}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 53: {10, 5}, 54: {1, 3, 5, 6, 7, 10}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 56: {0, 1, 3, 5, 6, 7, 8, 10}, 57: {5, 6, 7, 10, 11}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 59: {0, 1, 2, 4, 9, 11}, 60: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10}, 65: {9}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 68: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 72: {1, 5, 6, 7, 8, 10, 11}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 74: {10}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11}, 78: {1, 3, 5, 6, 7, 9, 10, 11}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 82: {10, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 87: {4}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 93: {0, 2, 4, 7, 8, 9}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 96: {0, 1, 2, 3, 4, 8, 9, 11}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 98: {2, 4}}
Iteration 24: Best valset aggregate score so far: 0.6767676767676768
Iteration 24: Best program as per aggregate score on valset: 1
Iteration 24: Best score on valset: 0.6767676767676768
Iteration 24: Linear pareto front program index: 1
Iteration 24: New program candidate index: 11
Iteration 25: Selected program 9 score: 0.6060606060606061
Iteration 25: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

========================
DECISION STANDARD (STRICT)
========================
Say YES only when the message itself provides a concrete, joinable earn offer with enough specifics to act without guessing.

Core requirements for YES (all must be satisfied):
1) WHAT (passive earn mechanism):
   - stake/staking, deposit, lend/supply, lock, provide liquidity/LP, farm, vault, pool, savings/earn, flexible savings, fixed/term earn, “hold to earn”/“just hold” programs that pay APR/APY, validator staking.
   - Must be passive yield/rewards on held/deposited assets (not trading/competition tasks).

2) WHERE (joinable venue + earn product/feature):
   - A specific platform/app/exchange/protocol AND a specific earn feature/product name.
   - Examples that satisfy WHERE:
     - “MEXC Savings”, “MEXC Flexible Savings”, “Binance Earn Simple Earn”, “OKX Earn”, “Bybit Savings/Earn”, “KuCoin Earn”
     - DeFi: “Aave supply”, “Morpho market”, “Uniswap v3 pool”, “Curve pool”, “Pendle pool”, “Yearn vault”, etc.
   - Not enough: only chain/ecosystem (“on Solana/Starknet”), only protocol name without an earn feature, or generic “earn on X”.

3) WHICH ASSET(S):
   - At least one explicit token/coin or LP pair (e.g., USDD, ETH, USDC, ETH/USDC LP).

If ANY of (1)-(3) is missing → NO.

“Live now” is assumed unless the message clearly says future-only (and no start time), ended, closed, or invite-only.

=================================
IMPORTANT: FILTER OUT “YIELD-LIKE”
=================================
Even if the text contains “yield/earn/rewards/APR/APY”, say NO if it’s not a concrete, joinable passive-earn offer.

Explicit NO categories:
- Points/XP/“kPoints”/multipliers, quests, missions, Zealy/Galxe, badges → NO.
- Trading competitions, “trade to win”, volume leaderboards, lotteries, raffles, airdrop-only hype without deposit/stake mechanics → NO.
- Listings, leverage/perp markets, “now listed”, “qualify for boosts” tied to trading → NO.
- General product/news/marketing (“designed to deliver yield”, dashboards showing APR, comparisons) without an instruction/offer to deposit/stake + asset + venue feature → NO.
- Past-only recaps (“rewards distributed”) without an ongoing joinable earn offer → NO.
- Institutional/private/closed beta without public participation instructions → NO.

========================
WHEN TO SAY YES (SUFFICIENT)
========================
YES if (1)-(3) are met and one of these is present:

A) Explicit instruction:
- “Stake/deposit/supply/lend/lock/provide liquidity/farm/subscribe” + venue/feature + asset(s).

B) Explicit earn offer (even without verbs) that clearly implies joinability:
- “USDD on MEXC earns up to 8% APR”, “Earn up to 6% APR with MEXC Flexible Savings”, “USDC in Binance Simple Earn 5% APY”
- Phrases like “just hold”, “no lock”, “daily rewards”, “flexible to redeem” COUNT as WHAT only if a venue/earn feature is named and an APR/APY or “earns” wording is present.

C) Earn promotion with start time/window:
- “Promotion starts …” + venue/feature + asset(s) (rate optional but helpful).

========================
COMMON POSITIVE PATTERNS (COUNT AS YES IF SPECIFIC)
========================
- CeFi hold-to-earn / savings:
  - “Just hold”, “no lock up”, “daily rewards”, “flexible savings”, “simple earn”
  - These are YES when tied to a named exchange/earn feature AND a token AND states earning/APR/APY.
- DeFi pools/vaults:
  - Named protocol + named pool/vault/market + asset(s), even if APR not shown.

========================
FINAL CHECKLIST (ALL MUST BE TRUE FOR YES)
========================
- WHAT passive-earn action/product is offered (including “hold to earn” savings programs)?
- WHERE is the named venue AND named earn feature/product/pool/vault/market?
- WHICH asset(s) are eligible?
If any answer is “no” → output no.

Respond with only: yes or no
Iteration 25: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 25: Valset score for new program: 0.6060606060606061 (coverage 99 / 99)
Iteration 25: Val aggregate for new program: 0.6060606060606061
Iteration 25: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 0.0, 28: 0.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 0.0, 36: 0.0, 37: 1.0, 38: 1.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 0.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 25: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 25: Valset pareto front aggregate score: 0.8686868686868687
Iteration 25: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}, 2: {2}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 7: {0, 1, 5, 6, 7, 10}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12}, 15: {0, 1, 2, 4}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 17: {0, 2, 3, 11, 12}, 18: {0, 1, 2, 3, 4, 9, 12}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 20: {0, 9, 2}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 33: {0, 1, 2, 4, 9}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 35: {0, 1, 3, 5, 6, 7, 8, 10}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 38: {3, 4, 5, 10, 12}, 39: {1, 10, 5, 7}, 40: {2}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12}, 43: {1, 5, 6, 7, 8, 10, 11}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12}, 45: {2, 11}, 46: {8, 9, 2, 11}, 47: {0, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 49: {0, 1, 5, 6, 7, 10, 11}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 53: {10, 5}, 54: {1, 3, 5, 6, 7, 10}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 56: {0, 1, 3, 5, 6, 7, 8, 10}, 57: {5, 6, 7, 10, 11, 12}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 59: {0, 1, 2, 4, 9, 11, 12}, 60: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10}, 65: {9}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 68: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 72: {1, 5, 6, 7, 8, 10, 11, 12}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 74: {10, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 82: {10, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 87: {4}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 93: {0, 2, 4, 7, 8, 9}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 98: {2, 4}}
Iteration 25: Best valset aggregate score so far: 0.6767676767676768
Iteration 25: Best program as per aggregate score on valset: 1
Iteration 25: Best score on valset: 0.6767676767676768
Iteration 25: Linear pareto front program index: 1
Iteration 25: New program candidate index: 12
Iteration 26: Selected program 2 score: 0.6363636363636364
Iteration 26: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

Definition (what counts as yield farming here):
A message is YES only when it offers (or announces as live) a passive earning mechanism such as staking, lending/supplying, vault deposit, liquidity provision/LP farming, savings/earn programs, fixed/locked/flexible earn products, or similar on-chain/off-chain earn products.

Core rule (must be actionable from the message alone):
Say YES only if the message provides enough to act by identifying:
1) WHAT: an earn mechanism (stake/deposit/supply/lend/lock/LP/farm/vault/earn/savings/launchpool/validator delegating)
AND
2) WHERE: a specific venue or product that is joinable (protocol/app/platform + a named feature/product/pool/vault/market/program)
AND
3) WHICH asset(s): at least one specific token/coin or LP pair OR it explicitly states “no deposit minimum” / “any deposit” while still being an earn product (see “asset exception” below).

If any of (1)-(3) is missing → NO, unless a listed exception applies.

Key YES exceptions (to reduce false NOs while staying strict):
1) Asset exception for “no minimum / any deposit”:
   - If the message clearly presents a live earn product/program and explicitly indicates deposits of any size (e.g., “no deposit minimums”) AND the venue/product is named AND a yield/rate is given (APR/APY/target yield), then YES even if the specific asset is not named.
   - Still require an actual earn product/program (not just “institutional grade yield” marketing alone).

2) Implicit action via clear earn product naming:
   - If the message names an unmistakable earn product/program + venue AND specifies asset(s) AND gives a yield/rate or explicitly says “earn rewards/yield”, treat the action as implied → YES.

3) “Live/Now available” launches:
   - “Staking is live / Earn is live / Vault launched / Farm is live / Incentives are live” can be YES if venue + earn product context + asset(s) are present (rate optional).

Strong YES signals (any, but still must satisfy core rule or an exception):
- Explicit APY/APR/reward rate tied to a named pool/vault/product.
- Clear instruction like “stake now”, “deposit”, “supply”, “add liquidity”, “farm”, “enter vault”.
- Named platforms: Aave/Morpho/Compound/Euler/Spark/Kamino/PancakeSwap/Uniswap/Curve/Balancer/Convex/Lido/Rocket Pool plus CEX earn products (Binance Earn/Savings, OKX Earn, Bybit Earn, KuCoin Earn/Fixed Promotion, Gate Earn, MEXC Launchpool, etc.) when paired with a specific product and asset(s) (or the “no minimum” exception).

NO conditions (common traps):
A) Vague yield marketing / brand claims without enough specifics
   - “earn”, “high APR”, “up to X%”, “institutional grade yield”, “targeting X%” WITHOUT a specific joinable product/program context AND venue → NO.
   - If venue is named but no identifiable earn product/program/pool/vault AND no actionable participation details → NO.

B) Missing asset(s)
   - If the asset is not specified → NO, except the “no deposit minimum / any deposit” exception above.

C) Non-yield incentives
   - Airdrops/points/quests/Zealy/leaderboards, giveaways, cashback/card rewards, referrals, lotteries, “trade to win”, competitions, funded trading accounts, leverage trading promos → NO.

D) Trading/news/infrastructure only
   - Listings, trading pairs, market launches, partnerships, SDK/tech updates, general revenue sharing narratives → NO unless there is a concrete earn action/product as per core rule.

E) Past distribution/status-only
   - “Rewards distributed”, “recap”, “airdrop sent”, “points credited” → NO unless it also invites joining an ongoing earn product with venue + asset(s) (or valid exception).

F) Not accessible
   - Explicitly institutional-only/private/closed beta with no public join path/time window → NO.

Decision procedure:
1) Identify if the message is about passive earning (staking/lending/vault/LP/earn product). If not → NO.
2) Check WHERE: is a specific venue + product/pool/vault/program named and plausibly joinable? If not → NO.
3) Check WHICH asset(s): if at least one asset/pair is named → proceed; else only allow YES if the “no deposit minimum / any deposit” exception is satisfied.
4) If still uncertain → NO.

Respond with only: yes or no
Iteration 26: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 26: Valset score for new program: 0.5757575757575758 (coverage 99 / 99)
Iteration 26: Val aggregate for new program: 0.5757575757575758
Iteration 26: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 0.0, 10: 1.0, 11: 0.0, 12: 1.0, 13: 1.0, 14: 0.0, 15: 0.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 0.0, 22: 1.0, 23: 0.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 0.0, 28: 1.0, 29: 0.0, 30: 0.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 0.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 1.0, 41: 1.0, 42: 0.0, 43: 0.0, 44: 1.0, 45: 0.0, 46: 1.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 0.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 26: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 26: Valset pareto front aggregate score: 0.8787878787878788
Iteration 26: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13}, 2: {2, 13}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 7: {0, 1, 5, 6, 7, 10}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12}, 15: {0, 1, 2, 4}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 17: {0, 2, 3, 11, 12, 13}, 18: {0, 1, 2, 3, 4, 9, 12, 13}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 20: {0, 9, 2, 13}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 33: {0, 1, 2, 4, 9, 13}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 35: {0, 1, 3, 5, 6, 7, 8, 10}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 38: {3, 4, 5, 10, 12}, 39: {1, 10, 5, 7}, 40: {2, 13}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12}, 43: {1, 5, 6, 7, 8, 10, 11}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13}, 45: {2, 11}, 46: {2, 8, 9, 11, 13}, 47: {0, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 49: {0, 1, 5, 6, 7, 10, 11}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 53: {10, 5}, 54: {1, 3, 5, 6, 7, 10}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 56: {0, 1, 3, 5, 6, 7, 8, 10}, 57: {5, 6, 7, 10, 11, 12}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 59: {0, 1, 2, 4, 9, 11, 12, 13}, 60: {13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 68: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 72: {1, 5, 6, 7, 8, 10, 11, 12}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 74: {10, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 82: {10, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 87: {4}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 93: {0, 2, 4, 7, 8, 9, 13}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 98: {2, 4}}
Iteration 26: Best valset aggregate score so far: 0.6767676767676768
Iteration 26: Best program as per aggregate score on valset: 1
Iteration 26: Best score on valset: 0.6767676767676768
Iteration 26: Linear pareto front program index: 1
Iteration 26: New program candidate index: 13
Iteration 27: Selected program 4 score: 0.6161616161616161
Iteration 27: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria below.

------------------------------------------------------------
YES (strict, actionable, not marketing)
Say "yes" ONLY if the message clearly provides a concrete, joinable earn action with enough details to answer:
“What should I do (stake/deposit/supply/LP), with which asset(s), and where?”

Requirements (ALL must be met):

1) Passive earn action (explicit & user-doable)
   The message explicitly tells the user they can do at least one of:
   - stake / restake / delegate / lock
   - deposit / subscribe to Earn/Savings/Fixed/Flexible
   - lend / supply / borrow-lend (as supplier) to earn
   - provide liquidity / farm / deposit into a vault/strategy
   Must be framed as something the user can participate in now or within a stated time window.

2) Specific venue + earn product context (not just a brand name)
   Must name WHERE the earning happens with an earn context, e.g.:
   - CEX: “<Exchange> Earn / Savings / Fixed Savings / Simple Earn / Dual Investment” etc.
   - DeFi: protocol/app + specific pool/vault/market/farm (pair, vault name, market, chain)
   If the venue is named but the earn product/pool is not clear → NO.

3) Asset(s) specified
   Must explicitly mention at least one asset to stake/deposit/supply/LP (ticker/name or pair),
   e.g., ETH, USDT, SOL, SOSO, ETH-USDC, MAG7.ssi.
   If no asset is stated → NO.

4) Joinable/live signal (actionable now)
   Must include at least one clear “can act now” indicator:
   - “stake now / deposit now / subscribe now / supply now / provide liquidity now / open now”
   - or “now live / launched” for the earn product/pool
   - or a clear start/end window for participation
   If it’s only “coming soon”, “next epoch”, “pool loading” without a current action → NO.

5) Earn mechanics are explicit for THIS offer
   Must include at least one of:
   a) a concrete yield/reward rate or terms tied to the offer (APY/APR/% boost/rewards rate), OR
   b) an explicit statement that users earn yield/rewards by doing the specified earn action in the specified product/pool (even if no % is given), AND it is live/joinable.
   Generic “earn”, “high yield”, “boost earnings” without tying to a specific enrollable product/pool → NO.

------------------------------------------------------------
Automatic NO rules (hard exclusions / common traps)
Always output "no" if ANY of the following apply:

A) Trading-only / active PnL:
   perps, futures, leverage, signals, “trade now”, DEX aggregator, listings for trading, “market live” for trading.

B) Competitions / leaderboards / lotteries / lucky draws / prize pools / referral contests / giveaways:
   even if it mentions “subscriptions decide rank” or “earn points” or “win USDC”.

C) Pure news / integration / support announcements:
   wallet integration, chain support, bridges, “now supported”, analytics commentary, buybacks, treasury updates.

D) Airdrop/points/quest campaigns as the primary mechanic:
   “claim rewards”, “epoch rewards”, “airdrop”, “points”, “quests”, “season”
   EXCEPT when the message ALSO clearly offers a live, deposit/stake/supply/LP-based earn product meeting ALL YES requirements.
   If it’s mainly “claim” with no clear current deposit/stake offer details → NO.

E) Vague CEX marketing with missing essentials:
   If the message mentions an earn product like “MEXC Fixed Savings / Binance Earn / HTX Earn” but lacks EITHER:
   - the asset(s), OR
   - a specific rate/terms OR explicit pool/product availability for a specific asset,
   then → NO.
   (Example: “% APR … check out MEXC Fixed Savings” with no asset/rate → NO.)

F) “Up to X%” without specifics:
   “up to X% APY” is NO unless it also includes venue + specific earn product context + asset(s) + joinable/live signal.

------------------------------------------------------------
Tie-breakers
- When in doubt, choose NO.
- If you cannot clearly extract: venue/product + action + asset(s) + (rate/explicit earning statement) + joinable-now signal → NO.
- “Stake now” with a specified token on a named protocol counts as YES even if the message also mentions an airdrop, as long as it is a real staking action and clearly live.

Respond with only: yes or no
Iteration 27: New subsample score 14.0 is better than old score 13.0. Continue to full eval and add to candidate pool.
Iteration 27: Valset score for new program: 0.6363636363636364 (coverage 99 / 99)
Iteration 27: Val aggregate for new program: 0.6363636363636364
Iteration 27: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 0.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 27: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 27: Valset pareto front aggregate score: 0.8787878787878788
Iteration 27: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14}, 2: {2, 13}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 7: {0, 1, 5, 6, 7, 10, 14}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14}, 15: {0, 1, 2, 4, 14}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 17: {0, 2, 3, 11, 12, 13, 14}, 18: {0, 1, 2, 3, 4, 9, 12, 13}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 20: {0, 2, 9, 13, 14}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 33: {0, 1, 2, 4, 9, 13}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 38: {3, 4, 5, 10, 12}, 39: {1, 10, 5, 7}, 40: {2, 13}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14}, 43: {1, 5, 6, 7, 8, 10, 11}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14}, 45: {2, 11}, 46: {2, 8, 9, 11, 13}, 47: {0, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 49: {0, 1, 5, 6, 7, 10, 11}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 53: {10, 5}, 54: {1, 3, 5, 6, 7, 10}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14}, 57: {5, 6, 7, 10, 11, 12}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14}, 60: {13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10, 14}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 68: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 74: {10, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 82: {10, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 87: {4}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 93: {0, 2, 4, 7, 8, 9, 13}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}, 98: {2, 4}}
Iteration 27: Best valset aggregate score so far: 0.6767676767676768
Iteration 27: Best program as per aggregate score on valset: 1
Iteration 27: Best score on valset: 0.6767676767676768
Iteration 27: Linear pareto front program index: 1
Iteration 27: New program candidate index: 14
Iteration 28: Selected program 13 score: 0.5757575757575758
Iteration 28: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

Definition (what counts as yield farming here):
YES only when the message offers (or announces as live) a passive earning mechanism such as staking, lending/supplying, vault deposit, liquidity provision/LP farming, liquidity mining, farm, earn/savings products, launchpool, validator delegation, or similar earn products.

Core rule (must be actionable from the message alone):
Say YES only if the message provides enough to act by identifying:
1) WHAT: an earn mechanism (stake/deposit/supply/lend/lock/LP/farm/vault/earn/savings/launchpool/validator delegate)
AND
2) WHERE: a specific, joinable venue + named product/pool/vault/market/program (protocol/app/platform + feature name)
AND
3) WHICH asset(s): at least one specific token/coin or LP pair.

If any of (1)-(3) is missing → NO, unless an exception below applies.

Critical clarification to prevent false YES (campaign/extension/continuation posts):
Even if the message mentions “rewards”, “APR”, “incentives”, “extended”, “week X”, “phase”, “continuing”, “airdrop boosters”, etc., output YES ONLY if the message itself clearly enables a NEW user to join, by including at least one of:
- an explicit call to action for new participants (e.g., “deposit/supply/stake/add liquidity now to join”)
- an access path or location (link, “in the app”, “on [platform] Earn”, “in [protocol] pool/vault/market”, or a clearly named product page)
- or a clearly stated start window for joining.

If it only talks to existing participants (e.g., “Already deposited? just keep your position”, “automatically included”, “rewards extended”) and does NOT clearly invite/enable new joining → NO.

Key YES exceptions (narrow; keep strict):
1) Asset exception for “any deposit / no minimum”:
   - If the message clearly presents a live earn product/program AND explicitly indicates deposits of any size (e.g., “no minimum”, “any amount”) AND the venue + product/program is named AND a yield/rate is given (APR/APY/target yield), then YES even if the specific asset is not named.
   - Still require a concrete earn product/program (not generic marketing).

2) Implicit action via clear earn product naming:
   - If the message names an unmistakable earn product/program + venue AND specifies asset(s) AND explicitly states “earn yield/rewards/APR/APY” (rate optional), treat action as implied → YES.

3) “Live/Now available” launches:
   - “Staking is live / Vault launched / Farm is live / Earn is live / Incentives are live” can be YES if venue + earn product context + asset(s) are present (rate optional), and it’s not only a recap/status update.

Strong YES signals (helpful but not sufficient alone; still must satisfy core rule/exception):
- Explicit APY/APR/reward rate tied to a named pool/vault/product.
- Clear instruction: “stake now”, “deposit”, “supply”, “add liquidity”, “farm”, “enter vault”, “subscribe”, “join launchpool”.
- Named venues with a specific earn product: Aave/Morpho/Compound/Euler/Spark/Kamino/PancakeSwap/Uniswap/Curve/Balancer/Convex/Lido/Rocket Pool, and CEX earn products (Binance Earn/Savings, OKX Earn, Bybit Earn, KuCoin Earn/Fixed Promotion, Gate Earn, MEXC Launchpool, etc.) WHEN paired with a specific product + asset(s) (or the “any deposit/no minimum” exception).

NO conditions (common traps):
A) Vague yield marketing:
   - “earn”, “high APR”, “up to X%”, “targeting X%”, “institutional yield” without a specific joinable product/pool/vault/program + venue → NO.

B) Incentive/campaign posts that don’t enable joining:
   - Reward extensions, top-ups, emission announcements, “X tokens added to rewards”, “rewards for next 2 weeks”, “already deposited keep position”, “automatically included” without clear join instructions/path → NO.

C) Missing asset(s):
   - If asset/pair is not specified → NO, except the “any deposit/no minimum” exception.

D) Non-yield incentives:
   - Airdrops/points/quests/Zealy/leaderboards, giveaways, cashback/card rewards, referrals, lotteries, “trade to win”, competitions, funded trading promos, “APR boosters” coupons → NO (unless it is clearly an actual staking/lending/LP product with venue+product+asset and joinable now).

E) Trading/news/infrastructure:
   - Listings, trading pairs, perps/futures, partnerships, tech updates, bridges/transfers → NO unless there is a concrete earn product action per core rule.

F) Past distribution/status-only:
   - “Rewards distributed”, “recap”, “week in review” → NO unless it also invites joining an ongoing earn product with venue + product + asset(s) (or valid exception).

G) Not accessible:
   - Institutional-only/private/closed beta with no public join path/window → NO.

Decision procedure:
1) Is there a passive earning mechanism (staking/lending/vault/LP/earn)? If not → NO.
2) WHERE: does it name a specific venue + named product/pool/vault/market/program that is plausibly joinable? If not → NO.
3) WHICH: does it specify at least one asset/pair? If not → NO unless “any deposit/no minimum” exception applies.
4) Joinability check: does this message enable a new user to join now (CTA/path/start window), or is it only a continuation/status message to existing users? If only continuation/status → NO.
5) If still uncertain → NO.

Respond with only: yes or no
Iteration 28: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 28: Valset score for new program: 0.6060606060606061 (coverage 99 / 99)
Iteration 28: Val aggregate for new program: 0.6060606060606061
Iteration 28: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 0.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 0.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 0.0, 36: 0.0, 37: 1.0, 38: 1.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 0.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 0.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 28: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 28: Valset pareto front aggregate score: 0.8787878787878788
Iteration 28: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15}, 2: {2, 13}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 7: {0, 1, 5, 6, 7, 10, 14}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15}, 15: {0, 1, 2, 4, 14}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 17: {0, 2, 3, 11, 12, 13, 14, 15}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 20: {0, 2, 9, 13, 14, 15}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 33: {0, 1, 2, 4, 9, 13, 15}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 38: {3, 4, 5, 10, 12, 15}, 39: {1, 10, 5, 7}, 40: {2, 13}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15}, 43: {1, 5, 6, 7, 8, 10, 11}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14}, 45: {2, 11}, 46: {2, 8, 9, 11, 13}, 47: {0, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 49: {0, 1, 5, 6, 7, 10, 11}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 53: {10, 5}, 54: {1, 3, 5, 6, 7, 10}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15}, 57: {5, 6, 7, 10, 11, 12}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14}, 60: {13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10, 14}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 68: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 74: {10, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 82: {10, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 87: {4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 93: {0, 2, 4, 7, 8, 9, 13, 15}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 98: {2, 4, 15}}
Iteration 28: Best valset aggregate score so far: 0.6767676767676768
Iteration 28: Best program as per aggregate score on valset: 1
Iteration 28: Best score on valset: 0.6767676767676768
Iteration 28: Linear pareto front program index: 1
Iteration 28: New program candidate index: 15
Iteration 29: Selected program 13 score: 0.5757575757575758
Iteration 29: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

Definition (what counts as yield farming here):
YES only when the message offers or announces as available a passive earning mechanism such as:
- staking / restaking / delegation / validator staking
- lending/supplying/borrowing-based earn (supply APY, lending markets)
- vault deposits / strategy vaults / earn vaults
- liquidity provision / LP farming / farms / gauges / incentives for LPs
- savings/earn programs on CEX/DEX (fixed/flexible/locked), launchpool/launchpad staking-type earns
- on-chain fee-share staking if it clearly describes staking/depositing a token to earn fees/rewards

What does NOT count:
- trading-only actions (buy/sell, leverage, “strategy: long/short”, “trade to win”)
- airdrops, points, quests, Zealy, giveaways, lotteries, raffles, lucky draws, “reward pools” for tasks
- “apply/whitelist/DM admin” creator programs or promotions unrelated to depositing crypto to earn yield
- general news/marketing (“earn up to”, “highest yields”, “yield optimization”) without a concrete joinable product
- status/recaps (“rewards distributed”) without inviting joining an ongoing earn product with specifics

Hard requirement (must be actionable from the message alone):
Say YES only if ALL of the following are satisfied:

1) WHAT (earn mechanism) is present:
   - explicit earn action or product type: stake, deposit, supply, lend, lock, farm, LP, add liquidity, vault, earn, savings, launchpool, “supply APY”, “borrow incentives”, “staking is live”, etc.

2) WHERE (joinable venue + specific product context) is present:
   - a specific protocol/app/exchange is named (e.g., Aave, Morpho, Kamino, Yearn, Binance, OKX, etc.)
   AND at least ONE of:
     a) a named feature/product/pool/vault/market/program (e.g., “USDT market”, “cbBTC supply”, “Vaults”, “Launchpool”, “Earn”, “Liquidity Vaults”, “xTOKEN staking”)
     b) a clear “live/now available” announcement tied to that venue’s earn feature (e.g., “Staking live on X”, “X Vaults launched”)

3) WHICH asset(s) are present:
   - at least one specific token/coin or LP pair is named (e.g., USDT, ETH, wETH, cbBTC, ORCA-xORCA, ETH/USDC)
   - token symbols and common wrapped variants count.

If any of (1)-(3) is missing → NO, unless an explicit exception below applies.

Allowed YES exceptions (narrow; still strict):

E1) “No minimum / any deposit” exception (asset omitted):
- YES if the message clearly describes a live/joinable earn product on a named venue with named earn feature (e.g., “X Vaults/Earn/Savings”) AND explicitly says “no minimum(s)” / “any amount” / “withdraw anytime” or equivalent AND includes an APY/APR/rate (“up to X%”) even if assets are not listed.

E2) Asset implied by unmistakable single-asset product name:
- YES if the product name itself unambiguously contains the asset (e.g., “cbBTC supply”, “USDT Earn”, “ETH staking”) even if the asset isn’t repeated elsewhere.

Rate handling:
- A stated APR/APY strongly supports YES but is NOT required if the message clearly announces a live earn product with venue + feature + asset(s).
- “Up to X%” counts as a rate only if tied to a named earn product/feature (not general marketing).

Actionability filter (avoid false YES on vague marketing):
Even if “earn/yield” is mentioned, output NO if the message is only a generic pitch without a joinable product context, e.g.:
- “Earn fees & rewards with [protocol] vaults” with no asset(s) and no rate and no concrete pool/vault/program named.
- “Institutional grade yield optimization” without deposit instructions or identifiable product.

Accessibility filter:
- If it’s clearly not publicly joinable now (institutional-only, closed beta, invite-only with no public start window) → NO.

Decision procedure (follow in order):
1) Is there a passive earning mechanism (staking/supply/vault/LP/earn/savings)? If not → NO.
2) Is there a specific venue + joinable earn feature/product context? If not → NO.
3) Are asset(s) specified? If yes → YES (assuming not a NO condition).
4) If assets are missing, only return YES if E1 applies (or E2).
5) If still uncertain → NO.

Respond with only: yes or no
Iteration 29: New subsample score 14.0 is not better than old score 15.0, skipping
Iteration 30: Selected program 10 score: 0.6464646464646465
Iteration 30: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, specific, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria below.

================================================
Core principle (what counts as a YES)
YES only when the message, by itself, presents a concrete earn action that a user can take now (or at an explicitly stated opening time) to earn yield/rewards, with enough specificity to identify:
- WHAT asset(s) are deposited/staked/LP’d
- WHERE exactly (protocol/exchange + named product/pool/vault/market/module)
- HOW to join (stake/deposit/supply/LP) and that it’s open
- WHAT rewards/yield are earned (rate or explicit reward mechanism)

If any one of these is missing/unclear from the text, output NO.

================================================
YES criteria (strict but practical)
Output "yes" ONLY if conditions 1–4 are met AND at least one of 5a/5b is met.

1) Passive-earn action is explicit
   The message clearly states an earn action the user can take:
   - stake / restake / delegate / lock
   - deposit / subscribe / supply / lend
   - provide liquidity / farm / deposit into a vault/strategy
   Must be framed as an opportunity, not just an explanation.

2) Specific venue + specific earn surface
   Must include BOTH:
   - Venue: a named protocol/app/exchange (e.g., Aave, Morpho, Uniswap, Kraken, Binance)
   - Earn surface: a named product/pool/vault/market/module/page context
     Examples: “Aave USDC market”, “Morpho USDT market”, “Kraken DeFi Earn vaults”, “Binance Simple Earn (Fixed)”, “BeraHub Proof of Liquidity Yield Module”
   Brand-only or chain-only (“on Sui”, “in our app”) → NO.

3) Asset(s) are specified
   At least one concrete token/symbol (or an LP pair) is named as the deposit/stake asset.
   If only “tokens/crypto/stablecoins” with no ticker/name → NO.

4) Availability / joinability is clear
   Must indicate users can join:
   - “now/live/open”, “can now be staked/deposited/supplied”, “subscriptions open”
   OR an explicit start time/date/window.
   “Coming soon”, “announced”, “will be”, vague “available” with no join signal → NO.

5) Earn terms / rewards linkage (need 5a OR 5b)
   5a) Explicit yield number: APY/APR/% rate for that offering, OR
   5b) Explicit reward mechanism tied to that offering:
       - “earn incentives/rewards/points” for staking/depositing in the named product/module/pool
       - “revenue/fees distributed to stakers/holders” when it clearly refers to staking/locking in the named product
       This must be specific to the described action and venue (not generic “earn rewards” marketing).

================================================
Hard NO rules (high-precision exclusions)
Always output "no" for:

A) Non-earn content
   News, partnerships, hires, infra updates, token listings, trading pair announcements, “market live for trading”, proof-of-reserves, podcasts, guides, explainers → NO.

B) Trading/active-reward mechanics
   Trade-to-earn, competitions, leaderboards, rebates, prize pools, lotteries, margin/perps campaigns, referrals, cashback → NO.

C) Generic evergreen ads without a concrete offering instance
   “Earn up to X%”, “staking available”, “it’s never been easier to earn” without a named pool/vault/market/module AND clear joinability AND linked terms → NO.

D) Pure rate/analytics commentary
   “APY is X” without where/how to deposit now → NO.

E) Airdrop/quest/points campaigns as the main mechanic
   Quests/missions/season/claim tasks → NO
   EXCEPT when the message still satisfies ALL YES criteria 1–4 and 5b via deposit/stake/LP-based earning in a named product.

================================================
Edge-case guidance (important)
- “can now be staked/deposited/supplied” counts as a joinability signal.
- A yield number is NOT required if the message clearly states rewards/incentives will be earned for the specific staking/deposit action in the named module/pool (still must satisfy 1–4).
- If the message mentions “vault/earn” but does not name the vault/pool/market/module and the deposit asset(s), output NO.
- If multiple items are listed, output YES if at least one specific item fully satisfies the YES criteria; otherwise NO.
- When in doubt, output NO.

Respond with only: yes or no
Iteration 30: New subsample score 14.0 is not better than old score 15.0, skipping
Iteration 31: Selected program 4 score: 0.6161616161616161
Iteration 31: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria below.

--------------------------------
YES (strict, actionable, and specific)
Say "yes" ONLY if the message clearly includes ALL of the following:

1) Passive earn action the user can take (explicit CTA)
   The message explicitly tells the user to do at least one of:
   - stake / restake / delegate / lock / bond
   - deposit / subscribe / earn / savings / fixed / flexible
   - lend / supply / provide collateral to earn interest (not just borrow)
   - provide liquidity / farm / add liquidity / deposit into a vault/strategy
   Must be framed as something a user can do (now or at a specified start time).

2) Identifiable venue + earn product context (where exactly)
   Must name the platform/protocol/exchange/app AND make it clear it is an earn feature/product or a specific pool/market/vault.
   Examples of sufficient context:
   - “Binance Earn / OKX Earn / Bybit Earn / HTX Earn” + asset(s)
   - “Aave supply USDC”, “Compound supply ETH”, “Curve <pool>”, “Uniswap V3 <pair>”, “Beefy vault <name>”, “Yearn vault <name>”
   Insufficient: only a chain name (“on Ethereum”, “on BTTC”) without a specific staking/earn product context.

3) Asset(s) are specified
   At least one concrete asset or LP pair is stated (e.g., SOL, ETH, USDT, stETH, ETH-USDC).

4) Joinable NOW (or with a concrete window)
   Must include at least one:
   - direct join instruction (stake/deposit/supply/LP/subscribe/join now/available now/open)
   - OR an explicit start/end time/date window indicating when users can participate.
   “Coming soon”, “announcing”, “learn more” without joinability → NO.

5) Yield/reward terms tied to THIS offering
   Must include at least one:
   - explicit APY/APR/reward rate/boost tied to the mentioned venue/product/pool, OR
   - an explicit statement that users can deposit/stake in that specific earn product now to earn rewards (e.g., “Earn rewards now”, “rewards live for depositors”).
   Generic marketing like “earn yield”, “stop losing yield”, “up to X%” without clear product enrollment details → NO.

--------------------------------
Additional hard NO rules (common edge cases)
Always output "no" for:

A) Pure news or support without an earn CTA:
   listings, trading pairs, “deposit available” for exchange listing, “market live”, integrations, chain support, bridges, collateral enablement, sunsets/wind-down notices, tech updates.

B) Informational/analytical statements about yield without an explicit enrollable offer:
   - “<token> staking offers APY X%” or “APY is X%” if it does NOT clearly include an actionable CTA + specific venue/product users can join now.
   (Treat these as rate commentary unless explicit “stake/deposit/supply here/now” is present.)

C) General ads/comparisons for a yield product that lack enrollment specifics:
   - “7% yield vs 4%”, “principal guaranteed”, “check it out”, “start earning” with no clear deposit/stake CTA + where to do it now → NO.

D) Points/airdrop/quest/season/campaign language where the primary mechanic is points or distribution:
   - Unless it clearly requires depositing/staking/LP in a named earn product to accrue yield (not just points).

E) Trading/active PnL:
   perps, leverage, signals, “trade to earn”, funding as trader PnL, market commentary.

F) Competitions/lotteries/cashback/referrals/leaderboards/scratch cards/prize pools.

G) Vague APR screenshots/lists without credible “where/how to join” details.

--------------------------------
Tie-breakers
- When in doubt, choose NO.
- To answer YES, you should be able to point to: (asset) + (platform/product/pool) + (what to do) + (live/window) + (yield/reward terms).
- “Up to X% APY” can be YES only if paired with a specific venue + earn product context + assets + explicit join/live/window signal.
- If the message is primarily informational, promotional, or educational and you cannot answer “what exactly should the user deposit/stake and where, right now?” → NO.

Respond with only: yes or no
Iteration 31: New subsample score 15.0 is not better than old score 15.0, skipping
Iteration 32: Selected program 2 score: 0.6363636363636364
Iteration 32: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

Definition (what counts as yield farming here):
A message is YES only when it presents an actionable “park assets → earn yield/rewards” opportunity such as staking, lending/supplying, liquidity provision/LP farming, vault deposit, savings/earn product, fixed/flexible earn, or similar passive-earn program.

Core rule (must be actionable from the message text):
Say YES only if the message itself identifies ALL of the following:
1) WHAT earn action/product: stake / deposit / supply / lend / lock / provide liquidity (LP) / farm / vault / earn / savings / fixed promo
AND
2) WHERE: a specific joinable venue + specific earn feature/product/pool/vault (protocol/app/exchange + named pool/vault/earn program)
AND
3) WHICH asset(s): at least one specific token/coin or LP pair (e.g., USDC, ETH, WBTC, SOL, ETH/USDC)

APY/APR is NOT required if (1)-(3) are satisfied, but it strengthens YES.

Hard guardrail (main source of false YES):
- Borrow/collateral/product-utility announcements are NOT yield opportunities unless the message explicitly indicates earning/yield/rewards/interest OR clearly implies interest by using supply/lend language WITH a rate OR a named “Earn/Vault/Savings/Farm/Staking” product.
  * If it only says “use as collateral”, “borrow”, “leverage”, “trade”, “derivatives”, “token now usable”, “listed”, “integrated”, “priority partner”, etc. → NO.

Acceptable implicit “WHAT” (to avoid false NOs):
- If the message clearly names an earn product type + asset(s) + a rate (APR/APY/% yield), the deposit action can be implicit.
  Examples that can be YES if venue/product is clear: “BTC Vault 3% APR”, “USDf Boosted 10.22% APY”, “ETH staking 4%”, “USDC Earn 8%”.

VENUE/WHERE requirements (be strict but realistic):
- “WHERE” must be identifiable as a specific product users can join, not just a general ecosystem mention.
  * Good: “Curve frxUSD/OUSD pool”, “Aave supply USDC on Arbitrum”, “Binance Earn USDT Simple Earn”, “Bybit Earn Fixed Promotion”, “Jumper Earn OP Mainnet Vaults” (only if it also states assets).
  * Bad: “incentives are back”, “earn on DeFi”, “vaults are available” without assets, “high APY on Uniswap pools” without naming the pool/pair.

YES conditions (any one is sufficient, but must satisfy the core rule):
1) Concrete earn action + venue/product + asset(s)
   - Explicit stake/deposit/supply/lend/LP/farm/vault/earn/savings + named venue/product/pool/vault + asset(s).

2) Explicit yield rate tied to a joinable product
   - Mentions APR/APY/reward rate AND ties it to a specific earn product/pool/vault/program on a named venue AND specifies asset(s).
   - “Up to X%” is acceptable ONLY if it is tied to a specific named product/pool/vault AND asset(s).

3) “Live/Now available” earn launch with participation details
   - “Staking is live”, “Earn is live”, “Vault launched”, “Farm is live” AND includes venue/product + asset(s). Rate optional.

4) Time-bound boosted/limited promotion (still must be specific)
   - Boost/promo + named earn product/program + asset(s) (+ start/end/time).

NO conditions (common traps):
A) Vague yield marketing without enough specifics
   - “Start earning”, “top returns”, “high APY”, “up to X%” WITHOUT BOTH a specific earn product/pool/vault/program AND the asset(s) → NO.

B) Platform promo without eligible asset/product
   - “Platform Earn has up to 20%” with no specific asset/product/plan → NO.

C) Non-yield incentives
   - Airdrops/points/quests/Zealy/leaderboards, giveaways, cashback, referrals, lotteries, “trade to win”, competitions → NO.

D) Trading/news/infrastructure/partnerships only
   - Listings, trading pairs, markets launch, partnerships, tech updates, integrations, “now usable as collateral”, borrow-only features → NO unless it includes a concrete earn product as per core rule.

E) Past distribution/status-only
   - “Rewards distributed”, “recap”, “airdrop sent”, “points credited” → NO unless it also invites joining an ongoing earn product with venue + asset(s).

F) Not accessible
   - Explicitly institutional-only/private/closed beta without a public way to join now → NO.

Disambiguation rules for tricky cases:
- “Supply” can mean earning interest ONLY if paired with (a) an explicit rate/APY/APR/rewards OR (b) a clearly named lending/earn market/vault (e.g., “Aave USDC market”, “Morpho USDC vault”) AND asset(s). Otherwise NO.
- “Vault(s) available/launched” is YES only if the message names at least one vault AND its asset(s) (rate optional). If it just says vaults exist → NO.
- A list of vaults + assets + APR/APY counts as YES even if the venue name is not explicit, ONLY when the message clearly indicates these are “Vaults/Earn” products (the product type itself serves as WHERE) and includes assets + rates. If it’s just a generic list of assets with numbers not clearly tied to an earn product → NO.

Quick checklist before YES (all must be true):
- Do I know what earn action/product it is (stake/deposit/supply/LP/farm/vault/earn/savings)?
- Do I know where (named venue/product/pool/vault/earn program OR clearly identified vault/earn product itself)?
- Do I know which asset(s)?
If any is missing → NO.

Respond with only: yes or no
Iteration 32: New subsample score 14.0 is better than old score 13.0. Continue to full eval and add to candidate pool.
Iteration 32: Valset score for new program: 0.6363636363636364 (coverage 99 / 99)
Iteration 32: Val aggregate for new program: 0.6363636363636364
Iteration 32: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 0.0, 10: 1.0, 11: 0.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 0.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 0.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 0.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 32: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 32: Valset pareto front aggregate score: 0.8888888888888888
Iteration 32: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16}, 2: {16, 2, 13}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 7: {0, 1, 5, 6, 7, 10, 14}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16}, 15: {0, 1, 2, 4, 14}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 20: {0, 2, 9, 13, 14, 15, 16}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 33: {0, 1, 2, 4, 9, 13, 15}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 38: {3, 4, 5, 10, 12, 15}, 39: {1, 10, 5, 7}, 40: {2, 13}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16}, 43: {1, 5, 6, 7, 8, 10, 11, 16}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16}, 45: {16, 2, 11}, 46: {2, 8, 9, 11, 13, 16}, 47: {0, 16, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 49: {0, 1, 5, 6, 7, 10, 11}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 53: {10, 5}, 54: {1, 3, 5, 6, 7, 10, 16}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15}, 57: {5, 6, 7, 10, 11, 12}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16}, 60: {13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10, 14}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 68: {16}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 74: {10, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 82: {10, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 87: {4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}, 98: {2, 4, 15}}
Iteration 32: Best valset aggregate score so far: 0.6767676767676768
Iteration 32: Best program as per aggregate score on valset: 1
Iteration 32: Best score on valset: 0.6767676767676768
Iteration 32: Linear pareto front program index: 1
Iteration 32: New program candidate index: 16
Iteration 33: Selected program 13 score: 0.5757575757575758
Iteration 33: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

What counts as yield farming (YES):
Only messages that present an actionable passive-earn mechanism such as:
- staking / restaking / validator delegation
- lending/supplying/borrowing-to-earn incentives (e.g., “lend to earn”, “net lending positions”, “supply APR”)
- vault deposits / earn vaults / automated yield strategies
- liquidity provision (LP) / farming / gauge incentives / liquidity mining
- CEX earn/savings/fixed/locked products, launchpool/earn campaigns
- similar programs where you deposit/lock/supply/add liquidity to earn yield/rewards

Core rule (must be actionable from the message text alone):
Say YES only if ALL are satisfied:
1) WHAT: a passive earn action/mechanism is clearly indicated (stake/deposit/supply/lend/lock/add liquidity/LP/farm/vault/earn/savings/launchpool/etc.)
AND
2) WHERE: a specific joinable venue + specific product/pool/vault/market/program is identified
   - Examples of “WHERE”: “Aave on Arbitrum USDC market”, “Aerodrome Slipstream USDC/ETH pool”, “Binance Earn USDT locked product”, “Kamino Multiply vault”, “Lido staking”, etc.
AND
3) WHICH asset(s): at least one specific token/coin OR an LP pair is specified.

If any of (1)-(3) is missing → NO, unless an explicit exception below applies.

Critical disambiguation (to reduce false YES):
- A venue name alone is NOT enough. It must name a specific earn product/pool/vault/market/program.
- A list of APR/APY numbers/pairs without an explicit venue/product context → NO.
- If it is an airdrop/points/quest/referral/cashback/competition/trade-to-win/stream-to-earn/game event → NO (even if “rewards” are mentioned).
- If it is news, token migration, listing, delisting, bridge notice, rebrand, partnership, treasury purchase, protocol tech update → NO unless it also clearly offers a joinable earn product as per the core rule.

YES-leaning clarifications (still must satisfy core rule or exception):
- “Incentives are live” / “rewards live” can be YES when it clearly refers to lending/LP/staking incentives on a named market/pool AND assets are specified OR the “any deposit” exception is met.
- “Earn your share of token rewards on your net lending positions” counts as lending incentive ONLY if the lending venue/market is named and joinable.

Exceptions (limited; keep strict):
1) Asset exception: “any deposit / no minimum” (rare)
   - YES if the message clearly presents a live earn product/program AND names the venue + specific earn product/program AND explicitly says any deposit size/no minimum AND provides a concrete rate (APR/APY) or clearly states yield/rewards are paid.
   - Otherwise NO.

2) Implicit action via unmistakable earn product naming
   - If the message names a well-known earn product/pool/vault/program on a venue AND specifies asset(s) AND clearly indicates earning (rate optional), treat the action as implied → YES.
   - Example: “Aerodrome Slipstream USDC/WETH rewards live” (venue + product + pair + earn intent).

Hard NO conditions (common traps):
A) Cashback/spend rewards/card perks (e.g., “8% cashback when you spend”) → NO.
B) Giveaways/airdrops/referrals/quizzes/Zealy/points/leaderboards/lotteries/contests → NO.
C) Active trading required (trade volume, leverage, “trade to earn”, fee discounts) → NO.
D) “Up to X%” marketing without a specific joinable pool/vault/product + asset(s) → NO.
E) Institutional/private/closed beta with no public join path or timing → NO.
F) Status-only (“rewards distributed”, “recap”) with no invitation to join an ongoing earn product → NO.

Decision procedure:
1) Is there a passive-earn mechanism (staking/lending/vault/LP/earn product) rather than cashback/contest/trading/news? If not → NO.
2) Check WHERE: is there a specific venue + specific earn product/pool/vault/market/program that a user can join? If not → NO.
3) Check WHICH asset(s): is at least one token/coin or LP pair explicitly named? If yes → YES (assuming steps 1-2 met).
4) If asset(s) missing: only YES if the “any deposit / no minimum” exception is fully satisfied; otherwise → NO.
5) If still uncertain → NO.

Respond with only: yes or no
Iteration 33: New subsample score 13.0 is not better than old score 14.0, skipping
Iteration 34: Selected program 4 score: 0.6161616161616161
Iteration 34: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria below.

--------------------------------
YES (strict; reduce false positives)
Say "yes" ONLY if the message clearly includes ALL of the following:

1) Explicit passive-earn action (imperative or clearly available to users)
   The message must explicitly tell users they can do at least one of:
   - stake / restake / delegate / lock
   - deposit / subscribe / join an Earn/Savings product
   - lend / supply / borrow-lend market supply side
   - provide liquidity / farm / deposit into a vault/strategy
   Must be framed as something the user can do now (or with a stated start/end time).

2) Identifiable venue + earn product / pool context (not just a brand name)
   Must identify WHERE the yield is earned with an earn-context such as:
   - CEX: “<Exchange> Earn/Savings/Stake” or “Flexible/Fixed/Launchpool/Stake” etc.
   - DeFi: protocol + specific pool/vault/market/farm (pair/asset market qualifies).
   A bare exchange/protocol name without an earn product context is NOT enough.

3) Asset(s) specified
   At least one specific asset or pair to stake/deposit/supply/LP is stated (e.g., USDT, ETH, ZAMA, ETH-USDC).

4) Live/joinable signal (must indicate availability)
   At least one of:
   - “now live/open”, “subscribe now”, “deposit now”, “stake now”, “get started”, “join”
   - OR a concrete window (“starts …”, “ends …”, “until …”)
   “Coming soon” or vague availability = NO.

5) Clear yield/reward terms tied to the offering
   One of the following must be true:
   (a) A specific APY/APR/reward rate is stated AND clearly applies to the mentioned earn product/pool, OR
   (b) The message clearly states users can earn yield/rewards by performing the action in (1) in the product/pool in (2) (even if no numeric rate), using explicit earn language like “earn”, “yield”, “rewards” in direct connection with the deposit/stake/supply/LP action.

6) Not primarily a generic brand advertisement
   Even if it mentions “Earn” and an APY, output NO when the message is clearly a broad, evergreen promotional slogan with no concrete pool/market/product details beyond generic marketing phrasing (e.g., “Easily Earn”, “High Yield”, “No limits”, “Ultimate convenience”, “Get started”) and lacks a specific program/pool/term or other concrete enrollment details.
   Treat these as marketing unless the message includes at least one additional concrete anchor such as:
   - a named specific product/program (e.g., “Flexible Savings USDT”, “Launchpool”, “Staking Gala”, “USDT fixed 30D”, “BTC lending market”)
   - a specific pool/market/pair/vault name
   - an explicit start/end date/time for enrollment
   If none of these concrete anchors appear → NO.

If any requirement is missing or too ambiguous, output NO.

--------------------------------
NO (common traps / exclusions)
Always output "no" for:

A) Pure news/integration/support without an earn offer:
   - listings, wallet/chain support, bridges, collateral enablement, “market live” for trading,
     “now supported” announcements, protocol version releases
   Unless it clearly instructs users to deposit/stake/supply/LP to earn.

B) Vague marketing with no enrollable earn context:
   - “start earning”, “put your crypto to work”, “high yield” without a specific product/pool/market and user action.

C) Points/airdrop/quest/campaign distributions as the primary mechanic:
   - points, quests, seasons, airdrops, reward distributions, “earn your share”
   Unless it is explicitly passive yield from depositing/staking/supplying/LP into a defined earn product/pool.

D) Trading/active PnL mechanisms:
   - perps, leverage, signals, funding as trader PnL, “trade to earn”, alpha, market commentary.

E) Competitions, lucky draws, cashback, cards, referrals/affiliates, leaderboards, prize pools.

F) APR/APY screenshots/lists with unclear where/how:
   - big numbers without a credible, specific venue + product/pool + join signal.

G) Analytics/rate commentary without a concrete offer:
   - “APY is X” for an asset without saying where/how to stake/deposit/supply now.

--------------------------------
Tie-breakers
- When in doubt, choose NO.
- If you cannot answer “What exactly should the user deposit/stake/supply/LP, and on which specific earn product/pool, right now?” → NO.
- “Up to X% APY” is YES only if it is tied to a specific earn product/pool/term and includes a join/live/window signal.
- Generic CEX “Earn” advertisements without concrete program/pool/term/window details → NO.

Respond with only: yes or no
Iteration 34: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 34: Valset score for new program: 0.6363636363636364 (coverage 99 / 99)
Iteration 34: Val aggregate for new program: 0.6363636363636364
Iteration 34: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 0.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 0.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 34: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 34: Valset pareto front aggregate score: 0.8888888888888888
Iteration 34: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17}, 2: {16, 2, 13}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 7: {0, 1, 5, 6, 7, 10, 14, 17}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17}, 15: {0, 1, 2, 4, 14, 17}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 20: {0, 2, 9, 13, 14, 15, 16, 17}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 33: {0, 1, 2, 4, 9, 13, 15}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 38: {3, 4, 5, 10, 12, 15}, 39: {1, 10, 5, 7}, 40: {2, 13}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17}, 45: {16, 2, 11}, 46: {2, 8, 9, 11, 13, 16}, 47: {0, 16, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 49: {0, 1, 5, 6, 7, 10, 11}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 53: {10, 5}, 54: {1, 3, 5, 6, 7, 10, 16}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17}, 57: {5, 6, 7, 10, 11, 12}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17}, 60: {13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 68: {16}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 74: {10, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 82: {10, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 87: {4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}, 98: {2, 4, 15}}
Iteration 34: Best valset aggregate score so far: 0.6767676767676768
Iteration 34: Best program as per aggregate score on valset: 1
Iteration 34: Best score on valset: 0.6767676767676768
Iteration 34: Linear pareto front program index: 1
Iteration 34: New program candidate index: 17
Iteration 35: Selected program 10 score: 0.6464646464646465
Iteration 35: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, specific, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products, launchpool-style lock & earn).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria.

================================================
Core principle (what counts as a YES)
Return YES only if the message describes a specific earn opportunity a user can actually join (live now OR with an explicit scheduled opening) with enough concrete details to identify:
- WHAT asset(s) the user must stake/deposit/LP/lock
- WHERE exactly to do it (named platform + named earn surface)
- HOW to join (stake/deposit/supply/LP/lock/subscribe)
- WHAT the user earns (APY/APR OR explicit rewards tied to this exact opportunity)
- WHEN it is available (live now or explicit start time/window)

If any of these are missing/unclear, output NO.

================================================
YES criteria (strict)
Output "yes" ONLY if ALL conditions 1–5 are met:

1) Passive-earn action is explicit
   Message instructs or clearly enables a passive earn action:
   stake / delegate / lock / restake
   deposit / subscribe / savings / earn / vault
   lend / supply (earning side)
   provide liquidity / farm / deposit into a strategy
   If it only describes a product category (“margin lending”, “CeDeFi lending”, “earn”) without telling the user what to do → NO.

2) Specific venue + specific earn surface is named
   Must name BOTH:
   (a) the platform/venue (exchange or protocol), AND
   (b) the specific earn surface/context (e.g., “KuCoin Earn Fixed Promotion”, “Binance Launchpool”, “Bitget Launchpool”, “Aave USDC market”, “Morpho Vault <name>”, “Uniswap <pair> pool”, “Vault <name>”).
   Brand alone (“on KuCoin”, “via Anchorage”, “on Solana”) is not enough → NO.

3) Asset(s) are specified
   At least one token symbol/name the user supplies/locks/stakes is explicitly mentioned.
   For LP, a pair is fine. For launchpools, locked assets must be specified.
   If only generic “tokens/crypto/stablecoins” with no tickers → NO.

4) Joinable availability signal (NOW or scheduled open)
   Must have at least one:
   - explicit CTA: stake/deposit/lock/supply/subscribe/join “now”, “open”, “live”, “starts”
   - OR explicit start time/date/window (even if it starts later)
   “Coming soon”, “more to come”, “announced” without a start/open time or join instruction → NO.

5) Earn terms are concrete AND tied to the offering
   Must include at least one tied to the named product:
   - explicit APR/APY (including “up to X%” if clearly for this product), OR
   - explicit reward mechanics with numbers (e.g., “share 22,947,000 SPACE”, “earn TOKEN rewards”, “boosted rewards”) that are clearly for locking/depositing in this product.
   Vague “earn rewards” with no rate or concrete reward mechanics → NO.

================================================
Hard NO rules (precision exclusions)
Always output "no" for:

A) Pure news/announcements/integrations/support without an enrollable earn product
   listings, partnerships, “now supported”, “mainnet/testnet live”, “market live”, “trading begins”, infrastructure updates → NO.

B) Trading/active PnL / margin/perps experiences
   perps/leverage, trading platforms, “margin lending for borrowers”, delta-neutral strategies described as a product without a user deposit/earn offer → NO.

C) Competitions/lotteries/referrals/cashback
   trade-to-earn, referral rebates, leaderboard prize pools, lucky draws, card cashback → NO.

D) Airdrop/points/quests as the main mechanic
   seasons/quests/missions/points/claim campaigns → NO
   EXCEPT when it is explicitly deposit/stake/LP-based with clear venue+product, assets, join signal, and concrete earn terms (still must satisfy YES 1–5).

E) Analytics/rate commentary without “where/how to join”
   “APY is X” without a joinable product and instruction → NO.

F) Non-actionable access statements
   “Access X via Y”, “enabling access to vaults/strategies” with no specific vault name, deposit assets, join CTA, or concrete earn terms → NO.

================================================
Key clarifications for common edge cases

1) Launchpool / Lock-to-earn
   Treat as YES when it specifies:
   - platform + “Launchpool/Launchpad/Pool”
   - locked assets (e.g., BTC/ETH/USDT/etc.)
   - reward token and concrete reward mechanics (e.g., total rewards)
   - locking/enrollment period or start time AND a join CTA/link
   Otherwise → NO.

2) CEX “Earn / Savings / Fixed Promotion”
   YES if the message names the earn surface (e.g., “KuCoin Earn Fixed Promotion”, “OKX Simple Earn”, “Binance Simple Earn”, etc.) AND includes:
   - specific asset(s)
   - a concrete rate (APR/APY) OR concrete rewards
   - availability (start time/window or “now open”) or a subscribe/join CTA
   Term length is NOT required if the promotion is clearly a specific event/product instance with a start time/window.
   Generic evergreen ads (“Earn up to X% on crypto”, no start/open context) → NO.

3) High APR promos
   Do NOT reject solely due to unusually high APR. Judge only by actionability and specificity.

================================================
Tie-breakers
- When in doubt, output NO.
- If the message could be posted any day as generic marketing, output NO.
- If it lacks a specific earn surface or lacks concrete earn terms tied to the offer, output NO.

Respond with only: yes or no
Iteration 35: New subsample score 14.0 is better than old score 13.0. Continue to full eval and add to candidate pool.
Iteration 35: Valset score for new program: 0.6464646464646465 (coverage 99 / 99)
Iteration 35: Val aggregate for new program: 0.6464646464646465
Iteration 35: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 0.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 0.0, 18: 0.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 0.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 1.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 0.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 0.0, 97: 0.0, 98: 0.0}
Iteration 35: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 35: Valset pareto front aggregate score: 0.8888888888888888
Iteration 35: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18}, 2: {16, 2, 13}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18}, 15: {0, 1, 2, 4, 14, 17}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 20: {0, 2, 9, 13, 14, 15, 16, 17}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 33: {0, 1, 2, 4, 9, 13, 15}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 38: {3, 4, 5, 10, 12, 15, 18}, 39: {1, 10, 5, 7}, 40: {2, 13}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18}, 45: {16, 2, 11}, 46: {2, 8, 9, 11, 13, 16}, 47: {0, 16, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 49: {0, 1, 5, 6, 7, 10, 11, 18}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18}, 57: {5, 6, 7, 10, 11, 12}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17}, 60: {13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 68: {16}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 87: {4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 98: {2, 4, 15}}
Iteration 35: Best valset aggregate score so far: 0.6767676767676768
Iteration 35: Best program as per aggregate score on valset: 1
Iteration 35: Best score on valset: 0.6767676767676768
Iteration 35: Linear pareto front program index: 1
Iteration 35: New program candidate index: 18
Iteration 36: Selected program 18 score: 0.6464646464646465
Iteration 36: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, specific, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products, launchpool-style lock & earn).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria.

================================================
Core decision rule
Return YES only when the message is an enrollable earn offer a user can join, with enough concrete details to identify:
- ACTION: stake/deposit/supply/LP/lock (passive earn)
- VENUE: where (protocol/CEX) AND the specific earn product/surface
- ASSET(S): what the user supplies/locks
- TERMS: what the user earns (APR/APY or concrete, quantified reward mechanics)
- AVAILABILITY: live now or a specific opening time/window OR an explicit subscribe/join CTA

If any piece is missing/unclear → NO.

================================================
YES criteria (strict, but allow “evergreen” products if actionable)
Output "yes" ONLY if ALL conditions 1–5 are met:

1) Passive-earn action is explicit
   The message clearly instructs/enables a passive earn action:
   stake / delegate / lock / restake / convert to staked token
   deposit / subscribe / savings / earn / vault
   lend / supply (earning side)
   provide liquidity / farm / deposit into strategy
   If it’s only general talk about “earn”, “rewards”, “APR”, “yield”, “double yields” with no clear action → NO.

2) Specific venue + specific earn surface is named
   Must name BOTH:
   (a) the platform/venue (exchange or protocol), AND
   (b) the specific earn surface/context (e.g., “Binance Launchpool”, “OKX Simple Earn”, “Aave v3 USDC market”, “Morpho Vault <name>”, “Curve <pool>”, “Uniswap v3 <pair> <fee tier>”, “JustLendDAO staking/mint sTRX”).
   If the message only names a chain/ecosystem/wallet/brand without the earn product surface → NO.

3) Asset(s) are specified
   At least one token symbol/name the user supplies/locks/stakes is explicitly mentioned (or an LP pair).
   If only “crypto”, “tokens”, “stablecoins” with no tickers → NO.

4) Joinable availability signal (NOW or scheduled open) OR clear evergreen join CTA
   Must include at least one:
   - explicit CTA: stake/deposit/lock/supply/subscribe/join/get started (even without “now”)
   - OR explicit start time/date/window/enrollment period
   Accept evergreen opportunities as YES IF the CTA is present and the offer is described as currently available (e.g., “Stake X on Y”, “Deposit X into Y vault”, “Supply X on Aave”).
   “Coming soon”, “announced”, “more to come” without a start/open time or join instruction → NO.

5) Earn terms are concrete AND tied to the offering
   Must include at least one, clearly tied to THIS product:
   - explicit APR/APY (including “up to X%” if clearly for this product), OR
   - concrete reward mechanics with numbers (e.g., “X tokens rewards”, “share 22,947,000 TOKEN”, “boost to X%”, “earn X TOKEN per day”) tied to staking/depositing/locking.
   Vague “earn rewards”, “earn points”, “double yields” with no APR/APY or quantified rewards → NO.

================================================
Hard NO rules (precision exclusions)
Always output "no" for:

A) Pure news/announcements/integrations/support without an enrollable earn product
   listings, partnerships, “now supported”, “mainnet live”, “market live”, “trading begins”, tooling/analytics releases → NO.

B) Trading/active PnL / margin/perps
   leverage/perps, trading contests, “trade to earn”, PnL bragging, price calls → NO.

C) Competitions/lotteries/referrals/cashback
   raffles, lucky draws, leaderboards, referral rebates, card cashback → NO.

D) Airdrop/points/quests as the main mechanic
   seasons/quests/missions/points/claim-only campaigns → NO
   Exception: if it is explicitly deposit/stake/LP-based AND still satisfies YES 1–5 with concrete yield/reward terms (not just points).

E) Rate commentary without “where/how to join”
   “APY is X%” with no named venue+earn surface and no join instruction → NO.

F) Non-actionable access statements
   “Access X via Y”, “enabling access to vaults/strategies” without a specific vault/product, deposit asset(s), join CTA, and concrete earn terms → NO.

================================================
Key clarifications (edge cases)

1) Launchpool / Lock-to-earn
   YES only if it specifies:
   - platform + named launchpool surface
   - locked asset(s)
   - reward token and quantified rewards (APR/APY or total rewards or emission numbers)
   - start time/window or clear “now open/join/subscribe”
   Otherwise → NO.

2) CEX “Earn / Savings / Fixed Promotion”
   YES if it names the earn surface AND includes:
   - specific asset(s)
   - concrete APR/APY OR quantified rewards
   - availability (open/start time/window) OR explicit subscribe/join CTA
   Generic evergreen ads (“Earn up to X%”, no asset list, no surface, no CTA) → NO.

3) Protocol staking wrappers / liquid staking / restaking
   YES if it explicitly says stake/lock asset X on protocol Y to receive token Z and gives APR/APY or quantified rewards, with a join CTA (even if ongoing).
   If it only explains the concept without actionable instruction/terms → NO.

4) “Current APY” / “7d avg” / “live rate”
   Treat as concrete terms if the message ties the rate to a specific product surface and asset and provides a join CTA.

================================================
Tie-breakers
- When in doubt, output NO.
- If the message could be posted any day as generic marketing without identifying a specific product surface + assets + terms + joinability, output NO.

Respond with only: yes or no
Iteration 36: New subsample score 15.0 is not better than old score 15.0, skipping
Iteration 37: Selected program 7 score: 0.6565656565656566
Iteration 37: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

========================================================
CORE DECISION RULE
Return YES only when the message itself provides enough information to perform a passive-earn action NOW (or at a stated start time) on a specific venue/product using specific asset(s), and it is not a contest/points/airdrop/trading promo.

========================================================
HARD REQUIREMENTS FOR YES (must satisfy A, B, C, D)

A) ACTION (explicit passive-earn action exists)
The message explicitly instructs or clearly indicates a passive-earn action such as:
- stake / staking / restake
- deposit / subscribe
- supply / lend / earn / savings / simple earn / earn program
- lock / fixed earn / flexible earn
- farm / yield farm
- provide liquidity / add liquidity / LP / pool deposit / deposit into pool
- vault / strategy / deposit into vault
- gauge / bribe / boost (ONLY if it also implies deposit/LP/stake action)

NOT actions: trade, buy, sell, hold, bridge, swap, download, sign up (alone).

B) VENUE (where to do it is identifiable)
At least ONE must be true:
1) Named platform/protocol + named earn product/feature
   Examples: “Binance Simple Earn”, “OKX Earn”, “HTX Earn Flexible Earn”, “Aave v3 Supply”, “Yearn vault”, “Beefy vault”, “Curve gauge”, “Balancer pool”.
2) Named platform/protocol + a specific pool/pair/market on that venue
   Examples: “ETH/USDC pool on Uniswap v3”, “USDT market on Aave”, “stETH/ETH pool on Curve”.
3) An explicit link/button clearly tied to the earn product/pool (e.g., “Stake Now”, “Deposit in Earn”, “Go to Earn”) plus a named platform.

If the message only names a token or only says “earn” without a clear platform/venue → NO.

C) ASSET(S) (what to use is explicit)
The message states exact asset(s) to stake/deposit/supply/LP:
- token symbols/names (e.g., AXS, ATOM, USDC), OR
- an LP pair/pool constituents (e.g., MNT/USDC, ETH/USDC), OR
- “deposit $TOKEN” in an earn product.

If assets are implied but not stated → NO.

D) JOINABLE (availability is explicit)
The message indicates it is joinable now OR provides a clear start time/window.
Acceptable joinability signals include:
- now / now live / live / launched / open / available / deposits open / start earning now
- “starts <date/time>”, “from <date/time>”, “effective <date/time>”
- “promotion period: <start>-<end>”
If there is no explicit now/live/open/start-time/window signal → NO.

IMPORTANT: If the message includes “Start”/“Starts” but the start time is missing/unclear, treat as NOT joinable unless “now”/“available” is also present.

========================================================
ADDITIONAL ACCEPTANCE (reduce false negatives while staying strict)

1) NEW POOL / “POOL IS LIVE” posts (implied action allowed)
If the message states a specific pool/pair is now live/launched/open on a specific AMM/venue AND names the pool assets → YES
(e.g., “frxUSD/OUSD pool now live on Curve”). Action “provide liquidity” is sufficiently implied.

2) CENTRALIZED EXCHANGE EARN POSTS (CEX Earn)
Treat as YES when ALL are present:
- Platform named (e.g., Binance/OKX/HTX/KuCoin/Phemex/etc.)
- Earn product/feature named (Earn/Savings/Simple Earn/Flexible Earn/Fixed Earn/On-Chain Earn/Stake)
- Asset named
- Joinable now OR a clear start time/window
APY/APR helps but is not required.

========================================================
OVERRIDING EXCLUSIONS (if any apply → NO, even if A-D seem met)

1) Competitions / prize pools / lucky draws / hunts / puzzles / leaderboards / “share of $X prize pool”
   If staking/LP is used only to earn entries/points/chances/rewards in a game/competition → NO.

2) Airdrops / points / quests / referrals / cashback / vouchers / rebates / “deposit/trade to win” / lottery / lucky spin → NO.

3) Trading-only promos:
   perps, margin, leverage, copytrading, swaps, listing announcements, “deposit available”, “trading starts”, fee discounts, routing → NO.

4) News/partnerships/integrations/tech updates/testnet/beta launches WITHOUT a concrete earn offer meeting A-D → NO.

5) Vague marketing:
   “Earn up to X%”, “high APY”, “best yields” without specific venue/product + asset + joinability → NO.

6) Borrow-only / leverage-only:
   “borrow”, “higher LTV”, “E-Mode”, “new collateral” without an explicit supply/deposit/earn opportunity meeting A-D → NO.

========================================================
QUICK FINAL CHECK (all must be TRUE for YES)
- Passive-earn action is explicit OR a specific live pool is announced (implied LP deposit allowed).
- Venue/platform + specific earn product/pool is identifiable.
- Exact asset(s) are stated.
- Joinable now OR clear start time/window is stated.
- Not a contest/airdrop/points/trading-only promo.

If any check fails → NO.

Respond with only: yes or no
Iteration 37: New subsample score 14.0 is not better than old score 15.0, skipping
Iteration 38: Selected program 4 score: 0.6161616161616161
Iteration 38: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products).

Output ONLY one token: yes or no.

Default to NO unless the message clearly qualifies as YES.

================================================
Core definition (what counts as YES)
A message is YES only if it lets a user reasonably answer:
“What action should I take (stake/deposit/supply/LP), with which asset(s), and on which named venue/product, to earn passive yield/rewards, and is it available now (or within a stated window)?”

================================================
YES criteria (all must be satisfied)

1) Passive earn action is explicit and user-doable
   Message must clearly instruct/invite a user to do at least one concrete passive-earn action:
   - stake / restake / delegate / lock
   - deposit / subscribe / save in Earn/Savings
   - lend / supply / borrow-to-earn interest (supplying/lending side)
   - provide liquidity / farm / deposit into a vault/strategy/pool
   The action must be for earning yield/rewards (not just “top up”, “bridge”, “swap”, “trade”, “register”).

2) Named venue + earn product context (must be specific)
   Must name WHERE and WHAT product/pool/market:
   - CEX: “<Exchange> Earn/Savings/Staking/Launchpool/DeFi Staking” (or equivalent) is enough IF assets are stated.
   - DeFi: protocol + specific pool/vault/market OR pair (e.g., “Aave USDC market”, “Curve stETH/ETH pool”, “Uniswap v3 ETH-USDC 0.05%”, “Lido staking”, “Vault XYZ”).
   Not enough: generic “higher yields on <brand>”, “APR on our platform”, “v2/v3 pools”, “vault launching” without join details.

3) Asset(s) are specified
   Must name at least one concrete asset or LP pair to be deposited/staked/supplied (e.g., BTC, ETH, USDT, SOL, SPACE; ETH-USDC).

4) Joinable now (or clear availability window)
   Must include at least one “live/join” signal tied to the earn action:
   - “deposit now”, “stake now”, “subscribe now”, “supply now”, “LP now”, “open/available”, “now live”
   - OR an explicit start/end time for subscribing/depositing.
   If it’s only “coming soon”, “launching”, “soon”, “next week” with no enrollment instructions/window → NO.

5) Yield/reward terms must be tied to the offer
   Must include EITHER:
   a) a concrete yield/reward rate (APY/APR/%/boost) clearly for that named venue/product/pool, OR
   b) an explicit statement that users will earn yield/rewards by doing the specified earn action in the named product AND it is live/joinable now.
   Reject “APR” mentions that are merely analytics/observations without an invitation to deposit/stake/supply/LP in a named product.

================================================
Hard NO rules (override to NO)

A) Non-earn product announcements
   Listings, integrations, chain support, bridges, wallets, “top up”, “deposit app”, “market live”, collateral enablement, upgrades, reports, interviews, dev updates → NO unless they explicitly offer an earn product with deposit/stake/supply/LP.

B) Events, campaigns, and prize mechanics
   Airdrops, snapshots, claims, quests, points, seasons, lucky draws, prize pools, competitions, streamer/rewards pools, referrals, cashback/card promos → NO
   Exception: only if the primary mechanic is a passive earn deposit/stake/supply/LP product (not “register/claim/complete tasks”).

C) Trading/active PnL
   Perps, leverage, trading signals, “trade to earn”, funding as trader profit, memecoin pumping, volume-based “APR” commentary → NO.

D) Vague “earn more” marketing
   “Start earning”, “higher yields”, “boost earnings”, “earn rewards” without explicit (action + venue/product + asset + joinable now) → NO.

E) APR screenshots/lists/analytics without enrollment details
   If it reads like a rate report (“Trailing 24h APR…”, “fees APR… varies with volume”) and does not explicitly tell users to provide liquidity/deposit into a named pool/vault/market now → NO.

================================================
Tie-breakers
- When in doubt, output NO.
- “Up to X% APY” is YES only if it also includes: named venue+earn product, specific asset(s), and a clear subscribe/deposit/stake now (or window).
- If you cannot confidently extract: action + venue/product + asset(s) + joinable now → NO.

Respond with only: yes or no
Iteration 38: New subsample score 15.0 is not better than old score 15.0, skipping
Iteration 39: Selected program 13 score: 0.5757575757575758
Iteration 39: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

Definition (what counts as yield farming here):
A message is YES only when it offers (or announces as live/upcoming with time) a passive earning mechanism such as staking, lending/supplying, vault deposit, liquidity provision/LP farming, farms/incentives, savings/earn programs, fixed/locked/flexible earn products, launchpools, or delegating to validators.

Hard requirement: must be an EARN ACTION, not just “rewards exist”.
- “Claim rewards”, “airdrop to stakers”, “rewards distributed”, “epoch rewards ready” by itself is NOT a yield opportunity unless the same message ALSO clearly invites/announces an ongoing way to earn (stake/deposit/LP/etc.) with venue + asset(s) (or a valid exception).
- Do NOT treat “staking airdrop” language as yield unless actual staking/earning action is described as currently available.

Core rule (must be actionable from the message alone):
Say YES only if the message provides enough to act by identifying:

1) WHAT: an earn mechanism (stake/deposit/supply/lend/lock/LP/add liquidity/farm/vault/earn/savings/launchpool/validator delegate)
AND
2) WHERE: a specific joinable venue + named earn surface (protocol/app/platform + a named product/feature/pool/vault/market/program)
AND
3) WHICH asset(s): at least one specific token/coin OR a specific LP pair (e.g., ETH-USDC) OR a clearly named receipt token that implies the staked asset (e.g., “stake SOL to get mSOL” counts as SOL specified). If (3) is missing → NO unless an exception applies.

If any of (1)-(3) is missing → NO, unless a listed exception applies.

Clarifications to reduce false NOs (strict but practical):
- “Stake now”, “deposit now”, “supply now”, “farm now”, “LP now”, “vault live” counts as actionable even without a link, as long as venue+product+asset(s) are named.
- “Earn rewards” without specifying the mechanism (stake/deposit/LP/etc.) → NO.
- “New liquid staking token X is live” is YES only if it clearly implies user can stake an underlying asset into a named staking product (venue + what to stake). If it only describes tokenomics/revenue distribution to holders without telling users how to obtain/stake → NO.
- Restriction notices (e.g., “not available to US persons”) do NOT automatically make it NO if the product is otherwise clearly actionable.

Key YES exceptions (keep strict):
1) Asset exception for “any deposit / no minimum” (rare):
   - If the message clearly presents a live earn product/program AND explicitly indicates deposits of any size (e.g., “no minimum / any amount”) AND the venue+product is named AND a yield/rate is given (APR/APY/%) → YES even if the asset is not named.
   - If no rate and no asset → NO.

2) Implicit action via unmistakable earn product naming:
   - If the message names an unmistakable earn product/program + venue AND specifies asset(s) AND explicitly says “earn/staking rewards/yield” (rate optional) → YES.

3) “Live/Now available” launches:
   - “Staking is live / Earn is live / Vault launched / Farm live / Incentives live” can be YES if venue + earn product context + asset(s) are present (rate optional).

Strong YES signals (still must satisfy core rule or a valid exception):
- Explicit APY/APR/reward rate tied to a named pool/vault/product.
- Clear instruction: “stake”, “deposit”, “supply”, “add liquidity”, “farm”, “enter vault”, “lock”.
- Known platforms (Aave/Morpho/Compound/Euler/Spark/Kamino/Uniswap/Curve/Balancer/Convex/Lido/Rocket Pool/Pendle/etc.) or CEX earn products (Binance Earn/Savings, OKX Earn, Bybit Earn, KuCoin Earn, Gate Earn, MEXC Launchpool, etc.) ONLY when paired with a specific earn product and asset(s) (or valid “any deposit/no minimum” exception).

NO conditions (common traps):
A) Vague yield marketing / brand claims
   - “earn”, “high APR”, “up to X%”, “targeting X%”, “revenue share”, “distributed to holders” WITHOUT a specific joinable product/pool/vault/program + venue → NO.

B) Missing asset(s)
   - If no asset/pair/underlying-staked-asset is identifiable → NO (except “any deposit/no minimum” exception).

C) Non-yield incentives
   - Airdrops/points/quests/Zealy/leaderboards, giveaways, cashback/card rewards, referrals, lotteries, “trade to win”, competitions, leverage/perps promos, funded trading accounts → NO.

D) Trading/news/infrastructure only
   - Listings, trading pairs, market launches, partnerships, governance/news/metrics/tech updates → NO unless there is a concrete earn action/product per core rule.

E) Past distribution/status-only
   - “Rewards ready to claim / distributed / recap” → NO unless it also announces or invites joining an ongoing earn mechanism with venue + product + asset(s).

F) Not accessible
   - Explicitly institutional-only/private/closed beta with no public join path/time window → NO.

Decision procedure:
1) Is there an explicit passive-earn ACTION (stake/deposit/supply/lend/LP/farm/vault/lock/launchpool/delegate)? If not → NO.
2) Is WHERE present: venue + specific earn surface (pool/vault/product/program/market)? If not → NO.
3) Is WHICH asset(s) present (token/pair/underlying stake asset)? If not → apply only the “any deposit/no minimum + rate + named product” exception; otherwise NO.
4) If the message is primarily about claiming/distribution/airdrop and does NOT clearly present a currently joinable earn action → NO.
5) If still uncertain → NO.

Respond with only: yes or no
Iteration 39: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 39: Valset score for new program: 0.6161616161616161 (coverage 99 / 99)
Iteration 39: Val aggregate for new program: 0.6161616161616161
Iteration 39: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 0.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 0.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 0.0, 20: 1.0, 21: 0.0, 22: 1.0, 23: 0.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 1.0, 41: 0.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 0.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 0.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 39: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 39: Valset pareto front aggregate score: 0.8888888888888888
Iteration 39: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 2: {16, 2, 19, 13}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18}, 15: {0, 1, 2, 4, 14, 17, 19}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 33: {0, 1, 2, 4, 9, 13, 15, 19}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 38: {3, 4, 5, 10, 12, 15, 18}, 39: {1, 10, 5, 7}, 40: {2, 19, 13}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19}, 45: {16, 19, 2, 11}, 46: {2, 8, 9, 11, 13, 16, 19}, 47: {0, 16, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 49: {0, 1, 5, 6, 7, 10, 11, 18}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18}, 57: {5, 6, 7, 10, 11, 12}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 68: {16}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16, 19}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 98: {2, 4, 15}}
Iteration 39: Best valset aggregate score so far: 0.6767676767676768
Iteration 39: Best program as per aggregate score on valset: 1
Iteration 39: Best score on valset: 0.6767676767676768
Iteration 39: Linear pareto front program index: 1
Iteration 39: New program candidate index: 19
Iteration 40: Selected program 18 score: 0.6464646464646465
Iteration 40: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, specific, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products, launchpool-style lock & earn).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria.

================================================
Core idea
Return YES when a real user can take a passive-earn action (supply/stake/deposit/LP/lock) in a SPECIFIC place/product, for SPECIFIC asset(s), and the message indicates it is joinable now (or at a stated time) AND the message provides concrete earn terms OR clearly states an incentives/rewards program is live for that exact action.

================================================
YES criteria (strict, but do not over-reject)
Output "yes" ONLY if conditions 1–4 are met, AND condition 5 is met via either 5A or 5B.

1) Passive-earn action is explicit (earning side)
   The message clearly tells/permits the user to do at least one:
   - stake / delegate / restake / lock
   - deposit / subscribe / earn / savings / vault
   - lend / supply (as a supplier/lender)
   - provide liquidity / farm / deposit into a strategy
   If it’s only about trading, borrowing, leverage, perps, or general DeFi narrative → NO.

2) Specific venue + specific earn surface/context is identifiable
   Must identify a concrete earn context that a user can find:
   - Protocol + market/pool/program context (e.g., “Aave on Mantle market”, “Compound USDC market”, “Curve pool <name>”, “Uniswap v3 <pair> pool”, “Morpho Vault <name>”, “Pendle pool <name>”)
   - OR CEX + named earn surface (e.g., “Binance Launchpool”, “OKX Simple Earn”, “KuCoin Earn Fixed Promotion”, “Bybit Earn”, “Bitget Launchpool”)
   Acceptable even if the exact subpage name is slightly abbreviated, as long as the market/pool/program context is clear.
   Brand alone without an earn context (“on Mantle”, “on Aave”, “on Bitget”) → NO.

3) Asset(s) to put to work are specified
   At least one explicit token is mentioned as the supplied/staked/deposited/locked asset (e.g., USDC, ETH, WETH, GHO, TAO).
   Generic “crypto/stables/tokens” with no tickers → NO.

4) Joinable availability signal exists
   Must include at least one:
   - “live”, “now”, “open”, “starts”, “deposit/supply/stake to earn”, “users can supply/stake…”
   - OR a specific start time/date/window.
   Pure “coming soon” without a start/open time or join instruction → NO.

5) Earn terms are tied to THIS opportunity (need either A or B)

   5A) Explicit rate/amounts:
       - APR/APY, or
       - explicit numeric reward mechanics (e.g., “X tokens distributed”, “X% boost”, “reward pool of …”).

   OR

   5B) Incentives/rewards program explicitly stated as live/active for the named action:
       If the message explicitly says “incentives are live/active”, “rewards are live”, “emissions”, “bonus rewards”, or “earning rewards” for supplying/staking/LPing those listed assets on the named market/pool/program, that is sufficient EVEN IF no APR/APY or numbers are given.
       (Rationale: many legit farming posts announce incentives going live without quoting rates.)

   Vague “earn rewards” with no clear link to a specific action + venue/context → NO.

================================================
Hard NO rules (precision exclusions)
Always output "no" for:

A) Pure news/announcements/integrations/support without an enrollable earn action
   listings, partnerships, “now supported”, “mainnet live”, “market live” (trading), infra updates → NO.

B) Trading/active PnL / leverage
   perps, margin, options, “trade now”, “volume”, “qualify for boosts by trading”, borrowing-side lending → NO.

C) Competitions/lotteries/referrals/cashback
   leaderboards, trade-to-earn, prize pools for trading, fee rebates, lucky draws, referrals → NO.

D) Airdrop/points/quests as the main mechanic
   seasons/quests/missions/points/claim-only campaigns → NO
   EXCEPT when it is explicitly deposit/stake/LP-based and still meets YES 1–5.

E) Commentary/education/product hype without a joinable instance
   “new era of staking”, “here’s why”, “upwards and onwards”, generic “earn up to X%” evergreen ads with no join window/CTA/context → NO.

================================================
Edge-case clarifications (important)
1) “Incentives are live on <protocol/chain> market; users can supply <assets> to earn rewards”
   Treat as YES if:
   - protocol/market context is named (e.g., “Aave Mantle market”, “Compound on Base”, “Spark market”), AND
   - supply assets are listed, AND
   - incentives/rewards are explicitly live/active.
   APR is NOT required in this specific pattern.

2) Staking integrations / validator providers
   If it only says a platform “brings staking access” or “teaming up” without a concrete staking product instance + join CTA + earn terms/incentives → NO.

3) Launchpool / lock-to-earn
   YES only if it specifies:
   - platform + launchpool surface,
   - locked asset(s),
   - reward token and either reward amounts or explicit “rewards live” mechanics,
   - and enrollment/availability (live or start time).

================================================
Tie-breakers
- When in doubt, output NO.
- If the message could be posted any day as generic marketing, output NO.
- Require a real passive-earn action + identifiable venue/context + assets + joinable availability.
- For earn terms: accept explicit “incentives/rewards live” tied to the action as sufficient; otherwise require APR/APY or numeric reward mechanics.

Respond with only: yes or no
Iteration 40: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 40: Valset score for new program: 0.6060606060606061 (coverage 99 / 99)
Iteration 40: Val aggregate for new program: 0.6060606060606061
Iteration 40: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 0.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 0.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 0.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 40: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 40: Valset pareto front aggregate score: 0.8888888888888888
Iteration 40: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 2: {16, 2, 19, 13}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20}, 15: {0, 1, 2, 4, 14, 17, 19, 20}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19, 20}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19, 20}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 33: {0, 1, 2, 4, 9, 13, 15, 19}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19}, 36: {2}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 38: {3, 4, 5, 10, 12, 15, 18}, 39: {1, 10, 5, 7}, 40: {2, 19, 13}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20}, 45: {2, 11, 16, 19, 20}, 46: {2, 8, 9, 11, 13, 16, 19, 20}, 47: {0, 16, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 49: {0, 1, 5, 6, 7, 10, 11, 18}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18, 20}, 57: {5, 6, 7, 10, 11, 12}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19, 20}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 68: {16}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18, 20}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16, 19}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 98: {2, 4, 15}}
Iteration 40: Best valset aggregate score so far: 0.6767676767676768
Iteration 40: Best program as per aggregate score on valset: 1
Iteration 40: Best score on valset: 0.6767676767676768
Iteration 40: Linear pareto front program index: 1
Iteration 40: New program candidate index: 20
Iteration 41: Selected program 2 score: 0.6363636363636364
Iteration 41: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

Definition (what counts as “yield farming opportunity” here)
A message is YES if it presents a concrete way to earn passive yield/rewards on crypto assets via staking, lending/supplying, vaults, savings/earn products, liquidity provision, farms, or similar “deposit-and-earn” programs.

Core actionability rule (primary)
Say YES only if the message itself is actionable, meaning it identifies at least:
1) WHAT to do: stake / deposit / supply / lend / lock / provide liquidity (LP) / farm / vault deposit / savings/earn subscription
AND
2) WHERE to do it: a specific venue or product that is joinable (protocol/app/exchange + named feature/product/pool/vault/program)
AND
3) WHICH asset(s): at least one specific token/coin or LP pair

APY/APR is NOT required if (1)-(3) are satisfied, but strengthens YES.

Important relaxation to avoid false NOs (common real-world phrasing)
A) Implicit action is allowed if the earn product is clearly joinable:
- If a message says a product is “live/now live/launched/now available” AND states a yield/rate AND indicates it’s an “earn/vault/yield” product, you may treat WHAT as “deposit/allocate funds” even if the verb is not written.
B) Some products are “yield accounts” by nature:
- “Vault”, “Earn”, “Savings”, “Lend”, “Staking”, “Farm”, “Pool”, “Fixed/Fixed rate/term promotion” can supply the WHAT if tied to a joinable product.

Special YES rule for “new product live + target yield” announcements (fixes a common miss)
Say YES when ALL are true:
- The message announces an earn/yield product is live/launching now (or gives a start time)
- It names a specific venue/product brand (e.g., “Zircuit Finance”, “X Earn”, “Y Vault”)
- It includes a concrete yield/range (APR/APY/%) or explicitly says users can earn yield
- It does NOT read as purely institutional-only (no “private/whitelist only/closed beta”)
Notes:
- Token/asset may be absent in these announcements; still say YES if the product is clearly a yield product that a regular user can join now with stated yield. (This is an explicit exception to the asset requirement to capture “live yield product with stated APR”.)
- If it’s vague marketing without “live/available” or without a yield/rate, keep NO.

NO conditions (common traps)
A) Vague yield marketing without enough specificity
- “Start earning”, “top returns”, “high APY”, “up to X%”, “earn more”, “yield szn” WITHOUT a clearly joinable product/venue and participation details → NO.
B) Brand/platform promo without a specific eligible product
- “Our platform has up to 20% APY” with no pool/vault/earn product and no clear joinable offer → NO.
C) Non-yield incentives
- Airdrops/points/quests/XP/Zealy, giveaways, cashback, referrals, lotteries, “trade to win”, competitions, red packets → NO (even if “rewards” are mentioned).
D) Trading/news/infrastructure only
- Listings, buybacks, partnerships, tech updates, events, stablecoin launches, “use as collateral to trade” → NO unless it contains a concrete earn product as per rules.
E) Status-only/past distribution
- “Rewards distributed/claim open/recap” → NO unless it also invites joining an ongoing earn product with venue/product and enough details.
F) Not accessible
- Explicitly institutional-only/private/closed/whitelist-only with no public participation path → NO.
G) Active/leveraged looping strategies as the main point
- Messages primarily about leveraged looping/trading strategies (“looping”, “up to 8x leverage”) without a clear passive earn product users can join directly → NO.

Practical “WHERE” signals (acceptable when tied to an earn offer)
- “Binance Earn/Savings”, “Bybit Earn”, “OKX Earn”, “KuCoin Earn Fixed Promotion”, “Aave supply”, “Morpho vault/market”, “vault”, “pool”, “farm”, “staking”, “savings”, “lending”.

Quick checklist before YES (apply in order)
1) Is there a joinable earn product or program (explicit or clearly implied by “vault/earn/savings/staking/farm/pool”)?
2) Is the venue/product identifiable (name of protocol/app/exchange or specific product brand)?
3) Do we have either:
   - specific asset(s), OR
   - the “new product live + target yield” exception (live/available + yield stated + product named)?
If not → NO.

Respond with only: yes or no
Iteration 41: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 41: Valset score for new program: 0.5656565656565656 (coverage 99 / 99)
Iteration 41: Val aggregate for new program: 0.5656565656565656
Iteration 41: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 0.0, 10: 1.0, 11: 0.0, 12: 1.0, 13: 1.0, 14: 0.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 0.0, 19: 0.0, 20: 1.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 0.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 0.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 1.0, 41: 0.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 0.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 0.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 41: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 41: Valset pareto front aggregate score: 0.8888888888888888
Iteration 41: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 2: {2, 13, 16, 19, 21}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20}, 15: {0, 1, 2, 4, 14, 17, 19, 20, 21}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19, 20, 21}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19, 20}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19, 21}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 21}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, 33: {0, 1, 2, 4, 9, 13, 15, 19}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19, 21}, 36: {2, 21}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 38: {3, 4, 5, 10, 12, 15, 18}, 39: {1, 10, 5, 7}, 40: {21, 2, 19, 13}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21}, 45: {2, 11, 16, 19, 20, 21}, 46: {2, 8, 9, 11, 13, 16, 19, 20, 21}, 47: {0, 16, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 49: {0, 1, 5, 6, 7, 10, 11, 18}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18, 20}, 57: {5, 6, 7, 10, 11, 12}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19, 20, 21}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 68: {16, 21}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18, 20}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16, 19, 21}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, 98: {2, 4, 21, 15}}
Iteration 41: Best valset aggregate score so far: 0.6767676767676768
Iteration 41: Best program as per aggregate score on valset: 1
Iteration 41: Best score on valset: 0.6767676767676768
Iteration 41: Linear pareto front program index: 1
Iteration 41: New program candidate index: 21
Iteration 42: Selected program 19 score: 0.6161616161616161
Iteration 42: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

What counts as “yield farming” here (YES):
- User can passively earn by taking an earn action: stake / delegate / liquid stake / supply / lend / deposit into earn or savings / lock / add liquidity (LP) / farm / enter a vault / join a launchpool or staking program.
- Opportunity is joinable now or has a clearly stated start time/window.

What does NOT count (NO):
- General marketing, “why choose our earn product”, “higher APY”, “up to X%”, “discover”, “get started” without a concrete, specific joinable pool/vault/product with asset(s).
- News/TVL reports/recaps/analytics even if they mention “incentives”, “campaign”, “rewards”, or rates, unless it clearly invites the user to join a specific earn market/pool with asset(s).
- Trading/price calls/competitions/quests/points/airdrops/raffles/referrals/cashback/cards.
- “Rewards distributed/claim now/airdrop to stakers” status-only messages.

Hard requirement: must be an EARN ACTION, not just “rewards exist”.

Core rule (must be actionable from the message alone):
Answer YES only if ALL are satisfied:

1) WHAT (earn action) is explicitly present:
   - stake / delegate / deposit / supply / lend / lock / add liquidity / farm / vault / earn / savings / launchpool
   If the message only says “earn”, “APY”, “rewards”, “incentives”, “campaign” without an action → NO.

2) WHERE (specific joinable venue + specific earn surface) is present:
   - Venue = protocol/app/exchange/platform name
   AND earn surface = a specific product/pool/vault/market/program name or clearly identified surface (e.g., “Aave v3 USDC market”, “Kamino Multiply vault”, “KuCoin Earn Fixed promotion”).
   If it’s only the venue or only a generic “Earn” brand page with no specific product/surface → NO.

3) WHICH asset(s) are present:
   - At least one explicit token/coin (e.g., BTC, ETH, USDT, USDC) OR an LP pair (e.g., ETH-USDC) OR an unmistakable receipt token that implies the underlying being staked (e.g., “stake SOL to get mSOL” implies SOL).
   If no identifiable asset(s) → NO except the narrow exception below.

Narrow exception (rare):
- “Any deposit / no minimum / any amount” exception:
  If the message names a specific live earn product/program + venue AND explicitly says any/no-minimum deposit AND provides an explicit yield rate (APR/APY/%) → YES even if the asset is not named.

Marketing / “brand pitch” guardrail (important; reduces false YES):
- If the message is primarily promotional language (e.g., “Why choose X Earn”, “3 advantages”, “higher APY”, “enjoy USDT level yields”, “discover”, “get started”) and does NOT name a specific joinable pool/vault/market/program (WHERE) with assets (WHICH), then output NO even if it mentions an APY and mentions popular assets in a generic way.
- A rate + generic product category (e.g., “SmartEarn”, “Earn”, “Savings”) is NOT enough unless a specific program/promotion/pool is identified as joinable (e.g., “Fixed Promotion”, “30-day BTC fixed product”, “USDC flexible savings”), with venue and asset(s).

Clarifications (keep strict but avoid false NO):
- Link is not required if venue + specific earn surface + asset(s) + earn action are present.
- “Live/Now available/Start time” launches can be YES if they satisfy WHAT+WHERE+WHICH (rate optional).
- Restrictions (e.g., region limits) do not automatically make it NO if otherwise actionable.
- Borrow incentives that “reduce borrowing cost” are NOT passive yield. Treat as NO unless the message clearly offers supplying/lending/staking/LP/vault earning to the user.

Decision procedure:
1) Does it clearly instruct/describe a passive earn action (stake/deposit/supply/lend/LP/farm/vault/lock/launchpool/delegate)? If not → NO.
2) Does it specify WHERE: a specific venue + specific earn surface (pool/vault/market/program/product/promotion) that is joinable? If not → NO.
3) Does it specify WHICH asset(s) (token/pair/underlying)? If not → apply only the “any deposit/no minimum + rate + named product” exception; otherwise NO.
4) If it is mainly claiming/distribution/status/marketing/analytics without a joinable earn action → NO.
5) If still uncertain → NO.

Respond with only: yes or no
Iteration 42: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 42: Valset score for new program: 0.6262626262626263 (coverage 99 / 99)
Iteration 42: Val aggregate for new program: 0.6262626262626263
Iteration 42: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 0.0, 15: 0.0, 16: 1.0, 17: 0.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 1.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 0.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 42: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 42: Valset pareto front aggregate score: 0.8888888888888888
Iteration 42: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 2: {2, 13, 16, 19, 21}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18, 22}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18, 22}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 22}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20}, 15: {0, 1, 2, 4, 14, 17, 19, 20, 21}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19, 20, 21}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19, 20, 22}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19, 21, 22}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 22}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19, 22}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22}, 33: {0, 1, 2, 4, 9, 13, 15, 19}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19, 21, 22}, 36: {2, 21}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 38: {3, 4, 5, 10, 12, 15, 18}, 39: {1, 10, 5, 7}, 40: {21, 2, 19, 13}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22}, 45: {2, 11, 16, 19, 20, 21, 22}, 46: {2, 8, 9, 11, 13, 16, 19, 20, 21}, 47: {0, 16, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 49: {0, 1, 5, 6, 7, 10, 11, 18, 22}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18, 20, 22}, 57: {5, 6, 7, 10, 11, 12}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19, 20, 21, 22}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18, 22}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 68: {16, 21}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18, 20}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16, 19, 21, 22}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}, 98: {2, 4, 21, 15}}
Iteration 42: Best valset aggregate score so far: 0.6767676767676768
Iteration 42: Best program as per aggregate score on valset: 1
Iteration 42: Best score on valset: 0.6767676767676768
Iteration 42: Linear pareto front program index: 1
Iteration 42: New program candidate index: 22
Iteration 43: Selected program 9 score: 0.6060606060606061
Iteration 43: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

========================
DECISION STANDARD (STRICT)
========================
Say YES only when the message itself provides enough concrete participation details that a user can take the next step (stake/deposit/supply/LP/etc.) without guessing.

Treat “yield farming opportunity” broadly as passive earn via:
- staking/validator staking/restaking
- lending/supplying/borrowing *to earn* (only if explicitly stated)
- LP/providing liquidity/farming
- vaults/pools/markets/earn/savings/fixed-term products
- incentive programs tied to deposits/LP/staking (token rewards)

Do NOT assume legitimacy from reputation; judge only the text.

========================
CORE REQUIREMENTS FOR YES
========================
All must be satisfied:

1) WHAT (passive earn action/product):
   Must include an explicit action or clearly joinable earn product:
   “stake”, “deposit”, “supply”, “lend”, “provide liquidity/LP”, “farm”, “vault”, “pool”, “market”, “earn/savings”, “lock”, “restake”.

2) WHERE (specific joinable venue + product context):
   Must name a protocol/app/exchange AND identify a specific joinable feature/product context.
   Acceptable WHERE examples:
   - “Aave supply…”, “Morpho market…”, “Kamino deposit…”, “Uniswap v3 pool…”, “Yearn vault…”, “Binance Earn Fixed…”
   - Multi-venue lists are allowed (e.g., “deposit into Yearn, Morpho, Spectra on Katana”).
   Not enough:
   - only a chain (“on Starknet/Solana/BNB”)
   - only a generic concept (“money market”, “vaults”, “earn” with no venue)
   - only “partnered with X” without a join instruction.

3) WHICH ASSET(S):
   Must specify at least one concrete deposit/stake/LP asset:
   - token symbols/names (ETH, USDC, BERA, iBERA, SNX, KAT)
   - LP pair (ETH/USDC)
   - derivative/re-staked tokens (stETH, PT/YT, iBERA, etc.)
   If the message provides only “incentives/rewards” without stating what the user deposits/stakes → NO.

APY/APR is helpful but NOT required if (1)-(3) are clearly met.

=============================
SPECIAL RULE: INCENTIVES/BOOSTS
=============================
YES if the message tells users to DEPOSIT/STAKE/SUPPLY/LP into named venue(s) with named asset(s) to earn incentives/rewards,
even if it also mentions points/XP/boosts.
Example that should be YES:
- “Deposit into Yearn/Morpho/Spectra on Katana to earn KAT incentives / boosted yields / XP bonuses”
As long as (1) action + (2) venue(s) + (3) asset(s) are present.

If it is ONLY points/XP/quests without an onchain earn action (deposit/stake/LP) → NO.

=========================
EXPLICIT NO (FILTER OUT)
=========================
Say NO if any of these apply (even if “earn/reward/yield” appears):
- Pure points/XP/quests/badges (Zealy/Galxe) with no deposit/stake/LP instruction.
- Trading activity required: “trade to earn”, perps, volume competitions, “trade to win”.
- Giveaways/lotteries/raffles/lucky draw/airdrops without a deposit/stake/LP product.
- Listings/news/partnerships/integration announcements with no participation instruction.
- Educational content (“learn about our Earn products”) without a specific product + asset.
- Past-only recaps (“rewards distributed”, “season ended”) with no invitation to join an active earn product.
- Private/closed/invite-only where a regular user cannot join now.

========================
VENUE/PRODUCT SPECIFICITY
========================
To satisfy WHERE, at least one of the following must be true:
- A named earn feature is stated: “Earn”, “Savings”, “Fixed/Term”, “Vault”, “Pool”, “Market”, “Module”, “Farm”, “Staking”
  AND it’s tied to a named venue (protocol/exchange/app).
- A direct action is tied to a named venue: “stake X on Y”, “deposit X into Y”, “supply X on Y”.

========================
FINAL CHECKLIST (ALL MUST BE YES)
========================
- Is there a passive earn action/product (stake/deposit/supply/LP/vault/etc.)?
- Is there a specific venue + joinable product context (protocol/app/exchange + module/vault/pool/market/earn plan or direct action on the venue)?
- Are the eligible asset(s) explicitly stated?

If any answer is “no” → output no.

Respond with only: yes or no
Iteration 43: New subsample score 14.0 is better than old score 13.0. Continue to full eval and add to candidate pool.
Iteration 43: Valset score for new program: 0.5959595959595959 (coverage 99 / 99)
Iteration 43: Val aggregate for new program: 0.5959595959595959
Iteration 43: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 0.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 0.0, 18: 0.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 0.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 0.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 0.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 43: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 43: Valset pareto front aggregate score: 0.8888888888888888
Iteration 43: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 2: {2, 13, 16, 19, 21}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18, 22}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18, 22}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 22, 23}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 23}, 15: {0, 1, 2, 4, 14, 17, 19, 20, 21}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19, 20, 21}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19, 20, 22}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19, 21, 22}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 22, 23}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 23}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19, 22, 23}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23}, 33: {0, 1, 2, 4, 9, 13, 15, 19, 23}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19, 21, 22}, 36: {2, 21}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 38: {3, 4, 5, 10, 12, 15, 18}, 39: {1, 10, 5, 7}, 40: {2, 13, 19, 21, 23}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18, 23}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23}, 45: {2, 11, 16, 19, 20, 21, 22}, 46: {2, 8, 9, 11, 13, 16, 19, 20, 21}, 47: {0, 16, 4}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 49: {0, 1, 5, 6, 7, 10, 11, 18, 22}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18, 20, 22}, 57: {5, 6, 7, 10, 11, 12}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19, 20, 21, 22, 23}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 63: {0, 1, 2}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18, 22}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 68: {16, 21}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18, 20, 23}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16, 19, 21, 22, 23}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, 98: {2, 4, 15, 21, 23}}
Iteration 43: Best valset aggregate score so far: 0.6767676767676768
Iteration 43: Best program as per aggregate score on valset: 1
Iteration 43: Best score on valset: 0.6767676767676768
Iteration 43: Linear pareto front program index: 1
Iteration 43: New program candidate index: 23
Iteration 44: Selected program 16 score: 0.6363636363636364
Iteration 44: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

----------------------------
What counts as YES (yield farming here)
----------------------------
A message is YES only when it presents an actionable “park assets → earn yield/rewards” opportunity such as:
- staking (including liquid staking), restaking
- lending/supplying to earn interest
- liquidity provision (LP) + farming/rewards
- vault deposit / strategy vault / “Earn” / “Savings” / “Simple Earn” / “Fixed/Flexible” earn products
- “deposit/lock/subscribe/supply” for yield, interest, APR/APY, rewards emissions

Crucial: It must be joinable by a regular user based on the message text.

----------------------------
Core rule (must be actionable from the message text)
----------------------------
Say YES only if the message itself identifies ALL of the following:

(1) WHAT earn action/product
- Explicit: stake, deposit, supply, lend, lock, provide liquidity/LP, farm, vault, earn, savings, subscribe (to earn), simple earn, fixed/flexible earn
- Acceptable implicit WHAT: if it clearly names an earn product type AND provides a yield rate (APR/APY/%), the “deposit” action can be implicit (e.g., “USDC Vault 8% APY”)

AND

(2) WHERE (specific joinable venue + specific earn feature)
- Must name a concrete venue/product/pool/vault/market/program that a user can join.
- Examples that satisfy WHERE: “Aave USDC market (Arbitrum)”, “Curve frxUSD/OUSD pool”, “Binance Earn USDT Simple Earn”, “Bybit Earn Fixed Promotion”, “Morpho USDC vault”, “Venus USDT vault via Binance Wallet”.

AND

(3) WHICH asset(s)
- At least one specific token/coin or LP pair (USDC, ETH, BTC, SOL, ETH/USDC, etc.)

APY/APR is not required if (1)-(3) are satisfied, but it strongly supports YES.

----------------------------
Hard guardrails (major false-YES sources)
----------------------------
1) Borrowing / fixed-rate borrow markets are NOT yield opportunities by themselves.
- If the primary action is “borrow”, “take a loan”, “fixed-rate borrowing”, “open a borrow position”, “use as collateral”, “leverage”, “margin”, “perps”, “trade”, “short/long” → NO
- Even if the message mentions “while your collateral earns X%”, still output NO UNLESS it clearly offers a straightforward, standalone earn path (deposit/stake/supply/earn/vault) that a normal user can do without borrowing.
  * Example: “Borrow X while collateral earns 200% APR” is usually a borrow-product ad → NO.

2) Collateral/utility announcements are NOT yield opportunities unless earning is explicit.
- “now usable as collateral”, “supported as collateral”, “borrow against” → NO unless it also explicitly offers earning/interest via supply/earn/vault/staking with a named market/product.

3) Points/airdrops/cashback/referrals/quests/competitions are NOT yield farming.
- “reward drops”, “daily drops”, “season”, “points”, “Zealy”, “airdrop”, “giveaway”, “cashback”, “invite”, “trade to win”, “leaderboard”, “allocation”, “snapshot”, “prize pool share” → NO
- Exception: If it is clearly an on-chain farm/vault/staking program for a specific asset on a specific venue (meets core rule) and the “rewards” are the yield from depositing/LPing (not just tasks). If ambiguous → NO.

4) General marketing without specifics → NO
- “high APY”, “start earning”, “top yields”, “incentives are back” without specific product+assets → NO.

5) Not accessible / not live
- Institutional-only, private, closed beta, or no ability to join now and no clear start time → NO.

----------------------------
YES conditions (must still satisfy core rule)
----------------------------
Return YES if ANY of the following holds:

A) Concrete earn action + venue/product + asset(s)
- “Stake ETH on Lido”, “Supply USDC on Aave”, “Deposit USDT in Binance Simple Earn”, “Provide liquidity to ETH/USDC pool on Uniswap and farm rewards”.

B) Explicit yield rate tied to a joinable product
- APR/APY/% is mentioned AND clearly tied to a named earn product/pool/vault/market on a named venue AND specifies asset(s).
- “Up to X%” is acceptable ONLY if the specific eligible asset(s) and specific earn product/program are stated.

C) “Live/Now available” earn launch with participation details
- “Staking is live / vault launched / farm live” AND includes venue/product + asset(s). Rate optional.

D) Time-bound boosted/limited earn promo (still must be specific)
- Boost/promo + named earn product/program + asset(s) (+ start/end/time).

----------------------------
Disambiguation rules for tricky cases
----------------------------
- “Supply” implies earning only if:
  (a) a rate/interest/APY/APR/rewards is explicitly stated, OR
  (b) a clearly named lending/earn market/vault is stated (Aave market, Morpho vault, Compound market, etc.)
  AND asset(s) are stated.
  Otherwise → NO.

- “Vaults available/launched” is YES only if at least one vault is named AND its asset(s) are specified (rate optional). Otherwise → NO.

- Liquid staking tokens: If the message states you can stake/deposit the base asset into a named liquid staking product (or clearly offers a named LST earn program) → YES. If it only claims “token delivers X%” without telling where/how to join (no venue/product) → NO.

- “Hold X to get rewards” is NOT yield farming unless it is explicitly a staking/earn product (lock/stake/deposit) on a named venue; simple holding for drops/points → NO.

----------------------------
Quick checklist before YES (all must be true)
----------------------------
- Do I know what the earn product/action is (stake/deposit/supply/LP/farm/vault/earn/savings)?
- Do I know where (named venue + specific earn product/pool/vault/market/program)?
- Do I know which asset(s)?
If any is missing → NO.

Respond with only: yes or no
Iteration 44: New subsample score 14.0 is not better than old score 15.0, skipping
Iteration 45: Selected program 19 score: 0.6161616161616161
Iteration 45: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. If any key detail is missing or ambiguous, output no.

========================
WHAT COUNTS AS YES
========================
YES only if the message offers an actionable passive-earn mechanism, such as:
- Staking / liquid staking / restaking / validator delegation
- Lending / supplying / depositing to money markets
- Vaults / earn products / savings / fixed or flexible earn
- Liquidity provision (add liquidity) + farming/incentives for an LP position
- Launchpool / staking campaigns / “earn” programs on CEX/DEX
- “Liquidity incentive program” only if it clearly tells users to provide liquidity/deposit into a specific pool

Must be joinable by a typical user (publicly available now or with a clear start time). If it’s closed, invite-only, institutional-only, or merely “coming soon” without a join window → NO.

========================
HARD REQUIREMENT: EARN ACTION (not just rewards exist)
========================
Messages that ONLY say:
- “rewards distributed”, “claim rewards”, “airdrop to stakers”, “APR update”, “epoch ended”, “points”, “incentives active”
are NOT yield opportunities unless the same message also clearly presents an ongoing way to start earning (stake/deposit/LP/etc.) with WHERE + WHICH.

========================
CORE RULE: MUST BE ACTIONABLE FROM THE MESSAGE
========================
Say YES only if all are satisfied:

(1) WHAT: explicit earn action/mechanism is present (stake/deposit/supply/lend/lock/add liquidity/farm/vault/earn/launchpool/delegate)
AND
(2) WHERE: a specific joinable venue + named earn surface is present:
    - venue = protocol/app/exchange/platform (e.g., Aave, Kamino, Binance, HTX, MEXC, Uniswap, etc.)
    - earn surface = a named product/pool/vault/market/program (e.g., “Binance Earn Dual Investment”, “HTX Earn”, “Aave v3 USDC market”, “ATOM staking with P2P”, “ETH-USDC pool on Uniswap v3”, “IP staking gala on MEXC”)
AND
(3) WHICH asset(s): at least one specific token/coin OR a specific LP pair is present.
    - Acceptable: “stake SOL to get mSOL” (SOL implied), “ETH-USDC LP”, “USDC on Aave”
    - Not acceptable: “deposit assets”, “stake now” with no asset named

If any of (1)-(3) is missing → NO, unless a strict exception below applies.

========================
STRICT EXCEPTIONS (RARE)
========================
Exception A: “Any deposit / no minimum” asset omission
You may say YES without a named asset ONLY if ALL hold:
- a clearly live earn product/program is named (WHERE satisfied),
- the message explicitly says “any amount / no minimum / any deposit”,
- and a concrete rate is given (APR/APY/%).
Otherwise → NO.

Exception B: Unmistakable earn product naming + asset
If the message names an unmistakable earn surface (e.g., “HTX Earn”, “Binance Earn”, “Bybit Earn”, “OKX Earn”, “KuCoin Earn”, “Gate Earn”, “Launchpool”, “Savings”, “Staking”) AND includes an asset AND clearly indicates earning/yield/rewards (rate optional) → YES.

Exception C: “Live/Now available” launches
“Staking is live / vault launched / farm live / incentives live” can be YES only if WHERE + WHICH are present (rate optional).

========================
IMPORTANT DISAMBIGUATION (COMMON TRAPS)
========================
Always NO for:
- Competitions/leaderboards/lotteries/giveaways (“rank top 100”, “up for grabs”, “reward pool for winners”), even if tied to an earn product
- Referral programs, invites, allocation boosts, “refer to win”
- Trading-focused promos (“trade to earn”, “volume contest”, perps/leverage, “copy trade”, funded accounts)
- Pure news/listings/partnerships/raising/roadmaps/metrics/tech upgrades
- APR/APY “updates” that don’t instruct how/where to join a specific pool now
- High APR screenshots/bots/“signals” without clear joinable venue + pool + asset(s)

APR/APY alone is NOT enough; must still meet WHAT+WHERE+WHICH.

========================
DECISION PROCEDURE (FAST)
========================
1) Does the message instruct or clearly offer a passive-earn ACTION (stake/deposit/supply/lend/LP/farm/vault/earn/launchpool/delegate)?
   - If no → NO.
2) Does it specify WHERE (venue + named earn surface/pool/vault/market/program)?
   - If no → NO.
3) Does it specify WHICH asset(s) (token/pair/underlying staked asset)?
   - If no → apply Exception A only; otherwise NO.
4) Is it primarily about claiming/distribution/points/competition/referral/trading/news?
   - If yes and no clear joinable earn action meeting 1-3 → NO.
5) If still uncertain → NO.

Respond with only: yes or no
Iteration 45: New subsample score 15.0 is not better than old score 15.0, skipping
Iteration 46: Selected program 19 score: 0.6161616161616161
Iteration 46: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

========================
What counts as YES (yield farming here)
========================
YES only if the message itself presents a concrete, joinable passive-earn action, such as:
- staking / delegating to validators / liquid staking deposit
- lending/supplying/borrowing markets where suppliers earn yield
- vault deposits / automated yield strategies
- liquidity provision (add liquidity) + farm/incentives
- savings/earn products (flex/locked), launchpool/earn programs

Must be something a normal user can do (public/permissionless or clearly open to individuals) now or at a stated start time.

========================
Hard requirements (core rule)
========================
Say YES only if ALL are satisfied:

(1) WHAT (earn action): explicit action verb or unmistakable earn mechanism
    stake / delegate / deposit / supply / lend / lock / add liquidity / LP / farm / vault / earn / savings / launchpool

AND

(2) WHERE (joinable venue + specific earn surface):
    a named protocol/app/platform/exchange AND a specific product/surface such as:
    pool/vault/market/farm/program/earn/savings/launchpool/validator

AND

(3) WHICH asset(s):
    at least one specific token/coin OR an LP pair OR an underlying implied by a receipt token
    (e.g., “stake SOL to get mSOL” implies SOL).

If any of (1)-(3) is missing → NO, unless an exception below applies.

========================
Critical strictness to prevent false YES (key change)
========================
If the message is primarily:
- a protocol/company deploying funds themselves (“we’re backing it with $10M deployment”, “our treasury deposited”, “strategy provider deposited”)
- descriptive PR about a vault/product without instructing users to deposit/stake/supply or stating it is open for users to join now
- institutional-only / private access / waitlist without a clear public join path/time
then output NO even if it mentions “yield vault”, “capacity”, “permissionless”, or “open to individuals”.
To be YES, the message must clearly invite/enable user participation (e.g., “Deposit X into Y vault on Z”, “Stake X on Z”, “Supply X on Z market”).

Also: “yield generating vault” language alone is NOT enough. Require an explicit user action or a clear “deposits are now live/open” statement.

========================
Clarifications (keep good behaviors)
========================
- Links are not required if venue + product + asset(s) + action are clearly stated.
- “Earn rewards” without specifying stake/deposit/supply/LP/etc. → NO.
- “Claim rewards”, “rewards distributed”, “epoch rewards ready”, “airdrop to stakers” → NO unless the same message also clearly presents an ongoing/joinable earn action with venue + product + asset(s).
- Launch announcements can be YES only when they clearly indicate users can now participate and what to deposit/stake/supply/LP.

========================
Exceptions (rare; keep strict)
========================
Exception 1) Asset omitted but explicitly “any deposit/no minimum” + rate:
YES if:
- named venue + named earn product/program is live/open,
- explicitly says deposits of any amount/no minimum,
- and provides a concrete rate (APR/APY/%).
Otherwise NO.

Exception 2) Implicit action via unmistakable earn product naming:
YES if the message names a well-defined earn surface (e.g., “Aave USDC market”, “Binance Earn USDT Simple Earn”, “Lido staking”) AND specifies asset(s) AND clearly indicates earning yield/rewards (rate optional).
If it’s just an integration/availability statement with no invitation to earn → NO.

========================
NO conditions (common traps)
========================
- General news, integrations, partnerships, listings, trading availability, methodology/metrics, infra updates → NO.
- Incentive “campaigns” that are ambiguous (volume/points/quests/leaderboards) and not explicit LP/staking/farming deposit mechanics → NO.
- Competitions/lotteries/giveaways/cashback/referrals → NO.
- “Up to X%” marketing without concrete joinable pool/vault/product + venue + asset(s) → NO.
- Revenue share to holders / tokenomics yield talk without a joinable staking/deposit mechanism described → NO.

========================
Decision procedure
========================
1) Is there a passive-earn ACTION a user can take (stake/deposit/supply/LP/farm/vault/lock/delegate/launchpool)? If not → NO.
2) Is WHERE present (named venue + specific earn surface/pool/vault/market/program/validator)? If not → NO.
3) Are WHICH asset(s) present? If not → apply Exception 1 only; else NO.
4) Does the message clearly indicate users can join (now or at stated start time), not merely that the team is deploying funds or describing a product? If not → NO.
5) If still uncertain → NO.

Respond with only: yes or no
Iteration 46: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 46: Valset score for new program: 0.6060606060606061 (coverage 99 / 99)
Iteration 46: Val aggregate for new program: 0.6060606060606061
Iteration 46: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 0.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 0.0, 15: 1.0, 16: 1.0, 17: 0.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 0.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 0.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 0.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 0.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 0.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 0.0, 97: 0.0, 98: 1.0}
Iteration 46: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 46: Valset pareto front aggregate score: 0.8888888888888888
Iteration 46: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 2: {2, 13, 16, 19, 21}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18, 22}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18, 22}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 22, 23, 24}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 23}, 15: {0, 1, 2, 4, 14, 17, 19, 20, 21, 24}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19, 20, 21}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19, 20, 22, 24}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19, 21, 22, 24}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 22, 23, 24}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 23, 24}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19, 22, 23}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24}, 33: {0, 1, 2, 4, 9, 13, 15, 19, 23, 24}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19, 21, 22}, 36: {2, 21}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 38: {3, 4, 5, 10, 12, 15, 18}, 39: {1, 10, 5, 7}, 40: {2, 13, 19, 21, 23}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18, 23}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 45: {2, 11, 16, 19, 20, 21, 22}, 46: {2, 8, 9, 11, 13, 16, 19, 20, 21, 24}, 47: {0, 16, 4, 24}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 49: {0, 1, 5, 6, 7, 10, 11, 18, 22}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18, 20, 22}, 57: {5, 6, 7, 10, 11, 12}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19, 20, 21, 22, 23, 24}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 63: {0, 1, 2, 24}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18, 22}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 68: {16, 24, 21}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18, 20, 23}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16, 19, 21, 22, 23, 24}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 98: {2, 4, 15, 21, 23, 24}}
Iteration 46: Best valset aggregate score so far: 0.6767676767676768
Iteration 46: Best program as per aggregate score on valset: 1
Iteration 46: Best score on valset: 0.6767676767676768
Iteration 46: Linear pareto front program index: 1
Iteration 46: New program candidate index: 24
Iteration 47: Selected program 9 score: 0.6060606060606061
Iteration 47: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

========================
DECISION STANDARD (STRICT)
========================
Say YES only when the message itself provides a concrete, joinable earn action with enough specifics that a user could take the next step without guessing.

Core requirements for YES (must ALL be met):
1) WHAT: a passive earn action/product is explicitly offered
   - stake/staking, deposit, supply, lend, lock, farm, provide liquidity/LP, vault, pool, savings/earn, fixed/term earn, liquidity mining, “earn APR/APY” tied to holding in an earn product.
2) WHERE: a specific joinable venue AND a specific product/pool/vault/market/earn plan name
   - Must identify a concrete place to do it (protocol/app/exchange) AND the exact earn surface (pool/vault/market/campaign/plan).
3) WHICH ASSET(S): at least one specific token/coin OR LP pair is named (e.g., USDC, ETH, USDT, ETH/USDC LP).

If ANY of (1)-(3) is missing → NO.

“Live/now/extended” does NOT override missing WHERE/WHAT/ASSET details.

APY/APR is optional; if present it must be tied to the named earn product.

Assume “live now” unless the message clearly says future-only, ended, closed, snapshot already taken, or invite-only.

=========================================
CRITICAL: FILTER OUT FALSE-POSITIVE TRAPS
=========================================
Even if words like “rewards”, “yield”, “APR”, “APY”, “earn” appear, say NO if it is not a concrete passive-earn deposit/stake/LP offer.

Always say NO for:
- Lucky draws, raffles, lotteries, prize pools, “chance to win”, spin-to-win, airdrop draws → NO.
- Trade-to-win, deposit-to-get tickets, competitions, referrals/affiliate contests → NO.
- Cashback, card spend rewards, shopping discounts → NO.
- Quests/points/XP multipliers, Zealy/Galxe tasks, badges, “earn points”/“points campaign” → NO.
- Pure news/announcements: listings, partnerships, infrastructure updates, “coming soon”, “beta/test it now” without a specific earn product + asset + venue → NO.
- Past-only recaps/distributions (e.g., “rewards distributed”, “week X rewards distributed”) → NO unless it ALSO explicitly invites joining/doing the earning action now with WHERE + WHAT + ASSET(S).

=========================================
CAMPAIGN / REWARDS EXTENSION RULE (KEY)
=========================================
Messages about “rewards extended”, “added X tokens to the campaign”, “keep your position”, “already deposited you’re included”, etc. are YES ONLY IF the message itself includes enough to join from scratch:
- It must still state WHAT to do (e.g., deposit/LP/supply/stake),
- AND WHERE (named venue + specific pool/vault/market/campaign),
- AND WHICH ASSET(S).

If it only mentions a pair/campaign name and extra rewards but does NOT clearly specify the venue/product in a joinable way → NO.
If it sounds like an insider/continuation update for existing participants without clear join instructions for new users → NO.

=================================
WHEN TO SAY YES (SUFFICIENT)
=================================
YES if the message contains one of the following AND satisfies ALL core requirements (WHAT + WHERE + ASSET):

A) Explicit instruction:
- “Stake/deposit/supply/lend/lock/LP/farm/vault deposit” + (venue + specific product/pool/vault/market/plan) + (asset(s)).

B) Explicit earn product with rate:
- APY/APR/reward rate tied to a named product/pool/vault/market/earn plan on a named venue AND specifies asset(s).

C) Earn launch “live/now available” WITH participation details:
- “Staking/vault/earn/pool is live/launched” AND it includes venue + specific product + asset(s) (and implies you can deposit/stake).

D) CeFi Earn promos (allowed if specific):
- “Binance/Bybit/OKX/KuCoin Earn/Savings/Fixed/Term/etc.” is YES only if it names the earn product type/plan AND eligible asset(s) (rate optional).

========================
VENUE/PRODUCT SPECIFICITY
========================
WHERE must be specific enough to identify a joinable earn surface.
Good:
- “Aave supply USDC”, “Morpho USDC market”, “Pendle PT/YT pool”, “Uniswap v3 ETH/USDC pool”, “Vesu sUSN vault”, “Lido stake ETH”, “KuCoin Earn fixed USDT”.
Not enough (→ NO):
- “on Starknet/BNB Chain/Solana”, “lending is coming”, “test it now”, “smart lending campaign” without named venue + specific pool/vault/market/plan.

========================
FINAL CHECKLIST (ALL MUST BE TRUE FOR YES)
========================
- Do I know WHAT passive-earn action/product the user should do?
- Do I know WHERE (named venue + specific product/pool/vault/market/earn plan)?
- Do I know WHICH asset(s) are used?
If any answer is “no” → output no.

Respond with only: yes or no
Iteration 47: New subsample score 14.0 is not better than old score 14.0, skipping
Iteration 48: Selected program 2 score: 0.6363636363636364
Iteration 48: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

Definition (what counts as “yield farming opportunity” here):
A message is YES only if it offers a concrete, passive-earn action a normal user can take (stake/deposit/supply/lend/lock/LP/farm/vault/earn/savings) on a specific venue/product for a specific asset (or LP pair), in a way that is joinable now (or with a clearly stated start time).

Core rule (must be satisfied for YES):
The message itself must identify all three:
1) WHAT to do: stake / deposit / supply / lend / lock / provide liquidity / farm / vault / earn / savings / fixed term / flexible earn
AND
2) WHERE to do it: a specific venue + specific earn surface (named protocol/app + pool/vault/market/product/program), not just a chain/ecosystem
AND
3) WHICH asset(s): at least one specific token/coin or LP pair

APY/APR is optional if (1)-(3) are present, but strengthens YES.

Important: platform/ecosystem-only guidance is NOT enough
- If the message only says “stake”, “deposit”, “lend”, “provide liquidity”, “let your tokens work”, “use X chain”, “on X ecosystem”, “on Movement”, etc. WITHOUT naming a specific joinable product/pool/vault/market on a protocol/app → NO.
- “Go stake for rewards” is NO unless it also names the staking product/venue and the asset.

Positive (YES) patterns — any of the following, but still must satisfy the core rule:
1) Concrete earn action + specific venue/product + asset(s)
   - Examples: “Stake SOL on Marinade”, “Supply USDC on Aave”, “Deposit ETH into Lido”, “Deposit USDC into Morpho Blue market [name]”, “Provide liquidity to ETH/USDC on Uniswap v3 pool”, “Deposit into Beefy vault [vault name] for [asset]”.
2) Explicit yield/rate tied to a joinable product with asset(s)
   - Mentions APY/APR/reward rate AND ties it to a named earn product/pool/vault/market on a named venue AND specifies asset(s).
   - “Starts [date/time]” is acceptable; otherwise assume live unless clearly ended/closed.
3) Earn product launch that is clearly joinable
   - “Staking/Farm/Vault/Earn is live” AND includes venue/product + asset(s). Rate optional.
4) Fixed/flexible promotions on CEX earn platforms (must be specific)
   - YES only if it names: the platform’s Earn product type (e.g., “Binance Earn Fixed”, “OKX Earn”, “Bybit Earn”, “KuCoin Earn Fixed Promotion”) AND the asset(s) (and term/rate if provided).
   - “Up to X% on Earn” without eligible asset/product → NO.

Hard NO (common traps):
A) Vague yield marketing or generic calls-to-action
   - “Start earning”, “high APY”, “up to 20%”, “earn rewards”, “boost”, “let it work for you” with no specific product/pool/vault/market + asset(s) → NO.
B) Education/instructions without a specific offer
   - Wallet setup instructions + “then stake/lend/LP” without naming where/product → NO.
C) Non-yield incentives
   - Airdrops, points, quests, Zealy, mint-to-earn with points/tickets, prize pools, giveaways, referrals, cashback, competitions, “trade to win”, claim/register announcements → NO.
D) Trading/news/infrastructure only
   - Listings, trading pairs, “deposits/withdrawals enabled”, partnerships, tech updates, security notices, interviews, ecosystem maps → NO.
E) Past/status-only rewards
   - “Rewards distributed”, “APR updated” without participation details (venue/product + asset) → NO.
F) Not accessible
   - Institutional-only/private/closed beta with no public join path → NO.

Venue specificity guidance (WHAT counts as “WHERE”):
- Acceptable WHERE requires a named protocol/app/exchange AND an earn surface (pool/vault/market/earn program/staking contract).
- Just a chain or ecosystem name (e.g., “on Base”, “on Movement”, “on Solana”) is NOT sufficient unless a specific protocol/product is named.

Joinability:
- If it clearly states future start time/window → can be YES if core rule is met.
- If it clearly says ended/closed/snapshot taken/claim only → NO (unless it also invites joining an ongoing earn product meeting the core rule).

Quick checklist before YES (all must be true):
- Do I know the earn action/program?
- Do I know the specific venue + specific product/pool/vault/market?
- Do I know the exact asset(s)?
If any is missing → output no.

Respond with only: yes or no
Iteration 48: New subsample score 15.0 is not better than old score 15.0, skipping
Iteration 49: Selected program 7 score: 0.6565656565656566
Iteration 49: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

========================
CORE DECISION RULE
========================
Return YES only if ALL of the following are satisfied:
1) EARN ACTION is explicit or unambiguously implied by a “pool/vault/staking live” announcement (see Special Case).
2) WHERE (venue/platform) is identifiable.
3) WHAT (asset(s)) is explicit.
4) WHEN (joinability) is explicit: joinable now OR a clear start time/window.
5) NONE of the exclusion cases apply.

If any item is missing or unclear → NO.

========================
1) EARN ACTION (required)
========================
The message must present a passive-earn action such as:
- stake / staking / restake
- deposit / add funds / subscribe
- supply / lend
- lock
- earn / savings / simple earn / earn program
- farm / farming
- provide liquidity / add liquidity / LP / pool deposit / gauge / vault deposit

NOT actions:
- trade / swap / buy / hold / bridge / mint / download / join community
- “claim rewards” without a described earn position to open

Special Case (counts as ACTION even if the verb isn’t written):
- A specific “pool/pair/vault/staking pool” is explicitly announced as live/launched/open AND assets are named AND venue is named.
  Example: “frxUSD/OUSD pool now live on Curve” → YES (action = provide liquidity/deposit into that pool).

========================
2) WHERE / VENUE (required)
========================
At least one of:
- Named protocol/platform + named earn venue/feature:
  (e.g., “MEXC” + “staking”, “Binance” + “Simple Earn”, “Aave v3” + “supply market”, “Curve” + “pool/gauge”, “Yearn” + “vault”)
- Named protocol/platform + explicit pool/pair on that venue
- An explicit link/button clearly tied to the earn product/pool (not just a generic homepage), with surrounding text making it the earn venue

If the message only says “earn with us”, “on our app”, “get started” without identifying the earn venue → NO.

========================
3) WHAT / ASSET(S) (required)
========================
The exact asset(s) to stake/deposit/supply/LP must be stated:
- token symbol/name (e.g., ZAMA, USDT, ETH)
- or an LP pair/constituents (e.g., ETH/USDC)

If assets are implied but not stated → NO.

========================
4) WHEN / JOINABLE (required)
========================
Must explicitly indicate availability:
- now live / live / launched / open / available now / deposits open / start earning now
- OR a clear start/end time or window (date/time)

If no explicit now/start-time signal → NO.

IMPORTANT: “announcement”, “introducing”, “new”, “launch of” alone is NOT enough unless it also clearly signals live/open/starts <time>.

========================
5) OVERRIDE EXCLUSIONS (any → NO)
========================
Always NO for:
1) Competitions, leaderboards, prize pools, lucky draws, red packets, hunts, puzzles, giveaways
   - Even if staking/LP is mentioned as a way to earn entries/points/chances
2) Airdrops, points/quests/campaigns, referrals, cashback, vouchers, “hold to earn points”, “trade/deposit to win”
3) Trading-only promos: perps/margin/leverage/copytrading/swap promos/listings/fee discounts
4) General news/partnerships/tech updates/testnet/beta/infrastructure announcements with no qualifying earn offer meeting requirements
5) Vague marketing: “earn up to X%” or “high APY” without specific venue + asset + joinability
6) Borrow-only / leverage-only updates (E-Mode, collateral, LTV, borrow rates) without explicit supply/deposit/earn offer

========================
APY/APR HANDLING
========================
- APY/APR is helpful but not required.
- If APY/APR is mentioned, requirements (Action, Venue, Assets, Joinable) still must be met.
- “Up to X%” is acceptable ONLY if the product is concrete and joinable (e.g., “Stake ZAMA on MEXC… during Staking Gala…”) and exclusions don’t apply.

========================
QUICK CHECK (all must be yes)
========================
- Can the user open a passive-earn position from this message alone (stake/deposit/supply/LP OR deposit into the named live pool)?
- Is the platform/venue explicitly identified?
- Are the asset(s) explicitly stated?
- Is it explicitly live now or provides a clear start time/window?
- Is it NOT points/airdrop/competition/trade-to-win/trading-only?

If any is no → output no.

Respond with only: yes or no
Iteration 49: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 49: Valset score for new program: 0.6060606060606061 (coverage 99 / 99)
Iteration 49: Val aggregate for new program: 0.6060606060606061
Iteration 49: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 0.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 0.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 0.0, 18: 0.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 1.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 0.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 0.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 0.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 0.0, 97: 0.0, 98: 0.0}
Iteration 49: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 49: Valset pareto front aggregate score: 0.8888888888888888
Iteration 49: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 2: {2, 13, 16, 19, 21}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18, 22, 25}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18, 22, 25}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 23, 25}, 15: {0, 1, 2, 4, 14, 17, 19, 20, 21, 24}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19, 20, 21}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19, 20, 22, 24}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19, 21, 22, 24}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 23, 24, 25}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19, 22, 23, 25}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25}, 33: {0, 1, 2, 4, 9, 13, 15, 19, 23, 24}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19, 21, 22, 25}, 36: {2, 21}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 38: {3, 4, 5, 10, 12, 15, 18, 25}, 39: {1, 10, 5, 7}, 40: {2, 13, 19, 21, 23}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18, 23, 25}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 45: {2, 11, 16, 19, 20, 21, 22}, 46: {2, 8, 9, 11, 13, 16, 19, 20, 21, 24}, 47: {0, 16, 4, 24}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 49: {0, 1, 5, 6, 7, 10, 11, 18, 22, 25}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 25}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18, 25}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18, 20, 22, 25}, 57: {5, 6, 7, 10, 11, 12, 25}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19, 20, 21, 22, 23, 24}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 63: {0, 1, 2, 24}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18, 22, 25}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 68: {16, 24, 21}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18, 25}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18, 20, 23, 25}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16, 19, 21, 22, 23, 24}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, 98: {2, 4, 15, 21, 23, 24}}
Iteration 49: Best valset aggregate score so far: 0.6767676767676768
Iteration 49: Best program as per aggregate score on valset: 1
Iteration 49: Best score on valset: 0.6767676767676768
Iteration 49: Linear pareto front program index: 1
Iteration 49: New program candidate index: 25
Iteration 50: Selected program 7 score: 0.6565656565656566
Iteration 50: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

CORE IDEA:
A message is YES if it clearly presents an actionable passive-earn product/pool/vault that a user can join, with enough specifics to identify what to deposit and where, and it’s available now (or has a clear start time).
However, allow certain “platform-native earn product announcements” (Earn/Vaults/Savings) even when token list is not provided, as long as the action + venue + joinability are explicit.

DECISION FLOW (apply in order):

STEP 0 — HARD EXCLUSIONS (if any applies → NO, even if “stake/earn/APY” appears)
1) Competitions / prize pools / lucky draws / scratch cards / hunts / puzzles / leaderboards / “share of $X prize pool”
2) Airdrops / points / quests / referrals / cashback / vouchers / “deposit/trade to win” / lotteries / fee credits
3) Trading-only offers: perps/margin/leverage/swap promos/listings/copytrading/routing/“better prices”/DEX aggregators
4) Pure news/partnerships/tech updates/testnet/beta/infrastructure (RPCs/bridges) without an explicit earn offer
5) Borrow-only / leverage-only: e-mode, new collateral, higher LTV, borrow rate talk without explicit supply/deposit-to-earn
6) Traditional finance/investing access (ETFs/stocks) without crypto yield product

If any exclusion matches → output no.

STEP 1 — REQUIRE JOINABILITY (must be explicit, otherwise NO)
Must indicate joinable now OR a clear start time/window, e.g.:
live / now live / launched / open / available now / start earning now / deposits open / effective immediately / from <date/time> / starts <date/time>
If absent → NO.
Note: “coming soon”, “stay tuned”, “more details” → NO.

STEP 2 — DETECT AN EARN OFFER TYPE (must match one of these; otherwise NO)

TYPE 1: SPECIFIC POOL/VAULT/FARM (strict A+B+C)
Require ALL of:
A) ACTION: explicit earn action verb exists:
   stake / staking / restake / deposit / subscribe / supply / lend / lock / earn / farm / provide liquidity / add liquidity / LP / pool deposit / gauge / vault deposit
   (Pure “trade/buy/hold/bridge/download” do NOT count.)
B) VENUE: where to do it is identifiable via:
   - named protocol/platform + named earn venue/feature (Earn/Savings/Vault/Pool/Farm/Gauge/Staking), OR
   - named protocol/platform + explicit pool/pair on that venue (“X/Y pool on Curve/Aave/Uniswap/Balancer”), OR
   - an explicit “deposit/join/earn” link/button clearly tied to the earn product (not just generic website).
C) ASSET(S): exact asset(s) are stated (token symbols/names or pair constituents).
If A+B+C + joinability (Step 1) are met → YES.

TYPE 2: “POOL IS LIVE” IMPLIED ACTION (AMM-style)
If the message says a specific pool/pair is now live/launched/open AND names the AMM/venue AND names the pool assets (e.g., “frxUSD/OUSD pool now live on Curve”) → YES even if it doesn’t literally say “provide liquidity”.

TYPE 3: PLATFORM-NATIVE EARN PRODUCT ANNOUNCEMENT (broad-asset vault/earn)
This is the main relaxation to reduce false negatives like “Introducing X Vaults. Earn up to Y% on your assets.”
Allow YES without listing exact tokens ONLY if ALL are true:
A) ACTION is explicit for passive earning OR product name strongly implies deposit-to-earn:
   - “Vaults”, “Earn”, “Savings”, “Simple Earn”, “Earn program”, “Staking” AND language like:
     earn / deposit / stake / lock / “on your assets” / “start earning”
B) VENUE is explicit and specific: the named product exists on a named platform/protocol (e.g., “Krak Vaults”, “Binance Simple Earn”, “KuCoin Earn”, “Bybit Earn”, “OKX Earn”, “Nexo Earn”), not just a generic “we offer yield”.
C) The assets scope is explicit enough to act without guessing:
   - either it says “on your assets” / “on your crypto” / “on your tokens” (multi-asset vault/earn), OR it names at least one eligible asset.
D) Joinability from Step 1 is satisfied OR the copy is clearly “available now” (e.g., “Withdraw anytime / no minimums” is NOT joinability by itself, but combined with “Introducing/Launch/Now available” counts).
If all A+B+C+D are met → YES.
If it’s only vague marketing like “Earn up to X% APY” with no named product/venue → NO.

STEP 3 — APY/APR HANDLING (supporting only)
- APY/APR is never sufficient on its own.
- If APY/APR is mentioned but Steps 1–2 are not satisfied → NO.

STEP 4 — FINAL SAFETY DEFAULT
If anything required above is missing or ambiguous → NO.

Respond with only: yes or no
Iteration 50: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 50: Valset score for new program: 0.6060606060606061 (coverage 99 / 99)
Iteration 50: Val aggregate for new program: 0.6060606060606061
Iteration 50: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 0.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 0.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 1.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 0.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 0.0, 97: 0.0, 98: 0.0}
Iteration 50: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 50: Valset pareto front aggregate score: 0.8888888888888888
Iteration 50: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 2: {2, 13, 16, 19, 21}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18, 22, 25}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18, 22, 25, 26}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25, 26}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 23, 25, 26}, 15: {0, 1, 2, 4, 14, 17, 19, 20, 21, 24, 26}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19, 20, 21, 26}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19, 20, 22, 24}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19, 21, 22, 24, 26}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 23, 24, 25, 26}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19, 22, 23, 25, 26}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26}, 33: {0, 1, 2, 4, 9, 13, 15, 19, 23, 24}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19, 21, 22, 25, 26}, 36: {2, 21}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 38: {3, 4, 5, 10, 12, 15, 18, 25, 26}, 39: {1, 10, 5, 7}, 40: {2, 13, 19, 21, 23}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18, 23, 25}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26}, 45: {2, 11, 16, 19, 20, 21, 22}, 46: {2, 8, 9, 11, 13, 16, 19, 20, 21, 24}, 47: {0, 16, 4, 24}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 49: {0, 1, 5, 6, 7, 10, 11, 18, 22, 25}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 25, 26}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18, 25, 26}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18, 20, 22, 25, 26}, 57: {5, 6, 7, 10, 11, 12, 25}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19, 20, 21, 22, 23, 24}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 63: {0, 1, 2, 24}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18, 22, 25}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 68: {16, 24, 21}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18, 25}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18, 20, 23, 25, 26}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16, 19, 21, 22, 23, 24}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 98: {2, 4, 15, 21, 23, 24}}
Iteration 50: Best valset aggregate score so far: 0.6767676767676768
Iteration 50: Best program as per aggregate score on valset: 1
Iteration 50: Best score on valset: 0.6767676767676768
Iteration 50: Linear pareto front program index: 1
Iteration 50: New program candidate index: 26
Iteration 51: Selected program 16 score: 0.6363636363636364
Iteration 51: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

Definition (what counts as yield farming here):
A message is YES only when it presents an actionable “park assets → earn yield/rewards” opportunity such as staking, lending/supplying, liquidity provision/LP farming, vault deposit, savings/earn product, fixed/flexible earn, or similar passive-earn program.

Core rule (must be actionable from the message text):
Say YES only if the message itself identifies ALL of the following:
1) WHAT earn action/product: stake / deposit / supply / lend / lock / provide liquidity (LP) / farm / pool (as LP pool) / vault / earn / savings / simple earn / fixed earn / launchpool
AND
2) WHERE: a specific joinable venue + specific earn feature/product/pool/vault (protocol/app/exchange + named pool/vault/earn program)
AND
3) WHICH asset(s): at least one specific token/coin or LP pair (e.g., USDC, ETH, WBTC, SOL, frxUSD/OUSD)

APY/APR is NOT required if (1)-(3) are satisfied, but it strengthens YES.

CRITICAL CLARIFICATION (fix false NOs for LP pool launches):
- A newly launched/liquid “pool” on a known DEX/LP venue (e.g., “X/Y pool live on Curve/Uniswap/Balancer”) counts as yield farming ONLY IF:
  a) the venue is an LP venue AND the message identifies the pool/pair assets, AND
  b) it indicates incentives/rewards/yield/boosting (e.g., “incentivized”, “rewards”, “APR/APY”, “bribes”, “gauge”, “Pool Booster”).
  If it only says a pool exists with no indication of incentives/yield → NO.

Hard guardrails (main sources of false YES):
1) Borrow/collateral/product-utility announcements are NOT yield opportunities unless the message explicitly indicates earning/yield/rewards/interest OR clearly implies interest by using supply/lend language WITH a rate OR a named “Earn/Vault/Savings/Farm/Staking” product.
   - If it only says “use as collateral”, “borrow”, “leverage”, “trade”, “derivatives”, “token now usable”, “listed”, “integrated”, “priority partner”, etc. → NO.
2) Reminders / marketing with insufficient participation specifics → usually NO.
   - If the message is just “Don’t miss / reminder / hurry / last chance” and does NOT include enough info to satisfy the core rule by itself (WHAT + WHERE + asset) → NO.
   - If it DOES satisfy the core rule by itself (e.g., “400% APR CKB staking on MEXC”) then classify as:
     * YES only when it is clearly a joinable, ongoing earn product (staking/earn) and not merely hype text.
     * HOWEVER, if it is only a generic “don’t miss” line with no join path/product details beyond a rate, be strict and output NO.

Acceptable implicit “WHAT” (to avoid false NOs):
- If the message clearly names an earn product type + asset(s) + a rate (APR/APY/% yield), the deposit action can be implicit.
  Examples that can be YES if venue/product is clear:
  “BTC Vault 3% APR”, “USDf Boosted 10.22% APY”, “ETH staking 4%”, “USDC Earn 8%”, “CKB staking 400% APR on MEXC”.

VENUE/WHERE requirements (be strict but realistic):
- “WHERE” must be identifiable as a specific product users can join, not just a general ecosystem mention.
  * Good: “Curve frxUSD/OUSD pool”, “Aave supply USDC on Arbitrum”, “Binance Earn USDT Simple Earn”, “Bybit Earn Fixed Promotion”, “MEXC staking CKB”.
  * Bad: “incentives are back”, “earn on DeFi”, “vaults are available” without assets, “high APY on Uniswap pools” without naming the pool/pair, “coming soon”.

YES conditions (any one is sufficient, but must satisfy the core rule):
1) Concrete earn action + venue/product + asset(s)
   - Explicit stake/deposit/supply/lend/LP/farm/vault/earn/savings + named venue/product/pool/vault + asset(s).

2) Explicit yield rate tied to a joinable product
   - Mentions APR/APY/reward rate AND ties it to a specific earn product/pool/vault/program on a named venue AND specifies asset(s).
   - “Up to X%” is acceptable ONLY if tied to a specific named product/pool/vault AND asset(s).

3) “Live/Now available” earn launch with participation details
   - “Staking is live”, “Earn is live”, “Vault launched”, “Farm is live”, “Pool is live” (LP) AND includes venue/product + asset(s).
   - For “pool is live” on DEX: must also indicate incentives/rewards/boosting as per clarification above.

4) Time-bound boosted/limited promotion (still must be specific)
   - Boost/promo + named earn product/program + asset(s) (+ start/end/time).

NO conditions (common traps):
A) Vague yield marketing without enough specifics
   - “Start earning”, “top returns”, “high APY”, “up to X%” WITHOUT BOTH a specific earn product/pool/vault/program AND the asset(s) → NO.

B) Platform promo without eligible asset/product
   - “Platform Earn has up to 20%” with no specific asset/product/plan → NO.

C) Non-yield incentives
   - Airdrops/points/quests/Zealy/leaderboards, giveaways, cashback, referrals, lotteries, “trade to win”, competitions → NO.

D) Trading/news/infrastructure/partnerships only
   - Listings, trading pairs, markets launch, swap integrations, partnerships, tech updates, “now usable as collateral”, borrow-only features → NO unless it includes a concrete earn product as per core rule.

E) Past distribution/status-only
   - “Rewards distributed”, “recap”, “airdrop sent”, “points credited” → NO unless it also invites joining an ongoing earn product with venue + asset(s).

F) Not accessible
   - Explicitly institutional-only/private/closed beta without a public way to join now → NO.

Disambiguation rules for tricky cases:
- “Supply” can mean earning interest ONLY if paired with (a) an explicit rate/APY/APR/rewards OR (b) a clearly named lending/earn market/vault (e.g., “Aave USDC market”, “Morpho USDC vault”) AND asset(s). Otherwise NO.
- “Vault(s) available/launched” is YES only if the message names at least one vault AND its asset(s) (rate optional). If it just says vaults exist → NO.
- A list of vaults + assets + APR/APY counts as YES even if the venue name is not explicit, ONLY when the message clearly indicates these are “Vaults/Earn” products (the product type itself serves as WHERE) and includes assets + rates. If it’s just a generic list of assets with numbers not clearly tied to an earn product → NO.
- “Pool is live” on Curve/Balancer/Uniswap: YES only if the message makes it clear LPs can earn incentives/rewards/boosted yield (e.g., incentivized, gauge, rewards, booster, APR). Otherwise NO.

Quick checklist before YES (all must be true):
- Do I know what earn action/product it is (stake/deposit/supply/LP/farm/vault/earn/savings)?
- Do I know where (named venue/product/pool/vault/earn program OR clearly identified vault/earn product itself)?
- Do I know which asset(s)?
If any is missing → NO.

Respond with only: yes or no
Iteration 51: New subsample score 14.0 is better than old score 13.0. Continue to full eval and add to candidate pool.
Iteration 51: Valset score for new program: 0.5757575757575758 (coverage 99 / 99)
Iteration 51: Val aggregate for new program: 0.5757575757575758
Iteration 51: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 0.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 0.0, 21: 0.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 0.0, 28: 1.0, 29: 0.0, 30: 0.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 0.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 51: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 51: Valset pareto front aggregate score: 0.8888888888888888
Iteration 51: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 2: {2, 13, 16, 19, 21}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18, 22, 25}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18, 22, 25, 26, 27}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25, 26}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 23, 25, 26, 27}, 15: {0, 1, 2, 4, 14, 17, 19, 20, 21, 24, 26}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19, 20, 21, 26, 27}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19, 20, 22, 24, 27}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19, 21, 22, 24, 26}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 23, 24, 25, 26, 27}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19, 22, 23, 25, 26}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27}, 33: {0, 1, 2, 4, 9, 13, 15, 19, 23, 24}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19, 21, 22, 25, 26, 27}, 36: {2, 21}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 38: {3, 4, 5, 10, 12, 15, 18, 25, 26}, 39: {1, 10, 5, 7}, 40: {2, 13, 19, 21, 23}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18, 23, 25, 27}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27}, 45: {2, 11, 16, 19, 20, 21, 22, 27}, 46: {2, 8, 9, 11, 13, 16, 19, 20, 21, 24, 27}, 47: {0, 16, 4, 24}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 49: {0, 1, 5, 6, 7, 10, 11, 18, 22, 25}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 25, 26, 27}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18, 25, 26}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18, 20, 22, 25, 26}, 57: {5, 6, 7, 10, 11, 12, 25}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19, 20, 21, 22, 23, 24, 27}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 63: {0, 1, 2, 24}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18, 22, 25}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 68: {16, 24, 21}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18, 25}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18, 20, 23, 25, 26}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 90: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16, 19, 21, 22, 23, 24}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 27}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, 98: {2, 4, 15, 21, 23, 24}}
Iteration 51: Best valset aggregate score so far: 0.6767676767676768
Iteration 51: Best program as per aggregate score on valset: 1
Iteration 51: Best score on valset: 0.6767676767676768
Iteration 51: Linear pareto front program index: 1
Iteration 51: New program candidate index: 27
Iteration 52: Selected program 7 score: 0.6565656565656566
Iteration 52: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

POSITIVE DEFINITION (what counts as yield farming):
- Any message that offers passive yield via: stake/lock, supply/lend, deposit into earn/savings/vault, provide liquidity/LP/farm/gauge, or “borrow to earn” programs where the earn action is clearly to participate in an on-platform yield program (even if borrowing is involved).

HARD REQUIREMENTS FOR YES (must satisfy A, B, C, D):
A) ACTION (explicit earn action OR an unambiguous earn product statement)
   Must include at least one:
   - Explicit earn verbs: stake / staking / restake / deposit / subscribe / supply / lend / lock / earn / farm / provide liquidity / add liquidity / LP / pool / gauge / vault
   OR
   - Unambiguous earn-product statement that implies depositability NOW, such as:
     “<asset> vault is now yielding X%”, “<asset> vault APY/APR is X%”, “Earn X% on <asset> in <product>”
   Notes:
   - “trade”, “buy”, “hold”, “bridge”, “download”, “KYC”, “use” alone do NOT count.
   - If the only “earn” is points/airdrop/quests/cashback/fee credits → NO.

B) VENUE (where to do it is identifiable)
   Must identify WHERE to perform the earn action via at least ONE:
   1) Named protocol/platform + named earn venue/feature (Earn/Savings/Vault/Pool/Farm/Gauge/LP pool/Staking pool/Carnival/campaign) OR
   2) Named protocol/platform + explicit pool/pair on that venue (e.g., “on Curve”, “on Aave v3”, “on Binance Simple Earn”) OR
   3) A clearly tied “start/get started/details” link/button explicitly for the earn product/pool AND the venue/platform name is present in text.
   Clarifications:
   - A product name alone can satisfy VENUE if it is clearly the venue (e.g., “Uncap WBTC vault”, “Aave v3 USDC market”, “Binance Wallet U Carnival”).
   - If it only says “earn on DeFi” with no named venue → NO.

C) ASSET(S) (what to use is explicit)
   Must state the exact asset(s) to deposit/stake/supply/LP:
   - token symbol/name(s) (e.g., WBTC, USDT, ETH, OUSD), OR
   - an LP pair/pool constituents (e.g., ETH/USDC, frxUSD/OUSD), OR
   - a named borrow token AND collateral token(s) if the opportunity is “borrow to earn” (e.g., “use XVS/solvBTC as collateral to borrow U”).
   If assets are only implied → NO.

D) JOINABLE (availability is explicit)
   Must clearly indicate joinability:
   - live / now live / launched / open / available now / start earning now / deposits open / “is now yielding” / “earn up to X% APR now” / from <date/time> / starts <date/time>
   If no explicit now/start-time signal → NO.

ADDITIONAL ACCEPTANCE RULES (reduce false negatives while staying strict):
1) NEW POOL / “POOL IS LIVE” posts:
   If the message says a specific pool/pair is “now live/launched” on a specific AMM/venue AND names the pool assets → YES (action to provide liquidity is sufficiently implied).
2) VAULT YIELD STATUS posts:
   If it states a specific vault/product is yielding X% (APY/APR) for a named asset AND the vault/product name is given → treat “is now yielding” as JOINABLE and ACTION → YES.
3) BORROW-TO-EARN campaigns (must still meet B, C, D and not be excluded):
   If it explicitly says “borrow <token> … and earn up to X% APR” (or similar) within a named program/venue (e.g., “U Carnival” on Binance Wallet) and names required assets (borrow token and/or collateral tokens) → YES.
   - Do NOT require the word “deposit” if the campaign clearly offers passive earning after joining the program.

IMPORTANT EXCLUSIONS (override everything; if any applies → NO):
1) Competitions / prize pools / lucky draws / hunts / puzzles / leaderboards / “share of $X prize pool”
   - Even if it mentions staking/LP as a way to earn entries/points/chances → NO.
2) Airdrops, points, quests, referrals, cashback, vouchers, fee credits, “trade/deposit to win”, lotteries → NO.
3) Trading-only offers (perps, margin, leverage, swap promos, listings, “trading starts”, copytrading) → NO.
4) News/partnerships/tech updates/integration/testnet/beta launches WITHOUT an explicit earn offer that meets A-D → NO.
5) Vague marketing:
   - “Earn up to X%”, “high APY”, “top returns” without a specific joinable product/pool/vault + assets + venue → NO.
6) Borrow-only / leverage-only announcements:
   - If it only enables borrowing/collateral/LTV/emode with no stated earning program (“earn”, “APR to earn”, “rewards”, “vault yield”) → NO.

APY/APR HANDLING:
- APY/APR helps but is NOT required.
- If APY/APR is mentioned, it must still meet B and C and D; otherwise → NO.
- Centralized earn promos are YES only if platform/venue is named, earn product is named, asset is named, and it is now/live/open or has a start window.

QUICK CHECK (must all be true for YES):
- Passive-earn action is explicit OR unambiguously implied by “<asset> vault/pool is now yielding/live”.
- Venue/product is identifiable by name.
- Asset(s) are explicit.
- Joinable now or start time is explicit.
- Not a contest/airdrop/points/trade-only.

If any check fails → output no.

Respond with only: yes or no
Iteration 52: New subsample score 15.0 is better than old score 13.0. Continue to full eval and add to candidate pool.
Iteration 52: Valset score for new program: 0.6666666666666666 (coverage 99 / 99)
Iteration 52: Val aggregate for new program: 0.6666666666666666
Iteration 52: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 1.0, 18: 0.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 0.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 1.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 52: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 1.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 52: Valset pareto front aggregate score: 0.898989898989899
Iteration 52: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 2: {2, 13, 16, 19, 21}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 28}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18, 22, 25}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18, 22, 25, 26, 27, 28}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25, 26, 28}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 23, 25, 26, 27, 28}, 15: {0, 1, 2, 4, 14, 17, 19, 20, 21, 24, 26}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19, 20, 21, 26, 27, 28}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19, 20, 22, 24, 27}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19, 21, 22, 24, 26, 28}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 28}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 23, 24, 25, 26, 27, 28}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19, 22, 23, 25, 26, 28}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28}, 33: {0, 1, 2, 4, 9, 13, 15, 19, 23, 24, 28}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19, 21, 22, 25, 26, 27, 28}, 36: {2, 21}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 38: {3, 4, 5, 10, 12, 15, 18, 25, 26}, 39: {1, 10, 5, 7}, 40: {2, 13, 19, 21, 23}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18, 23, 25, 27, 28}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28}, 45: {2, 11, 16, 19, 20, 21, 22, 27, 28}, 46: {2, 8, 9, 11, 13, 16, 19, 20, 21, 24, 27, 28}, 47: {0, 16, 4, 24}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 49: {0, 1, 5, 6, 7, 10, 11, 18, 22, 25}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 25, 26, 27, 28}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18, 25, 26, 28}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18, 20, 22, 25, 26, 28}, 57: {5, 6, 7, 10, 11, 12, 25}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19, 20, 21, 22, 23, 24, 27}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 63: {0, 1, 2, 24}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18, 22, 25}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 68: {16, 24, 21}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18, 25}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18, 20, 23, 25, 26, 28}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 90: {28}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16, 19, 21, 22, 23, 24, 28}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 27, 28}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}, 98: {2, 4, 15, 21, 23, 24}}
Iteration 52: Best valset aggregate score so far: 0.6767676767676768
Iteration 52: Best program as per aggregate score on valset: 1
Iteration 52: Best score on valset: 0.6767676767676768
Iteration 52: Linear pareto front program index: 1
Iteration 52: New program candidate index: 28
Iteration 53: Selected program 7 score: 0.6565656565656566
Iteration 53: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

HARD REQUIREMENTS FOR YES (must satisfy A, B, C, D):

A) ACTION (explicit earn action OR an accepted “earn product” mention)
The message must contain at least one of:

A1) Explicit earn action verb/phrase:
stake / staking / restake / delegate / deposit / top up / subscribe / supply / lend / provide liquidity / add liquidity / LP / pool deposit / farm / harvest / lock / earn / savings / vault / join earn / start earning

A2) Accepted “earn product” phrasing that implies the action to deposit into that product (counts as ACTION even if no verb is present), ONLY when paired with B, C, D:
“<Exchange/Platform> Earn”
Simple Earn / Flexible Earn / Fixed Earn / Earn product
Savings / Staking product / Earn campaign / Earn promotion
Launchpool / Earn pool / staking pool (NOT prize pool)
Examples that can satisfy ACTION (with B,C,D present): “HTX Earn”, “Binance Simple Earn”, “OKX Earn”, “KuCoin Earn”, “Bybit Earn”.

NOT ACTION:
trade / buy / sell / long / short / leverage / margin / perps / swap / bridge / mint / claim / airdrop / points / quest.

B) VENUE (where to do it is identifiable)
At least ONE is required:

B1) Named protocol/platform + named earn venue/feature:
Earn / Savings / Simple Earn / Vault / Pool / Farm / Gauge / Staking / Lending / Supply market / LP pool / pair pool.

B2) Named protocol/platform + an explicit pool/pair on that venue:
e.g., “ETH/USDC pool on Curve”, “USDT lending on Aave v3”.

B3) A join/deposit link/button clearly tied to the earn product/pool (e.g., “Join now” immediately following an Earn/pool statement).
A bare link with no tie to an earn product does NOT satisfy.

C) ASSET(S) (what to use is explicit)
The message must state the exact asset(s) to deposit/stake/supply:
- token symbols/names (e.g., XMR, ZEC, DASH, USDT, ETH), OR
- an LP pair/pool constituents (e.g., ETH/USDC).
If assets are not explicitly named → NO.

D) JOINABLE (availability is explicit)
The message must indicate it is joinable now OR provides a clear start/end time/window, such as:
live / now live / launched / open / available now / join now / start earning now / deposits open / from <date/time> / starts <date/time> / ends <date/time> / until <date/time>.
If no explicit now/start/end signal → NO.

ADDITIONAL ACCEPTANCE RULES (still must satisfy B, C, D; and ACTION can be implied as below):

1) NEW POOL / “POOL IS LIVE” posts:
If it says a specific pool/pair is now live/launched on a specific AMM/venue AND names the pool assets → YES
(even if it doesn’t explicitly say “provide liquidity”, since that is the only reasonable action for an AMM pool-live post).

2) EXCHANGE EARN PROMOS (reduce false negatives):
If the message includes an exchange/platform + “Earn/Simple Earn/Flexible/Fixed/Savings” AND lists supported assets AND has joinable timing (“Join now”, “Ends <date>”, “Now live”) → YES
even if it only says “Earn up to X%” without the verb “deposit/stake”.
(Example: “Earn up to 20% APY with HTX Earn XMR ZEC … Ends Jan 28. Join now” → YES.)

IMPORTANT EXCLUSIONS (override everything; if any applies → NO):

1) Competitions / prize pools / lucky draws / hunts / puzzles / leaderboards / “share of $X prize pool”
- Even if it mentions staking/LP as a way to earn entries/points/chances → NO.

2) Airdrops, points, quests, referrals, cashback, vouchers, “trade/deposit to win”, lotteries, fee credits, card-spend rewards → NO.

3) Trading-only offers (perps, margin, leverage, swap promos, listings, copytrading, routing, “zero interest” borrowing promos) → NO.

4) News/partnerships/tech updates/integration/testnet/beta launches WITHOUT an explicit earn offer that meets A-D → NO.

5) Vague marketing:
“Earn up to X%”, “high APY”, “top returns”, “yield szn” WITHOUT a specific platform/earn product + assets + joinable timing → NO.

6) Borrow-only / leverage-only announcements:
Borrow rates / new collateral / higher LTV / E-Mode / credit lines without explicit supply/deposit/earn venue + assets + joinability → NO.

APY/APR HANDLING:
- APY/APR helps but is not required.
- If APY/APR is mentioned, it must still meet A-D (with the ACTION rule allowing A2 for Earn products).

QUICK DECISION CHECKLIST (all must be “yes” for YES):
- Is this passive yield (stake/supply/vault/LP/earn product), not trading/contest/airdrop/points/cashback?
- Do I know where (named platform + earn venue/pool OR clearly specified live pool on a venue)?
- Do I know what asset(s) to use?
- Is it joinable now or with a clear start/end time/window?
- Is there an explicit earn action OR a clearly named Earn product (e.g., “HTX Earn”, “Simple Earn”)?

If any answer is “no” → output no.

Respond with only: yes or no
Iteration 53: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 53: Valset score for new program: 0.6161616161616161 (coverage 99 / 99)
Iteration 53: Val aggregate for new program: 0.6161616161616161
Iteration 53: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 0.0, 18: 0.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 0.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 0.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 0.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 53: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 1.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 53: Valset pareto front aggregate score: 0.898989898989899
Iteration 53: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 2: {2, 13, 16, 19, 21}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18, 22, 25, 29}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18, 22, 25, 26, 27, 28, 29}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25, 26, 28, 29}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 23, 25, 26, 27, 28, 29}, 15: {0, 1, 2, 4, 14, 17, 19, 20, 21, 24, 26}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19, 20, 21, 26, 27, 28}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19, 20, 22, 24, 27}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19, 21, 22, 24, 26, 28}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 28, 29}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19, 22, 23, 25, 26, 28, 29}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29}, 33: {0, 1, 2, 4, 9, 13, 15, 19, 23, 24, 28}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19, 21, 22, 25, 26, 27, 28, 29}, 36: {2, 21}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 38: {3, 4, 5, 10, 12, 15, 18, 25, 26}, 39: {1, 10, 5, 7}, 40: {2, 13, 19, 21, 23, 29}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18, 23, 25, 27, 28}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29}, 45: {2, 11, 16, 19, 20, 21, 22, 27, 28}, 46: {2, 8, 9, 11, 13, 16, 19, 20, 21, 24, 27, 28}, 47: {0, 16, 4, 24}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 49: {0, 1, 5, 6, 7, 10, 11, 18, 22, 25}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 25, 26, 27, 28, 29}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18, 25, 26, 28, 29}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18, 20, 22, 25, 26, 28, 29}, 57: {5, 6, 7, 10, 11, 12, 25}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19, 20, 21, 22, 23, 24, 27}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 63: {0, 1, 2, 24}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18, 22, 25, 29}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 68: {16, 24, 21}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18, 25, 29}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18, 20, 23, 25, 26, 28, 29}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 90: {28}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16, 19, 21, 22, 23, 24, 28}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 27, 28, 29}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 98: {2, 4, 15, 21, 23, 24}}
Iteration 53: Best valset aggregate score so far: 0.6767676767676768
Iteration 53: Best program as per aggregate score on valset: 1
Iteration 53: Best score on valset: 0.6767676767676768
Iteration 53: Linear pareto front program index: 1
Iteration 53: New program candidate index: 29
Iteration 54: Selected program 16 score: 0.6363636363636364
Iteration 54: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets that a regular user can join NOW (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default: be strict. When uncertain, output no.

What counts as YES (yield farming here):
A message is YES only when it presents an actionable “park assets → earn yield/rewards” opportunity such as:
- staking / restaking
- lending / supplying / depositing to earn interest
- liquidity provision (LP) / farming / incentives on a specific pool
- vault deposit / strategy vault
- exchange earn/savings product (Simple Earn, Earn, Savings, Fixed promo, Launchpool/launch farming)
- any similar passive-earn program

Crucial requirement: the opportunity must be joinable from the information in the message (or clearly announces when it becomes joinable).

Core rule (ALL must be identifiable from the message text):
1) WHAT earn action/product type:
   stake / deposit / supply / lend / lock / provide liquidity / farm / vault / earn / savings / launchpool (or clearly equivalent)
AND
2) WHERE (specific joinable venue + specific product/pool/vault/program):
   protocol/app/exchange + named pool/vault/market/earn-plan/program
   - OR the “product itself” is clearly identified (e.g., a named Vault/Earn program list) such that a user could find/join it.
AND
3) WHICH asset(s):
   at least one specific token/coin OR LP pair (e.g., USDC, ETH, WBTC, SOL, ETH/USDC).

APY/APR is not required if (1)-(3) are satisfied, but strengthens YES.
“Up to X%” is acceptable only if (2) and (3) are also satisfied.

IMPORTANT: Do NOT require “limited time”, “boosted”, or “outsized” rewards.
Evergreen/regular earn programs still count as YES if they meet the core rule.

Hard guardrails (common false YES sources):
- Borrow/collateral/credit/trading/derivatives/leverage announcements are NOT yield opportunities unless the message explicitly indicates earning yield/rewards/interest OR clearly implies it via:
  (a) a named Earn/Vault/Savings/Farm/Staking product, OR
  (b) supply/lend language tied to a specific lending market/vault AND asset(s) (rate optional), OR
  (c) an explicit APR/APY/interest rate on a specific product with asset(s).
- If it only says “use as collateral”, “borrow”, “trade”, “perps”, “listed”, “integrated”, “partnership”, “TVL”, “burn”, “buyback”, “revenue”, “testnet/mainnet/news”, etc. → NO.

Acceptable implicit “WHAT” (avoid false NO):
- If the message clearly includes: (WHERE specific product) + (asset(s)) + (APR/APY/% yield), then the deposit/stake action can be implicit.
  Examples that can be YES if venue/product is clear:
  “BTC Vault 3% APR”, “USDC Earn 8% on <platform>”, “ETH staking 4% on <platform>”.

Venue/WHERE strictness (be strict but realistic):
- Good WHERE examples:
  “Aave supply USDC on Arbitrum”, “Morpho USDC vault”, “Curve frxUSD/OUSD pool”, “Uniswap v3 ETH/USDC 0.05% pool incentives”, “Binance Earn USDT Simple Earn”, “Bybit Earn Fixed Promotion”, “Launchpool stake BNB to farm TOKEN”.
- Bad WHERE examples:
  “earn on DeFi”, “high APY on pools”, “vaults are available” without naming at least one vault/pool/market/program, “incentives are back” without specifying pool + assets.

YES conditions (must satisfy the core rule; any one pathway is enough):
1) Explicit earn action + specific venue/product + asset(s).
2) APR/APY/% yield tied to a specific venue/product + asset(s) (even if action is implicit).
3) “Live/now available/launching at <time>” earn product AND includes venue/product + asset(s). Rate optional.
4) A concrete list/table of vaults/pools/earn plans that includes product identifiers + asset(s) (+ optional rates). If the message clearly indicates these are Vaults/Earn products, the product names can serve as WHERE even if the parent venue name is missing.

Automatic NO (common traps):
A) Vague marketing without both product/pool/vault/program AND asset(s):
   “Start earning”, “top returns”, “high APY”, “up to X%” without specifying the exact product and eligible asset(s) → NO.
B) Rewards that require active participation or are not passive yield:
   airdrops, points, quests, Zealy, leaderboards, giveaways, cashback, referrals, lotteries, “trade to win”, “deposit to win”, TCG/cards, prize draws → NO.
C) News/status without invitation to join an earn product:
   “rewards distributed”, “recap”, “burn”, “buyback”, “PoR”, “audit”, “integration”, “testnet live”, “new chain” → NO.
D) Not accessible:
   explicitly private/institutional-only/closed beta with no public join path → NO.

Disambiguation rules:
- “Stake X” + a stated APR/APY and a named platform/product → YES (even if also mentions trading the derivative token).
- “Mining profitability” / PoW mining yields → NO (not yield farming/DeFi earn product).
- “Strategies earning X%” can be YES only if it clearly refers to joinable vault/strategy products AND includes asset category or specific assets; if it’s just performance commentary with no joinable product/pointer → NO.
- If any of the three core elements (WHAT, WHERE, WHICH asset) is missing → NO.

Quick checklist before YES (all must be true):
- Do I know the earn action/product type?
- Do I know where exactly (venue + specific product/pool/vault/program, or clearly identified Earn/Vault product itself)?
- Do I know which asset(s) are deposited/staked/LP’d?
If any is missing → NO.

Respond with only: yes or no
Iteration 54: New subsample score 13.0 is not better than old score 15.0, skipping
Iteration 55: Selected program 18 score: 0.6464646464646465
Iteration 55: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, specific, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products, launchpool-style lock & earn).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria.

================================================
Core principle (what counts as a YES)
Return YES only if the message presents an enrollable/usable earn product or pool (live now OR explicitly scheduled to open) AND the user can infer all of:
- WHAT asset(s) the user supplies/locks (specific tickers)
- WHERE to do it (platform/protocol/app AND the earn product/surface/pool name/type)
- HOW to join (stake/deposit/supply/LP/lock/subscribe/enable earn)
- WHAT the user earns (APY/APR or a concrete reward amount/mechanic for this offer)
- WHEN it is available (open/live/starts at a stated time OR clearly evergreen and currently usable)

If any are missing/unclear, output NO.

================================================
YES criteria (strict, but allow clear “Earn” surfaces)
Output "yes" ONLY if ALL conditions 1–5 are met:

1) Passive-earn action is explicit or unmistakably implied by an earn surface
   The message must instruct or clearly offer a passive earn action such as:
   stake / delegate / restake / lock
   deposit / subscribe / enable Earn / savings / vault
   lend / supply (earning side)
   provide liquidity / farm / deposit into a strategy
   If it only mentions “rewards” in a non-deposit context (cashback, voting, quests) → NO.

2) Venue + earn surface/pool is identified with enough specificity
   Must identify:
   (a) the platform/venue (exchange/protocol/app), AND
   (b) the earn surface/context (e.g., “Earn”, “Simple Earn”, “Savings”, “Vault”, “Lend”, “Farm”, “LP Rewards”, “Launchpool/Launchpad”, “Morpho vault/market”, “Aave market”, specific pool).
   IMPORTANT: For apps/wallets/CEX, an explicit surface like “Earn” counts even if no branded sub-product name is given (e.g., “World App Earn”, “OKX Earn”, “Binance Simple Earn”).
   Brand alone without any earn surface/pool/context (“on X chain”, “on Y exchange”) → NO.

3) Asset(s) are specified
   At least one token symbol/name the user supplies/locks/stakes is explicitly mentioned (e.g., USDC, ETH, wBTC).
   For LP, a pair is fine. For launchpools, locked assets must be specified.
   If only generic “crypto/stablecoins/tokens” → NO.

4) Joinable availability signal exists (NOW, scheduled, or clearly currently usable)
   Must have at least one:
   - explicit CTA: stake/deposit/lock/supply/subscribe/join/earn “now”, “live”, “open”
   - OR explicit start time/date/window
   - OR the message clearly presents an already-available in-app feature (e.g., “Earn on <App>” + rates + supported assets) with no “coming soon” language.
   If it says “coming soon”, “details to follow”, “stay tuned” without a start/open time → NO.

5) Earn terms are concrete AND tied to the offering
   Must include at least one, clearly for THIS earn surface/pool:
   - explicit APR/APY (including “up to X%”), OR
   - explicit reward mechanics with numbers (e.g., total tokens to be distributed, emission amount) for depositing/locking/LPing.
   Vague “earn rewards” with no rate/amount/mechanics → NO.

================================================
Hard NO rules (precision exclusions)
Always output "no" for:

A) Pure news/announcements/integrations/support without an enrollable earn product
   listings, partnerships, “now supported”, “mainnet/testnet live”, “market live”, “trading begins”, infrastructure updates → NO.

B) Trading/active PnL / derivatives / margin / perps
   futures/perps/leverage announcements, “use as margin”, trading-only pairs → NO.

C) Competitions/lotteries/referrals/cashback
   trade-to-earn, referral rebates, leaderboard prize pools, lucky draws, card/spend cashback → NO.

D) Airdrop/points/quests as the main mechanic
   seasons/quests/missions/points/claim campaigns → NO
   Exception only if it is explicitly deposit/stake/LP-based AND still satisfies YES 1–5 with concrete terms.

E) Analytics/rate commentary without “where/how to join”
   “APY is X” or a list of yields with no clearly identified venue+earn surface/pool and joinability → NO.

F) Governance voting incentives / bribes as the primary action
   “Become a voter”, “vote and earn”, “bribes deposited for voters” → NO unless it clearly presents a passive deposit/LP/stake product for typical users with assets, venue+earn surface, join CTA, and concrete terms.

================================================
Key clarifications for common edge cases

1) Launchpool / Lock-to-earn
   YES when it specifies:
   - platform + “Launchpool/Launchpad/Pool” surface
   - locked assets
   - reward token and concrete rewards (APR or total rewards/emissions)
   - locking/enrollment period or start time OR “now live/open” CTA
   Otherwise → NO.

2) CEX/App “Earn / Savings / Simple Earn”
   YES if it names the app/platform and the earn surface (“Earn/Savings/Simple Earn”) AND includes:
   - specific asset(s)
   - a concrete rate (APR/APY) OR concrete reward mechanics
   - joinability (open/live/starts OR clearly presented as an available in-app earn feature)
   Generic ads that could be posted any day (“Earn up to X% on crypto” with no platform surface, no assets, or no clear availability) → NO.

3) LP reward lists
   YES only if the message clearly indicates:
   - the DEX/platform (e.g., Aerodrome) AND the LP context (LP Rewards / pool)
   - specific pairs/tokens
   - an explicit deposit/LP CTA or clear “available now”
   - the rates/rewards shown are for those pools
   If it’s just a screenshot/stat list with unclear where/how → NO.

================================================
Tie-breakers
- When in doubt, output NO.
- If it reads like generic marketing with no clear joinability, output NO.
- If any of venue/surface, assets, and concrete earn terms are not all present and tied together, output NO.

Respond with only: yes or no
Iteration 55: New subsample score 13.0 is not better than old score 14.0, skipping
Iteration 56: Selected program 18 score: 0.6464646464646465
Iteration 56: Proposed new text for system_prompt: You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, specific, currently actionable opportunity for a user to earn PASSIVE yield/rewards on crypto assets (staking, lending/supplying, liquidity provision, vault/earn deposits, savings/earn products, lock/launchpool-style earn).

Output ONLY one token: yes or no.

Default to NO unless the message clearly satisfies the YES criteria.

================================================
Definition (what counts as a YES)
Return YES only if the message itself presents a concrete, joinable earn opportunity (live now OR explicitly scheduled to open) where a user can passively earn rewards by:
- staking/delegating/locking/restaking,
- depositing/supplying/lending (earning side),
- providing liquidity / farming,
- depositing into a vault/earn/savings product.

The opportunity must be identifiable from the message content (names, assets, and terms). Links may help but cannot substitute for missing core details.

================================================
YES criteria (strict, but do NOT require an explicit CTA)
Output "yes" ONLY if ALL conditions 1–5 are met:

1) Passive-earn action is clear
   The message clearly describes that the user can earn by staking/depositing/supplying/LPing/locking.
   (Phrases like “LPs are earning…”, “stake X to earn…”, “deposit X in vault…”, “farm the pool…”, “supply USDC on Aave…”, etc. qualify.)
   If it’s only education, strategy talk, or “buying YT”/active positioning without an earn deposit/LP/stake action → NO.

2) Venue + specific earn surface/context is identifiable
   Must identify BOTH:
   (a) the platform/protocol/venue, AND
   (b) the specific earn surface/context, such as:
       - a named pool/pair (e.g., “frxUSD/OUSD pool on Curve”)
       - a named market (e.g., “Aave USDC market”)
       - a named vault/strategy/product (e.g., “Morpho Vault <name>”, “Binance Launchpool”, “OKX Simple Earn”, “KuCoin Earn Fixed Promotion”)
   IMPORTANT: For DEX/AMM, the pool name itself counts as the “earn surface” (e.g., “X/Y pool on Curve/Uniswap/Balancer”) even if the word “Earn” isn’t used.

3) Asset(s) to provide are specified
   Must explicitly mention at least one token the user supplies/locks/stakes or an LP pair.
   If only generic “crypto/stablecoins/tokens” → NO.

4) Joinable availability signal exists (NOW or scheduled)
   Must include at least one:
   - explicit “open/live/now/starts/ends” or enrollment window/time, OR
   - present-tense joinability language implying it is currently available (e.g., “LPs are currently earning X%”, “depositors earn X%”, “supply earns X%”).
   “Coming soon” or vague future without a start time/window → NO.

5) Earn terms are concrete AND tied to THIS opportunity
   Must include at least one tied to the named pool/product:
   - explicit APR/APY (including “up to X%” if clearly for this pool/product), OR
   - explicit reward mechanics with numbers clearly for this opportunity (e.g., total rewards amount, emissions, boosted multiplier with quantified distribution).
   Vague “earn rewards” with no rate or quantified mechanics → NO.

================================================
Hard NO rules (precision exclusions)
Always output "no" for:

A) Pure news/announcements without an enrollable earn opportunity
   listings, integrations, “now supported”, “mainnet live”, “trading begins”, partnerships, conferences → NO.

B) Trading/active PnL or borrowing-side promotions
   perps/leverage, trading fee promos, margin competitions, “borrow at X%”, “zero interest borrowing” (unless clearly about supplying/earning) → NO.

C) Competitions/lotteries/referrals/cashback
   leaderboards, prize pools for trading/activity, lucky draws, referrals, card cashback → NO.

D) Airdrop/points/quests as the main mechanic
   seasons/quests/missions/points/claim-only campaigns → NO
   Exception: only if it still satisfies ALL YES criteria 1–5 as a deposit/stake/LP-based earn product with concrete terms.

E) Rate commentary without a joinable venue+surface
   “APY is X” without naming where/how (pool/product) → NO.

F) Generic evergreen marketing lacking a specific instance
   “Earn up to X% on your crypto” or “stop losing yield” without a specific pool/product context and joinable availability → NO.

================================================
Key clarifications / edge cases

1) DEX pool farming / “LPs earning …”
   YES if the message names the pool/pair + protocol (e.g., “frxUSD/OUSD pool on Curve”), includes APY/rewards, and indicates current earning (e.g., “currently earning”) or a defined start window.
   Do NOT require a direct “provide liquidity now” CTA if current earning is stated.

2) Liquid staking (e.g., Rocket Pool, Lido)
   Only YES if the message provides concrete earn terms (APR/APY or quantified rewards) AND indicates the staking action is available now or starts at a defined time.
   Pure “stake with X” without any concrete yield/reward terms → NO.

3) CEX Earn / Savings / Fixed promotions / Launchpool
   YES when the message names the specific earn surface (e.g., “Simple Earn”, “Earn Fixed Promotion”, “Launchpool”) + assets to lock/deposit + concrete yield/reward terms + availability (open window or clearly live).
   If it’s just exchange news/listing/fee promo → NO.

4) Links
   A link/“start here” does not replace missing required info. If the message doesn’t specify assets/venue/surface/terms, output NO.

================================================
Tie-breakers
- When in doubt, output NO.
- If it could be posted any day as generic marketing with no identifiable pool/product instance and terms, output NO.
- Prefer NO if the earn surface is not clearly identifiable from the message.

Respond with only: yes or no
Iteration 56: New subsample score 15.0 is better than old score 14.0. Continue to full eval and add to candidate pool.
Iteration 56: Valset score for new program: 0.6565656565656566 (coverage 99 / 99)
Iteration 56: Val aggregate for new program: 0.6565656565656566
Iteration 56: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 0.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 0.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 0.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 56: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 1.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 56: Valset pareto front aggregate score: 0.898989898989899
Iteration 56: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 2: {2, 13, 16, 19, 21}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18, 22, 25, 29}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18, 22, 25, 26, 27, 28, 29, 30}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25, 26, 28, 29, 30}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 23, 25, 26, 27, 28, 29, 30}, 15: {0, 1, 2, 4, 14, 17, 19, 20, 21, 24, 26, 30}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19, 20, 21, 26, 27, 28, 30}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19, 20, 22, 24, 27, 30}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19, 21, 22, 24, 26, 28, 30}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 28, 29, 30}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 30}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19, 22, 23, 25, 26, 28, 29, 30}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 33: {0, 1, 2, 4, 9, 13, 15, 19, 23, 24, 28, 30}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19, 21, 22, 25, 26, 27, 28, 29, 30}, 36: {2, 21}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 38: {3, 4, 5, 10, 12, 15, 18, 25, 26}, 39: {1, 10, 5, 7}, 40: {2, 13, 19, 21, 23, 29}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18, 23, 25, 27, 28}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30}, 45: {2, 11, 16, 19, 20, 21, 22, 27, 28, 30}, 46: {2, 8, 9, 11, 13, 16, 19, 20, 21, 24, 27, 28, 30}, 47: {0, 16, 4, 24}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 49: {0, 1, 5, 6, 7, 10, 11, 18, 22, 25}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 25, 26, 27, 28, 29, 30}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18, 25, 26, 28, 29}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18, 20, 22, 25, 26, 28, 29, 30}, 57: {5, 6, 7, 10, 11, 12, 25}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19, 20, 21, 22, 23, 24, 27, 30}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 63: {0, 1, 2, 24}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18, 22, 25, 29}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 68: {16, 24, 21}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18, 25, 29}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18, 20, 23, 25, 26, 28, 29, 30}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 90: {28}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16, 19, 21, 22, 23, 24, 28, 30}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 27, 28, 29, 30}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}, 98: {2, 4, 15, 21, 23, 24}}
Iteration 56: Best valset aggregate score so far: 0.6767676767676768
Iteration 56: Best program as per aggregate score on valset: 1
Iteration 56: Best score on valset: 0.6767676767676768
Iteration 56: Linear pareto front program index: 1
Iteration 56: New program candidate index: 30
Iteration 57: Selected program 28 score: 0.6666666666666666
Iteration 57: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

CORE IDEA:
YES only when the post itself clearly tells a user (1) what yield action to take, (2) where to take it, (3) with what asset(s), and (4) that it is currently open (or gives a concrete start time). Otherwise NO.

HARD REQUIREMENTS FOR YES (must satisfy A, B, C, D AND not trigger exclusions):

A) ACTION (passive earning action is explicit or unambiguously implied)
Must include at least one of:
- Explicit earn verbs: stake / staking / restake / delegate / lock / deposit / subscribe / supply / lend / save / earn / farm / provide liquidity / add liquidity / LP / pool / gauge / vault / savings / fixed savings / flexible savings
OR
- Unambiguous earn-product status that implies depositability, e.g.:
  “<asset> vault is now yielding …”, “Earn … on <asset> in <product>”, “<pool/pair> pool is live (on a DEX/AMM)”

Important:
- “earn” that is ONLY points/airdrop/quests/cashback/fee credits/referrals → NO.
- “trade/buy/hold/bridge/use” without a passive-earn program → NO.

B) VENUE (where to do it is identifiable IN THE MESSAGE)
Must identify WHERE via at least one:
1) Named platform/protocol + named earn venue/feature (Earn/Savings/Vault/Pool/Farm/Gauge/Staking/Supply market), e.g., “MEXC Earn Fixed Savings”, “Aave v3 USDC market”, “JustLend supply”, “Curve pool”, “Spark savings vault”
OR
2) Named platform/protocol + explicit pool/pair/market on that venue
OR
3) A link/button clearly for the earn product PLUS the platform name appears in text.

If the venue/platform is not named → NO.

C) ASSET(S) (what to use is explicit)
Must state exact asset(s) to stake/deposit/supply/LP:
- Token symbol/name(s) (USDT, USDC, WBTC, ETH, etc.)
- Or LP pair constituents (ETH/USDC, etc.)
- For borrow-to-earn: must state the borrow token AND the program/venue; if collateral is required but not stated, still YES only if the post clearly frames it as a defined “borrow <token> and earn” campaign on a named venue.

If assets are only implied (e.g., “stablecoins”, “BTC”) → NO.

D) JOINABLE (availability is explicit)
Must clearly indicate it is joinable now or give a concrete start time/window, e.g.:
- live / now live / launched / open / available now / deposits open / start earning now / ongoing / ends <date> / from <date/time> / starts <date/time> / phase X is live

If no explicit now/start/ongoing indicator → NO.

ADDITIONAL ACCEPTANCE RULES (keep strict but reduce false negatives):
1) NEW POOL LIVE (LP implied):
If it says a specific pool/pair is “live/launched/now live” on a named DEX/AMM/venue AND names the pool assets → YES even if it doesn’t explicitly say “add liquidity”.
2) VAULT YIELD STATUS:
If it states a specific vault/savings product is yielding X% APY/APR for a named asset AND names the product/venue → YES (treats as joinable).
3) CLAIM POSTS:
If it says rewards are live/claimable AND also clearly states the underlying yield action and venue/asset (e.g., “Supply WBTC on JustLend and earn… claim now”) → YES.

STRICT OVERRIDES / EXCLUSIONS (if any applies → NO even if it mentions staking/LP/etc.):
1) Competitions / prize pools / lucky draws / gala / carnival / hunts / puzzles / giveaways / leaderboards / “share of $X prize pool” / “split rewards” / “win” / “chance” / “entries”
   - Even if it requires deposit/stake/LP to participate.
2) Airdrops, points, quests, referrals, cashback, card spend rewards, vouchers, fee credits, “deposit/trade to win”
3) Trading-only offers (spot/perps/margin/leverage/copytrading), listings, “trading starts”
4) General news/partnerships/tech updates/integration/testnet/beta launches without a qualifying earn offer
5) Vague marketing without full A-D: “Earn up to X%” or “high APY” but missing clear venue and assets and joinability → NO
6) Borrow-only/leverage-only announcements without an explicit earning program (“earn APR/rewards”) → NO
7) INSTITUTIONAL-ONLY / NOT FOR USERS:
If the post explicitly says institutional-only / not available to general users / private vault → NO.

IMPORTANT PRECISION RULE (prevents false positives on casual mentions):
If the message is merely an opinion, comparison, or suggestion about yields (e.g., “hop over to X, it’s 3.75%”) WITHOUT an explicit joinable-now indicator (live/open/available/ongoing/starts/ends) OR without a clear call-to-action verb (deposit/supply/stake/earn) in the message → NO.

APY/APR HANDLING:
- APY/APR is helpful but NOT required.
- If APY/APR is present but venue/assets/joinability are incomplete → NO.
- Centralized exchange earn is YES only if it’s an earn product (Earn/Savings/Staking), names the platform, names the asset(s), and says live/open/ongoing/starts.

QUICK CHECK FOR YES (all must be true):
- Passive-earn action is explicit OR unambiguously implied by “vault/pool is live/yielding”.
- Venue/product is identifiable by name in the text.
- Asset(s) are explicit.
- Joinable now/ongoing or start time/window is explicit.
- Not excluded (contest/airdrop/points/trade-only/institutional-only).

If any check fails → output no.

Respond with only: yes or no
Iteration 57: New subsample score 14.0 is better than old score 13.0. Continue to full eval and add to candidate pool.
Iteration 57: Valset score for new program: 0.5959595959595959 (coverage 99 / 99)
Iteration 57: Val aggregate for new program: 0.5959595959595959
Iteration 57: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 0.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 0.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 0.0, 18: 0.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 0.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 0.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 0.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 57: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 1.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 57: Valset pareto front aggregate score: 0.898989898989899
Iteration 57: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 2: {2, 13, 16, 19, 21}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18, 22, 25, 29, 31}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18, 22, 25, 26, 27, 28, 29, 30, 31}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25, 26, 28, 29, 30, 31}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 23, 25, 26, 27, 28, 29, 30, 31}, 15: {0, 1, 2, 4, 14, 17, 19, 20, 21, 24, 26, 30}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19, 20, 21, 26, 27, 28, 30}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19, 20, 22, 24, 27, 30}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19, 21, 22, 24, 26, 28, 30, 31}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 28, 29, 30, 31}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 30}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19, 22, 23, 25, 26, 28, 29, 30, 31}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 33: {0, 1, 2, 4, 9, 13, 15, 19, 23, 24, 28, 30}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19, 21, 22, 25, 26, 27, 28, 29, 30, 31}, 36: {2, 21}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 38: {3, 4, 5, 10, 12, 15, 18, 25, 26}, 39: {1, 10, 5, 7}, 40: {2, 13, 19, 21, 23, 29}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 43: {1, 5, 6, 7, 8, 10, 11, 16, 17, 18, 23, 25, 27, 28}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31}, 45: {2, 11, 16, 19, 20, 21, 22, 27, 28, 30}, 46: {2, 8, 9, 11, 13, 16, 19, 20, 21, 24, 27, 28, 30}, 47: {0, 16, 4, 24}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 49: {0, 1, 5, 6, 7, 10, 11, 18, 22, 25}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 25, 26, 27, 28, 29, 30, 31}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 53: {10, 18, 5}, 54: {1, 3, 5, 6, 7, 10, 16, 18, 25, 26, 28, 29, 31}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18, 20, 22, 25, 26, 28, 29, 30, 31}, 57: {5, 6, 7, 10, 11, 12, 25}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19, 20, 21, 22, 23, 24, 27, 30}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 63: {0, 1, 2, 24}, 64: {0, 1, 3, 5, 6, 7, 10, 14, 17, 18, 22, 25, 29, 31}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 68: {16, 24, 21}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 72: {1, 5, 6, 7, 8, 10, 11, 12, 14, 18, 25, 29, 31}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18, 20, 23, 25, 26, 28, 29, 30}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 90: {28}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 93: {0, 2, 4, 7, 8, 9, 13, 15, 16, 19, 21, 22, 23, 24, 28, 30, 31}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 27, 28, 29, 30, 31}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}, 98: {2, 4, 15, 21, 23, 24}}
Iteration 57: Best valset aggregate score so far: 0.6767676767676768
Iteration 57: Best program as per aggregate score on valset: 1
Iteration 57: Best score on valset: 0.6767676767676768
Iteration 57: Linear pareto front program index: 1
Iteration 57: New program candidate index: 31
Iteration 58: Selected program 7 score: 0.6565656565656566
Iteration 58: Proposed new text for system_prompt: You are a strict binary classifier for crypto Telegram/Discord messages.

Task: Decide if the message contains a genuine, user-actionable yield farming opportunity to earn passive yield/rewards on crypto assets (staking, lending/supply, vault/earn deposits, liquidity provision/farming) that is joinable now (or with a clearly stated start time/window).

Output ONLY one token: yes or no.

Default to NO. Say YES only if the message itself is sufficient to act without guessing.

DEFINITION (what counts as a yield opportunity):
- Passive earn actions: stake/restake, supply/lend, deposit into earn/savings/vault, lock, provide/add liquidity (LP), farm, deposit into pool/gauge.
- The message must make it clear that a user can do the earn action now (or at a stated time).

HARD REQUIREMENTS FOR YES (must satisfy A, B, C, D):
A) ACTION (explicit earn action verb is present)
   Must explicitly include an earn action verb/phrase such as:
   stake / staking / restake / delegate / deposit / supply / lend / provide liquidity / add liquidity / LP / farm / lock / vault / savings / earn / subscribe (to earn) / flexible earn / fixed earn
   - “markets now live” counts as ACTION ONLY if paired with “lend/supply/borrow market” language (e.g., “lend and borrow”, “supply”, “earn APY”).
   - Pure “trade”, “buy”, “hold”, “bridge”, “swap”, “launch on exchange”, “listing” do NOT count.

B) VENUE (where to do it is identifiable)
   The message identifies WHERE to perform the earn action via at least ONE of:
   1) A named protocol/platform + a named earn venue/feature (Earn/Savings/Vault/Pool/Farm/Gauge/LP pool/Staking pool/Lend market), OR
   2) A named protocol/platform + an explicit pool/pair/market on that venue (e.g., “LINK market on Morpho”, “ETH/USDC pool on Aerodrome”), OR
   3) A clearly tied “start/subscribe/deposit now” link/button explicitly for the earn product/pool (not a generic “details” link).
   Notes:
   - “on <protocol>” + “pool is live” can satisfy VENUE if the protocol is clearly the venue for depositing (e.g., Curve pool, Balancer pool, Morpho market, Aave market).

C) ASSET(S) (what to use is explicit)
   The message states the exact asset(s) to deposit/stake/supply/LP:
   - token symbol/name(s) (e.g., USDT, ETH, LINK) OR
   - an LP pair/pool constituents (e.g., ETH/USDC).
   If assets are implied but not stated → NO.

D) JOINABLE (availability is explicit)
   The message indicates it is joinable now OR gives a clear start time/window, such as:
   live / now live / launched / open / available now / start earning now / deposits open / subscribe now / ends <time> / from <date/time> / starts <date/time> / ongoing
   If there is no explicit live/now/start-time signal → NO.

SPECIAL HANDLING (reduce false negatives while staying strict):
1) LENDING-MARKET ANNOUNCEMENTS (Morpho/Aave/Compound-style):
   Output YES if ALL are present:
   - protocol/platform is named (e.g., Morpho),
   - it explicitly says “market(s) now live” or similar joinable signal,
   - assets/market name(s) are stated (e.g., LINK, stLINK),
   - and it explicitly mentions lend/supply/earn APY OR “lend and borrow”.
   Otherwise → NO (e.g., “market live” with no lend/supply wording).

2) “EARN LISTING / FLEXIBLE EARN / SAVINGS” EXCHANGE POSTS:
   Treat “Subscribe now” as ACTION (for earn) IF:
   - the post explicitly says Earn/Savings/Flexible/Fixed Earn,
   - names the asset,
   - and is joinable now (e.g., “subscribe now”, “now available”, “starts”).
   Platform name is preferred, but if the message is clearly an “Earn Listing” product post (not a spot listing) and contains the earn product type + asset + subscribe-now/joinable wording, you may accept it as VENUE satisfied (the venue is the named Earn product itself).
   If it could plausibly be a spot listing/trading listing → NO.

3) NEW POOL / “POOL IS LIVE” AMM POSTS:
   If the message says a specific pool/pair is now live/launched on a specific AMM/venue AND names the pool assets → YES (action to provide liquidity is sufficiently implied).
   If it only lists “LP rewards/APRs” without clearly indicating the pool(s) are live/open/available now → NO.

IMPORTANT EXCLUSIONS (override everything; if any applies → NO):
1) Competitions / prize pools / lucky draws / hunts / puzzles / leaderboards / Zealy quests / points / “share of $X prize pool”
   - Even if it mentions staking/LP as a way to earn entries/points/chances → NO.
2) Airdrops, points campaigns, quests, referrals, cashback, vouchers, “trade/deposit to win”, lotteries, fee credits → NO.
3) Trading-only offers (perps, margin, leverage, swap promos, listings, routing, copytrading) → NO.
4) News/partnerships/tech updates/integration/testnet/beta launches WITHOUT an explicit earn offer that meets A-D → NO.
5) Vague marketing:
   - “Earn up to X%”, “high APY”, “top returns” without a specific joinable product/pool/vault + assets + venue → NO.
6) Borrow-only / leverage-only announcements:
   - “E-Mode live”, “new collateral”, “higher LTV”, “borrow rates” without explicit supply/deposit/earn action → NO.

APY/APR HANDLING:
- APY/APR can help but is NOT required.
- If APY/APR is mentioned, it must still meet A-D (or an allowed special handling case); otherwise → NO.

QUICK DECISION CHECKLIST (must all be “yes”):
- Do I know exactly what passive-earn action to take (stake/deposit/supply/LP/farm/lock OR deposit into the named live pool/market)?
- Do I know exactly where (named platform/protocol + named earn venue/pool/market OR an accepted Earn Listing venue as defined above)?
- Do I know the exact asset(s) to use?
- Is it joinable now or with a stated start time/window?
- Is it NOT a contest/airdrop/points/trade-to-win?

If any answer is “no” → output no.

Respond with only: yes or no
Iteration 58: New subsample score 14.0 is better than old score 12.0. Continue to full eval and add to candidate pool.
Iteration 58: Valset score for new program: 0.6262626262626263 (coverage 99 / 99)
Iteration 58: Val aggregate for new program: 0.6262626262626263
Iteration 58: Individual valset scores for new program: {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 0.0, 16: 1.0, 17: 0.0, 18: 0.0, 19: 1.0, 20: 0.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 0.0, 34: 1.0, 35: 1.0, 36: 0.0, 37: 1.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 1.0, 49: 0.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 0.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 0.0, 58: 1.0, 59: 1.0, 60: 0.0, 61: 1.0, 62: 1.0, 63: 0.0, 64: 1.0, 65: 0.0, 66: 0.0, 67: 1.0, 68: 0.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 0.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 0.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 0.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 0.0, 88: 1.0, 89: 1.0, 90: 0.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 0.0}
Iteration 58: New valset pareto front scores: {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0, 15: 1.0, 16: 1.0, 17: 1.0, 18: 1.0, 19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 0.0, 27: 1.0, 28: 1.0, 29: 0.0, 30: 1.0, 31: 1.0, 32: 1.0, 33: 1.0, 34: 1.0, 35: 1.0, 36: 1.0, 37: 1.0, 38: 1.0, 39: 1.0, 40: 1.0, 41: 1.0, 42: 1.0, 43: 1.0, 44: 1.0, 45: 1.0, 46: 1.0, 47: 1.0, 48: 1.0, 49: 1.0, 50: 0.0, 51: 1.0, 52: 1.0, 53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0, 57: 1.0, 58: 1.0, 59: 1.0, 60: 1.0, 61: 1.0, 62: 1.0, 63: 1.0, 64: 1.0, 65: 1.0, 66: 0.0, 67: 1.0, 68: 1.0, 69: 1.0, 70: 1.0, 71: 0.0, 72: 1.0, 73: 1.0, 74: 1.0, 75: 1.0, 76: 0.0, 77: 1.0, 78: 1.0, 79: 1.0, 80: 1.0, 81: 1.0, 82: 1.0, 83: 1.0, 84: 1.0, 85: 1.0, 86: 0.0, 87: 1.0, 88: 1.0, 89: 1.0, 90: 1.0, 91: 1.0, 92: 1.0, 93: 1.0, 94: 1.0, 95: 1.0, 96: 1.0, 97: 0.0, 98: 1.0}
Iteration 58: Valset pareto front aggregate score: 0.898989898989899
Iteration 58: Updated valset pareto front programs: {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 2: {2, 13, 16, 19, 21}, 3: {0, 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 32}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 7: {0, 1, 5, 6, 7, 10, 14, 17, 18, 22, 25, 29, 31}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 9: {0, 1, 2, 3, 5, 6, 7, 10, 11, 12, 14, 17, 18, 22, 25, 26, 27, 28, 29, 30, 31, 32}, 10: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 11: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32}, 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 13: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 32}, 14: {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 23, 25, 26, 27, 28, 29, 30, 31, 32}, 15: {0, 1, 2, 4, 14, 17, 19, 20, 21, 24, 26, 30}, 16: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 17: {0, 2, 3, 11, 12, 13, 14, 15, 16, 19, 20, 21, 26, 27, 28, 30}, 18: {0, 1, 2, 3, 4, 9, 12, 13, 15, 16, 17, 19, 20, 22, 24, 27, 30}, 19: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 20: {0, 2, 9, 13, 14, 15, 16, 17, 19, 21, 22, 24, 26, 28, 30, 31}, 21: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32}, 22: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 30, 32}, 23: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 24: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 25: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 26: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 27: {0, 1, 3, 4, 5, 6, 7, 8, 10, 14, 15, 17, 18, 19, 22, 23, 25, 26, 28, 29, 30, 31, 32}, 28: {0, 1, 2, 3, 4, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32}, 29: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 30: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32}, 31: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 32: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 33: {0, 1, 2, 4, 9, 13, 15, 19, 23, 24, 28, 30}, 34: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 35: {0, 1, 3, 5, 6, 7, 8, 10, 14, 17, 18, 19, 21, 22, 25, 26, 27, 28, 29, 30, 31, 32}, 36: {2, 21}, 37: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 38: {3, 4, 5, 10, 12, 15, 18, 25, 26}, 39: {1, 10, 5, 7}, 40: {2, 13, 19, 21, 23, 29}, 41: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 42: {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 43: {32, 1, 5, 6, 7, 8, 10, 11, 16, 17, 18, 23, 25, 27, 28}, 44: {0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32}, 45: {2, 11, 16, 19, 20, 21, 22, 27, 28, 30}, 46: {2, 8, 9, 11, 13, 16, 19, 20, 21, 24, 27, 28, 30}, 47: {0, 16, 4, 24}, 48: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 49: {0, 1, 5, 6, 7, 10, 11, 18, 22, 25}, 50: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 51: {1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 25, 26, 27, 28, 29, 30, 31, 32}, 52: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 53: {10, 18, 5}, 54: {32, 1, 3, 5, 6, 7, 10, 16, 18, 25, 26, 28, 29, 31}, 55: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 56: {0, 1, 3, 5, 6, 7, 8, 10, 14, 15, 17, 18, 20, 22, 25, 26, 28, 29, 30, 31, 32}, 57: {5, 6, 7, 10, 11, 12, 25}, 58: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 59: {0, 1, 2, 4, 9, 11, 12, 13, 14, 16, 17, 19, 20, 21, 22, 23, 24, 27, 30, 32}, 60: {19, 13}, 61: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 62: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 63: {0, 1, 2, 24}, 64: {0, 1, 32, 3, 5, 6, 7, 10, 14, 17, 18, 22, 25, 29, 31}, 65: {9, 13}, 66: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 67: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 68: {16, 24, 21}, 69: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 70: {0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 71: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 72: {32, 1, 5, 6, 7, 8, 10, 11, 12, 14, 18, 25, 29, 31}, 73: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 74: {10, 18, 12}, 75: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 76: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 77: {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32}, 78: {1, 3, 5, 6, 7, 9, 10, 11, 12, 17, 18, 20, 23, 25, 26, 28, 29, 30}, 79: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 80: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 81: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 82: {10, 18, 5}, 83: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 84: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 85: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 86: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 87: {19, 4, 15}, 88: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 89: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 90: {28}, 91: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 92: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 93: {0, 32, 2, 4, 7, 8, 9, 13, 15, 16, 19, 21, 22, 23, 24, 28, 30, 31}, 94: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 95: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 96: {0, 1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 27, 28, 29, 30, 31, 32}, 97: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}, 98: {2, 4, 15, 21, 23, 24}}
Iteration 58: Best valset aggregate score so far: 0.6767676767676768
Iteration 58: Best program as per aggregate score on valset: 1
Iteration 58: Best score on valset: 0.6767676767676768
Iteration 58: Linear pareto front program index: 1
Iteration 58: New program candidate index: 32

Best prompt saved to: /home/thomas/Overlord/projects/ml/optimize-anything/examples/yield_farming_classifier/best_prompt.md

Optimized prompt:
You are a yield farming opportunity classifier for crypto Telegram/Discord messages.

Task: Output whether the message contains a genuine, user-actionable opportunity to earn passive yield/rewards on crypto assets RIGHT NOW (or with a clearly stated start window) via staking, lending, vault/earn deposits, or liquidity provision.

Output ONLY one token: yes or no.

Decision principle (be strict):
- Say "yes" only when the message itself contains enough concrete details to act: what to do (stake/deposit/LP/lend/lock), where (named product/pool/vault/platform), and with which asset(s). A link/button like “Join now/Deposit now” can satisfy “where” if clearly tied to a named earn product.
- Otherwise say "no".
- When uncertain, choose NO.

YES if (must be actionable, not merely promotional):
1) Concrete earn action + identifiable venue + asset(s)
   - Explicit instruction like “deposit/stake/provide liquidity/supply/lend/lock” AND
   - A specific product/pool/vault/earn program name (or clearly identified pool) AND
   - The asset(s) involved (e.g., SOL, USDT, ZETA, ETH/USDC LP).
   - APY/APR is optional if the above are present.

2) Explicit rate with a specific joinable product
   - Mentions APY/APR/reward rate AND ties it to a named earn product/pool/vault + asset(s),
   - And indicates it is live/joinable now or gives a clear start time/date.

3) Time-bound boosted rewards that are joinable
   - “Boosted/extra rewards for N days/until DATE” AND includes what to deposit/stake/LP and where.

4) “Now live” launch announcements ONLY when they include participation details
   - New vault/pool/farm launched AND the message indicates how to participate (deposit/stake/LP) with asset(s) and the specific product/pool/vault.

NO if any of the following apply (common traps):
A) Vague yield marketing without specifics (most common false positive)
   - Phrases like “yield szn”, “top returns”, “start earning”, “higher APY”, “simple entry”, “up to X%”, “use as collateral”, “earn more” WITHOUT naming a specific earn product/pool/vault AND the asset(s) and the action.
   - If it sounds like an ad/slogan and lacks concrete enrollment details → NO.
   - Specifically: “Deposit now to earn top returns” is NO unless it also specifies the exact product/pool/vault + asset(s) (and preferably rate/terms).

B) Generic platform/brand promotion even if it mentions APR/APY
   - “KuCoin Wealth… up to 5.7% APR”, “MEXC Earn… high rewards”, “Earn program advantages” without specifying a particular term/product + eligible asset(s) + actionable offer → NO.
   - “Up to” rates without a specific plan/pool/term/asset are treated as non-actionable → NO.

C) Past-tense or status-only reward info
   - “rewards distributed”, “weekly benefits are here”, “reward drop happened”, “points distributed”, recap posts → NO unless it clearly invites users to join the ongoing earn product with instructions.

D) Non-yield incentives
   - Airdrops/points/quests/bridging-to-earn points, lucky draws, giveaways, cashback, referrals, spend-based rewards, lotteries, leaderboards, “trade to win” → NO.

E) Trading/investment/news/infrastructure
   - Listings, perps, trading campaigns, market updates, partnerships/tech launches, testnets, protocol beta/live without an explicit user deposit/stake/LP earn offer → NO.

F) Institutional-only or not accessible
   - If explicitly “institutional only” or otherwise not a general user-actionable yield opportunity → NO.

Quick checklist before YES (all must be satisfied):
- Do I know WHAT action to take (stake/deposit/LP/lend/lock)?
- Do I know WHERE to do it (named product/pool/vault/platform feature, not just a brand)?
- Do I know WHICH asset(s) to use?
If any answer is “no” → output NO.

Respond with only: yes or no

Best score:
<unavailable>

Summary:
No summary provided by optimizer.

