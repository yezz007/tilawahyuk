from .serializers import OrganizationSerializer, GroupSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from .models import Organization, Group, User
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .bot import base

@csrf_exempt
def line(request):
    return base(request)


@api_view(['GET'])
def api_root(request, format=None):
    return Response()

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
