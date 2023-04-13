import os

# file_name = "movement_analytics_page.py"
# path = os.path.abspath(os.curdir)
# print(path)
#
# join_path = os.path.join(path, file_name)
# print(join_path)


# file_name = "movement_analytics_page.py"
# ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
# print(ROOT_DIR)
# CONFIG_PATH = os.path.join(ROOT_DIR, 'movement_analytics_page.py')
# print(CONFIG_PATH)



# get the users Download dir path
from pathlib import Path
# downloads_path = str(Path.home() / "Downloads")
downloads_path = str(Path.home() / "C:\\Users\\hjasani\\OneDrive - tdkgroup\\Desktop\\work_automation\\LiveFeed_Analytic_Dashboard\\Downloaded_Files")
print(downloads_path)