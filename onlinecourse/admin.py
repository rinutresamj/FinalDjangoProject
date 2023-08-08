from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice,Enrollment,Submission


# <HINT> Register QuestionInline and ChoiceInline classes here
class ChoiceInline(admin.TabularInline):  # Inline for editing choices within a question
    model = Choice
    extra = 3  # Number of extra choice fields to display

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]  # Embed ChoiceInline within QuestionAdmin


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)

# Register the Choice model if needed
admin.site.register(Choice)
admin.site.register(Enrollment)
admin.site.register(Submission)
