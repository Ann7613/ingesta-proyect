import pandas as pd
from faker import Faker
import boto3, io, random

fake = Faker()

data = []
for i in range(500):
    data.append({
        "id": i,
        "user_id": random.randint(1, 500),
        "guide": fake.name(),
        "date": fake.date_this_year()
    })

df = pd.DataFrame(data)

csv_buffer = io.StringIO()
df.to_csv(csv_buffer, index=False)

s3 = boto3.client("s3")
s3.put_object(
    Bucket="proyect-storage",
    Key="microservicio2/reservas.csv",
    Body=csv_buffer.getvalue()
)

print("Archivo de reservas subido a S3!")
