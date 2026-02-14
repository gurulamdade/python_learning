name="lux"
qty=5
price=5


print("---------Memory Reference identification------")
print("name=",id(name))
print("qty=",id(qty))
print("price=",id(price))
print("------------------------")
print("bill=",qty * price)
print("price=",id(qty * price))

print("---------Type identification---------------")
print("name=",type(name))
print("qty=",type(qty))
print("price=",type(price))
print("------------------------")