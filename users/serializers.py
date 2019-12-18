from django.core.mail import EmailMessage, send_mail
from rest_framework import serializers
from django.contrib.auth.models import User
from django.template.loader import render_to_string


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
        rendered = render_to_string('email.html', {'name': user.first_name})
        try:
            msg = EmailMessage(
                'Verifica tu correo de clontrello',
                rendered,
                'Clontrello <from@example.com>',
                [user.email],
            )
            msg.content_subtype = 'html'
            msg.send()
        except Exception as error:
            print(error)

        return user
