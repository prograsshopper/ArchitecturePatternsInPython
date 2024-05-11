from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from core.models.ml_models import TrainedModel
from core.utils import mapping_dict
from .serializers import set_ml_model, save_ml_model


def get_ml_models(limit: int = 10):
    models_queryset = TrainedModel.objects.order_by('-id')[:limit]
    return models_queryset


def set_ml_model_training(df_data, ml_method: str, features: list):
    try:
        features = [mapping_dict[feature] for feature in features]
        X = df_data[features]
        y = df_data['SalePrice']
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model = set_ml_model(ml_method)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        save_ml_model(model)
        return mse
    except KeyError as ke:
        raise ke
    except Exception as ex:
        raise ex


def get_evaluate_model():
    try:
        pass
    except Exception as ex:
        raise ex


def tune_hyperparameter():
    try:
        pass
    except Exception as ex:
        raise ex
