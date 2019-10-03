from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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
def profile(request):
    return render(request,
                  'users/profile.html')

# using this decorator for: user must be logged to see this view
@login_required
def profile_update(request):
    if request.method == 'POST':
        # in brackets current information populated to the form
        user_form = UserUpdateForm(request.POST,
                                   instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account bas been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request,
                  'users/profile_update.html',
                  context)
