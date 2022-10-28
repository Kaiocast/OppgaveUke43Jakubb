from matplotlib import pyplot as plt 

## Oppgave 3##

countries  = ["Nicaragua", "Cuba", "Kina", "Østerrike", "Nederland", "Norge", "Chile", "Brasil","Venezuela"]
konsumprisindeks = [3.4, 1.2, 3.7, 5.3, 4.9, 6.9, 8.1, 7.2, 3.4 ]
colors = [ "yellow", "red", "blue", "silver", "deeppink", "brown", "grey", "cyan", "darksalmon"]

plt.pie(konsumprisindeks, labels=countries,
colors=colors, shadow=True, radius=1)
plt.title('oppgave3')

plt.show()