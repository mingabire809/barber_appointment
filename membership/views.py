from django.shortcuts import render
from .models import Membership
from .serializers import MembershipSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from django.http import HttpResponse


# Create your views here.

class MembershipView(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        membership = Membership.objects.all()
        serializer = MembershipSerializer(membership, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembershipDetails(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        membership = Membership.objects.filter(name=pk)
        serializer = MembershipSerializer(membership, many=True)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        try:
            membership = Membership.objects.get(name=pk)
            serializer = MembershipSerializer(membership, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Membership.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            membership = Membership.objects.get(name=pk)
            membership.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Membership.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
