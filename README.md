> **تدقيق إضافي (20 نوفمبر 2026):** تم التحقق من توكن VoltZilla رابع منفصل على **Raydium LaunchLab**، العقد `3cPWF3eKjcq4Y8d2oVXDRaN8ipKBHuyK1uYWY4GT7ray` (مليار VZLA، 6 خانات، سلطتا السك والتجميد null). فهرس Solana يربط إنشائه بمحفظة `28fU8SDMKLXe8hqmdy9dxYNHeddm7xQRzkxK16JLUpi4` يوم 15 مايو 2026. مجمع LaunchLab **غير متخرج**، وبيانات السعر المفهرسة ليست سعرًا حيًا مضمونًا. هذا عقد مختلف عن GDY Pump.fun، وليس سببًا لاختيار العقد الرسمي تلقائيًا. راجع [مطابقة جميع العقود](https://github.com/itsAAA1/VoltZilla/blob/main/docs/FOUR_MINT_RECONCILIATION_2026-11-20.md) وأداة [إثبات المحفظة برسالة](https://itsaaa1.github.io/verify-wallet.html).

# VoltZilla (VZLA) — actual minted Pump.fun token

**Status as reviewed 20 November 2026:** The Solana creator wallet and creation transaction link the VoltZilla project to a specific deployed Pump.fun token. Human control of the wallet has **not** been proven by a recent signature. Do not treat this repository as a licensed offering, exchange approval, wallet custody, or financial return guarantee.

## Current live project — use this first

**[CURRENT_ONCHAIN.md](CURRENT_ONCHAIN.md)** is the current canonical technical tokenomics statement; older allocation proposals are **historical-only**.

| Fact | Verified observation |
|---|---|
| Network | Solana mainnet |
| Original platform | Pump.fun |
| Creation date | **4 April 2026** |
| Token | **VoltZilla / VZLA** |
| Exact creator-matched mint | `GDYcemcZozG9ijhEZioRLRgNMtoxh1BBuV7nvdf1pump` |
| Mint program | **Token-2022** (`TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb`) |
| Decimals | **6** |
| Actual minted supply at audit | **1,007,005,921.840554 VZLA** |
| Original creator account | `GGSqpEPw3WDvfqJRj6frvrTz1C2wcUz28Sgfdg2NNJiD` |
| Mint authority / freeze authority | **both null** at time of canonical on-chain observation |
| Reported mint extensions | MetadataPointer, TokenMetadata; no mint-level TransferFeeConfig |
| Mayhem | Flag exists; original agent window completed |
| Cashback / holder reward flags | `true` / `false` respectively, according to Pump.fun indexed state |
| Bonding curve | Not graduated at checked time; no approved external LP claim |
| Exchange directory listing applications | **Not submitted / لم يُقدَّم بعد** to CoinGecko or CoinMarketCap |

[Pump.fun original contract](https://pump.fun/coin/GDYcemcZozG9ijhEZioRLRgNMtoxh1BBuV7nvdf1pump) · [Solscan creation transaction](https://solscan.io/tx/2frB6tsVzkEyPuteLX35fSbcKvq16fj3UbwD5pyQnhm3Mhgbutc3FGrB64tFacggnP1dkrC37EL26hsKZKQVC23U) · [technical audit monitoring](https://github.com/itsAAA1/VoltZilla/actions/workflows/primary-internals.yml)

### What the actual balances mean

The Pump.fun bonding curve held **1,000,000,000 VZLA (99.30428196%)** and the creator's publicly recorded wallet held **7,005,921.840554 (0.69571804%)**. These two balances exactly equal the mint's recorded supply, but the curve inventory is not developer treasury or locked liquidity. The 2026 Pump.fun **Mayhem** mechanism can explain supply above the normal billion, but this token's complete historical mint/burn event chain has not yet been independently reconciled. See the dedicated [current on-chain analysis](CURRENT_ONCHAIN.md).

### Are these royalties or buyback guarantees?

**No.** The indexed `agentConfig.buybackBps = 5000` is a Mayhem/agent configuration field, not evidence that anyone bought tokens back or that 50% of holders' investments will be returned. Pump.fun cashback fees can be redirected to buyers through relevant trade instructions, not automatically to all holders. The Holder Rewards flag on this coin is false. The normal platform and network fees still apply. [Pump.fun fees](https://pump.fun/docs/fees).

### Critical identity and supply safeguards

- **Different VZLA mint (historical million-unit SPL token):** `DHxStA9nRq6DdhBKT89s38fpxD9wE7MtyMn9HMuWeyN9`; this is a *different token* with **1,000,000 units, 9 decimals, active mint authority**. Do not use it as the contract for GDY.
- **Older historical Pump.fun VZLA mint:** `JBaHDseUdFEVbAik7rojwC8ZZ8EjyBi1qQPoK9tLpump`; separate asset, not connected by proven project-owner wallet signature.
- Pump.fun on-chain metadata links [@VoltZillaSOL](https://x.com/VoltZillaSOL); the owner-reported public account is [@voltzillasol1](https://x.com/voltzillasol1). They have different X account IDs and are not cryptographically reconciled. A GitHub metadata edit alone cannot alter the already-deployed Token-2022 record.
- The project remains blocked from describing itself as fully independently audited, exchange approved, legally cleared, liquid or guaranteed tradeable.

### Public engineering and source records

- [Main source-of-truth audit](https://github.com/itsAAA1/VoltZilla/blob/main/docs/PUMPFUN_PRIMARY_AUDIT_2026-11-20.md)
- [Read-only RPC mint and extension/holder auditor](https://github.com/itsAAA1/VoltZilla/blob/main/scripts/audit_primary_internals.py)
- [Release manifest and blockers](https://github.com/itsAAA1/VoltZilla/blob/main/project-manifest.json)
- [Official public project site](https://itsaaa1.github.io/) and [status/verification page](https://itsaaa1.github.io/status.html)
- [Listing application preparation, not sent](https://github.com/itsAAA1/VoltZilla/blob/main/docs/LISTING_APPLICATION_PACK.md)
- [Previously proposed distribution split, **historical-only**](tokenomics.md).

No new token, sale, LP pool, transactions or permissions changes were created by updating these files. These are public engineering records, not a claim of independent smart-contract or legal certification.
