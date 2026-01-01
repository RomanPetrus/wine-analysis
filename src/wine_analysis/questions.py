import pandas as pd

# valid:  -> cleaned pd.DataFrame with non-null price & points

def corr_price_points(valid: pd.DataFrame, col: str = "price") -> float:
    """Calculate Pearson correlation between a given column and wine rating."""
    if col not in valid.columns:
        raise ValueError(f"Column '{col}' not found in DataFrame.")
    return float(valid[col].corr(valid["points"], method="pearson"))

def best_value(valid: pd.DataFrame) -> pd.Series:
    """Return the wine with the highest points-to-price ratio."""
    idx = valid["point_price"].idxmax()
    cols = ["title", "country", "price", "points", "point_price"]
    return valid.loc[idx, cols]

def top_by_points(valid: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Return top N wines sorted by rating (points),
    and then sorted by price (ascending)."""
    top = (valid.sort_values("points", ascending=False)
           .head(n)[["country", "title", "price", "points"]]
           .sort_values("price", na_position="last")
           .reset_index(drop=True))
    return top

def sweet_spot(valid: pd.DataFrame, min_point: int = 90, max_price: float = 30, n: int = 10) -> pd.DataFrame:
    """
    Select wines with high rating and reasonable price.
    Filters wines with at least `min_point` points
    and price lower than `max_price`.
    """
    cols = ["title", "country", "price", "points", "point_price"]
    spot = (valid.loc[(valid["points"] >= min_point) & (valid["price"] <= max_price), cols]
            .sort_values(["points", "point_price"], ascending = [False, False])
            .head(n)
            .reset_index(drop=True))
    return spot
    
