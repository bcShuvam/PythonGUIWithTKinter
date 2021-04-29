row = int(input("Enter the number of rows : "))

# i=0
for i in range(row):
    print(" " * (row-i) + " *" * (i+1)) # row=5 i=0 row-5=5-1=4

for j in range(row-1):
    print(" " * (j+2) + " *" * (row-1-j))

# Practice
# while True:
#     user_input = int(input("press 1 for square pattern OR press 2 for rectangular pattern OR Press 0 to exit\n: "))
#     if user_input == 0:
#         print("************ The end ************")
#         break
#     sqrow = int(input("Enter number of rows : "))
#     # sqcol = int(input("Enter number of columns : "))
#     if user_input == 1:
#         print("\nThis is a square pattern.")
#         for i in range(sqrow):
#             print("* " * sqrow)
#         print()
#     elif user_input == 2:
#         print("\nThis is a rectangular pattern.")
#         for i in range(sqrow):
#             print("* " * sqrow*3)
#         print()
#     else:
#         print("Wrong Input , Please select an an option as given below.\n")