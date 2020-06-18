from django.contrib import admin
from .models import Activity, Group, UserA, UserGroup

# Register your models here.
admin.site.register(Activity)
admin.site.register(Group)
admin.site.register(UserA)
admin.site.register(UserGroup)