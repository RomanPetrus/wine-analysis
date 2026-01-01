import pandas as pd
from wine_analysis.clean import make_valid
from wine_analysis import questions as q
import logging
from typing import Tuple
from wine_analysis.config import DATA_PATH, OUTPUT_DIR, TOP_N, MIN_POINTS, MAX_PRICE

# --- LOGGING ---
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)



# --- OUTPUT FUNCTION ---
def print_results(valid: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Print and Save key analytical results to console."""
    print("\n--- Best value wine ---")
    best_value = q.best_value(valid)
    print(best_value.to_string())
    
    print("\n--- Top wines by points ---")
    top = q.top_by_points(valid, n=TOP_N)
    print(top.to_string(index=False))
    
    print("\n--- Sweet spot (>=90  points & <=30 price) ---")
    sweet = q.sweet_spot(valid, min_point=MIN_POINTS, max_price=MAX_PRICE, n=TOP_N)
    print(sweet.to_string(index=False))    
    return top, sweet
    

def main() -> None:
    logger.info("Starting wine analysis")  
    logger.info("Loading dataset")
    reviews = pd.read_csv(DATA_PATH, index_col=0)
    
    logger.info("Cleaning data")
    valid = make_valid(reviews)    
    logger.info("Total rows: %d", len(reviews))
    logger.info("Valid rows: %d", len(valid))
    
    logger.info("Computing correlations")
    logger.info("corr(price vs points): %.3f", q.corr_price_points(valid))
    logger.info("corr(log_price vs points): %.3f", q.corr_price_points(valid, col="log_price"))
    
    logger.info("Saving results")
    top, sweet = print_results(valid)
    top.to_csv(OUTPUT_DIR / "top5_by_points.csv", index=False)
    sweet.to_csv(OUTPUT_DIR / "sweet_spot.csv", index=False) 

if __name__ == "__main__":
    main()

    