# coding: utf-8

from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse_lazy

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

		def get_absolute_url(self):
			return reverse_lazy('view_single_photo', kwargs={'photo_id': self.id})

# image_file 과 filtered_image_file 의 upload_to 경로는 사실 settings.py에서 해야한다
# 나중에 수정 할 것임.
