import imp
from django.urls import path
from .views import *
urlpatterns = [
    path('uploadlink/', uploadlink, name='uploadlink'),
    path('preview/<int:srt_id>/',previewvideo,name="preview"),
    path('download/<str:driverFile>/',download_file2,name="downloadsrt")
]
