# MIS Dashboard

An interactive Management Information System (MIS) dashboard built with Python and Streamlit. This dashboard provides real-time visualization of key business metrics, including revenue collection, target achievements, and departmental performance indicators.

## Features

- **Interactive Filters**
  - Date Range Selection
  - Department Filter
  - ULB (Urban Local Body) Selection
  - DDR Filter
  - Denomination Options (Cr/Lac/Unit)

- **Key Performance Indicators (KPIs)**
  - Total Collection Overview
  - Target Achievement Tracking
  - Application Processing Status
  - SLA Achievement Metrics

- **Department-wise Analytics**
  - Property Tax Collection
  - Trade License Management
  - Complaints Tracking
  - MCollect Statistics
  - Fire NOC Status
  - Finance Overview

- **Visual Analytics**
  - Cumulative Collection Trends
  - Payment Mode Distribution
  - Usage Type Analysis
  - Performance Gauges
  - Progress Indicators

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the dashboard:
```bash
streamlit run app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

## Requirements

- Python 3.8+
- Streamlit
- Pandas
- Plotly
- NumPy

## Usage

1. Launch the dashboard using `streamlit run app.py`
2. Use the top filters to select:
   - Date Range
   - Department
   - ULB
   - DDR
   - Denomination
3. View KPIs and metrics in the cards
4. Explore interactive charts and visualizations
5. Monitor department-wise performance
6. Track progress using various indicators

## Project Structure

```
mis-dashboard/
│
├── app.py              # Main dashboard application
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with Streamlit
- Styled using KPMG design guidelines
- Inspired by municipal corporation dashboards 