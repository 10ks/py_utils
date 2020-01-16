import os
from os import path
from transliterate import translit

# fname = path.splitext(path.basename("/a/b/привет.txt"))[0]
# print(fname)

# base_path = "music"
# base_path = "D:"
base_path = ""
renamed_count = 0

print("starting transliterating")
# Setting topdown to False is important when directories are also renamed
for root, dirs, files in os.walk(base_path, topdown=False):
    # print(dirs)
    # for fname in files + dirs:  # rename files and dirs
    for fname in files:           # rename only files
        path_from = path.join(root, fname)
        path_to = path.join(root, translit(fname, language_code="ru", reversed=True))
        if path_from != path_to:
            # os.rename(path_from, path_to)
            renamed_count += 1
            # print(path_from)
            # print(path_to)
            # print("renamed")
print(f"renamed {renamed_count} objects")
