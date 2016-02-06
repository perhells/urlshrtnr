from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app.models import ShortenedURL
from app.forms import CreateForm

def make(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        shortened = request.POST.get('shortened')
        try:
            shortened_url = ShortenedURL.objects.get(shortened=shortened)
            if shortened_url:
                return HttpResponseRedirect('/exists/')
            else:
                new_shortened_url = ShortenedURL(shortened=shortened, url=url)
                new_shortened_url.save()
                return HttpResponseRedirect('/success/')
        except:
            new_shortened_url = ShortenedURL(shortened=shortened, url=url)
            new_shortened_url.save()
            return HttpResponseRedirect('/success/'+shortened)
    else:
        form = CreateForm()
        context = {'form': form}
        return render(request, 'make.html', context)

def go(request,shortened):
    try:
        shortened_url = ShortenedURL.objects.get(shortened=shortened)
        if shortened_url:
            return HttpResponseRedirect(shortened_url.url)
        else:
            return HttpResponseRedirect('/invalid/')
    except:
        return HttpResponseRedirect('/invalid/')

def exists(request):
    return render(request, 'exists.html')

def success(request,shortened):
    context = {'shortened': shortened}
    return render(request, 'success.html', context)

def invalid(request):
    return render(request, 'invalid.html')
