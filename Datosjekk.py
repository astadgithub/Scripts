import os
import datetime

pth = r"C:\GIS\tempzip"
count = 0
idag=datetime.date.today()

def listDir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        file_path = os.path.join(pth, fileName)

        #ct = os.path.getctime(file_path)        # this returns the creation timestamp.
        mt = os.path.getmtime(file_path)        # this returns the creation timestamp.
        #dtc = datetime.datetime.fromtimestamp(ct)    # this converts the timestamp to datetime object.
        dtm = datetime.datetime.fromtimestamp(mt)    # this converts the timestamp to datetime object.
        if dtm.date() == idag:
            global count
            count += 1

        print('{0} --> sist endret {1}'.format(fileName , dtm.date()))    # dt.date() will return only the date from the datetime object.

listDir(pth)

print("\n Dato i dag: " + str(idag))
print ("\n Filer som er modifisert idag: " + str(count))
