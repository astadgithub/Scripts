from arcgis.gis import GIS
from datetime import datetime

def main():
    username = 'xxxxxx' #brukernavn til eier av laget
    password = 'xxxxxxx' #passord til eier av laget

    layer_ID = 'c268d321938a4bc5878591e5d8b57e7f' #EDIT 1()ID fra laget 
    layer_type = 'Feature Service'
    download_format = 'File Geodatabase'
    download_location = r'F:\Kart\Backup_AGO\FremmedeTreslag' #EDIT 2()

    # Legger til dato for backpen
    today_date = datetime.now().strftime('%Y%m%d')
    new_filename = f'FremmedeTreslag_backup_{today_date}.zip' #EDIT 3() endre navn her. Alt mellom ..f' og {toda.. kan endres

    download_item(username, password, layer_ID, layer_type, download_format, download_location, new_filename)

def download_item(username, password, layer_ID, layer_type, download_format, download_location, new_filename):
    gis = GIS(None, username, password, verify=False)

    try:
        items = gis.content.search(layer_ID)
        print(items)

        for item in items:
            if item.type == layer_type:
                result = item.export(title=layer_ID, export_format=download_format) #eksporterer til fgdb
                result.download(save_path=download_location, file_name=new_filename) #laster ned fgdb
                result.delete() #sletter fgdb
                print(f'Nedlasting fullført: {new_filename}')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
