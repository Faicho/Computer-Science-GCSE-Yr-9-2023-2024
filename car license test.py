age = int(input("Enter your age: "))
car = input("Do you own a car? (y/n)").upper()
license = input("Do you have a driving license? (y/n)").upper()

if age >= 17 and car == "Y" and license == "Y":
    print("You're good to hit the road!")
elif age < 17:
    print("You're going to have to wait")
elif car == "N":
    print("You're going to need some wheels quick")
elif license == "N":
    print("Better take that test.")