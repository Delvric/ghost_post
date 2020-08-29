from django.shortcuts import render, reverse, HttpResponseRedirect

from ghost_postapp.models import GhostInput
from ghost_postapp.forms import GhostPostForm

html = 'index.html'


# Create your views here.
def index(request):
    data = GhostInput.objects.all().order_by('-submission_time')
    return render(request, html, {'data': data})


def ghost_postapp(request):
    if request.method == 'POST':
        form = GhostPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostInput.objects.create(
                boast_or_roast=data['boast_or_roast'],
                post=data['post'],
            )
        return HttpResponseRedirect(reverse('home'))

    form = GhostPostForm()
    return render(request, 'post.html', {'form': form})


def boasts(request):
    data = GhostInput.objects.filter(boast_or_roast=True).order_by('-submission_time')
    return render(request, html, {'data': data})


def roasts(request):
    data = GhostInput.objects.filter(boast_or_roast=False).order_by('-submission_time')
    return render(request, html, {'data': data})


def likes(request, id):
    post = GhostInput.objects.get(id=id)
    post.up_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))


def dislikes(request, id):
    post = GhostInput.objects.get(id=id)
    post.down_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))


def most_liked(request):
    data = GhostInput.objects.order_by('-up_votes')
    return render(request, html, {'data': data})


def least_liked(request):
    data = GhostInput.objects.order_by('up_votes')
    return render(request, html, {'data': data})