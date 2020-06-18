from django.urls import path
from . import views

urlpatterns = [
    path('creationEngine/', views.home, name='creationsEngine-home'),
    path('creationEngine/createUser/', views.createUser, name='creationEngine-createUser'),
    path('creationEngine/deleteUser/<str:id>', views.deleteUser, name='creationEngine-deleteUser'),
    path('creationEngine/createActivity/', views.createActivity, name='creationEngine-createActivity'),
    path('creationEngine/deleteActivity/<str:id>', views.deleteActivity, name='creationEngine-deleteActivity'),
    path('creationEngine/createGroup/', views.createGroup, name='creationEngine-createGroup'),
    path('creationEngine/groups/', views.groupOverview, name='groups'),
    path('creationEngine/groups/removeUserFromGroup/<str:ID>/', views.removeUserFromGroup, name='groups-removeUser'),
    path('creationEngine/groups/addToGroup/<str:groupID>/<str:userID>/', views.addUserToGroup, name='groups-addUser'),
    path('creationEngine/groups/addToGroup/<str:groupID>/', views.addUserToGroup, name='groups-addUser'),
    path('creationEngine/groups/deleteGroup/<str:id>/', views.deleteGroup, name='groups-delete'),
    path('creationEngine/groups/CreateActGroup/', views.createActivityForGroup,name='createActivity-group'),
]