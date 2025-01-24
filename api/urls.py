from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet, UserProjectsView
from django.urls import path, include

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/projects/', UserProjectsView.as_view(), name='user-projects'),
]
