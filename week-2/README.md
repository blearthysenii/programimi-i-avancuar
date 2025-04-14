# Data Analysis Tool

This is a simple data analysis tool written in Python that can perform basic statistical analysis on a given CSV file. It provides functionalities to calculate descriptive statistics, generate histograms, find correlations between columns, and identify outliers using Z-scores.

## Features

1. **Statistics Calculation**: Computes and displays mean, median, mode, standard deviation, minimum, maximum, and number of unique values of a specified column.
2. **Histogram Generation**: Generates a text-based histogram to visually represent the distribution of data in a specified column.
3. **Correlation Analysis**: Computes the Pearson correlation coefficient between two specified columns and provides a qualitative assessment of the correlation strength (strong positive, strong negative, etc.).
4. **Outlier Detection**: Identifies and lists outliers in a specified column based on a Z-score threshold.

## Requirements

- Python 3.x
- Pandas
- NumPy
- SciPy

You can install the required dependencies using `pip`:

```bash
pip install pandas numpy scipy
```

## How to Run the Project

To run this project, use the following commands in the terminal:

1. **Calculate Basic Statistics**:
   To calculate and display basic statistics (mean, median, mode, etc.) for a column (e.g., `temperature`):

   ```bash
   python data_analysis.py sample_data.csv stats temperature
   python data_analysis.py sample_data.csv histogram humidity 10
   python data_analysis.py sample_data.csv correlation temperature humidity
   python data_analysis.py sample_data.csv outliers wind_speed 2.0
   ```
## Sample output

Statistics for 'temperature':
  - Mean: 25.81
  - Median: 25.10
  - Mode: 23.9
  - Standard Deviation: 2.33
  - Min: 23.9
  - Max: 32.1
  - Number of Unique Values: 10


Histogram for 'humidity' (Bin Edges):
  - 55.00 - 57.00: #
  - 57.00 - 59.00: 
  - 59.00 - 61.00: #
  - 61.00 - 63.00: #
  - 63.00 - 65.00: #
  - 65.00 - 67.00: ##
  - 67.00 - 69.00: #
  - 69.00 - 71.00: ##
  - 71.00 - 73.00:
  - 73.00 - 75.00: #

Bin Edges: [55. 57. 59. 61. 63. 65. 67. 69. 71. 73. 75.]


Correlation between 'temperature' and 'humidity':
  - Correlation Coefficient: -0.82
  - Correlation Type: Strong Negative Correlation


Outliers in 'wind_speed' (Z-score threshold = 2.0):
  - Number of Outliers: 1
  - Outlier Data: 
    Index 9 | Wind Speed: 22


## Contributing
I worked on this project in collaboration with my friend Redon Berisha.
