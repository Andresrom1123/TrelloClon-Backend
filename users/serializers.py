from django.core.mail import EmailMessage, send_mail
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    General purposse User serializer
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        try:
            msg = EmailMessage(
                'Asunto',
                '<h1>Que onda compa chavaa!</h1>',
                'Salvador <from@example.com>',
                [user.email]
            )
            msg.content_subtype = 'html'
            msg.send()
        except Exception as error:
            print(error)

        return user

