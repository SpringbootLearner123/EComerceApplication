from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import contactModel, ProductModel,signupdata
from django.contrib.sessions.models import Session

# Sample serializers (You need to create these)
from .serializers import ContactSerializer, ProductSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Dashboard API
@api_view(['GET'])
def dashboard_api(request):
    
        return Response({"message": "Welcome to the Dashboard"}, status=status.HTTP_200_OK)
    
# Contact Management API
@api_view(['GET'])
def contact_mgmt_api(request):

        contacts = contactModel.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

# Delete Contact API
@api_view(['DELETE'])
def delete_contact_api(request, id):
    try:
        contact = contactModel.objects.get(id=id)
        contact.delete()
        return Response({"message": "Contact deleted"}, status=status.HTTP_200_OK)
    except contactModel.DoesNotExist:
        return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)

# Order Management API
@api_view(['GET'])
def order_mgmt_api(request):
        return Response({"message": "Order management zone"})

# Product Management API
@api_view(['GET'])
def product_mgmt_api(request):
        products = ProductModel.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# Add Product Page Placeholder (GET only)
@api_view(['GET'])
def add_product_api(request):
        return Response({"message": "Ready to add products"})

# Admin Logout API
@api_view(['POST'])
def admin_logout_api(request):
    try:
        del request.session['aid']
    except KeyError:
        pass
    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from General.models import contactModel, ProductModel
from django.contrib.sessions.models import Session

# Sample serializers (You need to create these)
from .serializers import ContactSerializer, ProductSerializer

# Dashboard API
@api_view(['GET'])
def dashboard_api(request):
        return Response({"message": "Welcome to the Dashboard"}, status=status.HTTP_200_OK)
   
# Contact Management API
@api_view(['GET'])
def contact_mgmt_api(request):
        contacts = contactModel.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

# Delete Contact API
@api_view(['DELETE'])
def delete_contact_api(request, id):
    try:
        contact = contactModel.objects.get(id=id)
        contact.delete()
        return Response({"message": "Contact deleted"}, status=status.HTTP_200_OK)
    except contactModel.DoesNotExist:
        return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)

# Order Management API
@api_view(['GET'])
def order_mgmt_api(request):
        return Response({"message": "Order management zone"})

# Product Management API
@api_view(['GET'])
def product_mgmt_api(request):
    products = ProductModel.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# Add Product Page Placeholder (GET only)
@api_view(['GET'])
def add_product_api(request):
    return Response({"message": "Ready to add products"})

# Admin Logout API
@api_view(['POST'])
def admin_logout_api(request):
    try:
        del request.session['aid']
    except KeyError:
        pass
    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

#registter and login logic

@csrf_exempt
def register_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if signupdata.objects.filter(susername=username).exists():
            return JsonResponse({"success": False, "message": "Username already exists"}, status=400)

        signupdata.objects.create(susername=username, semail=email, spassword=password)
        return JsonResponse({"success": True, "message": "Registration successful"})

    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def login_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        try:
            user = signupdata.objects.get(susername=username, spassword=password)
            request.session['aid'] = user.id
            return JsonResponse({"success": True, "message": "Login successful", "user_id": user.id})
        except signupdata.DoesNotExist:
            return JsonResponse({"success": False, "message": "Invalid credentials"}, status=401)

    return JsonResponse({"error": "Invalid request method"}, status=405)
