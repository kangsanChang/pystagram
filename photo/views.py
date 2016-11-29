# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse

def single_photo(req):
	return HttpResponse('3번 사진을 보여 줍니다.')
# Create your views here.
