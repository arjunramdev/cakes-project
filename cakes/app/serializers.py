from rest_framework import serializers

from .models import Cake,Category,Shape,Weight

class CategorySerializer(serializers.ModelSerializer):

    class Meta :

        model = Category 

        fields = '__all__'


class ShapeSerializer(serializers.ModelSerializer):

    class Meta :

        model = Shape 

        fields = '__all__'


class WeightSerializer(serializers.ModelSerializer):

    class Meta :

        model = Weight 

        fields = '__all__'

class CategoryField(serializers.PrimaryKeyRelatedField):

    def get_attribute(self, instance):

        return getattr(instance,self.source_attrs[0])

    def to_representation(self, value):

        return CategorySerializer(value).data


class ShapeField(serializers.PrimaryKeyRelatedField):

    def get_attribute(self, instance):

        return getattr(instance,self.source_attrs[0])

    
    def to_representation(self, value):

        return ShapeSerializer(value).data


class WeightField(serializers.PrimaryKeyRelatedField):

    def get_attribute(self, instance):

        return getattr(instance,self.source_attrs[0])

    
    def to_representation(self, value):

        return WeightSerializer(value).data


class CakeSerializer(serializers.ModelSerializer):

    category = CategoryField(queryset=Category.objects.all())

    shape = ShapeField(queryset=Shape.objects.all())

    weight = WeightField(queryset=Weight.objects.all())
    status = serializers.SerializerMethodField()
    
    def get_status(self,obj):
        if obj.price < 1000:
            return 'max saver'

        return None

    class Meta :

        model = Cake 

        # fields = ['name','description','photo']

        fields = '__all__'

        # exclude = []

        


         