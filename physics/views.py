from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms
from django.utils import timezone
from django.db.models import Max
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import LectureForm, PSetForm, TopicForm, AnnouncementForm, NewsForm, SuggestionForm, TopicRequestForm, EmailForm

from .models import Topic, Lecture, PSet, Announcement, News, TopicRequest, Suggestion
# Create your views here.

def index(request):
    announcements = Announcement.objects.order_by('-pub_date')
    newsItems = News.objects.order_by('-pub_date')
    context = {'announcements':announcements, 'newsItems':newsItems}
    return render(request, 'physics/index.html', context)

def experimental(request):
    topics = Topic.objects.order_by('order')
    context = {'topics': topics}
    return render(request, 'physics/experimental.html', context)

def theoretical(request):
    topics = Topic.objects.order_by('order')
    context = {'topics': topics}
    return render(request, 'physics/theoretical.html', context)

def authenticate_user(request):
    state = "Log in below.  If you test the system, I will find you..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('physics:upload'))
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('physics/auth.html',{'state':state,'username': username},context_instance = RequestContext(request))

def contact(request):
    suggestion = Suggestion()
    topic_request = TopicRequest()
    captains = User.objects.all()
    if request.POST:
        if 'email' in request.POST:
            emailform = EmailForm(request.POST)
            if emailform.is_valid():
                subject = emailform.cleaned_data['subject']
                from_email = emailform.cleaned_data['your_email']
                message = emailform.cleaned_data['message']
                try:
                    send_mail(subject, message, from_email, ['mbphysicsteam@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect(reverse('physics:index')) #change to notification page
        if 'suggestion' in request.POST:
            suggestionform = SuggestionForm(request.POST, instance=suggestion)
            if suggestionform.is_valid():
                suggestions=Suggestion.objects.all().order_by("-order")                
                if len(suggestions) == 0:
                    suggestion.order = 1                
                else:
                    suggestion.order = suggestions[0].order+1
                suggestion.pub_date=timezone.now()
                suggestionform.save()
                # If the save was successful, redirect to another page
                return HttpResponseRedirect(reverse('physics:index')) #change to notification page
        if 'topic_request' in request.POST:
            topic_request_form = TopicRequestForm(request.POST, instance=topic_request)
            if topic_request_form.is_valid():
                topic_requests=TopicRequest.objects.all().order_by("-order")                
                if len(topic_requests) == 0:
                    topic_request.order = 1                
                else:
                    topic_request.order = topic_requests[0].order+1
                topic_request.pub_date=timezone.now()
                topic_request_form.save()
                # If the save was successful, redirect to another page
                return HttpResponseRedirect(reverse('physics:index')) #change to notification page
    else:
        suggestionform = SuggestionForm()
        topic_request_form = TopicRequestForm()
        emailform = EmailForm()
        
    return render_to_response('physics/contact.html', {'suggestionform': suggestionform,'topic_request_form':topic_request_form,'emailform':emailform,'captains':captains}, context_instance=RequestContext(request))
    
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('physics:index'))

@login_required
def upload(request):

    return render(request, 'physics/upload.html')

@login_required
def lecture(request):
    topics = Topic.objects.order_by('order')
    context = {'topics': topics}
    return render(request, 'physics/lecture.html', context)

@login_required
def add_edit_lecture(request, lecture_id=None):
     
    state = "Add or Edit Lecture"
    if lecture_id:
        lecture = get_object_or_404(Lecture, pk=lecture_id)
    else:
        lecture = Lecture()
        lectures=Lecture.objects.all().order_by("-order")     
        if len(lectures) == 0:
            lecture.order = 1                
        else:
            lecture.order = lectures[0].order+1
    lecture.pub_date=timezone.now()

    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES, instance=lecture)
        if 'cancel' in request.POST:
            return HttpResponseRedirect(reverse('physics:upload'))
        if 'delete' in request.POST:
            if lecture_id:
                return HttpResponseRedirect(reverse('physics:delete_lecture',args=(lecture_id)))
            else:
                return HttpResponseRedirect(reverse('physics:upload'))
        if form.is_valid():
            form.save()
            # If the save was successful, redirect to another page
            return HttpResponseRedirect(reverse('physics:upload'))
    else:
        form = LectureForm(instance=lecture)

    return render_to_response('physics/add_edit_lecture.html', {'form': form, }, context_instance=RequestContext(request))

