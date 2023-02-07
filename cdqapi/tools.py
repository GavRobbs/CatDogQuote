from .models import Quote
from django.conf import settings
import boto3
from random import choice
import requests

def populate_quotes():
    #Read quotes.txt line by line
    #Split each line into quote text and author using the tilde as a delimiter
    #Create a new quote with the data and save it to the database
    print("Going to populate the database with the quotes from the file")
    with open('quotes.txt') as quotefile:
        for line in quotefile.readlines():
            [qtext, author] = line.split('~')
            added_quote = Quote(text=qtext.rstrip(), author=author.rstrip())
            added_quote.save()

def delete_quotes():
    print("Deleting all the quotes in the database")
    Quote.objects.all().delete()

def get_random_dog_pic_url():
    session = boto3.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_KEY)
    s3_resource = session.resource('s3')
    dog_bucket = s3_resource.Bucket(settings.DOG_PIC_BUCKET_NAME)
    all_dogs = dog_bucket.objects.all()

    #This is actually dangerous (and probably somewhat expensive)
    #but since I know I won't have a lot of dogs stored, I can get away with it
    selected_object = choice(list(all_dogs)).key

    client = session.client('s3')
    url = client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': settings.DOG_PIC_BUCKET_NAME,
            'Key': selected_object
        },
        ExpiresIn=3600
    )
    return url

def get_random_cat_pic_url():
    #Check the CAT API documentation
    #I didn't need an API key because I don't make a lot of requests
    cat_url = requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']
    return cat_url

