import math as m
import random as r
import statistics as s
import locale as l
import datetime as d

l.setlocale(l.LC_ALL, 'pt_BR.VTF-8')
#Entradas

#capital cp
#aporte ap
#meses ms
#cdi_anual cdi
#perc_cdb cdb
#perc_lci lci
#taxa_fii t
#meta mt

cp = float(input('Digite o seu capital: '))
ap = float(input('Aporte Mensal: '))
ms = int(input('Prazo (meses): '))
cdi = float(input('CDI anual (%)'))/100
cdb = float(input('Percentual do CDI (%)'))/100
lci = float(input('Percentual do LCI (%)'))/100
t = float(input('Rentabilidade mensal FII (%)'))/100
mt = float(input('Meta financeira (R$)'))

#CONVERSÃO CDI
cdi_mensal = m.pow((1+cdi), 1/12) -1

#TOTAL INVESTIDO
total_investido = cp + (ap * ms)

#CDB
taxa_cdb = cdi_mensal * cdb
montante_cdb = (cp * m.pow((1 + taxa_cdb), ms) + (ap * ms))
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * lci
montante_lci = (cp * m.pow((1 + taxa_lci), ms) + (ap * ms))

#POUPANÇA
taxa_poupanca = 0.005
montante_poupanca = (cp * m.pow((1+taxa_poupanca),ms) + (ap * ms))

#FII - SIMULAÇÕES