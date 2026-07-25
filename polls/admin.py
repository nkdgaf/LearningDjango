from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['questiontext']}),
        ('Date information', {'fields': ['pubdate'], 'classes': [ 'collapse']}),
    
    ]
    inlines = [ChoiceInline]
    listdisplay = ('questiontext', 'pubdate', 'waspublishedrecenlty')
    listfilter = ['pubdate']
    searchfields = ["questiontext"]

# Register your models here.

