import pandas as pd
from faker import Faker
import boto3, io, random

fake = Faker()

# Generar datos ficticios (pagos)
data = []
for i in range(500):
    data.append({
        "id": i,
        "reserva_id": random.randint(1, 500),
        "monto": round(random.uniform(20, 200), 2),
        "metodo": random.choice(["tarjeta", "paypal", "efectivo"])
    })

df = pd.DataFrame(data)

csv_buffer = io.StringIO()
df.to_csv(csv_buffer, index=False)

s3 = boto3.client("s3")
s3.put_object(
    Bucket="proyect-storage",
    Key="microservicio3/pagos.csv",
    Body=csv_buffer.getvalue()
)

print("Archivo de pagos subido a S3!")
