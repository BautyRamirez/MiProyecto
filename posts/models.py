from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    created_on =  models.DateTimeField(auto_now_add=True)
    content = models.TextField()


    def __str__(self):
        return self.title