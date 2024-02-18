class NegativeAgeError(Exception):
    """Exception raised for negative user age."""

def get_user_age():
    try:
        user_age = int(input("enter age"))
    except BaseException:
        print("balbla")
    if user_age < 0:
        raise NegativeAgeError("")

try:
    get_user_age()
except NegativeAgeError:
    print("age cant be negative")