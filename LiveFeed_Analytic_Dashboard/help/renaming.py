import os
import shutil
import sys
from pathlib import Path

# zip1 = ""
# zip2 = ""
#
# ROOT = sys.path[1]
# print(ROOT)
# downloaded_dir = os.path.join(ROOT, "Downloaded_Files")
# print(downloaded_dir)
#
# for filename in os.listdir(downloaded_dir):
#     # Get the full file path
#     file_path = os.path.join(downloaded_dir, filename)
#     # Print the file path
#     print(file_path)

#
# ROOT = sys.path[1]
# print(ROOT)
# downloaded_dir = os.path.join(ROOT, "Downloaded_Files")
# os.rename(downloaded_dir + "\\datasets.zip",
#           downloaded_dir + "\\datasets_assets_playback_1.zip")

# download_path = str(Path.home() / "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\")
# download_path = os.path.join(ROOT, "Downloaded_Files")
# download_path = str(ROOT + "\\Downloaded_Files\\")
#
# print(download_path)


# current_dir = os.getcwd()
# download_path = os.path.join(ROOT, "Downloaded_Files")
# print(download_path)


# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# current_dir = os.getcwd()
# print(current_dir)
# target_file = os.path.join(current_dir, "Downloaded_Files")
# print(target_file)
# ROOT_DIR = (os.path.relpath(target_file))
# print(ROOT_DIR)

# CONFIG_PATH = os.path.join(ROOT_DIR, 'Downloaded_Files')
# print(CONFIG_PATH)
#
# ROOT = sys.path[1]
# download_path = str(ROOT + "\\Downloaded_Files")
# print(download_path)

# ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
# CONFIG_PATH = os.path.join(ROOT_DIR, 'Downloaded_Files')  # requires `import os`
# print(CONFIG_PATH)


ROOT = sys.path[1]
downloaded_dir = os.path.join(ROOT, "Downloaded_Files")
shutil.move("C:\\tmp_downloaded_files\\", downloaded_dir)