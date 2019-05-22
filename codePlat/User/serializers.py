from rest_framework import serializers
from User.models import normal_user, expert, administrator,model_buyresources

class NormalUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = normal_user
		fields = '__all__'

class ExpertSerializer(serializers.ModelSerializer):
	class Meta:
		model = expert
		fields = '__all__'

class AdministratorSerializer(serializers.ModelSerializer):
	class Meta:
		model = administrator
		fields = '__all__'

class ModelBuyResourcesSerializer(serializers.ModelSerializer):
	class Meta:
		model = model_buyresources
		fields = '__all__'
