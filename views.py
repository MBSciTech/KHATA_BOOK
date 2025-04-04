from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def default_view(request):
    return JsonResponse({"message": "Event Transactions API is working!"})
from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users can access
