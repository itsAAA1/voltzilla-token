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
assert "These were conflicting proposals" in tokenomics, "Historical allocations disclaimer missing"
for text in (readme, tokenomics):
    assert "https://t.me/" not in text and "discord.gg/" not in text, "Unofficial social link"
    assert "guaranteed returns" not in text.lower(), "Unverified returns claim"
print("OK: VoltZilla token documentation checks passed")
