"""Fail closed when VZLA docs accidentally substitute old mints or invented allocations."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
readme=(ROOT/"README.md").read_text(encoding="utf-8")
live=(ROOT/"CURRENT_ONCHAIN.md").read_text(encoding="utf-8")
history=(ROOT/"tokenomics.md").read_text(encoding="utf-8")
PRIMARY="GDYcemcZozG9ijhEZioRLRgNMtoxh1BBuV7nvdf1pump"
CREATOR="GGSqpEPw3WDvfqJRj6frvrTz1C2wcUz28Sgfdg2NNJiD"
for name,text in (("README",readme),("CURRENT_ONCHAIN",live),("history",history)):
    assert PRIMARY in text and CREATOR in text, f"{name}: must name creator-matched original GDY token"
    assert "1,007,005,921.840554" in text, f"{name}: supply from canonical snapshot missing"
    assert "https://t.me/" not in text and "discord.gg/" not in text, f"{name}: unverified social account"
    assert "returns are guaranteed" not in text.lower(), f"{name}: illegal performance promise"
for phrase in ("Token-2022", "1,000,000,000", "7,005,921.840554", "Mayhem", "Cashback",
               "99.30428196%", "0.69571804%", "not yet cryptographically proven"):
    assert phrase in live, "Current tokenomics missing actual chain evidence: " + phrase
for phrase in ("40%", "30%", "20%", "10%", "historical-only",
               "These", "historical")[:5]:
    assert phrase in history, "Historical proposed allocation insufficiently labelled: " + phrase
assert "| Community airdrop/rewards | 40% |" not in live, "Unexecuted planned allocation must not be displayed as an active tokenomics table"
assert "[CURRENT_ONCHAIN.md](CURRENT_ONCHAIN.md)" in readme, "README must link to primary current tokenomics"
assert "historical-only" in readme, "README must distinguish stale technical notes"
assert "Not submitted / لم يُقدَّم بعد" in readme, "Do not announce a listing that was not approved"
assert "Mint authority" in readme or "mint authority" in readme, "Must document known authority risk"
assert "different token" in readme.lower(), "Must distinguish old million supply"
assert "Token-2022" in readme and "6" in readme, "Correct chain program and decimals required"
assert "Cashback" in readme, "Actual deployed launch mode must be disclosed"
print("OK: canonical GDY tokenomics, historical archives and public claims consistent")
