money = 50

while money > 0:
    print("Amount Due:", money)
    inmoney = int(input("Inset Coin: "))
    if inmoney in [5, 10, 25]:
        money -= inmoney
positive = abs(money)
print("Change Owed:", positive)



# while True:
#     inmoney = int(input("Inset Coin: "))
#     if inmoney in [5, 10, 25]:
#         money -= inmoney
#         if money > 0:
#             print("Amount Due:", money)
#             continue
#         elif money == 0:
#             print("Change Owed:", money)
#             break
#         else:
#             money = money * (-1)
#             print("Change Owed:", money)
#             break
#     else:
#         print("Amount Due:", money)
