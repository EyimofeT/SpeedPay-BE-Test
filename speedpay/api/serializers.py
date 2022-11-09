from rest_framework import serializers
from .models import User 



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('first_name','last_name','username','email','password')
        fields = '__all__'
        # extra_kwargs = {
        #     'password':{'write_only': True}
        # }
        
    def create(self, validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        # return super().create(validated_data)
        
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
        
class UserCreatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username','account_number', 'balance')
       
class UserDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('balance')        