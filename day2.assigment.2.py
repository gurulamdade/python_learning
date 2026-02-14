# print your bank account details

account_holder_name = "guru"
account_number = 2200003340
IFSC_CODE = "IPOS0000001"
branch_name = "miraj"
account_balance = 100000000.000
interest_rate = 7.2

print("---------Memory Reference identification------")

print("account_holder_name=",id(account_holder_name))   
print("account_number=",id(account_number))
print("IFSC_CODE=",id(IFSC_CODE))
print("branch_name=",id(branch_name))
print("account_balance=",id(account_balance))
print("interest_rate=",id(interest_rate))

print("-----------------------------------------------------------------")


print("---------Type identification---------------")

print("Type of account_holder_name:",type(account_holder_name))
print("Type of account_number:",type(account_number))
print("Type of IFSC_CODE:",type(IFSC_CODE))
print("Type of branch_name:",type(branch_name))
print("Type of account_balance:",type(account_balance))
print("Type of interest_rate:",type(interest_rate))