import traceback

from django.db import transaction
from django.utils import timezone

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

import pandas as pd

from house_prices.house_prices.core.utils import mapping_dict
from house_prices.house_prices.core.models.data_model import HousePriceFactor


class CSVDataView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            current_date = request.data.get("data_date", timezone.now())
            chunk_size = request.data.get("chunk_size", 146)
            file_path = request.data.get["path"]

            df_iterator = pd.read_csv(file_path, chunksize=chunk_size)
            current_chunk_num = 0

            with transaction.atomic():
                for chunk_num, chunk in enumerate(df_iterator):
                    current_chunk_num += 1
                    chunk = chunk.where(pd.notnull(chunk), None)

                    for batch_num in range(0, len(chunk), chunk_size):
                        batch = chunk.iloc[batch_num:batch_num + chunk_size]
                        instances = []
                        for index, row in batch.iterrows():
                            instance = HousePriceFactor()
                            for column, value in row.items():
                                setattr(instance, mapping_dict[column], value)
                            instance.created_at = current_date
                            instances.append(instance)
                        HousePriceFactor.objects.bulk_create(instances)
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
