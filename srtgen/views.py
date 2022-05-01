from django.shortcuts import render
import os
# importing the module 
import youtube_dl 
from django.conf import settings
import subprocess as sp
from whoosh_index_and_search_file_content import srtsearch
from .models import Srtgen
from moviepy.editor import *
from icecream import ic
from django.contrib import messages
from users.models import AuthUser
from django.http.response import HttpResponse
import mimetypes

# Create your views here.
def uploadlink(request):
    if request.method=="POST":
        print(request.POST["link"])
        videofolder=os.path.join(str(settings.BASE_DIR),"videos")
        os.chdir(videofolder)
        filename=request.user.username+'_'+str(request.user.id)+'_'+request.POST["title"]
        
    

        url = request.POST["link"]
        ydl_opts = {
            'format': 'best',
            'outtmpl': filename+".mp4"
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        MODEL_SCRIPT_PATH = os.path.join(str(settings.BASE_DIR),"py-srt-generator")
       
        file_location = os.path.join(str(settings.BASE_DIR) , "videos" ,filename+".mp4")
        #print(file_location)
       # args = [
        #    "python3", 
        #    f"{MODEL_SCRIPT_PATH}/run.py", 
        #    file_location,
        #    f"{filename}.srt",
        #]
        #print(" ".join(args))
        #logs = sp.run(args)
       # print(logs)
       # with open(f'py-srt-generator/Hi.srt', 'r') as f:
        #    file = f.read().split('\n')
         #   new_text = "<br>".join(file)
          #  print(file)
        #results=srtsearch("py-srt-generator/Hi.srt")
        
        file_location1 = os.path.join(str(settings.BASE_DIR) , "previews" ,filename+".mp4")
        clip=VideoFileClip(file_location)
        
        # getting subclip
        clip = clip.subclip(0, 10)

        
        
        # saving the clip
        previewoutput=file_location1
        clip.write_videofile(previewoutput)

        



    context={}
    return render(request,"index.html",context)
def previewvideo(request,srt_id):
    obj=Srtgen.objects.get(id=srt_id)
    a=obj.file.url
    print(a , "ppp")
    aname=os.path.basename(a)

    

    
    if request.user.authuser==obj.user:
        messages.success(request,"available")
        context={"obj":obj,"pathsrt":aname}
        
       
        
    else:
       context={"obj":None}
       messages.success(request,"not available")
    if request.method=="POST":
        val=request.POST["key"]
        v=val.split(",")
        appendd=str(settings.BASE_DIR)+str(a)
        
        print(appendd,"hahha")
        
        results=srtsearch(appendd,v)
        print(results)



    return render(request,"preview.html",context)
def download_file2(request, driverFile):
    # Define Django project base directory
    
    # Define text file name
    filename = driverFile

    # Define the full file path
    filepath = os.path.join(settings.BASE_DIR,"media","srt_uploaded",driverFile)
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

