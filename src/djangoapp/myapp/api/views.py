from rest_framework import generics
from myapp.models import TestModel
from myapp.api.serializers import TestSerealizer



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
