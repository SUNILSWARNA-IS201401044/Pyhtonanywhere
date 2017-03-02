from rest_framework import serializers
from .models import Stock1

class StockSerializer(serializers.ModelSerializer):
	class Meta:
		model=Stock1
		fields=('data',)
		#fields='_all_'


