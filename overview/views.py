from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Activity, Group, UserA, UserGroup




def home(request):
    content = {
        'activities': Activity.objects.all(),
        'users': UserA.objects.all()
        #TODO add pagnation
    }
    return render(request, 'overview/overview.html', content)

def activity(request):
    content = {
        'activities': Activity.objects.filter(startTime__date=timezone.now()).order_by('activityName'),
        'users': UserA.objects.all()
    }
    return render(request, 'overview/overview-activity.html', content)

def time(request):
    content = {
        'activities': Activity.objects.filter(startTime__date=timezone.now()).order_by('startTime__hour', 'startTime__minute'),
        'users': UserA.objects.all()
    }
    return render(request, 'overview/overview-time.html', content)

def user(request):
    content = {
        'activities': Activity.objects.all(),
        'users': UserA.objects.all()
    }
    return render(request, 'overview/overview-user.html', content)

def testPage(request):
    content = {
        'testdata' : Activity.objects.last(),
        'users' : UserA.objects.all()
    }
    return render(request, 'overview/test.html', content)



