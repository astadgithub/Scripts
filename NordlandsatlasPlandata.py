import os

#Stopper Arcgis Server
os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/Arealplaner_komm_vedtatt_sk -o stop')

os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/Arealplaner_komm_horing_SK -o stop')

os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/Arealplaner_kommdel_vedtatt_sk -o stop')

os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/Arealplaner_kommdel_horing_sk -o stop')

os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/Bebyggelsesplaner_vedtatt_sk -o stop')

os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/reguleringsplaner_vedtatt_sk -o stop')

os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/Reguleringsplaner_ettersyn_SK -o stop')

os.system ('TIMEOUT 30')

#Kjører Geonorge Massiv nedlster
os.system (r'"C:\Program Files (x86)\Geonorge\Nedlasting\Nedlaster\Geonorge.Nedlaster.exe" NedlasterArealplandata')

# Pakker ut data med 7z.
os.system (r'"E:\Program Files\7-Zip\7z.exe" x "E:\Data\arealplan_sk\Nynedlasting_2023\GeonorgeNedlaster\zip\Kommuneplaner FGDB-format\Plan_18_Nordland_25833_Kommuneplaner_FGDB.zip" -o"E:\Data\arealplan_sk\Nynedlasting_2023\Arealplandata\Kommuneplaner" -aoa')
os.system (r'"E:\Program Files\7-Zip\7z.exe" x "E:\Data\arealplan_sk\Nynedlasting_2023\GeonorgeNedlaster\zip\Kommuneplanforslag FGDB-format\Plan_18_Nordland_25833_Kommuneplanforslag_FGDB.zip" -o"E:\Data\arealplan_sk\Nynedlasting_2023\Arealplandata\Kommuneplanforslag" -aoa')
os.system (r'"E:\Program Files\7-Zip\7z.exe" x "E:\Data\arealplan_sk\Nynedlasting_2023\GeonorgeNedlaster\zip\Reguleringsplaner FGDB-format\Plan_18_Nordland_25833_Reguleringsplaner_FGDB.zip" -o"E:\Data\arealplan_sk\Nynedlasting_2023\Arealplandata\Reguleringsplaner" -aoa')
os.system (r'"E:\Program Files\7-Zip\7z.exe" x "E:\Data\arealplan_sk\Nynedlasting_2023\GeonorgeNedlaster\zip\Reguleringsplanforslag FGDB-format\Plan_18_Nordland_25833_Reguleringsplanforslag_FGDB.zip" -o"E:\Data\arealplan_sk\Nynedlasting_2023\Arealplandata\Reguleringsplanforslag" -aoa')

#kjører fme-løype
os.system (r'"E:\Admin_Programvare\FME\fme.exe" E:\Data\arealplan_sk\Nynedlasting_2023\FME\Plandata_Nordlandsatlas')

#Starter arcgis server
os.system ('timeout 30')
os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/Arealplaner_komm_vedtatt_sk -o start')

os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/Arealplaner_komm_horing_SK -o start')

os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/Arealplaner_kommdel_vedtatt_sk -o start')

os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/Arealplaner_kommdel_horing_sk -o start')

os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/Bebyggelsesplaner_vedtatt_sk -o start')

os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/reguleringsplaner_vedtatt_sk -o start')

os.system (r'"E:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "E:\Program Files\ArcGIS\Server\tools\admin\manageservice.py" -u SFNOGISADMIN -p Kartsjef11 --ignoressl -s http://localhost:6080/arcgis/admin -n Arealplan_SK/Reguleringsplaner_ettersyn_SK -o start')
