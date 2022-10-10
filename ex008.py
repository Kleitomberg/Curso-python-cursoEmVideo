print("====== DESAFIO 08 ======")

metro = float( input('Valor em Metro: '))

cm = metro *100
mm = metro *1000
km = metro/1000
hm = metro/100
dam = metro/10
dm = metro*10

print('{}m corresponde a {:.0f}cm  {:.0f}mm {}km {}hm {}dam {:.0f}dm' .format(metro, cm, mm,km, hm, dam, dm))