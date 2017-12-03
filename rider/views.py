from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from .models import Rider_profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def rider(request):
  return render(request, 'riders/rider.html')


def update_profile(request,username):
  user = User.objects.get(username = username)
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance = request.user)
    profile_form = ProfileForm(request.POST, instance =request.user.rider_profile, files = request.FILES)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, ('Your profile was successfully updated!'))
      return redirect(reverse('profile', kwargs = {'username': request.user.username}))
    else:
      messages.error(request, ('Please correct the error below.'))

  else:
    user_form = UserForm(instance = request.user)
    profile_form = ProfileForm(instance = request.user.rider_profile)
  return render(request, 'riders/profiles/profile_form.html', {"user_form":user_form, "profile_form":profile_form})

@login_required
def profile(request, username):
  user = User.objects.get(username =username)
  if not user:
    return redirect('rider')
  profile = Rider_profile.objects.get(user =user)
  print(profile.profile_pic)

  title = f"{user.username}"

  return render(request, 'riders/profiles/profile.html', {"title":title, "user":user, "profile": profile})

