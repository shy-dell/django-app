from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date information", {"fields":["pub_date"], "classes":["collapse"]}),
    ]
    inlines = [ChoiceInLine]
    list_display = ["question_text","pub_date","was_published_recently"]
    # displays the questions, date published and boolean of was_published_recently in questions view
    list_filter = ["pub_date"] 
    # create list filter on pub date

admin.site.register(Question, QuestionAdmin)