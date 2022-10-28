def myMonpayment(Principal, rate, year) :
    pp  = years * 12   
    # un
    kaki  = (rate/100)/12
    MonPayment = (kaki * Principal* ((1+kaki) **pp))/(((1+kaki) **pp)-1)
    return MonPayment

years = int(input('Please input amount of years.'))
rate = float(input('Please enter annual intrest Rate.'))
Principal = int(input('Please input amount of loan.'))

print('Monthly payment : {0:.2f}'.format(myMonpayment(Principal, rate, years)))

# i do not own this, and i did not create the code, this is someones tutorial on a Easy loane calculator.

# koden fngerer på denne måten'Enkelt forklaring': den tar "Principal" inputen og ganger den med "rate" inputen og deler den på antall år som er skrevet inn.
#antall år er gjort om til antall månder med "n = years * 12" fordi det er 12 månder. eks 10år * 12 = 120 månder, så Python tar "Principal * rate / years" og den finner måntelig betaling for lån.

# meninga med denne her er ikke at jeg lagde et kalkulator, men for o kjekke om jeg kjønner hvordan man lager en.



