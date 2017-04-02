from django.db import models
from django.core.urlresolvers import reverse
from multiselectfield import MultiSelectField
#from tinymce.widgets import TinyMCE

#Declare post types
letter = "Letter"
article = "Article"
image = "Image"
video = "Video"

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    tags_1 = MultiSelectField(choices = 
                        ((letter, 'Letter'),
                        (article, "Article"),
                        (image, "Image"),
                        (video, "Video"))
                        , null = True
                        , blank = True
                    )

class Blog(models.Model):
    slug = models.CharField(max_length = 120)
    name = models.CharField(max_length = 120)
    tag = models.CharField(max_length = 240)
    creator = models.CharField(max_length = 60)
    about = models.TextField()

class Meta:
    ordering = ['-created']

def __unicode__(self):
    return u'%s' % self.title

def get_absolute_url(self):
    return reverse('main.views.post', args=[self.slug])

    #widget=TinyMCE()