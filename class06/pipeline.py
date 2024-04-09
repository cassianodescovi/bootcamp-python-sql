from etl import sales_kpi_pipeline

path: str = 'data'
output_formats: list = ['csv']

sales_kpi_pipeline(path, output_formats)