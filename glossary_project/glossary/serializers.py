from rest_framework import serializers
from .models import Project, Term

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ['id', 'word', 'definition', 'created_at', 'updated_at']

class ProjectSerializer(serializers.ModelSerializer):
    terms = TermSerializer(many=True, read_only=True)  # вложенные термины в проект

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at', 'terms']
