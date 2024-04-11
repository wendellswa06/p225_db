import os
import shutil

# Create 10 folders
for i in range(1, 11):
    folder_name = f"folder_{i}"
    os.makedirs(folder_name, exist_ok=True)

# Move files to the folders
source_folder = "EN-US"  # Replace with the actual source folder containing the WAV files
file_list = os.listdir(source_folder)

for i, file_name in enumerate(file_list, start=1):
    folder_index = (i - 1) // 1000 + 1
    destination_folder = f"folder_{folder_index}"
    shutil.move(os.path.join(source_folder, file_name), os.path.join(destination_folder, file_name))

