from pathlib import Path

BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / "log"

for _dir in [LOG_DIR]:
    _dir.mkdir(parents=True, exist_ok=True)