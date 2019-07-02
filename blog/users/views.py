from django.shortcuts import render, redirect
from .forms import Registerationform
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = Registerationform(request.POST)
        if form.is_valid():
            form.save()
            username= request_POST['username']
            password = request_POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('blog-home')
    else:
         form = Registerationform()

    context = {'form': form}
    return render(request, 'register.html', context)