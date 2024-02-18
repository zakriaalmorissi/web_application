from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.home_view,name="home"),
    path('post/',views.post_view,name="posts"),
    path('comment/<int:id>/',views.comment_view,name="comment"),
    path("comment/<int:id>/delete/",views.delete_comments,name="delete_comment")
]
