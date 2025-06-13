# Interactive MIS Dashboard

This is an interactive Management Information System (MIS) dashboard built with Python and Streamlit. The dashboard provides real-time visualization of key business metrics including sales, revenue, customer count, and order statistics.

## Features

- Interactive date range selection
- Key performance metrics with trend indicators
- Sales and revenue trend analysis
- Customer and order analysis
- Summary statistics
- Raw data table view

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Dashboard

To run the dashboard, execute the following command in your terminal:
```bash
streamlit run app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`.

## Usage

1. Use the sidebar to select your desired date range
2. View the key metrics at the top of the dashboard
3. Explore the various charts and visualizations
4. Scroll down to view summary statistics and raw data

## Data

The dashboard currently uses sample data generated randomly. To use your own data, modify the `generate_sample_data()` function in `app.py` to load your data from a CSV file or database. 