from rest_framework import serializers
from TechResource.models import SciAchi

class SciAchiSerializer(serializers.ModelSerializer):
	class Meta:
		model = SciAchi
		fields = '__all__'
