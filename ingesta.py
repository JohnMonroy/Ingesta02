import boto3

ficheroUpload = "data.csv"
nombreBucket = "bucketjo123456"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, "Ingesta/" + ficheroUpload)
print(response)

print("Ingesta completada")