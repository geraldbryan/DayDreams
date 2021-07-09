from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SadListView,
    SadCreateView,
    AngerListView,
    AngerCreateView,
)

urlpatterns = [
    path('', views.landing,name='blog-landing'),
    path('menu/', views.menu,name='blog-menu'), #diganti pake yang baru nanti ya
    path('home/', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(),name='post-detail'),
    path('post/new', PostCreateView.as_view(),name='post-create'),
    path('sad/', SadListView.as_view(),name='blog-sad'),
    path('anger/new', AngerCreateView.as_view(),name='anger-create'),
    path('anger/', AngerListView.as_view(),name='blog-anger'),
    path('sad/new', SadCreateView.as_view(),name='sad-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(),name='post-delete'),
    path('about/', views.about,name='blog-about'),
]
