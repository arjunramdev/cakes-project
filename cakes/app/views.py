from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.authentication import  BasicAuthentication,SessionAuthentication,TokenAuthentication

from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly

from authentication.permissions import IsAdmin,IsUser  
# Create your views here.

from .models import Cake 

from .serializers import CakeSerializer


class CakeListCreateView(APIView):

    serializer_class = CakeSerializer

    # authentication_classes = [BasicAuthentication]
    
    authentication_classes = [TokenAuthentication]

    # permission_classes = [AllowAny]

    def get_permissions(self):

        permissions = []

        if self.request.method == 'POST':

            permissions = [IsAdmin]

        return [permission() for permission in permissions]
    

    def get(self,reques,*args,**kwargs):

        cakes = Cake.objects.all()

        serializer = self.serializer_class(cakes,many=True)

        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'cake created successfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)

class CakeRetrieveUpdateDestroyView(APIView):

    serializer_class = CakeSerializer

    # authentication_classes = [BasicAuthentication]

    
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
    
            permissions = []
    
            if self.request.method in ['PATCH','DELETE']:
    
                permissions = [IsAdmin]
    
            return [permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        id = kwargs.get('id')

        cake = Cake.objects.get(id=id)

        serializer = self.serializer_class(cake)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):

        id = kwargs.get('id')

        cake = Cake.objects.get(id=id)

        serializer = self.serializer_class(data=request.data,instance=cake,partial=True)

        if serializer.is_valid():

            data = {'msg':'cake updated succesfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):

        id = kwargs.get('id')

        cake = Cake.objects.get(id=id)

        cake.delete()

        data = {'msg':'cake deleted successfully'}

        return Response(data,status=204)