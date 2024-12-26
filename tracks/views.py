from django.shortcuts import render, redirect, get_object_or_404
from .models import Track



def home(request):
    return render(request, 'index.html')

def track_list(request):
    tracks = Track.objects.all()
    ctx = {'tracks': tracks}
    return render(request, 'tracks/music-list.html', ctx)

def track_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        data = request.POST.get('data')
        image = request.FILES.get('image')
        file = request.FILES.get('file')
        if title and artist and album and genre and data and image and file:
            Track.objects.create(
                title = title,
                artist = artist,
                album = album,
                genre = genre,
                data = data,
                image = image,
                file = file,
            )
            return redirect('tracks:list')
    return render(request, 'tracks/music-create.html')

def track_detail(request, detail_id):
    tracks = get_object_or_404(Track, pk=detail_id)
    ctx = {'tracks': tracks}
    return render(request, 'tracks/music-detail.html', ctx)

def music_update(request, update_id):
    track = get_object_or_404(Track, pk=update_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        data = request.POST.get('data')
        image = request.FILES.get('image')
        file = request.FILES.get('file')
        if title and artist and album and genre and data and image and file:
            track.title = title
            track.artist = artist
            track.album = album
            track.genre = genre
            track.data = data
            track.image = image
            track.file = file
            track.save()
            return redirect('tracks:list')
    ctx = {'track':track}
    return render(request, 'tracks/music-create.html', ctx)

def music_delete(request, del_id):
    tracks = get_object_or_404(Track, pk=del_id)
    if request.method == 'POST':
        tracks.delete()
        return redirect('tracks:list')
    ctx = {'tracks': tracks}
    return render(request, 'tracks/music-delete-confirm.html', ctx)

