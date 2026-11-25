from rest_framework import serializers
from apps.crops.models import CropCycle



class CropCycleCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropCycle
        fields = [
            'id','land','crop','variety','season','planting_date','expected_harvest_date'
        ]

    def validate(self, data):
        planting_date = data.get('planting_date')
        expected_harvest_date = data.get('expected_harvest_date')
        crop = data.get('crop')
        variety = data.get('variety')

        if expected_harvest_date and expected_harvest_date < planting_date:
            raise serializers.ValidationError(
                "Expected harvest date must be greater than to planting date."
            )

        if variety.crop != crop:
            raise serializers.ValidationError(
                "Selected variety does not belong to the selected crop."
            )



class CropCycleListSerializer(serializers.ModelSerializer):
    land_name = serializers.CharField(source='land.name', read_only=True)
    crop_name = serializers.CharField(source='crop.name', read_only=True)
    variety_name = serializers.CharField(source='variety.name', read_only=True)
    season_name = serializers.CharField(source='season.name', read_only=True)

    class Meta:
        model = CropCycle
        fields = [
            'id','land','crop','variety','season','planting_date','expected_harvest_date',
            'land_name','crop_name','variety_name','season_name'
        ]