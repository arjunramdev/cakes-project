from django.shortcuts import render

from rest_framework.views import APIView

from django.core.exceptions import ValidationError

from rest_framework.response import Response

from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import ProfileSerializer

from decouple import config

from cakes.utils import send_mail

import threading

class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        
        username = request.data.get('username')

        password = request.data.get('password')

        try:

            if not username:

                raise ValidationError('must provide username')

            if not password:

                raise ValidationError('must provide password')

        except Exception as e:

            data= {'error':e}

            return Response(data,status=400)

        user = authenticate(username=username, password=password)

        if user :

            refresh_token = RefreshToken.for_user(user)

            access_token = refresh_token.access_token

            data = {'access_token':str(access_token),'refresh_token':str(refresh_token)}

            return Response(data,status=200)

        data = {'msg':'Invalid username or password'}

        return Response(data,status=401)

class RegisterView(APIView):

    def post(self,request,*args,**kwargs):

        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():

            username=serializer.validated_data.get('username')

            password = serializer.validated_data.get('password')

            profile=serializer.save()

            profile.email = username

            profile.set_password(password)

            profile.save()

            receipient = profile.email

            subject = 'Welcome to Cakes'
            template='emails/registration.html'

            context={'name':profile.first_name,'email':receipient,'login_url':config('LOGIN_URL')}

            # send_mail(receipient,subject,template,context)
            thread=threading.Thread(target=send_mail,args=(receipient,subject,template,context))
            thread.start()

            data = {'msg':'user created successfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)