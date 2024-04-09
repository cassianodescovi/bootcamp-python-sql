# Class 06: ETL with Pandas, JSON, and Parquet

## Welcome to Class 06

In this session of our Python and SQL Bootcamp, we dive into creating an ETL (Extract, Transform, Load) process using Python functions. This class will guide you through using Pandas to manipulate data, focusing on extracting information from JSON files, transforming this data based on specific requirements, and loading the transformed data into Parquet files for efficient querying and storage.

## Project Structure

- **data/**: Contains sample JSON files with sales data to be processed.
- **etl.py**: Includes the functions required for executing the ETL steps.
- **pipeline.py**: A script to run the `sales_kpi_pipeline` function, showcasing the entire ETL process.

## Getting Started

### Step 1: Clone the Repository

Begin by cloning this repository to your local machine to access the project files.

### Step 2: Install Dependencies

This project uses Poetry for managing dependencies. If you haven't installed Poetry yet, please follow the [official installation guide](https://python-poetry.org/docs/#installation).

Once Poetry is installed, run the following command in the project's root directory to install the necessary Python packages:

`poetry install`

### Step 3 Execute the ETL Pipeline

With all dependencies in place, you're ready to run the ETL process. Execute the pipeline.py script using Poetry to see the ETL in action:

`poetry run python pipeline.py`

This command processes the JSON data in the `data/` directory, calculates sales KPIs, and outputs the results to both CSV and Parquet files.

What You Will Learn
- The fundamentals of ETL processes and their significance in data analytics.
- How to perform data extraction from JSON files using Pandas.
- Techniques for data transformation, including KPI calculation.
- Saving transformed data in CSV and Parquet formats for downstream use.

### Explore Further

Feel encouraged to enhance the existing ETL pipeline with additional data transformations or by incorporating more complex KPIs. Explore the vast functionality offered by Pandas for data manipulation and consider working with different data formats to broaden your data processing skills.

Happy coding and data exploring!