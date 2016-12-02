# coding: utf-8

from __future__ import unicode_literals
from django import forms
from photo.models import Photo
class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image_file', 'description', )
        # or exclude = ( 'filtered_image_file', )

# forms모듈에 있는 ModelForm class 를 상속받는 PhotoEditForm class를 만들면
# 이 class는 Form class입니다.
# exclude 이용하여 쓸 수 있다.
# list 나 tuple 객체를 할당해야 하므로 쉼표를 하나 더 찍어줘야 한다.
