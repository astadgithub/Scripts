import os, subprocess

komlist = ['Bodo', 'Bindal', 'Somna', 'Bronnoy', 'Vevelstad', 'Heroy', 'Alstahaug', 'Leirfjord', 'Vefsn', 'Hattfjelldal', 'Donna', 'Nesna', 'Hemnes', 'Rana', 'Luroy', 'Trena', 'Meloy', 'Gildeskal', 'Beiarn', 'Saltdal', 'Fauske', 'Sorfold', 'Steigen', 'Lodingen', 'Evenes', 'Veroy', 'Flakstad', 'Vestvagoy', 'Vagan', 'Hadsel', 'Bo', 'Oksnes', 'Sortland', 'Andoy', 'Moskenes', 'Hamaroy']
komnrlist = [1804, 1811, 1812, 1813, 1816, 1818, 1820, 1822, 1824, 1826, 1827, 1828, 1832, 1833, 1834, 1835, 1837, 1838, 1839, 1840, 1841, 1845, 1848, 1851, 1853, 1857, 1859, 1860, 1865, 1866, 1867, 1868, 1870, 1871, 1874, 1875]

#utelattekommuner = ['Rost','Grane','Rodoy','Vega','Narvik' - 1856,  1825,  1836,  1815,  1806,]    

#Kjører Geonorge Massiv nedlasting - kommunevis FKB data, plan for Nordland
os.system (r'"C:\Program Files (x86)\Geonorge\Nedlasting\Nedlaster\Geonorge.Nedlaster.exe" Arealregnskap')
os.system (r'"C:\Program Files (x86)\Geonorge\Nedlasting\Nedlaster\Geonorge.Nedlaster.exe" NedlasterArealplandata')

# Pakker ut data med 7z.
os.system (r'"C:\Program Files\7-Zip\7z.exe" x "C:\GIS\tempzip\Kommuneplaner FGDB-format\Plan_18_Nordland_25833_Kommuneplaner_FGDB.zip" -o"C:\GIS\GIS data\Plan\Arealplandata\Kommuneplaner" -aoa')
os.system (r'"C:\Program Files\7-Zip\7z.exe" x "C:\GIS\tempzip\Kommuneplanforslag FGDB-format\Plan_18_Nordland_25833_Kommuneplanforslag_FGDB.zip" -o"C:\GIS\GIS data\Plan\Arealplandata\Kommuneplanforslag" -aoa')
os.system (r'"C:\Program Files\7-Zip\7z.exe" x "C:\GIS\tempzip\Reguleringsplaner FGDB-format\Plan_18_Nordland_25833_Reguleringsplaner_FGDB.zip" -o"C:\GIS\GIS data\Plan\Arealplandata\Reguleringsplaner" -aoa')
os.system (r'"C:\Program Files\7-Zip\7z.exe" x "C:\GIS\tempzip\Reguleringsplanforslag FGDB-format\Plan_18_Nordland_25833_Reguleringsplanforslag_FGDB.zip" -o"C:\GIS\GIS data\Plan\Arealplandata\Reguleringsplanforslag" -aoa')


#itererer igjennom kommuner, pakker ut data, kjører fme-løype
for i in range(len(komlist)):
   komnavn = komlist[i]
   komnr = komnrlist[i]
   subprocess.run (r'"C:\Program Files\7-Zip\7z.exe" x "C:\GIS\tempzip\FKB-Veg FGDB-format\Basisdata_'+str(komnr)+'_'+komnavn+'_5973_FKB-Veg_FGDB.zip" -o"C:\GIS\Arealregnskap\Data\\'+komnavn+'" -aoa')
   subprocess.run (r'"C:\Program Files\7-Zip\7z.exe" x "C:\GIS\tempzip\FKB-Tiltak FGDB-format\Basisdata_'+str(komnr)+'_'+komnavn+'_5973_FKB-Tiltak_FGDB.zip" -o"C:\GIS\Arealregnskap\Data\\'+komnavn+'" -aoa')
   subprocess.run (r'"C:\Program Files\7-Zip\7z.exe" x "C:\GIS\tempzip\FKB-Bygning FGDB-format\Basisdata_'+str(komnr)+'_'+komnavn+'_5973_FKB-Bygning_FGDB.zip" -o"C:\GIS\Arealregnskap\Data\\'+komnavn+'" -aoa')
   subprocess.run (r'"C:\Program Files\7-Zip\7z.exe" x "C:\GIS\tempzip\FKB-AR5 FGDB-format\Basisdata_'+str(komnr)+'_'+komnavn+'_25833_FKB-AR5_FGDB.zip" -o"C:\GIS\Arealregnskap\Data\\'+komnavn+'" -aoa')
   subprocess.run (r'"C:\Program Files\7-Zip\7z.exe" x "C:\GIS\tempzip\Arealbruk FGDB-format\Befolkning_'+str(komnr)+'_'+komnavn+'_25833_Arealbruk2023_FGDB.zip" -o"C:\GIS\Arealregnskap\Data\\'+komnavn+'" -aoa')
   os.system (r'"C:\Program Files\FME\fme.exe" C:\GIS\Arealregnskap\Arealregnskap_dato_planer.fmw --Kommune '+str(komnr)+' --filkom '+komnavn)
