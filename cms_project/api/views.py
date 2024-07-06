from django.shortcuts import render

# Create your views here.
# api/views.py

from rest_framework import generics, viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.db.models import Q
# from .models import ContentItem, Category
from .serializers import UserSerializer, ContentItemSerializer
from .models import ContentItem, Category


User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        Token.objects.create(user=user)
        return Response({'token': Token.objects.get(user=user).key})

class ContentItemViewSet(viewsets.ModelViewSet):
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContentSearchView(generics.ListAPIView):
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body', 'summary', 'categories__name']



# api/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User  # Assuming User model is defined in models.py
from .serializers import UserSerializer
from .models import ContentItem, Category


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Example permission, adjust as needed





# api/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# api/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import ContentItem
from .serializers import ContentItemSerializer, ContentSearchSerializer

@api_view(['GET'])
def content_search(request):
    serializer = ContentSearchSerializer(data=request.query_params)
    if serializer.is_valid():
        search_query = serializer.validated_data['search_query']

        # Perform search query
        content_items = ContentItem.objects.filter(
            models.Q(title__icontains=search_query) |
            models.Q(body__icontains=search_query) |
            models.Q(summary__icontains=search_query) |
            models.Q(categories__name__icontains=search_query)
        )

        serializer = ContentItemSerializer(content_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
