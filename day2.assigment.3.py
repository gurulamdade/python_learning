# print Glossary list 

Soybean_oil_name = "Star"
Soybean_oil_quantity = "2kg"
Soybean_oil_rate = 250

tea_powder_name = "Taj"
tea_powder_quantity = "1.5kg"
tea_powder_rate = "945"

Soap_name = "Moti"
Soap_quantity = 2
Soap_rate = 80
print("----------------Memory Refence Identification-----------------")
print("Soybean_oil_name = ",id(Soybean_oil_name))
print("Soybean_oil_quantity =",id(Soybean_oil_quantity))  
print("Soybean_oil_rate = ",id(Soybean_oil_rate))

print("----------------Type Identification-----------------")
print("Soybean_oil_name = ",type(Soybean_oil_name))
print("Soybean_oil_quantity =",type(Soybean_oil_quantity))  
print("Soybean_oil_rate = ",type(Soybean_oil_rate))

print("----------------Memory Refence Identification-----------------")
print("tea_powder_name = ",id(tea_powder_name))
print("tea_powder_quantity = ",id(tea_powder_quantity))
print("tea_powder_rate = ",id(tea_powder_rate))

print("----------------Type Identification-----------------")
print("tea_powder_name = ",type(tea_powder_name))
print("tea_powder_quantity = ",type(tea_powder_quantity))
print("tea_powder_rate = ",type(tea_powder_rate))

print("----------------Memory Refence Identification-----------------")
print("Soap_name = ",id(Soap_name))
print("Soap_quantity = ",id(Soap_quantity))
print("Soap_rate = ",id(Soap_rate))

print("----------------Type Identification-----------------")
print("Soap_name = ",type(Soap_name))
print("Soap_quantity = ",type(Soap_quantity))
print("Soap_rate = ",type(Soap_rate))
