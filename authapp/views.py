from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    try:
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({'error': 'Please provide username and password and email.'}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_409_CONFLICT)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_409_CONFLICT)

        User.objects.create_user(username, email, password)
        return Response({'details': 'new user created successfully!'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Please provide username and password.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid username or password.'}, status=status.HTTP_400_BAD_REQUEST)

        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token

        return Response({'access': str(access_token), 'refresh': str(refresh_token)}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    try:
        token = request.data.get('refresh')
        refresh_token = RefreshToken(token)
        access_token = refresh_token.access_token
        return Response({'access': str(access_token)})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout(request):
    try:
        token = request.data.get('refresh')
        refresh_token = RefreshToken(token)
        refresh_token.blacklist()
        return Response({'details': 'Logout successfully!'})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
