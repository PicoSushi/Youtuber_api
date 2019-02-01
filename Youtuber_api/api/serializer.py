from rest_framework import serializers
from .models import Vtuber, Youtuber

# Serializer は

# 複雑な入力値をモデルに合わせてバリデーションしてレコードに伝えたり(入力)
# Model(レコード)を適切な形式にフォーマットしたり(出力)
# と言った具合に、 APIの リクエスト / レスポンス に特化した機能を提供します。


class VtuberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vtuber
        fields = '__all__'


class YoutuberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtuber
        fields = '__all__'
