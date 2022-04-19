from datetime import datetime
from rest_framework import generics, status
from myapp.models import TestModel, RoomModel
from myapp.api.serializers import TestSerealizer, RoomSerealizer, RoomSerealizerImagePath
from rest_framework.response import Response
import os
import datetime
import base64
from PIL import Image
from io import BytesIO
import uuid

MEDIA_DIR = "media/"
IMAGE_NAME = "upload_image"

# class TestInformation(generics.RetrieveAPIView):

#     queryset = TestModel.objects.all()
#     serializer_class = TestSerealizer


# RetrieveAPIViewにすることで、ログインユーザー以外のpkを返さない 404となる
class TestInformation(generics.ListAPIView):
# class TestInformation(generics.RetrieveAPIView):

    queryset = TestModel.objects.all()
    serializer_class = TestSerealizer

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases
    #     for the currently authenticated user.
    #     """
    #     # E-mailが格納される
    #     user = self.request.user

    #     return TestModel.objects.filter(email=user)

class RoomInformation(generics.RetrieveAPIView):
    queryset = RoomModel.objects.all()
    serializer_class = RoomSerealizer
    lookup_field = 'room_token'

    def get(self, request, **kwargs):
        url_path_token = kwargs.get('room_token')
        # .values()でクエリセットをjsonで取得
        try:
            room_model = RoomModel.objects.values().get(room_token=url_path_token)
        except RoomModel.DoesNotExist:
            print("【DEBUG】存在しないURL")
            # エラー404を返す
            content = {'error': "ページが存在しません"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


        if room_model["image1_path"] is not None:
            # saveディレクトリのpathを追加し、エンコード
            room_model["image1_path"] = "media/" + room_model["image1_path"]
            room_model["image1_path"] = encode_upload_image(room_model["image1_path"])
        
        if room_model["image2_path"] is not None:
            # saveディレクトリのpathを追加し、エンコード
            room_model["image2_path"] = "media/" + room_model["image2_path"]
            room_model["image2_path"] = encode_upload_image(room_model["image2_path"])

        # print("【DEBUG】", room_model)

        return Response(room_model)


class AddRoomInformation(generics.ListCreateAPIView):
    serializer_class = RoomSerealizer

    # def post(self, request):
    #     print("postOK!!")

    #     print(request.data)
    #     request.data['room_url'] = "http://creepfablic.site"
    #     # 継承元クラスのcreateメソッドがvalidationなどの処理を一括で実行する
    #     response = super().create(request)
    #     print(response)

    #     return Response(status=response.status_code)
    def get_queryset(self):
        return RoomModel.objects.all()


    def create(self, request, *args, **kwargs):
        print("【DEBUG】request headers {}".format(request.headers['Origin']))
        print(request.headers)

        if ( request.data['upload_image1'] is None ) or ( request.data['upload_image2'] is None ):
            # いずれかの画像が未選択の場合はデータなしとする
            request.data['upload_image1'] = None
            request.data['upload_image2'] = None
            save_image_dir_name_list = [None, None]
        else:

            img_base64_list = [request.data['upload_image1'], request.data['upload_image2']]

            # TODO:一旦仮でディレクトリの作成は日付+uuid
            token_uuid = str(uuid.uuid4())
            save_dir_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + "-" + token_uuid
            save_image_dir_name_list = decode_upload_image(img_base64_list, save_dir_name)

            # ここで任意のURLを作成する
            request.data['room_url'] = request.headers['Origin'] + "/vote/" + save_dir_name

            # ここでトークンを作成する
            request.data['room_token'] = save_dir_name

        print("【DEBUG】", request.data['room_name'], request.data['room_url'], request.data['image1_name'], request.data['image2_name'])
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        create_model = RoomModel.objects.create(
            room_name=request.data['room_name'],
            room_url=request.data['room_url'],
            room_token=request.data['room_token'],
            image1_name=request.data['image1_name'],
            image1_path=save_image_dir_name_list[0],
            image2_name=request.data['image2_name'],
            image2_path=save_image_dir_name_list[1],
            # create時は投票数は0
            image1_votenum=0,
            image2_votenum=0
        )

        result = RoomSerealizer(create_model)
        return Response(result.data, status=status.HTTP_201_CREATED)

class VoteRoomInformation(generics.RetrieveUpdateAPIView):
    queryset = RoomModel.objects.all()
    serializer_class = RoomSerealizer
    lookup_field = 'room_token'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


'''---------------------------------------------
@ base64エンコードイメージのデコード保存関数
@ in        img_base64_list: base64エンコード文字列(List(str))
            media_dir: 保存ディレクトリ名(str)
@ return    保存ディレクトリ名のリストList(str)
---------------------------------------------'''
def decode_upload_image(img_base64_list, media_dir):
    ret_list = []

    for index, img_base64 in enumerate(img_base64_list):
        # デコードの先頭で画像形式判別
        # PNG: iVBOR  gif: R0lGO  jpeg: /9j/4
        img_base64_data = img_base64.split(',')[1]

        if img_base64_data.startswith("iVBOR"):
            image_format = ".png"
        elif img_base64_data.startswith("R0lGO"):
            image_format = ".gif"
        elif img_base64_data.startswith("/9j/4"):
            image_format = ".jpeg"
        else:
            image_format = None
            print("【ERROR】無効な形式のアップロード")

        print("{} 形式の画像がアップロードされました".format(image_format))


        code = base64.b64decode(img_base64_data)

        image_decoded = Image.open(BytesIO(code))
    
        if not os.path.exists(MEDIA_DIR + media_dir):
            os.makedirs(MEDIA_DIR + media_dir)

        save_image_dir_name =  media_dir + '/' + IMAGE_NAME + str(index + 1) + image_format

        image_decoded.save(MEDIA_DIR + save_image_dir_name)

        ret_list.append(save_image_dir_name)

    return ret_list


'''---------------------------------------------
@ イメージのbase64エンコード関数
@ in        img_path: イメージの保存path(str)
@ return    base64エンコード文字列(str)
---------------------------------------------'''
def encode_upload_image(img_path):
    # 拡張子の取得
    image_format = img_path.split(".")[1]

    with open(img_path, 'rb') as f:
        data = f.read()
    encode_data = base64.b64encode(data)

    return "data:image/{};base64,{}".format(image_format, encode_data.decode())
