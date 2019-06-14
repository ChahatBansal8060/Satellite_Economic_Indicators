import os
import glob

cropped_images_direc =  r'/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Satellite Dataset/Cropped_State_Files'
cropped_files = os.listdir(cropped_images_direc)	#All cropped image files in the above directory
print("\nNumber of files in unprocessed cropped images: ",len(cropped_files))


village_list = dict()

for x in cropped_files:
    vCode2011 = (x.split('@')[3]).split('.')[0]
    if(vCode2011 in village_list):
        try: 
            #print("Deleting village ",x)
            os.remove(cropped_images_direc+'/'+x)
        except:
            #print("Error")
            continue
    else:
        village_list[vCode2011] = True

cropped_files = os.listdir(cropped_images_direc)	#All cropped image files in the above directory
print("\nNumber of files after duplicate removal in cropped images: ",len(cropped_files))


