from django.shortcuts import render
from .models import Video
# Create your views here.

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'playlist/play_list.html', {'videos': videos})

def video_create(request):
    if request.method == "POST":
        # Тут нужно использовать .get('key') вместо ['key'], 
        # но ученикам это рано использовать.
        # + будут видеть сразу ошибки в debug если что-то не верно.
        title = request.POST['title']
        embed_code = request.POST['embed_code']
        Video.objects.create(title=title, embed_code=embed_code)
    return render(request, 'playlist/video_create.html')