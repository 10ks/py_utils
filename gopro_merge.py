import pprint

files_names = [
    # "wrong.mp3",
    # "wrong2",
    # "wrong3MP4",
    "GH011882.MP4",
    "GH011883.MP4",
    "GH011884.MP4",
    "GH011885.MP4",
    "GH011886.MP4",
    "GH011887.MP4",
    "GH011888.MP4",
    "GH011889.MP4",
    "GH011890.MP4",
    "GH011891.MP4",
    "GH011892.MP4",
    "GH011893.MP4",
    "GH021885.MP4",
    "GH021886.MP4",
    "GH021887.MP4",
    "GH021888.MP4",
    "GH021892.MP4",
    "GH031887.MP4",
    "GH031888.MP4",
    "GH031892.MP4",
    "GH041887.MP4",
    "GH041892.MP4",
    "GH051892.MP4"
]


file_dict = {}
for f_name in files_names:
    print(f_name, f_name[4:8])
    elem = file_dict.get(f_name[4:8])
    if elem is None:
        file_dict[f_name[4:8]] = [f_name]
    else:
        elem.append(f_name)

# print(file_dict)

pp = pprint.PrettyPrinter()
pp.pprint(file_dict)