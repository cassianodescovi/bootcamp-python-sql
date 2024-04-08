import csv

def read_csv(file_csv: str) -> list[dict]:
    """Read data from a CSV file into a list of dictionaries.

    Args:
        file_csv (str): The path to the CSV file.

    Returns:
        list[dict]: A list of dictionaries, where each dictionary represents a row from the CSV file.
    """
    data = []    
    with open(file_csv, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            data.append(line)
    return data

def filter_not_delivered_products(data: list[dict]) -> list[dict]:
    """Filter out products that have not been delivered from the data list.

    Args:
        data (list[dict]): List of dictionaries, each representing a product with its delivery status.

    Returns:
        list[dict]: A list of dictionaries for products that have been delivered.
    """
    products_filtered = []
    for product in data:
        if product.get("delivery") == 'True':
            products_filtered.append(product)
    return products_filtered

def sum_delivered_products(products_filtered: list[dict]) -> int:
    """Calculate the total price of all delivered products.

    Args:
        products_filtered (list[dict]): List of dictionaries for delivered products, each containing a price.

    Returns:
        int: The total price of all delivered products.
    """
    total = 0
    for product in products_filtered:
        total += int(product.get("price"))
    return total
