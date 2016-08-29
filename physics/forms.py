from django import forms
from django.forms import ModelForm
from .models import Topic, Lecture, PSet, News, Announcement, TopicRequest, Suggestion

class TopicForm(ModelForm):
    class Meta:
        model=Topic
        fields=['title','description','level']
    

class LectureForm(ModelForm):
    
    class Meta:
        model = Lecture
        fields = ['title','description','lecture_file','level','topic']
        

class PSetForm(ModelForm):
    solutions_file = forms.FileField(required = False)
    solutions_description = forms.CharField(required =False )
    class Meta:
        model = PSet
        fields = ['title','description','problems_file','solutions_description','solutions_file','level','topic']
        
class NewsForm(ModelForm):
    
    class Meta:
        model = News
        fields=['title','text']
        
class AnnouncementForm(ModelForm):
    
    class Meta:
        model = Announcement
        fields=['title','text']
        
class SuggestionForm(ModelForm):
    
    class Meta:
        model = Suggestion
        fields=['title','description','response_email']
        
class TopicRequestForm(ModelForm):
    
    class Meta:
        model = TopicRequest
        fields=['title','description','response_email']
        
class EmailForm(forms.Form):
    your_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
        