from django import forms
from .models import NewPost
from cloudinary.models import CloudinaryField

class PostForm(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = ['title', 'slug', 'author', 'featured_image', 'content', 'status', 'excerpt']
