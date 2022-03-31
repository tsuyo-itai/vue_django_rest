from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseBadRequest

# 以下3行は最後にimport (上位階層からimportするにはこれしかない)
import sys
sys.path.append('../')
from myapp.models import RoomModel
# Create your views here.




class UploadVotePage(View):
    """投票ページ"""
    def get(self, request, **kwargs):
        url_path_token = kwargs.get('token')

        try:
            # 存在するURLの場合
            room_url_query = RoomModel.objects.get(room_url="http://127.0.0.1:8000/view/" + url_path_token)
            print("【DEBUG】room_url={}".format(room_url_query.room_url))
        # 例外の種類は後々絞り込む
        except:
            # 存在しないURLの場合
            return HttpResponseBadRequest('<h1>Bad Request errcode=1 (400)</h1>', content_type='text/html')

        return redirect('http://127.0.0.1:8080/vote')

