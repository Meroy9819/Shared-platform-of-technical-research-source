from rest_framework import serializers
from TechResource.models import SciAchi,Inst,Resource

class SciAchiSerializer(serializers.ModelSerializer):
	class Meta:
		model = SciAchi
		fields = '__all__'


class InstSerializer(serializers.ModelSerializer):
	class Meta:
		model = Inst
		fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Resource
		fields = '__all__'

