from django.shortcuts import render
from profiles.models import Profile

# Create your views here.

def main_view(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try: 
        profile = Profile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
        print('id',profile.id)
    except:
        pass
    print(request.session.get_expiry_date())

    return render(request, "main.html",{})