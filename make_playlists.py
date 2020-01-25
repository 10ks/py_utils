import os
import os.path

start_dir_name = "C:/DEV/GIT_Repos/py_utils/music"
add_ext=['.mp3']  # list of file extensions which to include in playlist
dir_data = os.walk(start_dir_name)
# print(os.getcwd())

# try:
#     top_dir = next(dir_data)
# except StopIteration as identifeier:
#     print("No start directory. Exiting")
#     exit()


for root, dirs, files in dir_data:
    print(root)
    print(dirs)
    print(files)
    print("---")
    playlist = ""
    for f in files:
        ext = os.path.splitext(f)[1]
        if ext in add_ext:
            # playlist += root[len(start_dir_name)+1:] + "\\" + f + "\r\n"
            playlist += f + "\r\n"
    if playlist:
        # print("generated playlist:")
        # print(playlist)

        # TODO Number sign in file name is the problem
        # playlist_name = root + "\\" + root[0:4] + "play.m3u"
        playlist_name = root + "\\" + "XXX" + "play.m3u"
        print("playlist_name=", playlist_name)
        with open(playlist_name, "w") as text_file:
            text_file.write(playlist)
    else:
        print("no playlist")