d = {}

# name = input("Enter friends name: ")
# lang = input("Enter Language name: ")
# d.update({name: lang})

# name = input("Enter friends name: ")
# lang = input("Enter Language name: ")
# d.update({name: lang})

# name = input("Enter friends name: ")
# lang = input("Enter Language name: ")
# d.update({name: lang})

# name = input("Enter friends name: ")
# lang = input("Enter Language name: ")
# d.update({name: lang})


# print(d)
n=int(input("enter no. of items: "))
while(n>0):
    name = input("Enter friends name: ")
    lang = input("Enter Language name: ")
    d.update({name: lang})
    n-=1
print(d)