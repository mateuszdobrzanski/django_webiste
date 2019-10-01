from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            # create flash message with redirection
            messages.success(request, f'Your account bas been created! You are able to log in.')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request,
                  'users/register.html',
                  {
                      'form': form
                  })


# using this decorator for: user must be logged to see this view
@login_required
def profile (request):
    return render(request,
                  'users/profile.html')
