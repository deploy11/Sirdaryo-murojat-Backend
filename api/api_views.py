from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from django.http import HttpResponse, JsonResponse

from .models import Sorov
from .serializers import SorovSerializer

class SorovApiView(ListCreateAPIView):
    serializer_class = SorovSerializer

    def get_queryset(self):
        # URL parametrlarini olish
        user_query = self.request.GET.get('user', None)
        if user_query:
            # Parametr bo'lsa, faqat shu user uchun so'rovlarni qaytarish
            return Sorov.objects.filter(user=user_query)
        # Parametr mavjud bo'lmasa, barcha so'rovlarni qaytarish
        return JsonResponse({'status':'user not found'})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SorovStatisticsView(APIView):
    def get(self, request, *args, **kwargs):
        total_count = Sorov.objects.all().count()
        korish_true_count = Sorov.objects.filter(korish=True).count()
        korish_false_count = Sorov.objects.filter(korish=False).count()

        data = {
            'total_count': total_count,
            'korish_true_count': korish_true_count,
            'korish_false_count': korish_false_count
        }

        serializer = SorovStatisticsSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetUserIdFromSession(APIView):
    def get_user_id(self, session_key):
        try:
            # Sessiyani bazadan izlash
            session = Session.objects.get(session_key=session_key)
            user_id = session.get_decoded().get('_auth_user_id')

            return user_id  # Foydalanuvchi ID ni qaytarish
        except Session.DoesNotExist:
            return None
        except User.DoesNotExist:
            return None

    def get(self, request, format=None):
        # JSON so'rovdan sessiya kalitini olish
        session_key = request.data.get('session_key')

        if session_key:
            user_id = self.get_user_id(session_key)
            if user_id:
                return Response({'user_id': user_id}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Session key not provided'}, status=status.HTTP_400_BAD_REQUEST)

