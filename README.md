Wine Quality Analysis
=====================

This project explores relationships between wine price, quality (points),
and value for money using a structured and reproducible Python workflow.

The goal is to demonstrate clean data processing, analysis logic,
and clear project organization.

## Project structure

wine-analysis/
│
├── README.md                         # Project description and usage
│
├── data/
│   └── winemag-data-130k-v2.csv      # Raw dataset (unchanged)
│
├── src/
│   ├── wine_analysis.py              # Main runner script (entry point)
│   │
│   └── wine_analysis/
│       ├── __init__.py               # Marks this folder as a Python package
│       ├── config.py                 # Central configuration (paths, constants)
│       ├── clean.py                  # Data cleaning & feature engineering
│       └── questions.py              # Analytical functions (metrics, queries)
│
├── notebook/
│   └── wine_analysis.ipynb           # Exploratory analysis & visualization
│
├── outputs/
│   ├── top5_by_points.csv            # Top wines by rating
│   └── sweet_spot.csv                # Best value wines
│
└── .gitignore                        # Files/folders excluded from Git

How to Run
----------
From the project root directory:

    python src/wine_analysis.py


What the script does
--------------------
- Loads the wine dataset
- Cleans invalid data (missing values, zero prices)
- Computes:
  - correlation between price and rating
  - best value wines
  - top-rated wines
  - “sweet spot” wines (high rating, reasonable price)
- Saves results into the `outputs/` folder


Key Ideas
---------
- Clean separation between logic and execution
- Reusable analysis functions
- Reproducible results
- Minimal but readable structure


Notes
-----
This project is designed as a portfolio example
showing data analysis workflow and clean Python structure.


Author
------
Created by Roman Petrus
