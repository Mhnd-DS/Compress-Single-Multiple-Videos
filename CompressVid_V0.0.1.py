#!/usr/bin/env python
# coding: utf-8

# In[]

def Vid_Info(src):
    video_Extenstion = src.suffix

    output_File = (Path(src).parent).joinpath(src.stem+user_convertType)
    return video_Extenstion, output_File
    


# ## File Case

# In[126]:


def Convert_OneVid(src, user_convertType):

    video_Extenstion, output_File = Vid_Info(src)
    
    if(output_File.exists()):
        raise Exception("File with the same desired format exists")
 
    converting_videoType(src,video_Extenstion, user_convertType)
    
# # Folder Case

# In[143]:

def Convert_MultipleVids(src, user_convertType):
    for filename in src.iterdir():
        print(filename)
        src = filename
        
        video_Extenstion, output_File = Vid_Info(src)
 
        
        if(video_Extenstion == user_convertType):
            continue
        try:
            Convert_OneVid(src, user_convertType)

        except:
            print('There is an existing file with the same requested format - This video has been skipped!! ('+src+')')
            continue
        

# In[107]:


def converting_videoType(src, video_Extenstion, user_convertType):
           
            
            inputfile = (Path(src).parent).joinpath(src.stem+video_Extenstion)
            
            print('This video will be converted to ('+user_convertType+')' , inputfile)
            
            outputfile = (Path(src).parent).joinpath(src.stem+user_convertType)
            
            print('New Video will be at:- ',outputfile)
            subprocess.call(['ffmpeg', '-i', inputfile, outputfile])
            
        


# In[144]:

# Calling main() function

import  sys
import subprocess
from pathlib import Path

import warnings
warnings.filterwarnings('error')


if __name__ == '__main__':
        U_input = input('Enter the path either a video path or \n'
                              'a directory path that contains multiple videos \n'
                              'Example of file path: /Downloads/myvideo.mp4 \n'
                              'Example of a directory: /Downloads/myvideos/\n')
    
        src = Path(U_input)     
        
        if(src.exists() != True):
            print('Path does NOT exists')
            sys.exit()
            
        print( '______________________')
        
        U_input = input('Enter the type you want to convert by, Examples [avi - mov - mp4 - mkv - etc..]\n')
        user_convertType = '.'+U_input.lower()
        
        print( '______________________')
        
        
        ##########
        
        src_Type = 'dir' if src.is_dir() else 'file'
    
        Convert_OneVid(src, user_convertType) if src_Type == 'file' else Convert_MultipleVids(src, user_convertType)

