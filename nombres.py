import boto3

# Configurar el cliente de S3
s3_client = boto3.client('s3')

def list_buckets():
    try:
        # Obtener la lista de buckets
        response = s3_client.list_buckets()
        buckets = response['Buckets']
        
        # Imprimir los nombres de los buckets
        for bucket in buckets:
            print(bucket['Name'])
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    list_buckets()

