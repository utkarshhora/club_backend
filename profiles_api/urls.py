from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
#router.register('hello-viewset', views.HelloViewSet, base_name = 'hello_viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
router.register('club', views.ClubFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.CustomObtainAuthToken.as_view()),
    path('logoutuser/', views.logoutuser),
    path('', include(router.urls) ),
    path('idToProfile/', views.idToProfile ),
    path('isclub/', views.isProfileClub),
    path('tokenToId/', views.CustomObtainAuthToken.as_view()),
]
