import boto3
from keys import ACCESS_KEY, SECRET_KEY
bucket_name = "bucket-aws15-curso"

def connectionS3():
    sessionAWS = boto3.Session(ACCESS_KEY, SECRET_KEY)
    sessionS3 = sessionAWS.resource('s3')
    return sessionS3

def get_file():
    sessionS3 = connectionS3()
    bucket_proj = sessionS3.Bucket(bucket_name)
    bucket_obj = bucket_proj.objects.all()
    for obj in bucket_obj:
        print(obj.key)
    print(bucket_obj)
    
def save_photo(id, photo):
    photo_path = "/tmp/" + photo.filename
    photo.save(photo_path)
    print("La Foto fue guardada")
    return photo_path

def upload_photoS3(sessionS3, photo_path):
    folder_imagesS3 = "images/photo1.jpg" 
    sessionS3.meta.client.upload_file(photo_path, bucket_name, folder_imagesS3)
    print("Foto Subida")