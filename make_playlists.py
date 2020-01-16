import os
import os.path

start_dir_name = "music"
add_ext={'.mp3'}
dir_data = os.walk(start_dir_name)
top_dir = next(dir_data)
# print(type(top_dir))
# print(top_dir)

for root, dirs, files in dir_data:
    # print(root)
    # print(dirs)
    # print(files)
    # print("---")
    playlist = ""
    for f in files:
        ext = os.path.splitext(f)[1]
        # print(ext)
        if ext in add_ext:
            playlist += root[len(start_dir_name)+1:] + "\\" + f + "\r\n"   ## TODO remove base
    if playlist:
        print("generated playlist:")
        print(playlist)

        # TODO output playlist to separate dirs. Number sign is the problem

        with open(root + "\\gen_play.txt", "w") as text_file:
            text_file.write(playlist)
    else:
        print("no playlist")