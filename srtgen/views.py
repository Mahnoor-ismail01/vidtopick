from re import S
from django.shortcuts import redirect, render, reverse
import os
# importing the module 
import youtube_dl 
from django.conf import settings
import subprocess as sp
from whoosh_index_and_search_file_content import srtsearch
from .models import Srtgen, Favourites
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
        
        file_location = os.path.join(str(settings.BASE_DIR) , "videos" ,filename+".mp4")

        file_location1 = os.path.join(str(settings.BASE_DIR) , "previews" ,filename+".mp4")
        clip=VideoFileClip(file_location)
        
        # getting subclip
        clip = clip.subclip(0, 10)

        
        
        previewoutput=file_location1
        clip.write_videofile(previewoutput)

        ic(request.POST.getlist('public'))
        theObject = Srtgen.objects.create(user=request.user.authuser,title=request.POST["title"], link=request.POST["link"], public=True if len(request.POST.getlist('public')) != 0 else False)
        os.chdir("..")
        from django.core.files import File
        with open(file_location1, 'rb') as fi:
            theObject.preview = File(fi, name=os.path.basename(filename+".mp4"))
            theObject.save()
        os.remove(file_location1)

        
        with open("Hi.srt", 'rb') as fi:
            theObject.file = File(fi, name=os.path.basename(filename+".srt"))
            theObject.save()
        return redirect(reverse("preview", kwargs={"srt_id": theObject.id }))
        # MODEL_SCRIPT_PATH = os.path.join(str(settings.BASE_DIR),"py-srt-generator")
       
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
        
        

        



    context={}
    return render(request,"uploadLink.html",context)


search_hwe_results = []
def previewvideo(request,srt_id):
    obj=Srtgen.objects.get(id=srt_id)
    a=obj.file.url
    print(a , "ppp")
    aname=os.path.basename(a)

    f = open(obj.file.path,'r')
    srt_content = f.read()
    f.close()


    
    if request.user.authuser==obj.user:
        messages.success(request,"available")
        context={"obj":obj,"pathsrt":aname,"srt":srt_content }
        
       
        
    else:
       context={"obj":None}
       messages.success(request,"not available")
    if request.method=="POST":
        val=request.POST["key"]
        v=val.split(",")
        appendd=str(settings.BASE_DIR)+str(a)
        
        print(appendd,"hahha")
        ic(str(appendd))
        ic(v)
        results=srtsearch(appendd,v)
        print(results)
        global search_hwe_results
        search_hwe_results = results
        

        return redirect(reverse("search_results", kwargs={"srt_id": srt_id }))



    return render(request,"newpreview.html",context)
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

def search_results_view(request, srt_id):
    ic(search_hwe_results)
    obj=Srtgen.objects.get(id=srt_id)
    a=obj.file.url
    print(a , "ppp")
    aname=os.path.basename(a)

    f = open(obj.file.path,'r')
    srt_content = f.read()
    f.close()


    
    if request.user.authuser==obj.user:
        messages.success(request,"available")
        context={"obj":obj,"pathsrt":aname,"srt":srt_content }
        
       
        
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



    return render(request,"searchResults.html",context)


def fav(request,srt_id):
    obj=Srtgen.objects.get(id=srt_id)
    Favourites.objects.create(user=request.user.authuser,link=obj)
    return redirect(reverse("history"))

def unfav(request, srt_id):
    obj=Srtgen.objects.get(id=srt_id)
    Favourites.objects.filter(user=request.user.authuser,link=obj).delete()
    return redirect(reverse("history"))
