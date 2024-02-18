# import random
#
#
# def generate_number(difficulty):
#     num1 = random.randint(0, difficulty)
#     print(num1)
#     return num1
#
#
# def get_guess_from_user():
#     num2 = input("Please enter a number between 1 to difficulty: ")
#     return int(num2)
#
#
# secret_number = generate_number(6)
# num = get_guess_from_user()
#
#
# def compare_results():
#     if secret_number < num:
#         return "win"
#     else:
#         return "lose"
#
#
# result = compare_results()
#
#
# def play():
#     if result == 'win':
#         print('True')
#     else:
#         print('False')
#
#
# play()