from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from ..forms import UserRegistrationForm, NoteSearchForm
from ..models import Note


def user_profile(request, user_pk):
    """ Get user profile for any user on the site. 
    Any user may view any other user's profile. 
    """
    form = NoteSearchForm
    search_title = request.GET.get('search_title')
    
    user = User.objects.get(pk=user_pk)
    usernotes = Note.objects.filter(user=user.pk).order_by('-posted_date')

    if search_title:
        usernotes = Note.objects.filter(user=user.pk, title__icontains=search_title).order_by('-posted_date')
    return render(request, 'lmn/users/user_profile.html', {'user_profile': user, 'notes': usernotes, 'form': form, 'search_term': search_title})


@login_required
def my_user_profile(request):
    """ Get the currently logged-in user's profile """
    # TODO - editable version for logged-in user to edit their own profile
    return redirect('user_profile', user_pk=request.user.pk)


def register(request):
    """ Handles user registration flow

    GET request - show a user registration form.
    POST request - register a new user
    """

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user:
                login(request, user)
                return redirect('user_profile', user_pk=request.user.pk)
            else:
                messages.add_message(request, messages.ERROR, 'Unable to log in new user')
        else:
            messages.add_message(request, messages.INFO, 'Please check the data you entered')
            # include the invalid form, which will have error messages added to it. 
            # The error messages will be displayed by the template.
            return render(request, 'registration/register.html', {'form': form})

    form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
