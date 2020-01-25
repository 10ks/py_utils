import os
import os.path

start_dir_name = "C:/DEV/GIT_Repos/py_utils/music"
# start_dir_name = "E:/"
add_ext = ['.mp3']  # list of file extensions which to include in playlist
dir_data = os.walk(start_dir_name)
# print(os.getcwd()) # TODO check why wrong working directory

for root, dirs, files in dir_data:
    files.sort()  # without this order is arbitrary
    playlist = ""
    for f in files:
        ext = os.path.splitext(f)[1]
        if ext in add_ext:
            playlist += f + "\r\n"
    if playlist:
        # TODO Number sign (№) in directory name is the problem, check how to avoid
        playlist_name = root + "/" + os.path.split(root)[1][0:9] + "_play.m3u"
        print("generated", playlist_name)
        with open(playlist_name, "w") as text_file:
            text_file.write(playlist)
    else:
        print("no playlist for ", root)

print("done")
