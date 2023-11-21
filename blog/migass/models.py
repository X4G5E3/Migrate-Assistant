from django.db import models
from django.urls import reverse

class Posts(models.Model):
    img = models.ImageField(upload_to='post_img')
    name = models.CharField(max_length=50)
    create_date = models.DateField(auto_now=False, auto_now_add=True)
    desc = models.TextField()
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    
    def get_absolute_url(self):
        return reverse("single-post", kwargs={"post_slug": self.slug})

    
class Comments(models.Model):
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.PROTECT)
    user = models.CharField(max_length=50, blank=True)
    message = models.TextField()
    created = models.DateField(auto_now=False, auto_now_add=True)
