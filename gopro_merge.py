import os
import pprint
import re
import subprocess


def process_videos(chapter_info):
    """
    Call ffmpeg to merge video chapters
    parameter cointains a tuple - (video number, file names)
    """

    print("Processing chapter_info:", chapter_info)

    # preparing text file containing file list for merging (for ffmpeg)
    video_list_file = os.path.join(dir_video_files, chapter_info[0] + "_merge.txt")
    with open(video_list_file, "w") as f:
        for video_chapter in chapter_info[1]:
            f.write(f"file {video_chapter}\n")

    command = f"{ffmpeg_exe} -f concat -i {video_list_file} -c copy {dir_video_files}M_GH00{chapter_info[0]}.MP4"
    print("command =", command)
    # p = subprocess.run("dir", shell=True, capture_output=True)
    # p = subprocess.run("dir", shell=True, stdout=subprocess.PIPE, text=True)
    p = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    print("returncode =", p.returncode)
    # print("stdout =", p.stdout)
    os.remove(video_list_file)  # remove file list after merging


def get_chapter_structure(dir_video):
    """
    Scans top directory, detect chapters, populates dictionary with chapter data
    key is video number; value - chapters
    """

    # get only top level dir info
    dir_data_video_files = next(os.walk(dir_video))
    list_video_files = dir_data_video_files[2]  # get file list
    pattern = re.compile(r"^GH\d{6}\.MP4$")

    # add files to a dictionary; key is video number; value - chapters
    file_dict = {}
    for f_name in list_video_files:
        if not pattern.search(f_name):
            # skip file if name does not match GoPro file format
            continue
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
    return file_dict_filtered


# constants
dir_video_files = "./gopro_merge/SampleVideo/"
ffmpeg_exe = "C:/DEV/GIT_Repos/py_utils/gopro_merge/SampleVideo/ffmpeg.exe"
###

if not os.path.isdir(dir_video_files):
    print(f"Directory not found: {dir_video_files}  Exiting.")
    exit()

all_chapter_info = get_chapter_structure(dir_video_files)
pp = pprint.PrettyPrinter()
print()
pp.pprint(all_chapter_info)
print()

if len(all_chapter_info) == 0:
    print(f"No GoPro chapters to process. Exiting.")
    exit()

for chapter_info in all_chapter_info.items():
    process_videos(chapter_info)
print(f"Video processing is done.")

# TODO set merged file dates same as 1st chapter
# TODO create file renamer to add datetime to file name
# TODO process subdirectories
