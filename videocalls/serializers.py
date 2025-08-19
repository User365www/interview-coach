from rest_framework import serializers
from .models import VideoRoom

class VideoRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoRoom
        fields = ('id', 'name', 'hr', 'created_at')
        read_only_fields = ('id', 'hr', 'created_at')