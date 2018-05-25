from django.db import models

# Create your models here.
class Post(models.Model):

    publish      = models.DateField(auto_now=False, auto_now_add=False)
    timupdate=models.DateTimeField(auto_now=True, auto_now_add=False)
    title= models.CharField(max_length=200)
    slug  = models.SlugField(unique=True)
    content =models.TextField()
    gambar = models.FileField(blank=True)



    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
