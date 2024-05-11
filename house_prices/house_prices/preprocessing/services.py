from django.db import transaction

import pandas as pd

from core.utils import mapping_dict
from core.models.data_model import HousePriceFactor


def save_dataset_to_db(current_date, chunk_size, file_path):
    try:
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
    except KeyError as ke:
        raise ke
    except Exception as ex:
        raise ex
