from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Facebook_Page(models.Model):
    name = models.TextField()
    fbid = models.TextField()
    image_url = models.TextField()

    @property
    def url(self):
        return "https://www.facebook.com/" + self.fbid

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name + ", " + self.fbid


class Video(models.Model):
    created = models.DateTimeField(null=True, blank=True)
    image_url = models.TextField()
    fbid = models.TextField()
    page_url = models.TextField()
    recipe_text = models.TextField()
    description = models.TextField()
    host_page = models.ForeignKey(Facebook_Page, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def url(self):
        return "https://www.facebook.com/video/embed?video_id=" + self.fbid

    class Meta:
        ordering = ('created',)

