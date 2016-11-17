from django.db.models import Q
from django import forms
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from instagram_filters import filters

from .models import Post, Like, Comment


def index(request):
    if request.user.is_authenticated():
        return redirect('feed')

    return redirect('login')


@login_required
def feed(request):
    posts = Post.objects.filter(Q(user=request.user.subscribes.all()) | Q(user=request.user)).order_by('-created_at')

    return render(request, 'feed.html', context={'posts': map(lambda p: (p, p.liked_by(request.user)), posts)})


class CreatePostForm(forms.ModelForm):
    name_to_filter = {
        'nashville': filters.Nashville,
        'kelvin': filters.Kelvin,
        'toaster': filters.Toaster,
        'gotham': filters.Gotham,
        'lomo': filters.Lomo
    }
    image_filter = forms.ChoiceField(choices=((None, 'Без фильтра'),
                                              ('nashville', 'Nashville'),
                                              ('kelvin', 'Kelvin'),
                                              ('toaster', 'Toaster'),
                                              ('gotham', 'Gotham'),
                                              ('lomo', 'Lomo'),),
                                     initial=None,
                                     label='Фильтр',
                                     required=False)

    def __init__(self, user, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.user = user

    class Meta:
        model = Post
        fields = ('image', 'text')

    def save(self, commit=False):
        instance = super(CreatePostForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
            if self.cleaned_data['image_filter']:
                self.name_to_filter[self.cleaned_data['image_filter']](instance.image.path).apply()

        return instance


@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save(True)
            return redirect('feed')
    else:
        form = CreatePostForm(request.user)

    return render(request, 'create_post.html', {'form': form})


@login_required
def like(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        if request.POST.get('delete') == 'True':
            Like.objects.filter(user=request.user, post=post).delete()
        else:
            Like.objects.get_or_create(user=request.user, post=post)
    except Post.DoesNotExist:
        raise Http404

    return redirect('feed')


@login_required
def add_comment(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        text = request.POST.get('comment')
        if text:
            Comment.objects.create(user=request.user, text=text, post=post)
        else:
            Like.objects.get_or_create(user=request.user, post=post)
    except Post.DoesNotExist:
        raise Http404

    return redirect('feed')
