import os
import glob
import pandas as pd
import numpy as np
from shutil import copyfile
from shutil import move
import pandas as pd
import random

'''
This function takes 80% of the randomly shuffled data as training data and remaining 20% as test data for each label of each indicator.
'''
def Create_Training_Test_Set(path):
    villages = os.listdir(path)
    
    file_count = len(villages)
    ir = np.arange(file_count)
    ir = np.asarray(ir,dtype=np.int32)
    random.shuffle(ir)
    training_count = int(0.8 * file_count)
    training_indices = ir[:training_count]
    test_indices = ir[training_count:]

    print("\n#training files: ",len(training_indices))
    print("\n#testing files: ",len(test_indices))

    training_set = []
    test_set = []
    for index in training_indices:
        training_set.append(villages[index])

    for index in test_indices:
        test_set.append(villages[index])    

    return training_set, test_set


'''
This function copies training and test data into target directories.
'''
def Copy_Files(train_path, test_path, direc, tr, te):
    for village in tr:
        copyfile(direc+'/'+village, train_path+'/'+village)

    for village in te:
        copyfile(direc+'/'+village, test_path+'/'+village)


def main():    
    print("\n Working on ASSETS Parameter")
    train_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/ASSETS/Training_Dataset"
    test_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/ASSETS/Test_Dataset"
    
    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/Assets/1'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_1, tr, te)
    
    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/Assets/2'
    tr, te = Create_Training_Test_Set(direc_2)
    Copy_Files(train_path, test_path, direc_2, tr, te)
    
    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/Assets/3'
    tr, te = Create_Training_Test_Set(direc_3)
    Copy_Files(train_path, test_path, direc_3, tr, te)
    
    
    print("\n Working on BF Parameter")
    train_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/BF/Training_Dataset"
    test_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/BF/Test_Dataset"

    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/BF/1'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_1, tr, te)

    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/BF/2'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_2, tr, te)

    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/BF/3'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_3, tr, te)

    print("\n Working on CHH Parameter")
    train_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/CHH/Training_Dataset"
    test_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/CHH/Test_Dataset"

    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/CHH/1'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_1, tr, te)

    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/CHH/2'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_2, tr, te)

    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/CHH/3'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_3, tr, te)

    print("\n Working on EMP Parameter")
    train_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/EMP/Training_Dataset"
    test_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/EMP/Test_Dataset"

    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/EMP/1'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_1, tr, te)

    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/EMP/2'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_2, tr, te)

    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/EMP/3'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_3, tr, te)

    print("\n Working on FC Parameter")
    train_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/FC/Training_Dataset"
    test_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/FC/Test_Dataset"

    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/FC/1'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_1, tr, te)

    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/FC/2'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_2, tr, te)

    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/FC/3'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_3, tr, te)
    

    print("\n Working on MSL Parameter")
    train_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/MSL/Training_Dataset"
    test_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/MSL/Test_Dataset"

    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSL/1'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_1, tr, te)

    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSL/2'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_2, tr, te)

    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSL/3'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_3, tr, te)

    print("\n Working on MSW Parameter")
    train_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/MSW/Training_Dataset"
    test_path = "/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Training_Test_Data/MSW/Test_Dataset"

    direc_1 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSW/1'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_1, tr, te)

    direc_2 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSW/2'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_2, tr, te)

    direc_3 = '/home/chahat/Desktop/PhD Research/Satellite for socio-economic indicators/Project/Label_wise_villages/MSW/3'
    tr, te = Create_Training_Test_Set(direc_1)
    Copy_Files(train_path, test_path, direc_3, tr, te)


if __name__ == '__main__':
    main()




