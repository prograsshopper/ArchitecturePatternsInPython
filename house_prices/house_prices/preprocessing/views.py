import traceback
import pandas as pd

from django.utils import timezone

from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .services import save_dataset_to_db


class CSVDataView(ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            current_date = request.data.get("data_date", timezone.now())
            chunk_size = request.data.get("chunk_size", 146)
            file_path = request.data.get["path"]
            result = save_dataset_to_db(current_date, chunk_size, file_path)
            return Response(status=status.HTTP_201_CREATED)
        except KeyError as ke:
            return Response(
                {
                    "error_type": "KEY",
                    "msg": f"{str(ke)} - {str(traceback.format_exc())}"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except pd.errors.ParserError as pe:
            traceback.print_exc()
            return Response(
                {
                    "error_type": "PANDAS",
                    "msg": f"{str(pe)} - {str(traceback.format_exc())}"
                },
                status=status.HTTP_409_CONFLICT
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
