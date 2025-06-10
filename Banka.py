import sqlite3 as db
import csv
con=db.connect("banka.db")
kursors=con.cursor()



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

kursors.execute('''select sum(Konta_atlikums) from Konts''')
izvade_sumatlikums=kursors.fetchall()
print(izvade_sumatlikums)
kursors.execute('''select avg(Konta_atlikums) from Konts''')
izvade_avgatlikums=kursors.fetchall()
print(izvade_avgatlikums)
kursors.execute('''select max(Konta_atlikums) from Konts''')
izvade_maxatlikums=kursors.fetchall()
print(izvade_maxatlikums)
kursors.execute('''select min(Konta_atlikums) from Konts''')
izvade_minatlikums=kursors.fetchall()
print(izvade_minatlikums)
kursors.execute('''select count(Konta_atlikums) from Konts''')
izvade_countatlikums=kursors.fetchall()
print(izvade_countatlikums)

csvdatne=open("banka.csv","w",encoding="utf-8")
csvwriter=csv.writer(csvdatne)
csvwriter.writerow(f"summa:{izvade_sumatlikums}, Vidējais:{izvade_avgatlikums}, lielākais:{izvade_maxatlikums}, mazākais:{izvade_minatlikums}, kontu daudzums{izvade_countatlikums}".split(","))

con.close()