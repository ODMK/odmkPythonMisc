# -*- coding: utf-8 -*-
# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header begin-----------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************
#
# __::((odmkPythonBasic.py))::__
#
# Clears all variables from the workspace & clears the Python console
#
# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header end-------------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************

import os
import csv
import locale
import collections

from odmkClear import *

# <<<import locale>>>
locale.getpreferredencoding()

# // *---------------------------------------------------------------------* //
clear_all()

print('\n')
print('// *--------------------------------------------------------------* //')
print('// *---::OS related activities::---*')
print('// *--------------------------------------------------------------* //')

print('\nshow environment variables:')
print(os.environ['PATH'])

print('\n')
print('// *--------------------------------------------------------------* //')

# When running a .py standalone (not importing) the default __name__ will be __main__
# can be used to create self-test function that only runs when
# the module runs standalone, bypassed when module is imported
print('\n"__name__" attribute currently = '+__name__)

print('\n"csv.__name__" attribute = '+csv.__name__)
print('"clear_all.__name__" attribute = '+clear_all.__name__)

print('\n')
print('// *--------------------------------------------------------------* //')

print('\nDefine a path+filename then split using os:')
gzFile = 'C:/usr/eschei/odmkPython/odmk/eye/imgSrc/barutanBreaks1.jpg'

gz_name = os.path.split(gzFile)[1]
gz_path = os.path.split(gzFile)[0]
print('\nImage Name = '+gz_name)
print('Image Path = '+gz_name)

print('\nRemove Filename extension:')
gz_name = gz_name.split('.')[0]
print('\nImage Name no extention = '+gz_name)


print('\n')
print('// *--------------------------------------------------------------* //')

print('\nGenerate a list of all files in a directory:\n')
imgSrcList = []
path =  'C:/usr/eschei/odmkPython/odmk/eye/imgSrc/process'
for filename in os.listdir(path):
    imgSrcList.append(filename)

print(imgSrcList)

# // *---------------------------------------------------------------------* //


print('\n')
print('// *--------------------------------------------------------------* //')

print('\nSearch for ".jpg" file in directory, store name if found:\n')

eyeDir = 'C:/usr/eschei/odmkPython/odmk/eye/imgSrc/exp1/'

try:
    for img in os.listdir(eyeDir):
        if img.endswith('.jpg'):
            eyeName = img
            print('\nfound at least one .jpg file: '+eyeName)
            eye_name = eyeName.split("00")[0]
            print('\nSet eye_name = "'+eye_name+'"')
            break
    if not('eye_name' in locals()):
        print('\nError: No .jpg files found in directory')        
except OSError:
    print('\nError: directory:\n'+eyeDir+'\ncannot be found')


print('\n')
print('// *--------------------------------------------------------------* //')
print('// *---::Search for .jpg images in eyeDir directory::---*')
print('// *--------------------------------------------------------------* //')

eyeDir = 'C:/usr/eschei/odmkPython/odmk/eye/imgSrc/exp1/'

# generate list all files in a directory
imgSrcList = []
try:
    for filename in os.listdir(eyeDir):
        if img.endswith('.jpg'):
            imgSrcList.append(filename)
    if imgSrcList == []:
        print('\nError: No .jpg files found in directory\n')
    else:
        imgCount = len(imgSrcList)
        print('\nFound '+str(imgCount)+' images in the eyeDir directory!')
        eye_name = imgSrcList[0]
        eye_name = eye_name.split("00")[0]
        print('\nSet eye_name = "'+eye_name+'"')
        print('\nCreated numpy array: <<imgSrcList>>\n')
except OSError:
    print('\nError: directory:\n'+eyeDir+'\ncannot be found\n')
    
print('// *--------------------------------------------------------------* //')


print('\n')
print('// *--------------------------------------------------------------* //')
print('// *---::Load CSV file into OBJ "sinesrc"::---*')
print('// *--------------------------------------------------------------* //')

sinesrc = u'C:\\usr\\eschei\\odmkPython\\odmk\\audio\\csvsrc\\sintest1.csv'

# reads .csv data into Python List:
datain = []
with open(sinesrc, mode='r') as infile:
    for line in infile.readlines():
        l,dumb = line.strip().split(',')
        datain.append((l))

print('\nLoaded file: ')

lgth = len(list(datain))    # get length by iterating csvin obj (only way?)
print('Length of datain = '+str(lgth))


print('\n')
print('// *--------------------------------------------------------------* //')
print('// *---::Bits Bytes etc..::---*')
print('// *--------------------------------------------------------------* //')


