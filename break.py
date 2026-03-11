# for num in range (1,21):
#     tbl = 5 * num
#     if num == 10:
#         print(f"atacha count:{num}")
#         break
#     if tbl == 30:
#         print("30 skiped") 
#         continue
#     print(tbl)
# print("Outside for loop")    
 
qty = 0
loop=0
for color in ["red", "yellow", "white" , "pink", "red" , "white", "blue", "pink", "green" , "red"]:
    loop +=1
    qty = 0
    if qty == 7:
        break
    if color == "white":
        print("white nako")
        continue
    qty = qty+1
    print(f"load kel. \nTotal Poti : {qty}  ->loops {loop}")