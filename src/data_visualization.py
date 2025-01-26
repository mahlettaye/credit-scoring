import matplotlib.pyplot as plt
import seaborn as sns

def plot_missing_values(data):
    """Visualizes missing values in the dataset."""
    plt.figure(figsize=(10, 6))
    sns.heatmap(data.isnull(), cbar=False, cmap="viridis")
    plt.title("Missing Values Heatmap")
    plt.show()

def plot_numeric_distributions(data, numeric_columns):
    """Plots histograms for numeric columns."""
    data[numeric_columns].hist(figsize=(15, 10), bins=20)
    plt.suptitle("Numeric Feature Distributions")
    plt.show()

def plot_categorical_distributions(data, categorical_columns):
    """Plots bar charts for categorical columns."""
    for col in categorical_columns:
        plt.figure(figsize=(8, 4))
        data[col].value_counts().plot(kind='bar')
        plt.title(f"Distribution of {col}")
        plt.show()

def plot_outliers(df, numeric_columns):
    """
    Creates boxplots to visualize outliers in numeric columns.
    """


    for column in numeric_columns:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=df[column])
        plt.title(f"Boxplot of {column}")
        plt.show()

def plot_correlation_heatmap(df, numeric_columns):
    """
    Plots a correlation heatmap for numeric columns.
    """


    correlation_matrix = df[numeric_columns].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()