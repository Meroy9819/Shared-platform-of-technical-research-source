from rest_framework import serializers
from User.models import NormalUser, ExpertUser, Administrator

class NormalUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = NormalUser
		fields = '__all__'

class ExpertSerializer(serializers.ModelSerializer):
	class Meta:
		model = ExpertUser
		fields = '__all__'

class AdministratorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Administrator
		fields = '__all__'

