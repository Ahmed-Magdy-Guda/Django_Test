from django.contrib import admin
from poll.models import Question
from poll.models import Person
from poll.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Text Information', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class personAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Person Information', {'fields': ['name', 'age', 'height']})
    ]
    list_display = ('name', 'age', 'height')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Person, personAdmin)