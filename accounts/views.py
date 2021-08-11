from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from accounts.forms import ProfileForm
from django.shortcuts import redirect, render


@login_required
def user_home_page(request, pk):
    profile = Profile.objects.get(pk=pk)
    if profile.is_complete:
        context = {
            "profile": profile,
        }
        return render(request, 'profile/user_home_page.html', context)
    else:
        return redirect('complete profile')



def complete_profile(request):
    profile = Profile.objects.get(pk=request.user.pk)
       
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile.is_complete = True
            profile.save()
            form.save()
            return redirect('user home page', pk=request.user.pk)
        else:
            form = ProfileForm(instance=profile)
            context = {
                "form": form,
            }
            return redirect('user home page', pk=request.user.pk)
        
    form = ProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile/complete_profile.html', context)



def edit_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user home page', pk=pk)
        else:
            return redirect('edit profile', pk=pk)
    form = ProfileForm(instance=profile)
    context ={
        "form":form,
    }
    return render(request, 'profile/edit_profile.html', context)
