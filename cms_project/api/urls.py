# api/urls.py

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet, ContentItemViewSet, UserRegistrationView, UserLoginView, ContentSearchView

# # Create a router and register our viewsets with it
# router = DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'content', ContentItemViewSet)

# urlpatterns = [
#     # API views
#     path('', include(router.urls)),

#     # Authentication
#     path('register/', UserRegistrationView.as_view(), name='user-register'),
#     path('login/', UserLoginView.as_view(), name='user-login'),

#     # Search functionality
#     path('search/', ContentSearchView.as_view(), name='content-search'),
# ]




# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ContentItemViewSet, UserRegistrationView, UserLoginView, ContentSearchView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'content', ContentItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('search/', ContentSearchView.as_view(), name='content-search'),
]
