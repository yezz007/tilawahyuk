from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'organization', views.OrganizationViewSet, 'organization')
router.register(r'user', views.UserViewSet, base_name='user')
router.register(r'group', views.GroupViewSet, 'group')

app_name = 'responder'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^callback/', views.line, name='webhook')
]