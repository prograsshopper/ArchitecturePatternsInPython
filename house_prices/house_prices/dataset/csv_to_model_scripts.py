import pandas as pd
from django.utils import timezone
from datetime import timedelta

from house_prices.house_prices.core.models.data_model import HousePriceFactor
from house_prices.house_prices.core.utils import mapping_dict

days_per = 5
now = timezone.now()
# datetime.datetime(2024, 4, 20, 8, 2, 51, 949630, tzinfo=datetime.timezone.utc)
td = timedelta(days=days_per * 10)
cur_date = now - td
current_chunk_num = 0

chunk_size = 146
csv_file = 'dataset/train.csv'
df_iterator = pd.read_csv(csv_file, chunksize=chunk_size)

excluded_batches_data = pd.DataFrame()

for chunk_num, chunk in enumerate(df_iterator):
    cur_date = now - timedelta(days=days_per * (10 - current_chunk_num))
    current_chunk_num += 1
    chunk = chunk.where(pd.notnull(chunk), None)

    for batch_num in range(0, len(chunk), chunk_size):
        batch = chunk.iloc[batch_num:batch_num + chunk_size]
        if current_chunk_num > 7:
            excluded_batches_data = pd.concat([excluded_batches_data, batch])
            continue
        instances = []
        for index, row in batch.iterrows():
            instance = HousePriceFactor()
            for column, value in row.items():
                setattr(instance, mapping_dict[column], value)
            instance.created_at = cur_date
            instances.append(instance)
        HousePriceFactor.objects.bulk_create(instances)
excluded_batches_data.to_csv('excluded_batches.csv', index=False)
