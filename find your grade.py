print("Welcome to Grade Finder")
mark = int(input("Write your mark? "))
if mark >= 90 :
    print("You passed your exam with full A's ")
elif mark>= 75 :
    print("You passed your exam with all B's ")
elif mark >= 50 :
    print("You passed your exam with all C's ")
else :
    print("You failed your exam")