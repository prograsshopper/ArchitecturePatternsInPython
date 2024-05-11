from django.db import transaction

from .utils import ml_method_dict
from core.models.ml_models import TrainedModel


def set_ml_model(ml_method, random_state=None, n_estimators=None):
    if ml_method == 'random_forest' and not (False in [random_state, n_estimators]):
        model = ml_method_dict[ml_method](random_state=random_state, n_estimators=n_estimators)
    elif ml_method == 'gradient_boost' and not random_state:
        model = ml_method_dict[ml_method](random_state=random_state)
    else:
        model = ml_method_dict[ml_method]()
    return model


def save_ml_model(trained_model: dict):
    try:
        with transaction.atomic():
            current_model = TrainedModel.objects.create(**trained_model)
        return current_model
    except Exception as ex:
        raise ex