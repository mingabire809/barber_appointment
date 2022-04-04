from tokenize import Token
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .authentication import CsrfExemptSessionAuthentication


from .models import Member
from .serializers import MemberSerializer
from rest_framework import response, status
from django.contrib.auth.models import User


# Create your views here.

class RegisterMemberView(GenericAPIView):
    # User = get_user_model()

    def post(self, request, *args, **kwargs):
        """Handles post request logic"""
        registration_serializer = MemberSerializer(data=request.data)

        # Generate tokens for existing users
        for user in Member.objects.all():
            if not user:
                break
            else:
                try:
                    # Token.objects.get(user_id=user.id)
                    Token.objects.get(user_id=user.id)
                except Token.DoesNotExist:
                    Token.objects.create(user=user)

        if registration_serializer.is_valid():
            user = registration_serializer.save()
            token = Token.objects.create(user=user)

            return Response(
                {
                    "user": {
                        "id": serializer.data["id"],
                        "full_name": serializer.data["full_name"],
                        "email": serializer.data["email"],
                        "username": serializer.data["username"],
                        "phone_number": serializer.data["phone_number"],
                        "profile_picture": serializer.data["profile_picture"],
                        # "is_staff": serializer.data["is_staff"],
                    },
                    "status": {
                        "message": "User created",
                        "code": f"{status.HTTP_200_OK} OK",
                    },
                    "token": token.key,
                }
            )
        return Response(
            {
                "error": serializer.errors,
                "status": f"{status.HTTP_203_NON_AUTHORITATIVE_INFORMATION} \
        NON AUTHORITATIVE INFORMATION ",
            }
        )


# @api_view(['POST'])
# @authentication_classes([])
# @permission_classes([AllowAny])
# def member_signup(request):
#    try:
#        data = []
#        serializer = MemberSerializer(data=request.data)
#        if serializer.is_valid():
#            member = serializer.save()
#            member.is_active = True
#            member.save()
#            token = Token.objects.get_or_create(user=member)[0].key
#            data["message"] = "user registered successfully"
#            data["email"] = member.email
#            data["username"] = member.username
#            data["token"] = token

#        else:
#            data = serializer.errors


#       return Response(data)
#   except IntegrityError as e:
#      account=Member.objects.get(username='')
#      account.delete()
#      raise ValidationError({"400": f'{str(e)}'})

#  except KeyError as e:
#     print(e)
#     raise ValidationError({"400": f'Field {str(e)} missing'})
# def member_signup(request):
#    try:
#        data = []
#       serializer = MemberSerializer(data=request.data)
#        print('any')
#        if serializer.is_valid():
#            member = serializer.save()
#            member.is_active = True
#            member.save()
#            login(request, member)
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    except IntegrityError as e:
#        member = Member.objects.get(username='')
#        member.delete()
#        raise ValidationError({"400": f'{str(e)}'})
#    except KeyError as e:
#        print(e)
#        raise ValidationError({"400": f'Field {str(e)} missing'})
# return Response(status=status.HTTP_401_UNAUTHORIZED)


class MemberView(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, username, *args, **kwargs):
        member = get_object_or_404(Member, username=request.user.username)
        print("")
        print("")

        print(request.user.id)
        print(request.user.username)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def update(self, request, username, *args, **kwargs):
        member = get_object_or_404(Member, username=request.user.username)
        if member == request.user:
            serializer = MemberSerializer(request.user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, username, *args, **kwargs):
        member = get_object_or_404(Member, username=request.user.username)
        if member == request.user:
            member.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
