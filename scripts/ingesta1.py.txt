import pandas as pd
from faker import Faker
import boto3, io

fake = Faker()

data = [{"id": i, "name": fake.name(), "city": fake.city()} for i in range(500)]
df = pd.DataFrame(data)

csv_buffer = io.StringIO()
df.to_csv(csv_buffer, index=False)

s3 = boto3.client("s3")
s3.put_object(
    Bucket="proyect-storage",
    Key="microservicio1/usuarios.csv",
    Body=csv_buffer.getvalue()
)

print("Archivo de usuarios subido a S3!")
