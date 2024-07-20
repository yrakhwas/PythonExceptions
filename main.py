# age =0
# try:
#     name = input("Enter your name : ")
#     age = int(input("Enter your age : "))
#     if type(age) !=int:
#         raise ValueError("This is block raise ValueError")
#     phoneNumber = int(input("Enter your phone number : "))
#     if phoneNumber <0:
#         raise ZeroDivisionError
# except (ZeroDivisionError):
#     print("Invalid phone number")
# except ValueError as mass:
#     print(str(mass))    
# except:
#     print("Invalid input")
# else:
#     print("This is block else")
# finally:
#     print("Thank you for using our service")


# print(f"Name : {name} Age : {age}")

def dividing(a,b):
    return a/b

def dividingV2(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Second value cann`t be zero"
    except:
        return "Invalid input"

print(dividingV2(10,0))
# try:
#     a = int(input("Enter first number : "))
#     b = int(input("Enter second number : "))
#     print(dividing(a,b))
# except ZeroDivisionError:
#     print("Second value cann`t be zero")
# except:
#     print("Invalid input")

# def retStr(string):
#     try:
#         return int(string)
#     except ValueError:
#         print("Invalid input")


# try:
#     someStr = int(input("Enter your str"))
# except ValueError:
#     print("Invalid input")

# someS = input("Enter your string")
# retStr(someS)    
myDict = {"Key1" : "Value1", "Key2" : "Value2"}   
def menu():
    print("1. Show dict")
    print("2. Search value dict")
    print("3. Replace mean")
    print("4. Show by key")
    print("5. Delete by key")
    print("0. Exit")
    return int(input("Enter your choice : "))

def showDict(dictinary):
    for key, value in dictinary.items():
        print(f"Key: {key} Value : {value}")

def showValue(myDict):
    key = input("Enter key : ")
    if key in myDict:
        print(f"Value : {myDict[key]}")
    else:
        print("Invalid key")

choice = menu()
match choice:
    case 1:
        showDict(myDict)
    case 2:
        showValue(myDict)