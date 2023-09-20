from distutils.command.upload import upload
from statistics import mode
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class contact_me(models.Model):
    name=models.CharField(max_length=265)
    email=models.EmailField(max_length=100, null=False,error_messages={'invalid_choice':"you custom error message"})    
    subject=models.CharField(max_length=150)
    company=models.CharField(max_length=150)
    project_Summary=models.TextField(max_length=1500)

    def __str__(self):

        return self.name+"|"+str(self.email)+"|"+self.subject+"|"+ self.company+"|"+ str(self.project_Summary)

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now())
    status = models.IntegerField(choices=STATUS, default=0)
    Img = models.ImageField(null =True, blank = True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
        


