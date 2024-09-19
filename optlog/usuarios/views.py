# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile

@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            profile = form.save()
            request.user.first_name = profile.first_name
            request.user.last_name = profile.last_name
            request.user.save()
            return redirect('core:admin_panel')
        else:
            print("Form errors:", form.errors)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'usuarios/edit_profile.html', {'form': form})
