import requests

try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    result = a/b
    print(result)
except ValueError:
    print("enter a correct number")

except ZeroDivisionError:
    print("could not ba bla")




#  //////
my_file = open("names.txt")
for name in my_file.readlines():
    print(f"hello {name}", end='')


try:
    requests.get("gntkjrn:.//tgj")
except BaseException as e:
    print("something went wrong")
    print(e.args)