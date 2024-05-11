from rest_framework.serializers import ModelSerializer

from core.models.ml_models import TrainedModel


class TrainedModelSerializer(ModelSerializer):
    class Meta:
        model = TrainedModel
        fields = '__all__'
