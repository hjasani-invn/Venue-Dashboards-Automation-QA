import os
import sys


ROOT = sys.path[1]
print(ROOT)
screnshot_dir = os.path.join(ROOT, "screenshots")
print(screnshot_dir)
for f in os.listdir(screnshot_dir):
    print(f)
    file_name = os.path.join(screnshot_dir, f)
    # os.remove(os.path.join(screnshot_dir, f))
    if os.path.exists(file_name):
        os.remove(file_name)
    print(f"{f} is deleted successfully.")