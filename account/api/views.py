from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.api.serializers import RegisterSerializer
from account.models import Account


@api_view(['POST',])
def api_register_view(request):

    if request.method =='POST':
        serializer = RegisterSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            account=serializer.save() #call the  save method we have overwritten
            data['response'] ='successfully registered a new user'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)        




