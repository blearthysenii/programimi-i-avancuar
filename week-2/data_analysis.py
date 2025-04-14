import argparse
import pandas as pd
import numpy as np
from scipy import stats

def read_csv(file_path):
    """Read CSV file and return DataFrame."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        exit(1)

def calculate_stats(df, column):
    """Calculate and display basic statistics for a given column."""
    if column not in df.columns:
        print(f"Column '{column}' not found in the file.")
        exit(1)
    
    data = df[column].dropna()
    mean = np.mean(data)
    median = np.median(data)
    mode_result = stats.mode(data)[0]
    mode = mode_result[0] if isinstance(mode_result, np.ndarray) and len(mode_result) > 0 else mode_result
    std_dev = np.std(data, ddof=1)
    min_value = np.min(data)
    max_value = np.max(data)
    unique_values = len(data.unique())
    
    print(f"Statistics for {column}:")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {std_dev:.2f}")
    print(f"Min: {min_value}")
    print(f"Max: {max_value}")
    print(f"Number of Unique Values: {unique_values}")

def generate_histogram(df, column, bins):
    """Generate a simple text-based histogram."""
    if column not in df.columns:
        print(f"Column '{column}' not found in the file.")
        exit(1)
    
    data = df[column].dropna()
    hist, bin_edges = np.histogram(data, bins=bins)
    
    print(f"Histogram for {column} (Bin Edges):")
    for i in range(len(hist)):
        print(f"{bin_edges[i]:.2f} - {bin_edges[i+1]:.2f}: {'#' * hist[i]}")
    print(f"Bin edges: {bin_edges}")

def find_correlation(df, col1, col2):
    """Find and display correlation between two columns."""
    if col1 not in df.columns or col2 not in df.columns:
        print("One or both columns not found in the file.")
        exit(1)
    
    data1 = df[col1].dropna()
    data2 = df[col2].dropna()
    min_len = min(len(data1), len(data2))
    correlation = np.corrcoef(data1[:min_len], data2[:min_len])[0, 1]
    
    correlation_type = "No correlation"
    if correlation > 0.7:
        correlation_type = "Strong positive correlation"
    elif correlation < -0.7:
        correlation_type = "Strong negative correlation"
    elif correlation > 0:
        correlation_type = "Positive correlation"
    elif correlation < 0:
        correlation_type = "Negative correlation"
    
    print(f"Correlation between {col1} and {col2}: {correlation:.2f}")
    print(f"Correlation type: {correlation_type}")

def identify_outliers(df, column, threshold):
    """Identify and display outliers in a column based on Z-score."""
    if column not in df.columns:
        print(f"Column '{column}' not found in the file.")
        exit(1)
    
    data = df[column].dropna()
    z_scores = np.abs(stats.zscore(data))
    outliers = data[z_scores > threshold]
    
    print(f"Outliers in {column} (threshold {threshold}):")
    print(f"Number of outliers: {len(outliers)}")
    print(outliers)

def main():
    parser = argparse.ArgumentParser(description="Data Analysis Tool")
    parser.add_argument("file", help="Path to the CSV file")
    parser.add_argument("command", choices=["stats", "histogram", "correlation", "outliers"], help="Operation to perform")
    parser.add_argument("column1", help="Primary column")
    parser.add_argument("column2", nargs="?", help="Secondary column (for correlation)")
    parser.add_argument("--bins", type=int, default=10, help="Number of bins for histogram")
    parser.add_argument("--threshold", type=float, default=2.0, help="Z-score threshold for outliers")
    
    args = parser.parse_args()
    df = read_csv(args.file)
    
    if args.command == "stats":
        calculate_stats(df, args.column1)
    elif args.command == "histogram":
        generate_histogram(df, args.column1, args.bins)
    elif args.command == "correlation":
        if not args.column2:
            print("Correlation requires two columns.")
            exit(1)
        find_correlation(df, args.column1, args.column2)
    elif args.command == "outliers":
        identify_outliers(df, args.column1, args.threshold)
    
if __name__ == "__main__":
    main()
