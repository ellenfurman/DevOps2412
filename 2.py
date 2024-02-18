x = 1
if x == 2:
    print("x is 2")
else:
    print("x is 1")
full_name = "%s %s" % ("ellen","furman")
a = "ellen"
b = "furman"
full_name2 = f"{a}{b}"  # same as full name
full_name3 = "{} {}".format(a,b)  # same
print(full_name)
full_d = 'name:"ellen"\nlast name:"furman"'
print(full_d)