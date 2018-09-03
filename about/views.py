# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'judul':'About',
		'subjudul':'ini adalah about kelas terbuka',
		'banner':'about/img/banner_about.png',
	}
	return render(request,'index.html',context)
