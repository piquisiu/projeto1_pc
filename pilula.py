
import math as m
import random as r
import statistics as s
import locale as l
import datetime as d

l.setlocale(l.LC_ALL, 'pt_BR.UTF-8')
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
t = 0.010
montante_fii = (cp * m.pow ((1+t), ms) + (ap * ms))
montante_fii2 = (cp * m.pow ((1+t), ms) + (ap * ms))
montante_fii3 = (cp * m.pow ((1+t), ms) + (ap * ms))
montante_fii4 = (cp * m.pow ((1+t), ms) + (ap * ms))
montante_fii5 = (cp * m.pow ((1+t), ms) + (ap * ms))
taxa_mensal = s.mean (m.pow (1+t), -3 or +3)
montante_fii = float(input('Produção lote 1: '))
montante_fii2 = float(input('Produção lote 2: '))
montante_fii3 = float(input('Produção lote 3: '))
montante_fii4 = float(input('Produção lote 4: '))
montante_fii5 = float(input('Produção lote 5: '))
media = s.mean( (montante_fii, montante_fii2, montante_fii3, montante_fii4, montante_fii5) )
desvio = s.stdev( (montante_fii, montante_fii2, montante_fii3, montante_fii4, montante_fii5) )
print(f'Media: {media:.2f}')
print(f'Desvio padrão: {desvio:.2f}')

montante_fii_liquido = t + (ap * 0.85) /100
t_liquido = (ap * m.pow (1+ cp),ms (cp * cdi /100))

#Formatação
l.setlocale(l.LC_ALL, 'pt_BR.UTF-8')
total = float(input('O Total é (R$):'))
print(f'Total {l.currency(total,grouping=True)}')  

#Data do Resgate
data = d.datetime.strptime(d, '%d/%m/%Y')
data_final = d.datetime + d.timedelta(days = ms * 30) /100
data = d.datetime.strftime (cp* 50 "-" (ms)) /100
cp * m.pow ((1+d), ms) + (ap * ms)

