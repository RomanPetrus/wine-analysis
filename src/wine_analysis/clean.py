#from __future__ import annotations
import numpy as np
import pandas as pd

def make_valid(reviews: pd.DataFrame) -> pd.DataFrame:
    """Keep rows with non-null price/points, price > 0, and add helpful features."""
    valid = reviews.dropna(subset=["price", "points"]).copy()
    valid = valid[valid["price"] > 0].copy()
    valid["point_price"] = valid["points"] / valid["price"]
    valid["log_price"] = np.log10(valid["price"])
    return valid