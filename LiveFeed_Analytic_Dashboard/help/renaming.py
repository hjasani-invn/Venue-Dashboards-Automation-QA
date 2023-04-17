import os
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


ROOT = sys.path[1]
# print(ROOT)
# downloaded_dir = os.path.join(ROOT, "Downloaded_Files")
# os.rename(downloaded_dir + "\\datasets.zip",
#           downloaded_dir + "\\datasets_assets_playback_1.zip")

# download_path = str(Path.home() / "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\")
download_path = os.path.join(ROOT, "Downloaded_Files")
print(download_path)