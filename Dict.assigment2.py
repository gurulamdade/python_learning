product = {
            "product_id": "P101",
            "name": "wireless Headphones",
            "price": 2999,
            "brand": "Sony",
            "stock": 50,
            "specifications" : {
                "color": "Black",
                "battery": "20 hours",
                "warranty": "1 year"

            }
}

print(product["price"])
print("")

print(product["specifications"]["battery"])
print("")


product["stock"] = 40
print(product)
print("")


product["specifications"]["color"] = "Blue"
print(product)  
print("")


product["discount"] = "8%"
print(product)
print("")


product["specifications"]["Bluetoot version "] = "5.3"
print(product)
print("")


del product["specifications"]["warranty"]    
print(product)
print("")
