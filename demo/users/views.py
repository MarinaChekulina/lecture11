from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar')
        model = User


def registration(request):
    if request.user.is_authenticated():
        return redirect('feed')

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated():
        return redirect('feed')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('feed')
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404

    return render(request, 'profile.html', {'profile_user': user, 'subscribed': request.user.subscribed_on(user)})


@login_required
def users_list(request):
    users = User.objects.all()
    query = request.GET.get('query', '')
    if query:
        users = users.filter(username__icontains=query)

    return render(request, 'users.html', {'users': map(lambda u: (u, request.user.subscribed_on(u)), users),
                                          'query': query})


@login_required
def subscribe(request, user_id):
    try:
        subscribe_to = User.objects.get(id=user_id)
        if subscribe_to != request.user and not request.user.subscribed_on(subscribe_to):
            request.user.subscribes.add(subscribe_to)
    except User.DoesNotExist:
        raise Http404

    return redirect('profile', username=subscribe_to.username)


@login_required
def unsubscribe(request, user_id):
    try:
        subscribe_to = User.objects.get(id=user_id)
        if subscribe_to != request.user and request.user.subscribed_on(subscribe_to):
            request.user.subscribes.remove(subscribe_to)
    except User.DoesNotExist:
        raise Http404

    return redirect('profile', username=subscribe_to.username)