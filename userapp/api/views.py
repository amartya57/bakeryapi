from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from userapp.api.serializers import RegistrationSerializer
from userapp import models

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        data={"Response" : "Logout Succesful"}
        return Response(data, status=status.HTTP_200_OK)
    return Response({"Response":"Not successful"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def registration_view(request):
    if request.method == "POST":
        serializer=RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['username']=account.username
            data['email']=account.email
            data['token'] = Token.objects.get(user=account).key
            return Response(data)
        
        data=serializer.errors
        return Response(data)