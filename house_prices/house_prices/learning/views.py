import traceback

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .services import get_ml_models, set_ml_model_training
from .serializers import TrainedModelSerializer


class MLModelViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        try:
            limit = request.query_params.get('limit', 10)
            ml_model_list = get_ml_models(limit)
            result = TrainedModelSerializer(ml_model_list, many=True).data
            return Response(
                data={'models': result}, status=status.HTTP_200_OK
            )
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {
                    "error_type": "SERVER",
                    "msg": f"{str(ex)} - {str(traceback.format_exc())}"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def create(self, request, *args, **kwargs):
        '''
        :param 'model_set'
        - shape
            {
                ml_method: linear_regression, decision_tree, random_forest, ..,
                model_features: picked_features (default: all)
                - [feature1, feature2, ....]
            }
        :return:
        '''
        try:
            ml_method: str = request.data.get('ml_method', 'linear_regression')
            model_features: dict = request.data_get('model_features', None)
            result_mse = set_ml_model_training(
                ml_method=ml_method, features=model_features
            )
            msg = f'{ml_method} model set and trained'
            return Response(
                data={'mse': result_mse, 'msg': msg},
                status=status.HTTP_201_CREATED
            )
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {
                    "error_type": "SERVER",
                    "msg": f"{str(ex)} - {str(traceback.format_exc())}"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )