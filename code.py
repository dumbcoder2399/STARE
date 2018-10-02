import numpy as np 
from zipfile import ZipFile 
import shutil
import os

source="/home/anushka/Desktop/database/all-images"

d1="/home/anushka/Desktop/database/Diagnosis/Emboli/"
d2="/home/anushka/Desktop/database/Diagnosis/BRAO/"
d3="/home/anushka/Desktop/database/Diagnosis/CRAO/"
d4="/home/anushka/Desktop/database/Diagnosis/BRVO/"
d5="/home/anushka/Desktop/database/Diagnosis/CRVO/"
d6="/home/anushka/Desktop/database/Diagnosis/Hemi-CRVO/"
d7="/home/anushka/Desktop/database/Diagnosis/BDR/"
d8="/home/anushka/Desktop/database/Diagnosis/PDR/"
d9="/home/anushka/Desktop/database/Diagnosis/ASR/"
d10="/home/anushka/Desktop/database/Diagnosis/HTR/"
d11="/home/anushka/Desktop/database/Diagnosis/Coat/"
d12="/home/anushka/Desktop/database/Diagnosis/Macro/"
d13="/home/anushka/Desktop/database/Diagnosis/CNV/"
d14="/home/anushka/Desktop/database/Diagnosis/Other/"


a=open("abc.txt")

x = []
for line in a.readlines():
    y = [value for value in line.split(  )]
    x.append( y )

data=np.asarray(x)
a.close()

files = os.listdir(source)

i=0
print (data[0])

for fee in files:
    f=source+"/"+fee
    list=data[i]
    for k in list:
        if (k=='1'):
            shutil.copyfile(f,d1+fee)
        elif (k=='2'):
            shutil.copyfile(f,d2+fee)
        elif (k=='3'):
            shutil.copyfile(f,d3+fee)
        elif (k=='4'):
            shutil.copyfile(f,d4+fee)
        elif (k=='5'):
            shutil.copyfile(f,d5+fee)
        elif (k=='6'):
            shutil.copyfile(f,d6+fee)
        elif (k=='7'):
            shutil.copyfile(f,d7+fee)
        elif (k=='8'):
            shutil.copyfile(f,d8+fee)
        elif (k=='9'):
            shutil.copyfile(f,d9+fee)
        elif (k=='10'):
            shutil.copyfile(f,d10+fee)
        elif (k=='11'):
            shutil.copyfile(f,d11+fee)
        elif (k=='12'):
            shutil.copyfile(f,d12+fee)
        elif (k=='13'):
            shutil.copyfile(f,d13+fee)
        elif (k=='14'):
            shutil.copyfile(f,d14+fee)

    i=i+1

    

