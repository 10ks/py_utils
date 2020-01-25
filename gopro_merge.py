import os
import pprint
import re
import subprocess
import time

# constants (DIR_VIDEO_FILES must end with a backslash)
# DIR_VIDEO_FILES = "./gopro_merge/SampleVideo/"
# DIR_VIDEO_FILES = "D:/GoProContent/2019_08_28/"
DIR_VIDEO_FILES = "D:/GoProContent/2019_09_24_Turcija_Alanija/"
# FFMPEG_EXE = "C:/DEV/GIT_Repos/py_utils/gopro_merge/SampleVideo/ffmpeg.exe"
FFMPEG_EXE = "D:/GoProContent/big/ffmpeg.exe"
GOPRO_PATTERN = re.compile(r"^GH\d{6}\.MP4$")
###


def process_videos(chapter_info):
    """
    Call ffmpeg to merge video chapters
    parameter cointains a tuple - (video number, file names)
    """

    print("Processing chapter_info:", chapter_info)

    # getting creation time of the first chapter
    # TODO update when adding multiple directory proccessing
    os.chdir(DIR_VIDEO_FILES)
    print("1st chapter", chapter_info[1][0])
    chap1_time = time.strftime(
        r"%Y-%m-%d_%H-%M", time.localtime(os.path.getctime(chapter_info[1][0])))
    print("1st chapter creation", chap1_time)

    # output_file = f"M_GH00{chapter_info[0]}_{chap1_time}.MP4"
    output_file = f"{chap1_time}_GH00{chapter_info[0]}_MRG.MP4"
    if os.path.isfile(output_file):
        print(f"Chapter already processed, found file: {output_file}")
        return

    # preparing text file containing file list for merging (for ffmpeg)
    video_list_file = chapter_info[0] + "_merge.txt"
    with open(video_list_file, "w") as f:
        for video_chapter in chapter_info[1]:
            f.write(f"file {video_chapter}\n")

    command = f"{FFMPEG_EXE} -f concat -i {video_list_file} -c copy {output_file}"
    print("command =", command)
    # p = subprocess.run("dir", shell=True, capture_output=True)
    # p = subprocess.run("dir", shell=True, stdout=subprocess.PIPE, text=True)
    p = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    print("returncode =", p.returncode)
    # print("stdout =", p.stdout)
    os.remove(video_list_file)  # remove file list after merging
    # rename original chapters after processing
    for video_chapter in chapter_info[1]:
        os.rename(video_chapter, f"OK_{video_chapter}")


def get_chapter_structure(dir_video):
    """
    Scans top directory, detect chapters, populates dictionary with chapter data
    key is video number; value - chapters
    """

    # get only top level dir info
    dir_data_video_files = next(os.walk(dir_video))
    list_video_files = dir_data_video_files[2]  # get file list

    # add files to a dictionary; key is video number; value - chapters
    file_dict = {}
    for f_name in list_video_files:
        if not GOPRO_PATTERN.search(f_name):
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


def add_timestamps(dir_video):
    """
    Adds creation dates to file names
    """
    print("Adding creation dates to file names")
    os.chdir(dir_video)
    # get only top level dir info
    dir_data_video_files = next(os.walk(dir_video))
    list_video_files = dir_data_video_files[2]  # get file list
    for f_name in list_video_files:
        if GOPRO_PATTERN.search(f_name):
            f_time = time.strftime(r"%Y-%m-%d_%H-%M", time.localtime(os.path.getctime(f_name)))
            os.rename(f_name, f"{f_time}_{f_name}")


print("Starting chapter merging.")
if not os.path.isdir(DIR_VIDEO_FILES):
    print(f"Directory not found: {DIR_VIDEO_FILES}  Exiting.")
    exit()

all_chapter_info = get_chapter_structure(DIR_VIDEO_FILES)
pp = pprint.PrettyPrinter()
print()
pp.pprint(all_chapter_info)
print()

if len(all_chapter_info) == 0:
    print(f"No GoPro chapters to process. Exiting.")
    exit()

for chapter_info in all_chapter_info.items():
    process_videos(chapter_info)

# files which still have GoPro file naming are the ones whic unprocessed
# add creation date to filenames
add_timestamps(DIR_VIDEO_FILES)

print("Chapter merging script is finished.")

# TODO create file renamer to add datetime to file name
# TODO process subdirectories
# TODO handle slashes
# TODO add proper logging levels
