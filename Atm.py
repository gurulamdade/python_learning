balance = 15000
withdrawal_amount = int(input("Enter the amount to withdraw: "))
ac_type = "premium"  # Account type can be "normal" or "premium"

if withdrawal_amount<=balance:
    wid_limit = 10000
    wid_limit_premium = 20000
    if withdrawal_amount<=wid_limit and ac_type=="normal":
        print("transaction successful! Please collect your cash.")
    elif withdrawal_amount<=wid_limit_premium and ac_type=="premium":
        print("transaction successful! Please collect your cash.")
    else:
        print("Withdrawal amount exceeds the limit of 10000. ")
else:
    print("Insufficient balance! Please check your balance and try again.")
