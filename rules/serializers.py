from rest_framework import serializers
from rules.models import User, Camera, Rule

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'password', 'email']

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ['id', 'user_id', 'rule', 'camera_id']

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['id', 'user_id', 'cam_number', 'location']
