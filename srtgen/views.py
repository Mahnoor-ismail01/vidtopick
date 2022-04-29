from django.shortcuts import render
import os
# importing the module 
import youtube_dl 
from django.conf import settings
import subprocess as sp
# Create your views here.
def uploadlink(request):
    if request.method=="POST":
        print(request.POST["link"])
        os.chdir("videos")
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
        print(file_location)
        args = [
            "python3", 
            f"{MODEL_SCRIPT_PATH}/run.py", 
            file_location,
            f"{filename}.srt",
        ]
        print(" ".join(args))
        logs = sp.run(args)
        print(logs)
        with open(f'{MODEL_SCRIPT_PATH}/{filename}.srt', 'r') as f:
            file = f.read().split('\n')
            new_text = "<br>".join(file)
            print(file)
        



    
    return render(request,"index.html",{})