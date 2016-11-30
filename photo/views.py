# coding: utf-8
from django.shortcuts import render, get_object_or_404
# HttpResponse는 HTTP handler로 보내는 객체를 만드는데 여기엔 template을 따로 처리하는
# 기능이 없다. render함수를 이용하여 rendered 한 출력물을 plain text 로 받아서 출력하여
# HttpResponse로 보냄

from django.http import HttpResponse
from .models import Photo
#.models 는 photo.models와 같은 내용인데 views.py와 같은 path에 있기 때문

def single_photo(req, photo_id):
	# try:
	# 	photo = Photo.objects.get(pk=photo_id)
	# except Photo.DoesNotExist:
	# 	return HttpResponse("사진이 없습니다.")

	photo = get_object_or_404(Photo, pk=photo_id)

	response_text = '<p>{photo_id}번 사진을 보여 드릴게요.</p>'
	response_text += '<p><img src="{photo_url}" /></p>'

	return HttpResponse(response_text.format(
	        photo_id=photo_id,
			photo_url=photo.image_file.url
	    )
	)
# single_photo(req, photo_id)
# 첫 번째로 받는 req 인지는 request와 관련된 여러 정보와 기능을 수행
# urls.py 에서 view 함수로 넘길 인자 이름을 지정하지 않아도 된다. args로 표현
# 이 경우 urls.py에서는 ?P<photo_id>와 같은 id값이 따로 필요 없다.
# 만약 인자가 여러개인 경우는 args[0] ,args[1], args[2] 이런식으로 해도 되지만
# args보다 인자 이름을 지정하는것이 가독성이 좋음

# try,except 사진이 없으면 DoesNotExist 이용하여 exception handdling
# DoesNotExist 인 경우에는 없는 페이지로 봐도 부방하니 404 오류를 일으키고 오류 안내 페이지를
# 따로 만들어 주는것이 좋다.
# 이를 한방에 해주는 친구가 get_object_or_404

# Django 는 이용자가 업로드한 파일은 MEDIA_URL과 MEDIA_ROOT라는 설정값을 참조하여 제공
# models.py 의 FileField 필드 클래스나 ImageField 필드 클래스로 지정하는 upload_to 인자는
# MEDIA_URL 과 MEDIA_ROOT 경로 아래에 위치함
# settings로 가서 MEDIA 설정해주자
