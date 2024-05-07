from management.product_handler import get_product_by_id, get_product_by_type, add_product, menu_report
from management.calculate_tab import calculate_tab
from menu import products

if __name__ == "__main__":

    print (get_product_by_id(1))
    print(get_product_by_type("fruit"))

    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }

    print(add_product(products, **new_product))
    print(add_product([], **new_product))

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))

    print(menu_report())