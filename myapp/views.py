# myapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import InstituteForm
from .models import InstituteProfile

from .serializers import InstituteSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView



from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView 
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy



def index(request):
    return render(request, 'index.html')

def pages_profile_settings(request):
    return render(request, 'pages-profile-settings.html')

def app_chat(request):
    return render(request, 'apps-chat.html') 

def apps_tasks_kanban(request):
    return render(request, 'apps-tasks-kanban.html') 

def pages_faqs(request):
    return render(request, 'pages-faqs.html') 

def profile_page(request):
    return render(request, 'pages-profile.html') 

def auth_lockscreen_basic(request):
    return render(request, 'auth-lockscreen-basic.html')

def auth_logout_basic(request):
    return render(request, 'auth-logout-basic.html')

def pages_search_results(request):
    return render(request, 'pages-search-results.html')

def ecommerce_products(request):
    return render(request, 'apps-ecommerce-products.html')

def ecommerce_product_details(request):
    return render(request, 'apps-ecommerce-product-details.html')

def ecommerce_checkout(request):
    return render(request, 'apps-ecommerce-checkout.html')

class CreateAndUpdateView(APIView):
    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(InstituteProfile, pk=pk)
            serializer = InstituteSerializer(obj)
            return Response(serializer.data)
        else:
            objs = InstituteProfile.objects.filter(user=request.user)
            serializer = InstituteSerializer(objs, many=True)
            return Response(serializer.data)

    def post(self, request):
        if InstituteProfile.objects.filter(user=request.user).exists():
            return Response({'detail': 'You have already created an instance.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = InstituteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = get_object_or_404(InstituteProfile, pk=pk)
        if obj.user != request.user:
            return Response({'detail': 'You do not have permission to edit this object.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = InstituteSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)