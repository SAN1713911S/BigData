import boto3

# Configurar el cliente de S3
s3_client = boto3.client('s3')

def download_file(bucket_name, object_name, local_path):
    try:
        # Descargar el archivo desde el bucket
        s3_client.download_file(bucket_name, object_name, local_path)
        print(f"Archivo '{object_name}' descargado exitosamente y guardado en '{local_path}'.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    bucket_name = "bigdata07"
    object_name = "vockey"  
    local_path = "/home/ubuntu/python-project/v" 
    
    download_file(bucket_name, object_name, local_path)

