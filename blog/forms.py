from django  import forms

from .models import Post


# Create your views here.

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title','text','created_date','published_date','dest_date')

