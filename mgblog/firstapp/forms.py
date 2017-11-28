from django import forms
from django.core.exceptions import ValidationError


def words_validator(comment):
    if len(comment) < 4:
        raise ValidationError('not enough words')


def keyword_validator(comment):
    keyword = ['钱', '发票']
    for k in keyword:
        if k in comment:
            raise ValidationError('Your comment contains invaild words please check it again')


class CommentForm(forms.Form):
    name = forms.CharField(max_length=250)
    content = forms.CharField(
        widget=forms.Textarea(),
        error_messages={
            'required': 'wow, NO SUCH words'
        },
        validators=[words_validator, keyword_validator]
    )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()