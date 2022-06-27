from django.urls import path
from . import views
# from .views import LikeView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/detail/', views.post_details, name='post_details'),
    path('post_new/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('ordering/', views.OrderDateView.as_view(), name='ordering'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('latest/', views.TodayView.as_view(), name='todayDate'),

    # path('post/<int:pk>/post-detail', PostDetailView.as_view(), name='post-detail'),
    path('register', views.register_request, name="register"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),
    # path('like/<int:pk>', LikeView, name='like_post'),
]