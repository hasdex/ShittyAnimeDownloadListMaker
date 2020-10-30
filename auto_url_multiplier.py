import re
import string
import io

print("")
print("################## SHITTY ANIME DOWNLOAD LIST MAKER ##################")
print("")
print("Welcome to the Shitty Anime Download List Maker, aka SADLM")
print("")
url = raw_input('Enter the full url of the anime: ')
start = int(input('Enter the number of first episode to download (ex. 11): '))
end = int(input('Enter the number of the last episode to download: (ex. 24) '))

splitted_dict = re.split('(\d+)',url)

print("")
print("Download list successfully generated!")
print("")
out_file = open("download_link.txt","w")
for x in range(start, end+1):
    if (x>9):    
        #print(splitted_dict[0]+str(x)+splitted_dict[2]+splitted_dict[3])
        out_file.write(splitted_dict[0]+str(x)+splitted_dict[2]+splitted_dict[3]+"\n")
    else:
        #print(splitted_dict[0]+"0"+str(x)+splitted_dict[2]+splitted_dict[3])
        out_file.write(splitted_dict[0]+"0"+str(x)+splitted_dict[2]+splitted_dict[3]+"\n")
out_file.close()