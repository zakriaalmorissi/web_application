from django import forms
from .models import Post


class PostForm(forms.ModelForm):
   # username = forms.CharField()
    class Meta:
        model = Post
        fields = ['text','image']

        widgets = {"text":forms.Textarea(attrs={"class":"mt-2 py-6 px-2 bg-gray-100 rounded-xl","id":"text"}),
                   "image":forms.FileInput(attrs={"class":"mb-3 bg-gray-100  py-6 px-3","id":"image"})}

