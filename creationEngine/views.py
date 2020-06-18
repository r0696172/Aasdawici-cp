from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from overview.models import *


# Create your views here.

def home(request):
    return render(request, 'creationEngine/home.html')


def createUser(request):
    form = UserAForm()
    content = { 'form' : form }

    if request.method == 'POST':
        #print('printnig POST request', request.POST)
        form = UserAForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('userName')
            messages.success(request, 'account created for {}'.format(username))
            return redirect('creationEngine-createUser')

    return render(request, 'creationEngine/createUser.html', content)

def deleteUser(request, id):
    user = UserA.objects.get(userID=id)
    
    if request.method == 'POST':
        user.delete()
        messages.warning(request, 'account deleted for {}'.format(user.userName))
        return redirect('/')
    content = { 'user' : user }
    return render(request, 'creationEngine/deleteUser.html', content)

def createActivity(request):
    form = ActivityForm()
    content = {'form' : form}

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            activityName = form.cleaned_data.get('activityName')
            messages.success(request, 'Activty created: {}'.format(activityName))
            return redirect('/')

    return render(request, 'creationEngine/createActivity.html', content)

def deleteActivity(request, id):
    activity = Activity.objects.get(activityID=id)

    if request.method == 'POST':
        messages.warning(request, 'account deleted for {}'.format(activity.activityName))
        activity.delete()
        return redirect('/')
    content = {'activity':activity}
    return render(request, 'creationEngine/deleteActivity.html', content)

def groupOverview(request):
    groups = Group.objects.all()
    users = UserA.objects.all()
    links = UserGroup.objects.all()
    content = {
        'groups' : groups,
        'users' : users,
        'links' : links
    }

    return render(request, 'creationEngine/groups.html', content)

def createGroup(request):
    form = GroupForm()
    content = {'form' : form }

    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Group {} Created'.format(form.cleaned_data.get('groupName')))
            return redirect('/')

    return render(request, 'creationEngine/createGroup.html', content)

def deleteGroup(request, id):
    group = Group.objects.get(GroupID=id)
    content = {'group':group}
    if request.method == 'POST':
        group.delete()
        messages.warning(request, 'Group {} deleted'.format(group.groupName))
        return redirect('groups')
    return render(request, 'creationEngine/groupDeleteGroup.html', content)

def addUserToGroup(request, groupID, userID=0):
    form = UserGroupForm()
    content = {'form':form}
    #print(request.POST)
    if request.method == 'POST':
        form = UserGroupForm(request.POST)
        form.save()
        userID = form.cleaned_data.get('userID')
        user = UserA.objects.get(userID=userID.userID)
        groupID = form.cleaned_data.get('groupID')
        #print(groupID)
        group = Group.objects.get(GroupID=groupID.GroupID)
        messages.success(request, '{} added to {}'.format(user.userName,group.groupName))
        redirect('groups')
    return render(request, 'creationEngine/groupAddUser.html', content)

def removeUserFromGroup(request, ID):
    link = UserGroup.objects.get(linkID=ID)
    groups = Group.objects.all()
    users = UserA.objects.all()

    #print(link)

    content = { 'link' : link,
        'groups' : groups,
        'users' : users,
     }

    if request.method == 'POST':
        link.delete()
        messages.success(request,'Operation completed succesfully')
        return redirect('groups')
    return render(request, 'creationEngine/userUnlink.html', content)

def createActivityForGroup(request):
    form1 = CreateTaskGroup()
    content = {'form' : form1}
    
    if request.method == 'POST':
        form1 = CreateTaskGroup(request.POST)
        #only run if nothing funky is going on
        if form1.is_valid:
            group = request.POST.get('group')

            #for every user in group 
            for link in UserGroup.objects.filter(groupID=group):
                #create activity object
                newActivity = Activity()

                #fill values in object
                newActivity.userID = link.userID
                newActivity.activityName = request.POST.get('activityName')
                newActivity.startTime = request.POST.get('startTime')
                newActivity.endTime = request.POST.get('endTime')
                newActivity.activityImage = request.POST.get('activityImage')

                #if loop for boolean
                if request.POST.get('isComplete') == None:
                    newActivity.isComplete = False
                else:
                    newActivity.isComplete = True
                
                #save to db and rederect with message
                newActivity.save()
                messages.success(request, 'Activity {} created for {}'.format(request.POST.get('activityName'), link.userID.userName))
        return redirect('groups')


    return render(request, 'creationEngine/activityGroup.html',content)

def createActiviyMdays(request, days):














    
    pass



# TODO make the image stuff, check https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/