x = int('00100001', 2)  # >>> 33

x = int('0xff', 16)  # >>> 255
x = int('ff', 16)  # >>> 255

# convert TO Hex String:

x = "0x%x" % (int('00100001',2))  # >>> '0x21'


print('\n')
print('// *--------------------------------------------------------------* //')
print('// *---::Open file in binary mode and read bytes::---*')
print('// *--------------------------------------------------------------* //')

wavfile = 'C:\\usr\\eschei\\odmkPython\\odmk\\audio\\wavsrc\\rmeWav\\100_24\\100_24.wav'

print('<<\nOpen Wave File>>\n')
print('-opens a file in binary mode (supports mixed text/numerical data)-\n')
# Append .wav extension if necessary
if (len(wavfile.split(".")) <= 1):  # splits text at '.' => ['name', 'ext']
    wavfile = wavfile+'.wav'

# Append .wav extension if necessary
if (len(wavfile.split(".")) <= 1):  # splits text at '.' => ['name', 'ext']
    wavfile = wavfile+'.wav'

# open wav file in read mode
try:
    fwav = open(wavfile, 'rb')
    fwav_path, fwav_name = os.path.split(wavfile)
    print('Loaded WAV File: '+str(fwav_name))
    print('WAV File Path = '+str(fwav_path))
except IOError:
    print('Error: File does not exist')

print('\n// *----------------------------------------------------------* //\n')
print('::Detect RIFF Chunk::\n')

# read 4 bytes (default = string)
# original used scilab 'stripblanks' command, do we need this?
# ID = fwav.read(4)    # 4 bytes chunk ID
# Filed opened in binary mode, so use decode to convert ID bytes to Char
ID = fwav.read(4).decode('UTF-8')    # 4 bytes chunk ID
# check to make sure the ID matches with riff, (microsoft wave format ID)
if ( not(str(ID)=='riff' or str(ID)=='RIFF') ):
    print('.wav file does not contain the RIFF identifier')
else:
    print('chunk ID: '+str(ID))

Size = fwav.read(4)    # ?4 bytes Chunk Size in bytes
# pdb.set_trace()
#    # worked for python2.7, not 3.x
#    asciiSize = [ord(c) for c in Size]  # ord() converts a string to its ascii value
#    # !*little endian format
#    Size = int(str(asciiSize[3]) + str(asciiSize[2]) + str(asciiSize[1]) + str(asciiSize[0]))

# ***need to verify how the chunk size is calculated***
Size = int(str(Size[3]) + str(Size[2]) + str(Size[1]) + str(Size[0]))
print('chunk size: '+str(Size))
rifftype = fwav.read(4).decode('UTF-8')
dtype = str(rifftype)
print('dtype: '+dtype)
if ( not(dtype=='wave' or dtype=='WAVE') ):
    print('error: .wav file does not contain the wave identifier')


print('\n')
print('// *--------------------------------------------------------------* //')
print('// *---::Create Ordered Dictionary::---*')
print('// *--------------------------------------------------------------* //')

print('\n-initializes an ordered dictionary with tuple list-\n')

# **NG - passes keys/values as "Unordered kwargs", then Dict is unordered
# gorgulan = collections.OrderedDict(g = (1, 0, 1), o = (3, 1, 3), r = (7, 7, 7), t = (5, 6, 7))

# to init an ordered dict, first create a list or tuple
gort_init = [('g', ('gorgulan', 'great')), ('o', ('outer', 'base')),
             ('r', ('space', 'beast')), ('t', ('bar', 'bat'))]

print('Create INIT tuple:')
print(gort_init)

gorgulan = collections.OrderedDict(gort_init)

print('\nPrint ordered Keys:')
for key in gorgulan.keys():
    print(key)

print('\nOutput ordered Keys as a list:')
gortKeyList = list(gorgulan.keys())
print(gortKeyList)

print('\nPrint ordered Values:')
for key in gorgulan.keys():
    print(gorgulan[key])

print('\nPrint Full Dictionary:')
for key in gorgulan.keys():
    print(key+' = '+str(gorgulan[key]))

print('\nUpdate Dict with new entry:')
gorgulan.update([('z', ('UB313', '93'))])
for key in gorgulan.keys():
    print(key+' = '+str(gorgulan[key]))

print('\nPop item from Gorgulan Dict:')    
gpop = gorgulan.popitem()
print(gpop)

print('\n')
print('// *--------------------------------------------------------------* //')
print('// *---::end::---*')
print('// *--------------------------------------------------------------* //')