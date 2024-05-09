from menu import products

def get_product_by_id(_id: int):

    if not type(_id) == int:
        raise TypeError("product id must be an int")
    
    try:
        for product in products:
            if product["_id"] == _id:
                return product
        return {}        
    except TypeError:
        return "product id must be an int"
        
        
def get_products_by_type(type: str):

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
    
    if len(menu) == 0:
        new_id = 1
    else:
        max_id = max(item['_id'] for item in menu)
        new_id = max_id + 1
    
    kwargs['_id'] = new_id
    menu.append(kwargs)
    
    return kwargs


def menu_report():
    product_count = len(products)

    total_price = sum(product["price"] for product in products)
    average_price = total_price / product_count

    type_counts = {}

    for product in products:
        product_type = product["type"]
        
        if product_type in type_counts:
            type_counts[product_type] += 1
        else:
            type_counts[product_type] = 1

    most_common_type = None
    max_count = 0

    for product_type, count in type_counts.items():
        if count > max_count:
            max_count = count
            most_common_type = product_type

    return f"Products Count: {product_count} - Average Price: ${average_price:.1f} - Most Common Type: {most_common_type}"