from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm):
    caption = forms.CharField(widget=forms.Textarea(attrs={
            'class':'form-control border-1',
            'height':"30",
            'rows':"5"
        }))
    class Meta:
        model = Post
        fields = ['caption', 'posted_photo']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control border-0 rounded-pill bg-gray",
            "placeholder":"Write a comment"
        }))
    class Meta:
        model = Comments
        fields = ['post', 'comment']