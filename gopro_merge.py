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
    "GH041892.MP4",  # second to last, changed position
    "GH031892.MP4",
    "GH041887.MP4",
    "GH051892.MP4"
]

# add files to a dictionary; key is video number; value - chapters
file_dict = {}
for f_name in files_names:
    video_num = f_name[4:8]
    # print(f_name, video_num)
    f_list = file_dict.get(video_num)
    if f_list is None:
        file_dict[video_num] = [f_name]
    else:
        f_list.append(f_name)

# filter out entries containing a single video; sort chapters
file_dict_filtered = file_dict.copy()  # shallow copy, but that's ok
for video_num, f_list in file_dict.items():
    if len(f_list) == 1:
        del file_dict_filtered[video_num]
    else:
        file_dict_filtered[video_num].sort()


pp = pprint.PrettyPrinter()
# pp.pprint(file_dict)
print()
pp.pprint(file_dict_filtered)

# TODO add file name check for type, format; avoid processing outpt or non-GoPro videos
# TODO call ffmpg process
