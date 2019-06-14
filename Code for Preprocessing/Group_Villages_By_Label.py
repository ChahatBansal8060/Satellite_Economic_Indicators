import os
import glob
import pandas as pd
import numpy as np
from shutil import copyfile
from shutil import move
import pandas as pd


def Split_Villages_By_Label(cropped_images_path, labels_file_path, label_column_name, direc_1, direc_2, direc_3, direc_null):
    
    cropped_files = os.listdir(cropped_images_path)
    df = pd.read_csv(labels_file_path)

    #Extract the village codes and their corresponding labels and make a pandas series out of it.
    village_code = df["Town/Village"].values
    emp_label = df[label_column_name].values
    actual_labels= [ int(c) for c in emp_label]
    s1 = pd.Series(actual_labels,index=list(village_code))	#The label of each village can be extracted by using village code as index
    s2 = s1.groupby(s1.index).first()

    label_1_villages_filepaths = []
    label_2_villages_filepaths = []
    label_3_villages_filepaths = []
    label_null_villages_filepaths = []

    for village in cropped_files:
        vCode =  (village.split('.tif')[0])[-6:]
        if(int(vCode) in s2):
            label = s2[int(vCode)]
            if (label == 1):
                label_1_villages_filepaths.append(village)
            else:
                if (label == 2):
                    label_2_villages_filepaths.append(village)
                else:
                    if (label == 3):
                        label_3_villages_filepaths.append(village)
        
        else:
            label_null_villages_filepaths.append(village)
    

    print(len(label_1_villages_filepaths))
    print(len(label_2_villages_filepaths))
    print(len(label_3_villages_filepaths))
    print(len(label_null_villages_filepaths))

    for village in label_1_villages_filepaths:
        copyfile(cropped_images_path+'/'+village, direc_1+'/'+village)

    for village in label_2_villages_filepaths:
        copyfile(cropped_images_path+'/'+village, direc_2+'/'+village)

    for village in label_3_villages_filepaths:
        copyfile(cropped_images_path+'/'+village, direc_3+'/'+village)

    for village in label_null_villages_filepaths:
        copyfile(cropped_images_path+'/'+village, direc_null+'/'+village)


def main():
    cropped_images_path = r"/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Satellite Dataset/Cropped_State_Files"

    print("\n Working on Assets Parameter")
    labels_file_path = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Village_Labels/VillageLabels_ASSETS.csv'
    label_column_name = "Village_HHD_Cluster_ASSETS"
    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/Assets/1'
    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/Assets/2'
    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/Assets/3'
    direc_null = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/Assets/null'
    Split_Villages_By_Label(cropped_images_path, labels_file_path, label_column_name, direc_1, direc_2, direc_3, direc_null)

    print("\n Working on BF Parameter")
    labels_file_path = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Village_Labels/VillageLabels_BF.csv'
    label_column_name = "Village_HHD_Cluster_BF"
    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/BF/1'
    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/BF/2'
    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/BF/3'
    direc_null = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/BF/null'
    Split_Villages_By_Label(cropped_images_path, labels_file_path, label_column_name, direc_1, direc_2, direc_3, direc_null)

    print("\n Working on CHH Parameter")
    labels_file_path = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Village_Labels/VillageLabels_CHH.csv'
    label_column_name = "Village_HHD_Cluster_CHH"
    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/CHH/1'
    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/CHH/2'
    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/CHH/3'
    direc_null = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/CHH/null'
    Split_Villages_By_Label(cropped_images_path, labels_file_path, label_column_name, direc_1, direc_2, direc_3, direc_null)

    print("\n Working on EMP Parameter")
    labels_file_path = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Village_Labels/VillageLabels_EMP.csv'
    label_column_name = "Village_HHD_Cluster_EMP"
    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/EMP/1'
    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/EMP/2'
    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/EMP/3'
    direc_null = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/EMP/null'
    Split_Villages_By_Label(cropped_images_path, labels_file_path, label_column_name, direc_1, direc_2, direc_3, direc_null)

    print("\n Working on FC Parameter")
    labels_file_path = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Village_Labels/VillageLabels_FC.csv'
    label_column_name = "Village_HHD_Cluster_FC"
    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/FC/1'
    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/FC/2'
    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/FC/3'
    direc_null = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/FC/null'
    Split_Villages_By_Label(cropped_images_path, labels_file_path, label_column_name, direc_1, direc_2, direc_3, direc_null)

    print("\n Working on MSL Parameter")
    labels_file_path = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Village_Labels/VillageLabels_MSL.csv'
    label_column_name = "Village_HHD_Cluster_MSL"
    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSL/1'
    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSL/2'
    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSL/3'
    direc_null = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSL/null'
    Split_Villages_By_Label(cropped_images_path, labels_file_path, label_column_name, direc_1, direc_2, direc_3, direc_null)

    print("\n Working on MSW Parameter")
    labels_file_path = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Village_Labels/VillageLabels_MSW.csv'
    label_column_name = "Village_HHD_Cluster_MSW"
    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSW/1'
    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSW/2'
    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSW/3'
    direc_null = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSW/null'
    Split_Villages_By_Label(cropped_images_path, labels_file_path, label_column_name, direc_1, direc_2, direc_3, direc_null)



if __name__ == '__main__':
    main()



