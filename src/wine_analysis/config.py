from pathlib import Path

# --- PATHS ---
PROJECT_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_DIR / "data" / "winemag-data-130k-v2.csv"
OUTPUT_DIR = PROJECT_DIR/"outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# --- PARAMETERS ---
TOP_N = 5
MIN_POINTS = 90
MAX_PRICE = 30