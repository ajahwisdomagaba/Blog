from django.db import models


# Create your models here.

class Blog(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=100)
    author_email = models.EmailField(
        null=True # Makes a column optional database specific feature
        default="any_author@email.com", #The fixed data that is used when the inpu is not provided
        blank=False #Form-specific
    )
    published_at = models.DateTimeField(auto_now=True)



    def __str__(self):  #This helps us reference in dashboard with the headline of each blog
        return f"{self.headline} by {self.author}"