from django import forms
from article.models import TopicArticle
class StudentTeamForm(forms.ModelForm):
    class Meta:
        model =TopicArticle
        fields = ("title","topic","image","artice_content",)

