from django.contrib import admin

from django.contrib import admin

from .models import Topic, Lecture, PSet, News, Announcement, TopicRequest, Suggestion

class LectureInLine(admin.TabularInline):
	model = Lecture
	extra = 2

class PSetInLine(admin.TabularInline):
	model = PSet
	extra = 2

class TopicAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['order', 'title', 'description']}),
		('Date information', {'fields': ['pub_date']}),
	]
	inlines = [LectureInLine, PSetInLine]
	list_display = ('order','title','pub_date')
	list_filter = ['order']
	search_fields = ['title']
	
class NewsAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['title', 'text']}),
		('Date information', {'fields': ['pub_date']}),
	]
	list_display = ('order','title','pub_date')
	list_filter = ['pub_date']
	search_fields = ['title']
	
class AnnouncementAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['title', 'text']}),
		('Date information', {'fields': ['pub_date']}),
	]
	list_display = ('order','title','pub_date')
	list_filter = ['pub_date']
	search_fields = ['title']
	
class TopicRequestAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['title','description','response_email']}),
		('Date information', {'fields': ['pub_date']}),
	]
	list_display = ('order','pub_date')
	list_filter = ['pub_date']
	search_fields = ['title']
	
class SuggestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['title','description','response_email']}),
		('Date information', {'fields': ['pub_date']}),
	]
	list_display = ('order','pub_date')
	list_filter = ['pub_date']
	search_fields = ['title']

admin.site.register(Topic, TopicAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(TopicRequest, TopicRequestAdmin)
admin.site.register(Suggestion, SuggestionAdmin)



