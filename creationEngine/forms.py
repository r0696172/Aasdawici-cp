from django.forms import ModelForm
from overview.models import *
from django import forms


class UserAForm(ModelForm):
    class Meta:
        model = UserA
        fields = '__all__'


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class UserGroupForm(ModelForm):
    class Meta:
        model = UserGroup
        fields = '__all__'

class CreateTaskGroup(ActivityForm):
    group = forms.ModelMultipleChoiceField(queryset=Group.objects.all())
    class Meta:
        model = Activity
        exclude = ['userID']
