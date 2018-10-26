from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.views import APIView


def get_users(request):
    users = User.objects.all()
    response = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return JsonResponse(response, safe=False)


def get_user(request, pk=None):
    user = get_object_or_404(klass=User, pk=pk)
    response = {"id": user.id, "username": user.username, "email": user.email}
    return JsonResponse(response, safe=False)


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        user_request = dict(request.POST)  # request.POST is in type of QueryDict
        print(user_request)
        print(request.POST)
        # print(request.body)

        # destructing QueryDict
        username, password, email, first_name, last_name, is_staff, is_superuser = request.POST.values()

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                        last_name=last_name, is_staff=bool(is_staff), is_superuser=bool(is_superuser),
                                        is_active=True)
        user_request['id'] = user.id
        return JsonResponse(user_request, safe=False)

# @api_view(['get'])
# def get_users(request):
#     users = User.objects.all()
#     response = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
#     return Response(response)
#
#
# @api_view(['get'])
# def get_user(request, pk=None):
#     user = get_object_or_404(klass=User, pk=pk)
#     response = {"id": user.id, "username": user.username, "email": user.email}
#     return Response(response)
#
#
# @api_view(['post'])
# def create_user(request):
#     user_request = request.data
#     print(request.data)
#     # destructing dict
#     username, password, email, first_name, last_name, is_staff, is_superuser = request.data.values()
#
#     user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
#                                     last_name=last_name, is_staff=bool(is_staff), is_superuser=bool(is_superuser),
#                                     is_active=True)
#     user_request['id'] = user.id
#     return Response(user_request)


# @api_view(['get'])
# def get_users(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['get'])
# def get_user(request, pk=None):
#     user = get_object_or_404(klass=User, pk=pk)
#     serializer = UserSerializer(user)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['post'])
# def create_user(request):
#     serializer = UserSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['put'])
# def update_user(request, pk=None):
#     user = get_object_or_404(klass=User, pk=pk)
#     print(user)
#     serializer = UserSerializer(user, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
#
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserAPIView(APIView):
#     serializer_class = UserSerializer
#     permission_classes = ()
#
#     def get(self, request, pk=None, format=None):
#         """ Handles both listing and retrieving an object. """
#         if pk is None:
#             users = User.objects.all()
#             serializer = UserSerializer(users, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             try:
#                 user = User.objects.get(pk=pk)
#                 serializer = UserSerializer(user)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except User.DoesNotExist:
#                 return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     def post(self, request):
#         """ Handles creating an object. """
#         serializer = UserSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk=None):
#         """ Handles updating an object. """
#         try:
#             user_in_db = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = UserSerializer(instance=user_in_db, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
