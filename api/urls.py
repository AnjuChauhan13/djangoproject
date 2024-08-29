from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreateView, UserProfileViewSet, ClothingItemViewSet, OutfitViewSet,Home

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)
router.register(r'clothing-items', ClothingItemViewSet)
router.register(r'outfits', OutfitViewSet)

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('', include(router.urls)),
    path('', Home.as_view()),
]
