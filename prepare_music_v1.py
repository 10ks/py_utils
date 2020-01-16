import os
from transliterate import translit, get_available_language_codes

# print(translit(u"Привет, ёжик, чо? Лорем ипсум долор сит амет", 'ru', reversed=True))
# print(translit("Привет, ёжик, чо? Лорем ипсум долор сит амет", 'ru', reversed=True))

# for a in os.walk(top):
# for root, dirs, files in os.walk(top, topdown=False):
for root, dirs, files in os.walk("."):
    # print(root)
    # print(dirs)
    # print(files)
    # if files:
        # print("found files")
    for f in files:
        # print(root + "\\" + f)
        print(type(f))
        print(type(u"sdf"))
        # print(root + "\\" + translit(f, 'ru', reversed=True))
        print(root + "\\" + translit("fasdf", 'ru'))
        
    # print("------")
