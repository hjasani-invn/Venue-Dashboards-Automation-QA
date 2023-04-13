import os
import sys

# # dir_del = "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\"
# # dir_del = "C:\\Users\\hjasani\\OneDrive - tdkgroup\\Desktop\\work_automation\\LiveFeed_Analytic_Dashboard\\Downloaded_Files"
# dir_del = "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files"
# file_list = os.listdir(dir_del)
# print(file_list)
#
# # Loop through the list and delete each file
# for filename in file_list:
#     file_path = os.path.join(dir_del, filename)
#     print(file_path)
#     try:
#         os.remove(file_path)
#     except Exception as e:
#         print(f"Error deleting file: {file_path} - {e}")



# dir_del = "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\"
# file_list = os.listdir(dir_del)
# print(file_list)
#
# # Loop through the list and delete each file
# for filename in file_list:
#     file_path = os.path.join(dir_del, filename)
#     print(file_path)
#     try:
#         os.remove(file_path)
#     except Exception as e:
#         print(f"Error deleting file: {file_path} - {e}")



ROOT = sys.path[1]
print(ROOT)
downloaded_dir = os.path.join(ROOT, "Downloaded_Files")
print(downloaded_dir)
for f in os.listdir(downloaded_dir):
    print(f)
    file_name = os.path.join(downloaded_dir, f)
    if os.path.exists(file_name):
        os.remove(file_name)
    print(f"{f} is deleted successfully.")