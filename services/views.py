from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import HairCut, ExtraService
from .serializers import ExtraServiceSerializer, HairCutSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework import status, request
from django.http import HttpResponse
from rest_framework.views import APIView


# Create your views here.

class HaircutView(APIView):
    def get(self, request, format=None):
        haircut = HairCut.objects.all()
        serializer = HairCutSerializer(haircut, many=True)
        return Response(serializer.data)

    #def check_admin(user):
    #    return user.is_superuser

    #@user_passes_test(check_admin)
    @user_passes_test(lambda user: user.is_superuser)
    def post(self, request):
        serializer = HairCutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HairCutDetails(APIView):
    def get(self, request, pk, format=None):
        haircut = HairCut.objects.filter(hair_cut_type=pk)
        serializer = HairCutSerializer(haircut, many=True)
        return Response(serializer.data)

    #def check_admin(user):
    #    return user.is_superuser

    #@user_passes_test(check_admin)
    @user_passes_test(lambda user: user.is_superuser)
    def patch(self, request, pk, format=None):
        try:
            haircut = HairCut.objects.get(hair_cut_type=pk)
            serializer = HairCutSerializer(haircut, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except HairCut.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    #def check_admin(user):
    #    return user.is_superuser

    #@user_passes_test(check_admin)
    @user_passes_test(lambda user: user.is_superuser)
    def delete(self, request, pk, format=None):
        try:
            haircut = HairCut.objects.get(hair_cut_type=pk)
            haircut.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except HairCut.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)


class ExtraServiceView(APIView):

    def get(self, request, format=None):
        extra_service = ExtraService.objects.all()
        serializer = ExtraServiceSerializer(extra_service, many=True)
        return Response(serializer.data)

    #def check_admin(user):
    #    return user.is_superuser

    #@user_passes_test(check_admin)
    @user_passes_test(lambda user: user.is_superuser)
    def post(self, request):
        serializer = ExtraServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExtraServiceDetails(APIView):

    def get(self, request, pk, format=None):
        extra_service = ExtraService.objects.filter(type_of_service=pk)
        serializer = ExtraServiceSerializer(extra_service, many=True)
        return Response(serializer.data)

    #def check_admin(user):
    #    return user.is_superuser

    #@user_passes_test(check_admin)
    @user_passes_test(lambda user: user.is_superuser)
    def patch(self, request, pk, format=None):
        try:
            extra_service = ExtraService.objects.get(type_of_service=pk)
            serializer = ExtraServiceSerializer(extra_service, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ExtraService.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    #def check_admin(user):
        return user.is_superuser

    #@user_passes_test(check_admin)
    @user_passes_test(lambda user: user.is_superuser)
    def delete(self, request, pk, format=None):
        try:
            extra_service = ExtraService.objects.get(type_of_service=pk)
            extra_service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ExtraService.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
