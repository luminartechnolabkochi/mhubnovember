from django.db import models

# Create your models here.



class Movie(models.Model):

    title=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    director=models.CharField(max_length=200)

    run_time=models.PositiveIntegerField()

    language=models.CharField(max_length=200)

    genre=models.CharField(max_length=200)

    producer=models.CharField(max_length=200,null=True)


    def __str__(self):

        return self.title
    
    

   


