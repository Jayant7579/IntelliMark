# Weekly Sales Forecasting Project

## Overview
This project analyzes and forecasts weekly sales quantities for a specific product (or set of products) using historical data. The workflow is split into two Jupyter Notebooks:
- **EDA.ipynb**: Exploratory Data Analysis
- **Modeling_and_Forecasting.ipynb**: Model building, validation, and forecasting

## Data
- Place the provided dataset (e.g., `Assessment-2-Associate-DS(in).csv`) in the `data/` directory.
- The dataset should have columns: `weekend_date`, `channel`, `brand`, `category`, `sub_category`, `SerialNum`, `quantity`.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Open and run the notebooks in the `notebooks/` directory.

## Notebooks
- **EDA.ipynb**: Load and inspect data, visualize trends, check for anomalies, and summarize initial insights.
- **Modeling_and_Forecasting.ipynb**: Prepare data, build and validate a forecasting model, report monthly accuracy for Jun-Jul-Aug 2024, and forecast for Sep-Nov 2024.

## Outputs
- Model objects are saved in the `models/` directory for reproducibility.
- Forecast results and accuracy metrics are displayed in the modeling notebook.

## Notes
- Ensure the data file is present in the `data/` folder before running the notebooks.
- Update file paths in the notebooks if your directory structure differs.

