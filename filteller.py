import os

folder_path = r"C:\GIS\Arealregnskap\arealregnskap2023_stat"  # Replace with the actual path to your folder

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    print("Number of files in the folder:", file_count)
else:
    print("The specified folder does not exist or is not a directory.")
