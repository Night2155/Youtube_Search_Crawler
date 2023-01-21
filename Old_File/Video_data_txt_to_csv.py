import os
from pathlib import Path
import re


def read_all_file(directory: str):
    row_number = 0
    file_text = ""
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_directory = os.path.join(directory, filename)
            filereader = open(file_directory, "r", encoding="UTF-8")
            csvname = Path(filename).stem
            csvwriter = open(directory+csvname+".csv",
                             "w", encoding="UTF-8-sig")
            csvwriter.write("Video_Title,VideoID,ChannelID\n")

            for row in filereader:
                row_number += 1
                if row != "\n":
                    if row_number == 1:
                        text_line = re.split("Title : ", row)
                        file_text += text_line[-1].replace("\n", ",")
                    if row_number == 2:
                        text_line = re.split("VideoID : ", row)
                        file_text += text_line[-1].replace("\n", ",")
                    if row_number == 3:
                        text_line = re.split("ChannelID : ", row)
                        file_text += text_line[-1].replace("\n", "")
                if row == "\n":
                    csvwriter.write(file_text+"\n")
                    file_text = ""
                    row_number = 0
            csvwriter.close()
            filereader.close()
        else:
            continue


def read_file(filename: str):
    file_reader = open(filename, "r", encoding="UTF-8")
    for row in file_reader:
        print(row)


if __name__ == "__main__":
    # 資料夾路徑
    read_all_file("Youtube_Video_data/")
    # read_file("英文單字教學_Searchmp4.txt")
