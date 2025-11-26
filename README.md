# Python Data Helper
A modular Python package offering tools for data processing, analytics, and visualization.
---

## 📘 Project Contribution Guide

Thank you for checking out this project!  
If you'd like to contribute, please follow these simple steps:

1. **Fork** the repository to your own GitHub account.  
2. **Create a new branch** for your feature or fix.  
3. **Make your changes** clearly and commit them.  
4. **Open a Pull Request** describing what you improved.

💡 Every small contribution helps improve this project for everyone!

---
---

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Module Documentation](#module-documentation)
- [Usage Examples](#usage-examples)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- **Data Loading**: Easy-to-use functions for loading data from various file formats (CSV, JSON, Excel)
- **Data Cleaning**: Utility functions for cleaning and preprocessing text and data
- **Data Summarization**: Statistical summary generation with comprehensive analytics
- **Modular Design**: Well-organized modules for different data processing tasks
- **Fully Documented**: Comprehensive docstrings and usage examples

---

## 📦 Installation

### Install from Source

```bash
# Clone the repository
git clone https://github.com/ai-pythonworks/python-data-helper.git

# Navigate to the project directory
cd python-data-helper

# Install in development mode
pip install -e .
```

---

## 🚀 Quick Start

```python
# Import the modules
from src.io.loader import load_csv
from src.core.summary import summarize
from src.utils.cleaner import clean_text

# Load data from a CSV file
data = load_csv('path/to/your/data.csv')

# Generate statistical summary
summary_stats = summarize(data)
print(summary_stats)

# Clean text data
cleaned_text = clean_text('  Hello World  ')
print(cleaned_text)  # Output: 'Hello World'
```

---

## 📚 Module Documentation

### `src.io.loader`
Handles data loading operations from various file formats.

**Functions:**
- `load_csv(path)`: Load data from CSV files
  - **Parameters**: `path` (str) - File path to the CSV file
  - **Returns**: pandas DataFrame containing the loaded data
  - **Raises**: FileNotFoundError, PermissionError, ParserError

### `src.core.summary`
Provides statistical analysis and summary generation.

**Functions:**
- `summarize(data)`: Generate comprehensive statistical summaries
  - **Parameters**: `data` - pandas DataFrame or array containing numerical data
  - **Returns**: Dictionary with statistical metrics (mean, median, mode, std, min, max, quartiles)
  - **Raises**: ValueError, TypeError

### `src.utils.cleaner`
Utility functions for data cleaning and preprocessing.

**Functions:**
- `clean_text(text)`: Clean and normalize text by removing whitespace
  - **Parameters**: `text` (str) - Input text string
  - **Returns**: Cleaned text with leading/trailing whitespace removed

---

## 💡 Usage Examples

### Example 1: Loading and Analyzing Data

```python
from src.io.loader import load_csv
from src.core.summary import summarize

# Load sales data
sales_data = load_csv('data/sales.csv')

# Get statistical summary
stats = summarize(sales_data)

# Print results
print(f"Mean: {stats['mean']}")
print(f"Median: {stats['median']}")
print(f"Standard Deviation: {stats['std']}")
```

### Example 2: Text Cleaning

```python
from src.utils.cleaner import clean_text

# Clean messy text data
raw_text = "  Python Programming  \n\t"
cleaned = clean_text(raw_text)
print(cleaned)  # Output: 'Python Programming'
```

---

## 🔧 Requirements

- Python 3.7+
- pandas >= 1.0.0
- numpy >= 1.18.0

---



## 📄 MIT License (Explained)

This project is licensed under the **MIT License**, which means:

- You can freely use the code  
- Modify it  
- Distribute it  
- Even use it in commercial projects  

as long as you include the original MIT License notice.

The MIT License is one of the most permissive open-source licenses, encouraging wide usage and contribution.

---
## License

This project is licensed under the **Apache License 2.0**.

The Apache 2.0 License allows:

- Free use of the software  
- Modification and redistribution  
- Commercial usage  

as long as you:

- Include a copy of the Apache 2.0 License  
- Provide proper attribution to the original authors  
- Clearly state any modifications  

Full license text:  
👉 https://www.apache.org/licenses/LICENSE-2.0

This improves clarity and aligns the README with standard open-source documentation practices.
