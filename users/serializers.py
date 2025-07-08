from rest_framework import serializers
from .models import Users

class HRSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = 'name', 'description', 'interview_count_taken'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = 'name', 'description', 'interview_count_passed', 'positive_results', 'negative_results'
