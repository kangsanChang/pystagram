# coding: utf-8
from django.shortcuts import render,redirect, get_object_or_404
# HttpResponse는 HTTP handler로 보내는 객체를 만드는데 여기엔 template을 따로 처리하는
# 기능이 없다. render함수를 이용하여 rendered 한 출력물을 plain text 로 받아서 출력하여
# HttpResponse로 보냄

from django.http import HttpResponse
from .models import Photo
#.models 는 photo.models와 같은 내용인데 views.py와 같은 path에 있기 때문

# view함수는 언제나 첫 번쨰 인자로 request 객체를 전달 받는다.

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

from .forms import PhotoEditForm

def new_photo(request):
	if request.method == "GET":
		edit_form = PhotoEditForm()
	elif request.method == "POST":
		edit_form = PhotoEditForm(request.POST, request.FILES)
		if edit_form.is_valid():
			new_photo = edit_form.save()
			return redirect(new_photo.get_absolute_url())

	return render(request, 'new_photo.html', {'form': edit_form})
	# PhotoEditForm class 객체를 인스턴스 객체로 생성한 edit_form 을 전달

# render는 대개 세 가지 인자를 필요로 함. request, template file, template context
# request는 Template 에서 context로 request객체 를 지정하는(mapping)하는데 사용됨
# 두 번째 인자는 template file path를 문자열로 지정
# 세 번째 인자는 template file안에서 사용할 context를 dict객체로 전달.
# key인 'form'은 template파일 안에서 form이라는 이름으로 사용하는 template 변수가 됨
# value인 edit_form (PhotoEditForm()의 인스턴스 객체)가 이 템플릿 변수에 연결된 객체

# Django 는 이용자가 업로드한 파일은 MEDIA_URL과 MEDIA_ROOT라는 설정값을 참조하여 제공
# models.py 의 FileField 필드 클래스나 ImageField 필드 클래스로 지정하는 upload_to 인자는
# MEDIA_URL 과 MEDIA_ROOT 경로 아래에 위치함
# settings로 가서 MEDIA 설정해주자

# 같은 url을 이용하여
# GET으로 접근 시 파일 제출할 폼을 띄어주고
# POST로 접근 시 submit을 한다.

# is_valid()는 오류가 없으면 True를 반환하고 있으면 False를 반환하고, 유효 여부는 폼 인스턴스
# 객체의 errors 맴버에 사전형 객체처럼 생긴 ErrorDict 의 인스턴스 객체로 할당함.

# save() 는 django forms의 ModelForm 클래스에 있는 Method인데 연결한 모델의 데이터를 저장하고
# 저장한 모델의 인스턴스 객체를 반환합니다.

# .get.absolute.url() 메서드는 모델의 개별 데이터에 접근할 수 있는 URL문자열을 반환함.
# 우리는 개별 사진 보는 url을 /photo/사진 ID/ 패턴으로 할 것임.
# permalink()를 써도 되지만 get.absolute.url()은 Django가 감춰진 동작으로 알아서 처리(magic)
# 이런 관례(convention)를 따르면 일일이 지정하고 설정하지 않아도 되어 코드가 간결해진다.
