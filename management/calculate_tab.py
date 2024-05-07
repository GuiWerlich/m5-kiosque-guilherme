from menu import products

def calculate_tab(consumption: list):
    subtotal = 0.0
    for item in consumption:
        product_id = item["_id"]
        for product in products:
            if product["_id"] == product_id:
                subtotal += product["price"] * item["amount"]
                
    return {"subtotal": round(subtotal, 2)}
        