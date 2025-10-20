from rest_framework import serializers
# from watchlist_app.models import Movie
from watchlist_app.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = '__all__'

# --------------------------------------------------------------------------------------------------
# Model Serializer

# 3. Validators --> bar bar likhne ki jagah ek baar hi use kr skte hai
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")

# class MovieSerializers(serializers.ModelSerializer):
    # released_date = serializers.SerializerMethodField()       # SerializerMethodField
    # name_letter_count = serializers.SerializerMethodField()
    # class Meta:
        # model = Movie
        # fields = '__all__'
        # exclude = ['active']
        # OR
        # fields = ['id', 'name', 'description','active']

    # SerializerMethodField used
    # def get_name_letter_count(self, object):
        # return len(object.name)

    # 2. Field-level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short !')
    #     else:
    #         return value
    
    # 1. Object-level validation
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     else:
    #         return data



# ----------------------------------------------------------------------------------------------------------------
# COVERED--> SERIALIZER, 3 TYPES VALIDATORS

# 3. Validators --> bar bar likhne ki jagah ek baar hi use kr skte hai
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")

# class MovieSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField(default=True)

    # The create() and update() methods define how instances are created or modified when calling serializer.save()

    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
        # instance is old data and validated_data is new data

        # validated_data.get('name') --> extracting name from new data than updating in new instance.name
        # instance.name = validated_data.get('name', instance.name)
        # instance.description = validated_data.get('description', instance.description)
        # instance.active = validated_data.get('active', instance.active)
        # instance.save()
        # return instance     # now this instance is new data
    

    # 2. Field-level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short !')
    #     else:
    #         return value
    
    # 1. Object-level validation
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     else:
    #         return data
