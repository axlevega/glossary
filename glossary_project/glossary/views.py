from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Project, Term
from .serializers import ProjectSerializer, TermSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TermViewSet(viewsets.ModelViewSet):
    serializer_class = TermSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        project = get_object_or_404(Project, id=project_id, user=self.request.user)
        return Term.objects.filter(project=project)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = get_object_or_404(Project, id=project_id, user=self.request.user)
        serializer.save(project=project)

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TermsByReferrerView(APIView):
    permission_classes = [AllowAny]  # открытый доступ к этому эндпоинту

    def get(self, request, *args, **kwargs):
        # Извлекаем домен из реферера
        referrer = request.META.get('HTTP_REFERER', '').split('//')[-1].split('/')[0]
        project = get_object_or_404(Project, domain=referrer)  # `domain` — поле домена в модели Project

        terms = Term.objects.filter(project=project)
        serialized_terms = TermSerializer(terms, many=True).data
        # Устанавливаем ensure_ascii=False, чтобы передавать данные в UTF-8
        return JsonResponse(serialized_terms, safe=False, json_dumps_params={'ensure_ascii': False})
