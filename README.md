# Quantium Data Analytics Virtual Experience

A Python data analytics project built as part of the Quantium Virtual Experience Program. This project processes Soul Foods Pink Morsel sales data, builds an interactive Dash visualisation, and includes an automated test suite with CI-ready bash script.

---

## Project Structure

```
quantium-starter-repo/
├── app.py                    # Dash web application
├── data3.py                  # Data processing script
├── pink_morsel_sales.csv     # Processed output data
├── requirements.txt          # Python dependencies
├── run_tests.sh              # CI bash script to run test suite
├── assets/
│   └── style.css             # Custom styling for Dash app
├── data/
│   ├── daily_sales_data_0.csv
│   ├── daily_sales_data_1.csv
│   └── daily_sales_data_2.csv
└── test/
    └── test_app.py           # Pytest test suite
```

---

## Tasks Completed

### Task 1 — Environment Setup
- Forked and cloned the starter repository
- Created a Python 3.9 virtual environment
- Installed `dash`, `pandas`, and `dash[testing]` dependencies
- Committed `requirements.txt` to the repository

### Task 2 — Data Processing
- Read three CSV files from the `data/` folder containing Soul Foods transaction data
- Filtered rows to keep only **Pink Morsel** products
- Computed `Sales = quantity × price`, cleaning `$` symbols from price values
- Retained only `Sales`, `Date`, and `Region` columns
- Merged all three CSVs into a single output file: `pink_morsel_sales.csv`

### Task 3 — Dash Visualisation
- Built an interactive Dash web app (`app.py`) to visualise Pink Morsel sales over time
- Includes a line chart sorted by date with labelled axes
- A red dashed vertical line marks the **15 January 2021 price increase** so the before/after trend is visually obvious
- A header clearly titles the visualiser

### Task 4 — Region Filter + Styling
- Added a `dcc.RadioItems` region picker with five options: **All, North, East, South, West**
- Selecting a region filters the line chart to show only that region's data
- Custom CSS styling applied via `assets/style.css`

### Task 5 — Automated Test Suite
- Created `test/test_app.py` with three Pytest tests:
  - `test_header_present` — verifies the app header is present
  - `test_visualisation_present` — verifies the line chart is present
  - `test_region_picker_present` — verifies the region picker is present

### Task 6 — CI Bash Script
- Created `run_tests.sh` to automate test execution in a CI environment
- Script activates the virtual environment, runs Pytest, and returns exit code `0` on success or `1` on failure

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/GaneshMahanti/quantium-starter-repo.git
cd quantium-starter-repo
```

### 2. Create and activate a virtual environment

```bash
python3.9 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install "dash[testing]"
```

### 4. Process the data

```bash
python data3.py
```

This generates `pink_morsel_sales.csv`.

### 5. Run the Dash app

```bash
python app.py
```

Open your browser at `http://127.0.0.1:8050/`.

---

## Running Tests

```bash
python -m pytest test/test_app.py -v
```

Or using the CI bash script:

```bash
./run_tests.sh
```

---

## Business Question Answered

**"Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?"**

The line chart in the Dash app makes this immediately visible. The red dashed vertical line marks the date of the price change, and the sales trend on either side answers the question at a glance.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.9 | Core language |
| pandas | Data processing |
| Dash | Web application framework |
| Plotly Express | Interactive charts |
| Pytest | Test automation |
| Bash | CI scripting |

---

## Author

**Ganesh Mahanti**  
BTech CSE | Junior Software Engineer  
[GitHub](https://github.com/GaneshMahanti)
