"""Fail closed on outdated public token documentation claims."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
readme = (ROOT / "README.md").read_text(encoding="utf-8")
tokenomics = (ROOT / "tokenomics.md").read_text(encoding="utf-8")

assert "https://x.com/voltzillasol1" in readme
assert "https://x.com/voltzillasol1" in tokenomics
assert "Not submitted / لم يُقدَّم بعد" in readme, "Listing status must be unsubmitted"
assert "not been submitted" in tokenomics, "Historical draft needs listing disclaimer"
assert "not a confirmed mint belonging to this project" in readme, "Mint disclaimer missing"
assert "DHxStA9nRq6DdhBKT89s38fpxD9wE7MtyMn9HMuWeyN9" in readme and "DHxStA9nRq6DdhBKT89s38fpxD9wE7MtyMn9HMuWeyN9" in tokenomics, "Owner-reported mint is missing"
assert "Mint authority remains active" in readme and "Mint authority remains active" in tokenomics, "Mint risk flag missing"
assert "These were conflicting proposals" in tokenomics, "Historical allocations disclaimer missing"
for text in (readme, tokenomics):
    assert "https://t.me/" not in text and "discord.gg/" not in text, "Unofficial social link"
    assert "returns are guaranteed" not in text.lower(), "Unsupported positive guarantee"
assert "no built-in transfer-fee extension" in readme, "SPL fee clarification missing"
assert "does **not** mean the token or project is cancelled" in tokenomics, "Freeze authority must not be described as token cancellation"
assert "27 October 2024" in readme, "Historical Pump.fun mint date missing"
print("OK: VoltZilla token documentation checks passed")

# Current canonical tokenomics must refer to the creator's actual deployed token,
# not to stale million-token SPL and 40/30/20/10 proposed allocations.
live_path = ROOT / "CURRENT_ONCHAIN.md"
assert live_path.is_file(), "Primary minted token supply/holders and Pump mode need a separate current document"
live = live_path.read_text(encoding="utf-8")
PRIMARY = "GDYcemcZozG9ijhEZioRLRgNMtoxh1BBuV7nvdf1pump"
CREATOR = "GGSqpEPw3WDvfqJRj6frvrTz1C2wcUz28Sgfdg2NNJiD"
for required in (PRIMARY, CREATOR, "Token-2022", "1,007,005,921.840554",
                 "1,000,000,000", "7,005,921.840554", "Mayhem", "Cashback",
                 "99.30428196%", "0.69571804%", "not yet cryptographically proven"):
    assert required in live, "Current tokenomics missing exact observed state: " + required
assert "[CURRENT_ONCHAIN.md](CURRENT_ONCHAIN.md)" in readme, "README must link to current canonical tokenomics"
assert "historical-only" in readme, "README should explicitly mark stale technical paragraphs as historical-only"
assert "40% community" not in live.lower(), "Unexecuted historical allocations are not current tokenomics"
