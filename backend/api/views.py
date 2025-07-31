from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import SubmissionSerializer


# Create your views here.


# Receive the data and save it to the db if authentic.
class SubmissionView(APIView):
    def post(self, request):
        serializer = SubmissionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)