@login_required
def delete_lecture(request, lecture_id=None):
    
        
    lecture = Lecture.objects.get(pk=lecture_id)
    if lecture:
        lecture.delete()
    return HttpResponseRedirect(reverse('physics:upload'))

@login_required
def pset(request):
     
        
    topics = Topic.objects.order_by('order')
    context = {'topics': topics}
    return render(request, 'physics/pset.html', context)

@login_required
def add_edit_pset(request, pset_id=None):
     
    state = "Add or Edit Problem Set"
    if pset_id:
        pset = get_object_or_404(PSet, pk=pset_id)
    else:
        pset = PSet()
        psets=PSet.objects.all().order_by("-order")                
        if len(psets) == 0:
            pset.order = 1                
        else:
            pset.order = psets[0].order+1
    pset.pub_date=timezone.now()
    if request.method == 'POST':
        form = PSetForm(request.POST, request.FILES, instance=pset)
        if 'cancel' in request.POST:
            return HttpResponseRedirect(reverse('physics:upload'))
        if 'delete' in request.POST:
            if pset_id:
                return HttpResponseRedirect(reverse('physics:delete_pset',args=(pset_id)))
            else:
                return HttpResponseRedirect(reverse('physics:upload'))
        if form.is_valid():
            form.save()
            # If the save was successful, redirect to another page
            return HttpResponseRedirect(reverse('physics:upload'))
    else:
        form = PSetForm(instance=pset) # A empty, unbound form

    # Render list page with the documents and the form
    return render_to_response('physics/add_edit_pset.html', {'form': form,}, context_instance=RequestContext(request))

@login_required
def delete_pset(request, pset_id=None):
    PSet.objects.get(pk=pset_id).delete()
    return HttpResponseRedirect(reverse('physics:upload'))

@login_required                                         
def topic(request):
     
        
    topics = Topic.objects.order_by('order')
    context = {'topics': topics}
    return render(request, 'physics/topic.html', context)

@login_required
def add_edit_topic(request, topic_id=None):
     
    state = "Add or Edit Topic"
    if topic_id:
        topic = get_object_or_404(Topic, pk=topic_id)
    else:
        topic = Topic()
        topics=Topic.objects.all().order_by("-order")                
        if len(topics) == 0:
            topic.order = 1                
        else:
            topic.order = topics[0].order+1
    topic.pub_date=timezone.now()
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if 'cancel' in request.POST:
            return HttpResponseRedirect(reverse('physics:upload'))
        if 'delete' in request.POST:
            if topic_id:
                return HttpResponseRedirect(reverse('physics:delete_topic',args=(topic_id)))
            else:
                return HttpResponseRedirect(reverse('physics:upload'))
        else:
            if form.is_valid():
                form.save()
                # If the save was successful, redirect to another page
            return HttpResponseRedirect(reverse('physics:upload'))
    else:
        form = TopicForm(instance=topic) # A empty, unbound form

    # Render list page with the documents and the form
    return render_to_response('physics/add_edit_topic.html', {'form': form,}, context_instance=RequestContext(request))

@login_required
def delete_topic(request, topic_id=None):
    Topic.objects.get(pk=topic_id).delete()
    return HttpResponseRedirect(reverse('physics:upload'))


@login_required
def announcement(request):
    announcements = Announcement.objects.order_by('-pub_date')
    context = {'announcements': announcements}
    return render(request, 'physics/announcement.html', context)

@login_required
def add_edit_announcement(request, announcement_id=None):
     
    state = "Add or Edit Announcement"
    if announcement_id:
        announcement = get_object_or_404(Announcement, pk=announcement_id)
    else:
        announcement = Announcement()
        announcements=Announcement.objects.all().order_by("-order")                
        if len(announcements) == 0:
            announcement.order = 1                
        else:
            announcement.order = announcements[0].order+1
    announcement.pub_date=timezone.now()
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if 'cancel' in request.POST:
            return HttpResponseRedirect(reverse('physics:upload'))
        if 'delete' in request.POST:
            if announcement_id:
                return HttpResponseRedirect(reverse('physics:delete_announcement',args=(announcement_id)))
            else:
                return HttpResponseRedirect(reverse('physics:upload'))
        else:
            if form.is_valid():
                form.save()
                # If the save was successful, redirect to another page
            return HttpResponseRedirect(reverse('physics:upload'))
    else:
        form = AnnouncementForm(instance=announcement) # A empty, unbound form

    # Render list page with the documents and the form
    return render_to_response('physics/add_edit_announcement.html', {'form': form,}, context_instance=RequestContext(request))

