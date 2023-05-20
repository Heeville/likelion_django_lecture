from django import forms 
from .models import Post
from django.forms import ValidationError

# class PostBaseForm(forms.Form):
#     CATEGORY_CHOICES=[
#         ('1','일반'),
#         ('2','계정'),
#     ]
#     image=forms.ImageField(label='IMAGE')
#     content=forms.CharField(label="CONTENT",widget=forms.Textarea,required=True)
#     category=forms.ChoiceField(label='CATEGORY',choices=CATEGORY_CHOICES)
    
    
class PostBaseForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        

class PostCreateForm(forms.ModelForm):
    class Meta(PostBaseForm.Meta):
        fields=['image','content']
        
    def clean_content(self):
        data=self.cleaned_data['content']
        if "비속어"==data:
            raise ValidationError("'비속어'는 사용하실 수 없습니다.")
        return data

class PostUpdateForm(forms.ModelForm):
    class Meta(PostBaseForm.Meta):
        fields=['image','content']
