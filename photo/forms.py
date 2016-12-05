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

# photoEditForm 모델 폼의 Meta 클래스에서 폼 필드로 사용할 모델 필드를 지정하면 됨
# 이 모델에서 meta 클래스를 이용하면 image_file. description 필드만 사용하는 녀석으로 만든다.

# 필드의 element를 한개 씩 적을 수도 있고, 전체 element에서 한개 씩 지워나갈 수도 있다.
# 지워나가는 경우 exclude 이용하여 쓸 수 있다.
# element를 하나만 적었을 경우 필드 자체를 list 나 tuple 객체로 할당해야 하므로 쉼표를 하나 더 찍어줘야 한다.
