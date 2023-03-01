from django.urls import path, include
from profiles.api.views import ProfileViewSet, ProfileStatusViewSet, ProfilePhotoUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'status', ProfileStatusViewSet, basename='status')

# profil_list = ProfilViewSet.as_view({'get':'list'})
# profil_detay = ProfilViewSet.as_view({'get':'retrieve'}) 

urlpatterns = [
    path('', include(router.urls)),
    path('profile_photo/', ProfilePhotoUpdateView.as_view(), name='profile-photo')
    #path('kullanici-profilleri/', profil_list, name='profiller'),
    #path('kullanici-profilleri/<int:pk>', profil_detay, name='profil-detay'),
]