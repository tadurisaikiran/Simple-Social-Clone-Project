from django.urls import path, re_path
from groups.views import CreateGroupView, ListGroupView, DetailGroupView
from groups import views

app_name = 'groups'
urlpatterns = [
     path('', ListGroupView.as_view(), name="list"),
    path('create/', CreateGroupView.as_view(), name="create"),
    re_path(r"^posts/in/(?P<slug>[-\w]+)/$",views.DetailGroupView.as_view(), name="single"),
    re_path(r"join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
    re_path(r"leave/(?P<slug>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),

 ]
