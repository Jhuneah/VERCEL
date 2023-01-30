from ast import Try
from django.shortcuts import render,redirect
from pytube import YouTube
from pathlib import Path
from django.contrib import messages
import datetime
import moviepy.editor
from tkinter import Tk 
from tkinter.filedialog import askdirectory
from proglog import *
from tqdm import *



# Create your views here.
def index(request):
    yr=datetime.datetime.now().year

    if request.method=='POST':
        format=request.POST['format']
        if format.lower()=='video':
            try:
                # For Video Downloads
                link=request.POST['link']
                downloads_path = askdirectory(title='Select Folder')
                yt = YouTube(link)
                stream=yt.streams.get_highest_resolution()
                stream.download(downloads_path)
                print("Video Download successful!!!")
                
                messages.info(request,"Video Download successful!!!")
                return redirect('index')
            except:
                print("Download unsuccessful, please provide a valid link!!!")
                messages.info(request,"Download unsuccessful, please provide a valid link!!!")
                return redirect('index')
        elif format.lower()=='audio' :
            # For Audio downloads
            try:
                link=request.POST['link']
                downloads_path = askdirectory(title='Select Folder')
                yt = YouTube(link)
                stream=yt.streams.get_audio_only()
                stream.download(downloads_path)
                
                messages.info(request,"Audio Download successful!!!")
                return redirect('index')
            except:
                print("Download unsuccessful, please provide a valid link!!!")
                messages.info(request,"Download unsuccessful, please provide a valid link!!!")
                return redirect('index')
            
        else:
                print("Invalid format!!!")
                messages.info(request,"Invalid format!!!")
                return redirect('index')
                
        
    return render(request,'index.html',{'yr':yr})