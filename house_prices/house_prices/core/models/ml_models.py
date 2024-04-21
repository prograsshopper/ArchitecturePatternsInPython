from django.db import models


class TrainedModel(models.Model):
    name = models.CharField(max_length=100)
    model_type = models.CharField(max_length=50)
    serialized_model = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)


class ModelEvaluation(models.Model):
    model_name = models.CharField(max_length=100)
    metric_name = models.CharField(max_length=50)
    train_score = models.FloatField()
    test_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
