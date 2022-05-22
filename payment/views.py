from datetime import date

from django.shortcuts import render
from .models import Payment
from member.models import Member
from .serializers import PaymentSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from django.http import HttpResponse
from premium.models import Premium
from rest_framework.generics import get_object_or_404


# Create your views here.

class PaymentView(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        payment = Payment.objects.filter(member=request.user)
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(member=request.user, name=request.user.full_name, email=request.user.email,
                            phone=request.user.phone_number)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetails(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        member = request.user
        if member == request.user:
            payment = Payment.objects.filter(transaction_number=pk)
            serializer = PaymentSerializer(payment, many=True)
            return Response(serializer.data)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, pk, format=None):
        if request.user:
            if request.user.is_superuser:
                try:
                    payment = Payment.objects.get(transaction_number=pk)
                    serializer = PaymentSerializer(payment, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                except Payment.DoesNotExist:
                    return HttpResponse(status=status.HTTP_404_NOT_FOUND)
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk, format=None):
        if request.user:
            if request.user.is_superuser:
                try:
                    payment = Payment.objects.get(transaction_number=pk)
                    payment.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                except Payment.DoesNotExist:
                    return HttpResponse(status=status.HTTP_404_NOT_FOUND)
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
