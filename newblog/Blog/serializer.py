from .models import Comments
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comments
        fields = ["id","blog", "content", "created_at"]
