from django.db.models import fields
from rest_framework import serializers
from myapp.models import TestModel

class TestSerealizer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'
        # fields = ['store_name', 'seating_capacity', 'takeout_support', 'store_url',
        #           'store_telnum', 'store_postal_code', 'store_address1', 'store_address2',
        #           'store_address3', 'store_address4', 'store_address5']
        # exclude = ['email']       # こんな感じでemail以外を返すことが出来る

    #? 個別のバリデーション 参考に残しておく
    # def validate_store_name(self, store_name):
    #     if 'hoge' in store_name.lower():
    #         raise serializers.ValidationError('The store_name `hoge` can not be used.')
    #     return store_name
