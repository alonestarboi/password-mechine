 #random password genarator


import random
print("NEW PASSWORD CREATION CENTRE")
randomechars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@$%)(*&"
pwcount=int(input("ENTER HOW MANY PASSWORD YOU WANT: "))
pwlength=int(input("ENTER THE LENGTH OF THE PASSWORD:"))


print("THE PASSWORDS ARE READY FOR YOU!!!")
for x in range(pwcount):
    pwd=""
    for chars in range(pwlength):
        pwd=pwd+random.choice(randomechars)
    print(pwd)
                                                                                     

                                                                                     
