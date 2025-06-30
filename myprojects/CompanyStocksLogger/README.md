# Company Stocks Logger

A simple GUI-based Python application to log company stock purchases. It collects:
- Company name
- Purchase date
- Number of shares

The data is saved to:
- `company-stocks.csv`
- `company-stocks.xlsx` (automatically converted using pandas)

## Requirements
- Python 3.x
- pandas
- openpyxl

## Setup
1. Clone/download this repo
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Run the app
```
python main.py
```

## Features
- GUI with input validation
- CSV and Excel export
- Clean, minimal interface
