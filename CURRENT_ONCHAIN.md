# VoltZilla (VZLA) — CURRENT deployed token internals
**As-of:** 20 November 2026 (Asia/Riyadh). On-chain supply/authority source: Helius-backed Solana mainnet RPC via Nova, re-checked by [GitHub RPC monitoring](https://github.com/itsAAA1/VoltZilla/actions/workflows/primary-internals.yml). Pump.fun token/program features: indexed Pump.fun status plus official Pump documentation. **Observed facts are snapshots, not investment, liquidity or security guarantees.**

## 1. The actual token that matches the creator wallet
- Token: **VoltZilla (VZLA)**, launched **4 April 2026**, Pump.fun.
- Mint / contract: `GDYcemcZozG9ijhEZioRLRgNMtoxh1BBuV7nvdf1pump`
- Solana program: **Token-2022**, id `TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb`.
- Decimals: **6**.
- Original Pump.fun creator: `GGSqpEPw3WDvfqJRj6frvrTz1C2wcUz28Sgfdg2NNJiD`.
- [Creation transaction](https://solscan.io/tx/2frB6tsVzkEyPuteLX35fSbcKvq16fj3UbwD5pyQnhm3Mhgbutc3FGrB64tFacggnP1dkrC37EL26hsKZKQVC23U).
- [Original Pump.fun token](https://pump.fun/coin/GDYcemcZozG9ijhEZioRLRgNMtoxh1BBuV7nvdf1pump).
- Original creator address match is **on-chain provenance**, not proof that the current human owner controls the wallet: **not yet cryptographically proven**.

## 2. Real supply and token ownership, not the old planned split
Total on-chain issued supply observed: **1,007,005,921.840554 VZLA**.

| Account type | Recorded balance, VZLA | % of actual minted supply |
|---|---:|---:|
| Pump.fun original bonding-curve account | 1,000,000,000 | 99.30428196% |
| Original creator wallet | 7,005,921.840554 | 0.69571804% |
| Reported Mayhem/agent account (third observed account) | 0 | 0.00000000% |
| **Total** | **1,007,005,921.840554** | **100.00000000%** |

- Bonding-curve **inventory is not the developer's treasury**, not automatically a Raydium/PumpSwap LP position, and not evidence of locked liquidity.
- Top-account balance precision is from the canonical mint; provider percentages can be inconsistent and must be recomputed against **1,007,005,921.840554**, not a hard-coded 1B or the Solana Tracker `percentage=100` pool field.
- The earlier **40% Community / 30% Liquidity / 20% Development / 10% Marketing** table was a **historical-only draft** and was never shown as executed transactions. It is not this minted token's actual allocation.
- Two **other** mints bearing VZLA must be excluded from this supply: `DHxStA9nRq6DdhBKT89s38fpxD9wE7MtyMn9HMuWeyN9` (separate 1M standard SPL Token with active mint authority) and `JBaHDseUdFEVbAik7rojwC8ZZ8EjyBi1qQPoK9tLpump` (historical unrelated Pump.fun contract).

## 3. Source of the extra ~7.006M tokens — what is proven?
- Observed supply exceeds a standard 1,000,000,000 by **7,005,921.840554** units.
- Pump's **Mayhem Mode** explicitly starts with *additional agent-minted tokens* up to a 2-billion initial total and burns the agent's unsold tokens after its initial trading period. Existing tokens retain the Mayhem mode label even when that period has ended. [Official Pump Mayhem Mode documentation](https://pump.fun/docs/mayhem-mode) and [official Mayhem risk disclaimer](https://pump.fun/docs/mayhem-mode-disclaimer).
- The **mechanism plausibly explains** the remaining supply above 1B; the exact mint/burn/transfer lineage for this specific GDY token must still be reconciled from the original agent transactions before calling the mechanism the proven arithmetic explanation. **Never say there is an ongoing mint authority** when Solana's canonical mint authority is null.

## 4. Live program functionality and rights
- **Mint authority:** revoked / null at review snapshot.
- **Freeze authority:** revoked / null at review snapshot.
- Token-2022 extension types reported by canonical safety review: **MetadataPointer** and **TokenMetadata**. No TransferFeeConfig, PermanentDelegate, TransferHook or PausableConfig was reported in this mint-level snapshot. The project uses a conservative raw-extension integrity verifier in GitHub CI.
- A null mint/freeze authority does **not** prove code-free transfers, trading liquidity, locked capital, control of Pump program accounts, or zero platform fees.
- On-chain Token-2022 metadata URI: `https://ipfs.io/ipfs/Qmdgqvtw7fJuahenbvVJrbvnMX35XT4snN3vJyRdyKGiYG`, published X: **@VoltZillaSOL**. Owner-reported public X: **@voltzillasol1**. The accounts are distinct and relationship not proven; GitHub JSON edits do **not** rewrite this chain metadata.

## 5. Pump.fun Mayhem, Cashback, Holder Rewards, buybacks
| Feature in indexed Pump.fun account | Observed setting | Actual interpretation |
|---|---|---|
| `isMayhemMode` | `true` | Coin was created with Mayhem; **does not** mean the 24-hour trading agent is still active |
| Mayhem run status | **Completed** on original Pump page | Agent activity completed; does not imply trading liquidity or graduation |
| `isCashbackCoin` | `true` | Eligible platform trades may route creator fee back to buyers using cashback instructions |
| `isHolderReward` | `false` | No holder-rewards distribution model shown for this token |
| Agent config `buybackBps` | 5000 (=50% as configuration) | **Mayhem/agent setting**, not a promise that half of investors' funds will be bought back |
| Executed buyback / payout ledger | **Unverified** | Parameter is **not** evidence that transfers or purchases occurred |

According to [official Pump fees](https://pump.fun/docs/fees), existing cashback tokens credit eligible creator fees back to buyers when using cashback-enabled instructions; flows using other instructions may pay creator fees instead. There are other protocol/platform/network fees. A changed platform policy or custody arrangement can affect observed cashflows. Without transaction-level proofs, no holder return, automatic creator income or cashback balance is assumed.

## 6. Market microstructure and status
- Pump.fun curve: **not graduated** at latest evidence; a dedicated graduated PumpSwap/Raydium LP was not established from inspected records.
- Original Pump page displayed **24h volume: US$0.00**, very low interface liquidity (~0.07 SOL), and 2 nonzero owners at its recent observation. Separate indexed models include **virtual SOL reserves** (example: 22.345 SOL quote) and estimated cap; **never present virtual reserves as withdrawable real liquidity**.
- Quote/route sellability and deep liquidity are **not verified**. Low turnover is a market limitation, not necessarily a faulty mint.
- Creating more token supplies, unrelated pools, fabricated volume or unverified airdrops will not fix these facts.

## 7. Actual execution still gated
- No proof of current human control over the creator-wallet signing key.
- Actual public X identity cross-link needs a genuine announcement from a controlled account.
- No signed independent security evaluation of the Pump/Token-2022 program interaction or Mayhem/agent custom state.
- No independent qualified legal conclusion for any Saudi-directed sale, retail marketing or fundraising.
- No verified funded liquidity plan or evidence of active meaningful swaps.
- No official CoinGecko or CoinMarketCap application receipt. Technical submission records are prepared in the [primary project](https://github.com/itsAAA1/VoltZilla/blob/main/docs/LISTING_APPLICATION_PACK.md).

**Consolidated engineering source of truth:** [primary mint inspector](https://github.com/itsAAA1/VoltZilla/blob/main/scripts/inspect_mints.py), [Token-2022 extension + holder reconciliation audit](https://github.com/itsAAA1/VoltZilla/blob/main/scripts/audit_primary_internals.py), [source observations](https://github.com/itsAAA1/VoltZilla/blob/main/docs/PUMPFUN_PRIMARY_AUDIT_2026-11-20.md). No new mint was created, no funds transferred, no listing accepted, and no smart-contract permissions changed in preparing this document.
