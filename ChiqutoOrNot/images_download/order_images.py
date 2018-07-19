import os
from shutil import copy
import random
from os import listdir
from os.path import isfile, join

path = "C:\\Users\\pablogonzalez\\Dropbox\\Programacion\\Python\\ChiqutoOrNot\\images_download\\downloads\\otras\\lfw"
folders = [x[0] for x in os.walk(path)]
print(len(folders))

rnd_numbers=[]
num_images=270
while(len(rnd_numbers)<270):
    num = random.randint(0,len(folders)-1)
    if(not (num in rnd_numbers)):
        rnd_numbers.append(num)

for num in rnd_numbers:
    onlyfiles = [f for f in listdir(folders[num]) if isfile(join(folders[num], f))]
    image = folders[num]+"\\"+onlyfiles[0]
    copy(image,path)
    
print("\n Finished")