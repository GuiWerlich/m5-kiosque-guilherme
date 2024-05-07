from menu import products

def get_product_by_id(_id: int):

    if not isinstance(_id, int):
        raise TypeError("product id must be an int")
    
    try:
        for product in products:
            if product["_id"] == _id:
                return product
    except TypeError:
        return "product id must be an int"
        
        
def get_product_by_type(type: str):

    if not isinstance(type, str):
        raise TypeError("product type must be a str")
    
    try:
        type_list = []
        for product in products:
            if product["type"] == type:
                type_list.append(product)
        return type_list
    except TypeError:
        return "product type must be a str"
    

def add_product(menu, **kwargs):
    products_list = menu

    if len(products_list) == 0:
        new_id = 1
    else:
        max_id = max(item['_id'] for item in products_list)
        new_id = max_id + 1
    
    kwargs['_id'] = new_id    
    products_list.append(kwargs)
    return kwargs


def menu_report():
    product_count = len(products)

    if product_count == 0:
        return "No products available"

    total_price = sum(product["price"] for product in products)
    average_price = total_price / product_count

    type_counts = {}
    for product in products:
        product_type = product["type"]
        type_counts[product_type] = type_counts.get(product_type, 0) + 1

    most_common_type = max(type_counts, key=type_counts.get)

    return f"Products Count: {product_count} - Average Price: ${average_price:.2f} - Most Common Type: {most_common_type}"