fist = input()
second = input()
third = input()
if fist == second and fist == third:
    print(3)
elif fist==second or fist==third or second==third:
    print(2)
else:
    print(0)

