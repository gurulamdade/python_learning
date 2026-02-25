employe = {
            "emp_id": 101,
            "name": "Guru", 
            "department": "IT",
            "salary": 50000
            }

print(employe["name"])
print(employe.get("department"))
print("")

employe["location"] = "Mumbai"
print(employe)
employe.update({"salary":60000})
print(employe)
print("")

print(employe.keys())
print(employe.values())
print(employe.items())
print("")

print(len(employe))

employe.pop("location")
print(employe)

employe_copy = employe.copy()
print(employe_copy)

employe.clear()
print(employe)
