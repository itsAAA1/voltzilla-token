# VoltZilla (VZLA) — Token Documentation

> **Verification pending / قيد التحقق** — This repository is documentation, **not proof of token ownership, verified token supply, available liquidity, exchange listing, or investment returns**.

## Current confirmed project references

- Network discussed: Solana.
- Project name used in this repository: VoltZilla (VZLA).
- **X account confirmed by the project owner:** [@voltzillasol1](https://x.com/voltzillasol1).
- Public project website: [itsAAA1.github.io](https://itsaaa1.github.io/).
- Actual files in this repository: `README.md`, `tokenomics.md`, `LICENSE`.

## Live on-chain observation: owner-reported mint, not yet cryptographically authenticated

**On-chain inspection — 5 November 2026 (Solana mainnet; Helius RPC via Nova):** The owner previously supplied mint `DHxStA9nRq6DdhBKT89s38fpxD9wE7MtyMn9HMuWeyN9`. The mint exists as **VoltZilla (VZLA)**, SPL Token (standard Token Program), **1,000,000 current units**, **9 decimals**. Mint authority remains active (more tokens can be created); freeze authority is null; metadata update authority is active. The largest reported token account holds **100% of the current supply**. No reliable spot price or verified liquidity pair was returned. This validates observable mint data **but not a cryptographic signature proving the owner's control or public approval of this mint as the project's sole official address**. Never call this supply immutable, decentralized, tradeable, or liquidity-locked without separate evidence. Another mint shown in an old whitepaper (`JBaHDseUdFEVbAik7rojwC8ZZ8EjyBi1qQPoK9tLpump`) is **a separate token** with **6 decimals** and approximately **999,992,926.77** current units; its authorities and creator differ, so those figures must not be merged.

## Live technical checks and what can actually be changed

- The project's [read-only SPL Mint inspector](https://github.com/itsAAA1/VoltZilla/blob/main/scripts/inspect_mints.py) fetches **both candidate addresses** directly from Solana mainnet; it checks the supply, decimal precision, mint and freeze authorities against a dated snapshot. A [daily GitHub Actions audit](https://github.com/itsAAA1/VoltZilla/actions/workflows/onchain-mint-audit.yml) performs the same read-only comparison.
- The reported million-unit mint is a standard SPL token; the [mint account on Solscan](https://solscan.io/token/DHxStA9nRq6DdhBKT89s38fpxD9wE7MtyMn9HMuWeyN9) presently has active mint authority and mutable Metaplex metadata. The verified Metaplex creator/authority public key is `28fU8SDMKLXe8hqmdy9dxYNHeddm7xQRzkxK16JLUpi4`. **A verified creator signature does not establish that the GitHub account holder controls the private key.**
- The [separate older mint on Solscan](https://solscan.io/token/JBaHDseUdFEVbAik7rojwC8ZZ8EjyBi1qQPoK9tLpump) has no mint or freeze authority and immutable on-chain metadata. Its historical promotional description contains claims that should **not** be repeated as verified facts.
- Changing actual Solana mint or Metaplex settings is **not a GitHub edit**. It requires a transaction approved and signed by the controlling wallet; the connected research tools cannot sign it. Website edits cannot modify immutable metadata.

These observations do not choose an official mint or create a tradeable market, nor do they establish token ownership.

## Mint identity — not yet confirmed as the project mint

A historical whitepaper lists `JBaHDseUdFEVbAik7rojwC8ZZ8EjyBi1qQPoK9tLpump` as an unverified address, not a confirmed mint belonging to this project. Its on-chain mint is a distinct Solana token with **6 decimals** and a mint creation transaction dated **27 October 2024**, whereas older project documentation states **9 decimals** and a **29 March 2026** project launch. Another historic project note describes a separate million-unit mint. **No verified owner-to-mint link is available here**, so do not describe a mint as officially verified solely because it appears on this site.

A token display name, social account or a README cannot prove ownership or authority over a mint. Before publishing a trading link, verify a full mint address, creator wallet evidence, supply, decimals, metadata authorities, liquidity and relevant transactions from original blockchain records.

## Listing and roadmap status

- **CoinGecko:** Not submitted / لم يُقدَّم بعد.
- **CoinMarketCap:** Not submitted / لم يُقدَّم بعد.
- **Phase 1:** Incomplete; verifying the mint and ownership is required.
- **Phase 2:** Only after mint identity is approved; not currently underway.
- **Launch platform/date:** Not confirmed; older launch dates are historical draft claims.
- **Canonical status:** [VoltZilla/STATUS.md](https://github.com/itsAAA1/VoltZilla/blob/main/STATUS.md).

## Tokenomics

[Historical draft tokenomics](tokenomics.md) conflict with allocations shown in `VoltZilla/README.md`, its CoinGecko application draft and the live site's whitepaper. **No allocation is currently endorsed as verified.** Reconcile the original mint and on-chain flow before presenting percentages to buyers.

## Status of features

An X profile exists. Telegram and Discord have **not** been identified as official VoltZilla channels, so they are deliberately omitted. A generic DexScreener homepage is not evidence of a token-specific listing. Do not claim automated liquidity locking, guaranteed returns or verified market traction without underlying on-chain evidence.

This document does not request a transaction and does not make any changes to a Solana contract or wallet.
