from matplotlib import pyplot as plt

renta = []

tb = []

avdrag = []

nedbetalingstid = int(input('insert years.'))
ønsket_bel = int(input('insert ønsket beløp.'))
n_renta = float(input('insert rente.'))

pp = 0
for pp in range(nedbetalingstid):
    årlig_avdrag = ønsket_bel/nedbetalingstid
    årlig_renta = ønsket_bel*n_renta
    terminbeløp = årlig_avdrag+årlig_renta

    avdrag.append(årlig_avdrag)
    renta.append(årlig_renta)

print(terminbeløp)


#tusen takk til edgardo for at han gjennom gikk et eksmpel som jeg gjordet omm til min egen.s
