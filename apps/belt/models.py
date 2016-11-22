from __future__ import unicode_literals
from ..login.models import User
from django.db import models

class QuoteManager(models.Manager):
    def make_quote(self, request):
        errors = self.validate_quote(request)

        if errors:
            return errors

        poster = User.objects.get(id=request.session['user']['user_id'])
        self.create(poster=poster, author=request.POST['author'],content=request.POST['content'])
      
        return errors
    def validate_quote(self,request):
        errors = []
        if not request.POST['content']:
            errors.append('Message cannot be blank')
        elif len(request.POST['content']) < 10:
            errors.append('Message must be more than 10 characters')
        if not request.POST['author']:
            errors.append('Quoted by cannot be blank')
        elif len(request.POST['author']) < 3:
            errors.append('Quoted by, cannot be less than 3 characters')
        return(errors)

class Quote(models.Model):
    poster = models.ForeignKey(User, related_name='posted_quote')
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    favorites = models.ManyToManyField(User, related_name='favorite_quotes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuoteManager()