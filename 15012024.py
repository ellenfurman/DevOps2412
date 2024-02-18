#  1+2:
# try:
#     a = 1/0
# except:
#     print('Error')
#
#  3 is legal:
# try:
#     x = 1
# finally:
#     print('Finally')
#  4: Any exception
#  5: We can't know what is the problem specifically its too general
#  6: except IOError - an error related to file, occurs when the file that we passed in as argument,
#  does not exist or as a different name or the file location path is incorrect
#  except ZeroDivisionError - handles divison by zero
#  7+8
# my_file = open("words.txt",'w') # creats a txt file named ellen
# my_file.write('Ellen')
# my_file.close()
# #  9
# my_file = open("words.txt",'r') # creats a txt file named ellen
# print(my_file.read())
# my_file.close()
# #  10
# my_file = open("words.txt",'w',encoding='utf-8') # creats a txt file named ellen
# my_file.write('אלן')
# my_file.close()
#
# my_file = open("words.txt",'r',encoding='utf-8') # creats a txt file named ellen
# print(my_file.read())
# my_file.close()
#
# #11
# my_file = open("words.txt",'w') # creats a txt file named ellen
# my_file
# my_file.close()

