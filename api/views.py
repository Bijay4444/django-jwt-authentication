from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser  # Import your custom user model
from .serializers import CustomUserSerializer  # Import the serializer you'll create in the next step
from rest_framework.views import APIView
from django.contrib.auth import authenticate


# Create your views here.

"""Using function-based views:"""""
@api_view(['POST'])
@permission_classes([AllowAny])  # Allow anyone to register
def register_user(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow anyone to log in
def login_user(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout_user(request):
    if request.method == 'POST':
        # No need to handle anything here for JWT. The frontend should handle the logout by discarding the token.
        return Response({"success": "User successfully logged out."}, status=status.HTTP_200_OK)


"""Using class-based views:"""""

# #new class-based view for login:
# class LoginAPIView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         user = authenticate(email=email, password=password)

#         if user:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })

#         return Response({'error': 'Invalid credentials'}, status=400)

# #new class-based view for register:
# class RegisterAPIView(APIView):
#     def post(self, request):
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #new class-based view for logout:
# class LogoutAPIView(APIView):
#     def post(self, request):
#         refresh_token = request.data.get('refresh_token')

#         if refresh_token:
#             try:
#                 token = RefreshToken(refresh_token)
#                 token.blacklist()
#                 return Response({'success': 'User successfully logged out.'})
#             except Exception as e:
#                 return Response({'error': 'Invalid token'}, status=400)

#         return Response({'error': 'No refresh_token provided'}, status=400)
