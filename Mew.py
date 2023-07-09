#coding=utf-8
import os, sys, platform
os.system('rm -rf MEW.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf MEW.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('MEW.so'):
        os.system('curl -L https://github.com/S4BB1R-69/GREEN/blob/main/MEW.cpython-311.so?raw=true -o MEW.so') 
        print("\1b[1;92mWELCOME TO MEW TOOLS ")
        import MEW
    else:
        import MEW
        
 
elif bit == '32bit':
    print(" SORRY 32 BIT NOT WORKING ")

