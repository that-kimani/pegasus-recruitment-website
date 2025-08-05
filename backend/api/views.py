from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import SubmissionSerializer
import requests , random


# Create your views here.


# Receive the data and save it to the db if authentic.
class SubmissionView(APIView):
    def post(self, request):
        serializer = SubmissionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    

class ChatAssistancView(APIView):
    def post(self , request):
        chat_message = request.data.get('message')
        sessionId = random.randint(1 , 100)

        if not chat_message:
            return Response({"error":"Message is required."} , status.HTTP_400_BAD_REQUEST)
        
        n8n_webhook_production_url = "http://host.docker.internal:5678/webhook/1d94fbec-03f7-47b3-829e-38feeed496cf"

        # Contact the n8n workflow(AI agent).
        try:
            n8n_response = requests.post(n8n_webhook_production_url , json={
                "chatInput" : chat_message,
                "sessionId" : sessionId
            })

            if n8n_response.status_code != 200:
                return Response({"error": "n8n workflow failed", "details": n8n_response.text},
                                status=n8n_response.status_code)
            
            response_data = n8n_response.json()

        except requests.exceptions.RequestException as e:
            return Response({"error": "Could not contact n8n workflow", "details": str(e)},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        return Response({
            "reply": response_data.get("output"),
            "conversation_id": response_data.get("conversation_id", sessionId)
        }, status=status.HTTP_200_OK)