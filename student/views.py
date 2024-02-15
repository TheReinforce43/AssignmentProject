from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import StudentSerializer
from .models import StudentModel
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def signup(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
      
        email = request.data.get('email')

        # Creating the user with the provided email
        user = StudentModel.objects.create_user(email=email)

        # Setting the password for the user
        user.set_password(request.data['password'])
        user.save()

       
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    return Response({})

@api_view(['GET'])
def test_token(request):
    return Response({})