import random as rn

freia = 0


def skjokolade_fabrikk():
    freia = rn.randint(0,10)
    print(freia)

def catch_the_number() :
    your_number = int(input('Please enter a number from 0 to 10. '))
    ran_num= skjokolade_fabrikk()
    if your_number == ran_num:
       print('congrats! you won!!!')
    else:
         print('sorry, try again!!!')
         catch_the_number()
        

catch_the_number()