@login_required
def delete_announcement(request, announcement_id=None):
     
        
    announcement = Announcement.objects.get(pk=announcement_id)
    if announcement:
        announcement.delete()
    return HttpResponseRedirect(reverse('physics:upload'))

@login_required    
def news(request):  
    newsItems = News.objects.order_by('-pub_date')
    context = {'newsItems': newsItems}
    return render(request, 'physics/news.html', context)

@login_required
def add_edit_news(request, news_id=None):
     
    state = "Add or Edit News"
    if news_id:
        news = get_object_or_404(News, pk=news_id)
    else:
        news = News()
        newsItems=News.objects.all().order_by("-order")                
        if len(newsItems) == 0:
            news.order = 1                
        else:
            news.order = newsItems[0].order+1
    news.pub_date=timezone.now()
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if 'cancel' in request.POST:
            return HttpResponseRedirect(reverse('physics:upload'))
        if 'delete' in request.POST:
            if news_id:
                return HttpResponseRedirect(reverse('physics:delete_news',args=(news_id)))
            else:
                return HttpResponseRedirect(reverse('physics:upload'))
        else:
            if form.is_valid():
                form.save()
                # If the save was successful, redirect to another page
            return HttpResponseRedirect(reverse('physics:upload'))
    else:
        form = NewsForm(instance=news) # A empty, unbound form

    # Render list page with the documents and the form
    return render_to_response('physics/add_edit_news.html', {'form': form,}, context_instance=RequestContext(request))

@login_required
def delete_news(request, news_id=None):   
        
    news = News.objects.get(pk=news_id)
    if news:
        news.delete()
    return HttpResponseRedirect(reverse('physics:upload'))

def resources(request):
        return render(request, 'physics/resources.html')

@login_required
def topic_requests(request):
    topic_requests = TopicRequest.objects.order_by('-pub_date')
    context = {'topic_requests': topic_requests}
    return render(request, 'physics/topic_requests.html', context)

@login_required   
def view_topic_request(request,topic_request_id=None):
    topic_request=TopicRequest.objects.get(pk=topic_request_id)
    title = topic_request.title
    description = topic_request.description
    response_email = ''
    if topic_request.response_email:
        response_email=topic_request.response_email
    if request.POST:
        if 'cancel' in request.POST:
            return HttpResponseRedirect(reverse('physics:topic_requests'))
        if 'delete' in request.POST:
            return HttpResponseRedirect(reverse('physics:delete_topic_request',args=(topic_request_id)))

    return render_to_response('physics/view_topic_request.html',{'title':title,'description':description,'response_email':response_email},context_instance = RequestContext(request))

@login_required   
def delete_topic_request(request,topic_request_id):
    topic_request=TopicRequest.objects.get(pk=topic_request_id)
    topic_request.delete();
    return HttpResponseRedirect(reverse('physics:topic_requests'))

@login_required   
def suggestions(request):
    suggestions = Suggestion.objects.order_by('-pub_date')
    context = {'suggestions': suggestions}
    return render(request, 'physics/suggestions.html', context)

@login_required    
def view_suggestion(request,suggestion_id=None):
    suggestion=Suggestion.objects.get(pk=suggestion_id)
    title = suggestion.title
    description = suggestion.description
    response_email = ''
    if suggestion.response_email:
        response_email=suggestion.response_email
    if request.POST:
        if 'cancel' in request.POST:
            return HttpResponseRedirect(reverse('physics:suggestions'))
        if 'delete' in request.POST:
            return HttpResponseRedirect(reverse('physics:delete_suggestion',args=(suggestion_id)))

    return render_to_response('physics/view_suggestion.html',{'title':title,'description':description,'response_email':response_email},context_instance = RequestContext(request))

@login_required 
def delete_suggestion(request,suggestion_id):
    suggestion=Suggestion.objects.get(pk=suggestion_id)
    suggestion.delete();
    return HttpResponseRedirect(reverse('physics:suggestions'))









    

