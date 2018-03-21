from django import forms
from .models import Post, Comment


class EmailPostForm(forms.Form):
    """
    Form to share posts via Email
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
