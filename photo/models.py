# coding: utf-8

from __future__ import unicode_literals

from django.db import models

# django db 의 models 를 상속받음.

class Photo(models.Model):
		image_file = models.ImageField(upload_to='static_files/uploaded/original/%Y/%m/%d') 
		filtered_image_file = models.ImageField(upload_to='static_files/uploaded/filtered/%Y/%m/%d') 
		description = models.TextField(max_length=500, blank=True)
		created_at = models.DateTimeField(auto_now_add=True)
		
		def delete(self, *args, **kwargs):
			self.image_file.delete()
			self.filtered_image_file.delete()
			super(Photo, self).delete(*args, **kwargs)

