import sqlite3 as db
import csv
#savieno kodu ar datubāzi
con=db.connect("banka.db")
kursors=con.cursor()
#veido automātiskos ID
kursors.execute('''select Klienta_ID from Klients''')
izvade_klienta_ID=kursors.fetchall()
Klienta_ID="KLI"+str(len(izvade_klienta_ID)+1)

kursors.execute('''select Konta_ID from Konts''')
izvade_Konta_ID=kursors.fetchall()
Konta_ID="KON"+str(len(izvade_Konta_ID)+1)

kursors.execute('''select Dar_ID from darijumi''')
izvade_Dar_ID=kursors.fetchall()
Dar_ID="DAR"+str(len(izvade_Dar_ID)+1)

#ievade datiem
KlVards=input("Ievadi Klienta Vārdu:")
KlUzvards=input("Ievadi Klienta Uzvārdu:")
Klepasts=input("Ievadi Klienta epastu:")
Kltelefons=input("Ievadi Klienta telefona numuru:")
Kladrese=input("Ievadi Klienta adresi:")
Kldzimsana=input("Ievadi Klienta dzimšanas datumu:")
#ievada datus datubāzē
kursors.execute('''insert or ignore into Klients values(?,?,?,?,?,?,?)''',(Klienta_ID,KlVards,KlUzvards,Klepasts,Kltelefons,Kladrese,Kldzimsana))
con.commit()
#ievade datiem
Konnumus=input("Ievadi Konta numuru:")
Kontips=input("Ievadi Konta tipu:")
Konatlikums=float(input("Ievadi Konta atlikus:"))
Kondatums=input("Ievadi Konta izveides datumu:")
#ievada datus datubāzē
kursors.execute('''insert or ignore into Konts values(?,?,?,?,?)''',(Konta_ID,Konnumus,Kontips,Konatlikums,Kondatums))
#ievade datiem
con.commit()
Dardatums=input("Ievadi Darijuma datumu:")
Darapraksts=input("Ievadi Darijuma aprakstu:")
Darklients=input("Ievadi Darijuma klientu:")
Darkonts=input("Ievadi Darijuma kontu:")
Darsumma=float(input("Ievadi Darijuma summu:"))
#ievada datus datubāzē
kursors.execute('''insert or ignore into darijumi values(?,?,?,?,?,?)''',(Dar_ID,Dardatums,Darapraksts,Darklients,Darkonts,Darsumma))
con.commit()
#izvada specifiskus datus no datubāzes
kursors.execute('''select Klienta_Vards from Klients''')
izvade_klienta_vards=kursors.fetchall()
print(izvade_klienta_vards)
kursors.execute('''select Klienta_dzimsana from Klients''')
izvade_klienta_dzimsana=kursors.fetchall()
print(izvade_klienta_dzimsana)
kursors.execute('''select Konta_atlikums from Konts''')
izvade_konta_atlikums=kursors.fetchall()
print(izvade_konta_atlikums)
kursors.execute('''select Dar_apraksts from darijumi''')
izvade_Dar_apraksts=kursors.fetchall()
print(izvade_Dar_apraksts)
kursors.execute('''select Dar_summa from darijumi''')
izvade_Dar_summa=kursors.fetchall()
print(izvade_Dar_summa)
#izvada summu atlikumam
kursors.execute('''select sum(Konta_atlikums) from Konts''')
izvade_sumatlikums=kursors.fetchall()
print(izvade_sumatlikums)
#izvada vidējo atlikumam
kursors.execute('''select avg(Konta_atlikums) from Konts''')
izvade_avgatlikums=kursors.fetchall()
print(izvade_avgatlikums)
#izvada lielāko atlikumu
kursors.execute('''select max(Konta_atlikums) from Konts''')
izvade_maxatlikums=kursors.fetchall()
print(izvade_maxatlikums)
#izvada zemāko atlikumu
kursors.execute('''select min(Konta_atlikums) from Konts''')
izvade_minatlikums=kursors.fetchall()
print(izvade_minatlikums)
#izvada kontu skaitu
kursors.execute('''select count(Konta_atlikums) from Konts''')
izvade_countatlikums=kursors.fetchall()
print(izvade_countatlikums)
#izveido csv datni
csvdatne=open("banka.csv","w",encoding="utf-8")
csvwriter=csv.writer(csvdatne)
#ievada datus csv datnē
csvwriter.writerow(f"summa:{izvade_sumatlikums}, Vidējais:{izvade_avgatlikums}, lielākais:{izvade_maxatlikums}, mazākais:{izvade_minatlikums}, kontu daudzums{izvade_countatlikums}".split(","))

con.close()