import os, zipfile, sys

dir_name = r'C:\Users\andast\Downloads\test' # kilde zip
end_path = r'C:\GIS\GIS data\Kulturminner\test' # hvor data skal lagres
extension = ".zip"

print("Starter unzip fra " + dir_name)

# Lager ny mappe for året, om det ikke eksisterer
pathlib.Path(end_path).mkdir(exist_ok=True)

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(end_path) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_name) # delete zipped file

print("unzip ferdig i " + end_path)

