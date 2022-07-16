from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from rest_framework.authtoken.models import Token


from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    form = UserCreationForm()
    context = {'form': form}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            return redirect('/login')

    return render(request, 'register.html', context)


def GenerateTokenView(request, pk):
    print(request.POST.get('token'))
    user = get_object_or_404(User, id=request.POST.get('token'))
    try:
        Token.objects.get(user_id=request.POST.get('token')).delete()
        Token.objects.create(user_id=request.POST.get('token'))
    except:
        Token.objects.create(user_id=request.POST.get('token'))

    return redirect('home')





