from etl import read_csv, filter_not_delivered_products, sum_delivered_products


if __name__ == "__main__":
    path_name = "sell.csv"
    data = read_csv(path_name)
    delivered_products = filter_not_delivered_products(data)
    valor_produtos_entregues = sum_delivered_products(delivered_products)
    print(valor_produtos_entregues)