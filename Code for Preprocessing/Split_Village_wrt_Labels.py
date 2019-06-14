import os
import glob
import pandas as pd
import numpy as np
from shutil import copyfile
from shutil import move
import pandas as pd

'''
image_pathOrissa="/home/ictd/Desktop/Arpit/Satellite project/data/landsat/croppedImagesOddisa"
image_pathMaha="/home/ictd/Desktop/Arpit/Satellite project/data/landsat/croppedImagesMaha"
image_pathKer="/home/ictd/Desktop/Arpit/Satellite project/data/landsat/croppedImagesKerela"
image_pathKar="/home/ictd/Desktop/Arpit/Satellite project/data/landsat/croppedImagesKarnataka"
image_pathGuj="/home/ictd/Desktop/Arpit/Satellite project/data/landsat/croppedImagesGuj"
image_pathBihar="/home/ictd/Desktop/Arpit/Satellite project/data/landsat/croppedImagesBihar"
dirs1=os.listdir(image_pathOrissa)
dirs2=os.listdir(image_pathMaha)
dirs3=os.listdir(image_pathKer)
dirs4=os.listdir(image_pathKar)
dirs5=os.listdir(image_pathGuj)
dirs6=os.listdir(image_pathBihar)
files1=[]
files2=[]
files3=[]
files4=[]
files5=[]
files6=[]
for direc1 in dirs1:
       file1=glob.glob(os.path.join(image_pathOrissa,direc1))
       files1.extend(file1)
for direc2 in dirs2:
       file2=glob.glob(os.path.join(image_pathMaha,direc2))
       files2.extend(file2)
for direc3 in dirs3:
       file3=glob.glob(os.path.join(image_pathKer,direc3))
       files3.extend(file3)
for direc4 in dirs4:
       file4=glob.glob(os.path.join(image_pathKar,direc4))
       files4.extend(file4)
for direc5 in dirs5:
       file5=glob.glob(os.path.join(image_pathGuj,direc5))
       files5.extend(file5)
for direc6 in dirs6:
       file6=glob.glob(os.path.join(image_pathBihar,direc6))
       files6.extend(file6)
files=[]
files=files1+files2+files3+files4+files5+files6
'''

cropped_images_path = r"/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Satellite Dataset/Cropped_State_Files"
cropped_files = os.listdir(cropped_images_path)
files = []

#save the complete path name of all images in array files
for direc in cropped_files:
    file1 = glob.glob(os.path.join(cropped_images_path,direc))
    files.extend(file1)


df = pd.read_csv('/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Village_Labels/VillageLabels_ASSETS.csv')	#read the labels csv file of each indicator

#Extract the village codes and their corresponding labels and make a pandas series out of it.
village_code = df["Town/Village"].values
emp_label = df["Village_HHD_Cluster_ASSETS"].values
actual_labels= [ int(c) for c in emp_label]
s1 = pd.Series(actual_labels,index=list(village_code))	#The label of each village can be extracted by using village code as index
s2 = s1.groupby(s1.index).first()
#print(s2)

#Create a list of items having key-value pairs as file path without village code and the 2011 village code
wotif = map(lambda x: x.split('.tif')[0], files)
list_dict = []
for e in wotif:
    (a,b) = e[:-6], e[-6:]
    list_dict.append((a,b))
#print(list_dict)

'''
This this code snippet for each village we check its corresponding label in grouped pandas series s2 and then 
We create a new file path for each such village by concatenating its full path with @label_1/2/3/NULL 
'''
new_file_paths = []
for a,b in list_dict:
    try:
        label = s2[int(b)]
        x = a + b + '@label_' + str(label) #+ '.tif'
        new_file_paths.append(x)
    except KeyError:
        x = a + b + '@label_' + 'NULL' #+ '.tif'
        new_file_paths.append(x) 

#print(new_file_paths)

ll = map(lambda x: x.split('@label_')[1], new_file_paths)	#create a map 
anp = np.array(ll)
np.unique(anp,return_counts=True)
new_file_paths[0].split('@label_')[1]

assets_1 = []
assets_2 = []
assets_3 = []
assets_null = []

for e in new_file_paths:
    if(str(e.split('@label_')[1]) == '1'):
        assets_1.append(e)
    elif(str(e.split('@label_')[1]) == '2'):
        assets_2.append(e)
    elif(str(e.split('@label_')[1]) == '3'):
        assets_3.append(e)
    else:
        assets_null.append(e)

#Check
labelsss = map(lambda x:x.split('@label_')[1], assets_null)

#Check
pp = np.array(labelsss)
np.unique(pp)

#Check
print(len(assets_null) + len(assets_1)+ len(assets_2)+ len(assets_3))

assets_1[0].split('@label_')[0]

assets_1_tif = map(lambda x:x.split('@label_')[0]+'.tif', assets_1)
assets_2_tif = map(lambda x:x.split('@label_')[0]+'.tif', assets_2)
assets_3_tif = map(lambda x:x.split('@label_')[0]+'.tif', assets_3)
assets_null_tif = map(lambda x:x.split('@label_')[0]+'.tif', assets_null)

direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/Assets/1'
direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/Assets/2'
direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/Assets/3'
direc_null = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/Assets/null'

assets_1_path = []
for e in assets_1_tif:
    a,b = os.path.split(e)
    x = os.path.join(direc_1,b)
    assets_1_path.append(x)
for i in range(len(assets_1_tif)):
    print(i)
    copyfile(assets_1_tif[i], assets_1_path[i])


assets_3_path = []
for e in assets_3_tif:
    a,b = os.path.split(e)
    x = os.path.join(direc_3,b)
    assets_3_path.append(x)

for i in range(len(assets_3_tif)):
    #print(i)
    copyfile(assets_3_tif[i], assets_3_path[i])

assets_2_path = []
for e in assets_2_tif:
    a,b = os.path.split(e)
    x = os.path.join(direc_2,b)
    assets_2_path.append(x)
for i in range(len(assets_2_tif)):
    #print(i)
    copyfile(assets_2_tif[i], assets_2_path[i])

assets_null_path = []
for e in assets_null_tif:
    a,b = os.path.split(e)
    x = os.path.join(direc_null,b)
    assets_null_path.append(x)
for i in range(len(assets_null_tif)):
    #print(i)
    copyfile(assets_null_tif[i], assets_null_path[i])


