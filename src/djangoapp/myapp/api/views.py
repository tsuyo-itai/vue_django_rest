from rest_framework import generics, status
from myapp.models import TestModel, RoomModel
from myapp.api.serializers import TestSerealizer, RoomSerealizer
from rest_framework.response import Response



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

class RoomInformation(generics.ListAPIView):

    queryset = RoomModel.objects.all()
    serializer_class = RoomSerealizer

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

    def create(self, request, *args, **kwargs):

        # ここで任意のURLを作成する
        request.data['room_url'] = "http://testurl8888.com"

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        create_model = RoomModel.objects.create(
            room_name=request.data['room_name'],
            room_url=request.data['room_url'],
        )

        result = RoomSerealizer(create_model)
        return Response(result.data, status=status.HTTP_201_CREATED)
