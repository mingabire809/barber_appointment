from django.shortcuts import render
from .serializers import BookingSerializer
from .models import Booking
from member.models import Member
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework import status, viewsets


# Create your views here.

class BookingListView(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # member = get_object_or_404(Booking, full_name=request.user.full_name)
        # if member==request.user.is_authenticated():
        booking = Booking.objects.filter(member=request.user)
        serializer = BookingSerializer(booking, many=True)
        return Response(serializer.data)

    # else:
    #   return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        serializer = BookingSerializer(data=request.data, context={
            'request': request,

        })
        if serializer.is_valid():
            serializer.save(member=request.user, name=request.user.full_name, email=request.user.email,
                            phone=request.user.phone_number)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingDetails(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk, format=None):
        booking = Booking.objects.filter(booking_reference_number=pk, member=request.user)
        serializer = BookingSerializer(booking, many=True)
        return Response(serializer.data)

    def update(self, request, pk, format=None):

        booking = Booking.objects.get(member=request.user,
                                      booking_reference_number=pk)
        serializer = BookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, format=None):
        member = get_object_or_404(Booking, member=request.user)
        if member == request.user:
            booking = Booking.objects.filter(
                booking_reference_number=pk)
            booking.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
