#  This program will parse a dat file from bittorrent and parse out the relevent forensic data


import time
import bencoder


#  Function to convert the time from epoch to est

def convert(epoch):
    return time.strftime("%m-%d-%Y %H:%M:%S", time.localtime(epoch))

#  Ask user what file they wish to decode resume.dat or fastresume

mode = input("Enter 1 to decode a resume.dat or Enter 2 to decode a fastresume file:  ")

#  Asks the user for the path to the resume.dat
path = input("Enter path to file you wish to decode (include file in path):  ")
#path = "C:\\Users\\syrinx\\Desktop\\datsAWrap\\test.fastresume"

#  Reading of the file for decoding
f = open(path, "rb")
d = bencoder.decode(f.read())

if mode == "1":
    #  Ignore two enteries that are not torrent files, prints out the relevent data
    print("File_Name," + "Added_On," + "Completed_On," + "Downloaded," + "Uploaded," + "Path," + "Seedtime")
    for key in d:
        if key == b'.fileguard':
            print("Ignore this!")
        elif key == b'rec':
            print("Ignore this!")
        else:
            fileName = str(key)
            added_on = str(convert(d[key][b'added_on']))
            completed_on = str(convert(d[key][b'completed_on']))
            downloaded = str(d[key][b'downloaded'])
            uploaded = str(d[key][b'uploaded'])
            path = str(d[key][b'path'])
            seedtime = str(d[key][b'seedtime'])
            print(fileName + "," + added_on + "," + completed_on + "," + downloaded + "," + uploaded + "," + path + "," + seedtime)
elif mode == "2":
    seedtime = str(d[b'seeding_time'])
    uploaded = str(d[b'total_uploaded'])
    downloaded = str(d[b'total_downloaded'])
    maxuploads = str(d[b'max_uploads'])
    maxconnections = str(d[b'max_connections'])
    numseeds = str(d[b'num_seeds'])
    activetime = str(d[b'active_time'])
    seedmode = str(d[b'seed_mode'])
    superseeding = str(d[b'super_seeding'])
    numdownloaders = str(d[b'num_downloaders'])

    print("Number_of_Downloaders" + "," + "Super_Seeding" + "," + "Seed_Mode" + "," + "Time_Active" + "," + "Number_of_Seeds" + "," + "Max_Connections" + "," + "Max_Uploads" + "," + "Total_Downloaded" + "," + "Total_Uploaded" + "," + "Seeding_Time")
    print(numdownloaders + "," + superseeding + "," + seedmode + "," + activetime + "," + numseeds + "," + maxconnections + "," + maxuploads + "," + downloaded + "," + uploaded + "," + seedtime)
else:
    print("You must select either 1 or 2")



