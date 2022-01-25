from django.contrib import admin
from django import forms
from django.contrib.admin.helpers import ActionForm
from django.db import connection
# Register your models here.

from .models import *


# FlashcardCategory, Flashcard
@admin.register(FlashcardCategory)
class FlashcardCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    pass    

@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ['id','question','categoryid','sql_category']
    def sql_category(self, obj):
        p = Flashcard.objects.raw(f"""
        SELECT *
        FROM flashcard_category
        Where id = {obj.categoryid.id}
        limit 1
        """)[0]
        return f"{p.name}"

#----------------------------------------------
# Student, StudentCategory
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    # list_display = ['stu_id','username','balance']
    list_display = ['id_username_balance']
    def id_username_balance(self, obj):
        p = Students.objects.raw(f"""
        SELECT *
        FROM students
        Where stu_id = {obj.stu_id}
        limit 1
        """)[0]
        return f"{p.stu_id},{p.username},{p.balance}"

@admin.register(StudentCategory)
class StudentCategoryAdmin(admin.ModelAdmin):
    list_display = ['stu_id','category']
    pass

#----------------------------------------------
# Department, Professors
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['dep_id','name']
    pass

@admin.register(Professors)
class ProfessorsAdmin(admin.ModelAdmin):
    list_display = ['prof_id','username','department']
    pass

#----------------------------------------------
# QuizzesSubject, Quizzes, Questions

class QuestionsInline(admin.TabularInline):
    model = Questions

class QuizzesInline(admin.TabularInline):
    model = Quizzes

@admin.register(QuizzesSubject)
class QuizzesSubjectAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    inlines = [QuizzesInline]

@admin.register(Quizzes)
class QuizzesAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','prof_id','began_at','end_at','sql_prof_name',]
    inlines = [QuestionsInline]
    def sql_prof_name(self, obj):
        p = Professors.objects.raw(f"""
        SELECT *
        FROM professors
        Where prof_id = {obj.prof_id}
        limit 1
        """)[0]
        return f"{p.username}"




@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id','question','quiz','sql_quiz_name']
    
    def sql_quiz_name(self, obj):
        p = Quizzes.objects.raw(f"""
        SELECT *
        FROM quizzes
        Where id = {obj.quiz_id}
        limit 1
        """)[0]
        return f"{p.name}"


#----------------------------------------------
# Enroll, Participated
class XForm(ActionForm):
    parm = forms.CharField()


@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    action_form = XForm

    sortable_by = ['order_id','quiz_id','stu_id']
    list_display = ['order_id','quiz_id','stu_id','sql_username']


    def sql_username(self, obj):
        p = Students.objects.raw(f"""
        SELECT *
        FROM students
        Where stu_id = '{obj.stu_id}'
        limit 1
        """)[0]
        return f"{p.username}"



from datetime import date

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.db.models.expressions import RawSQL
class ParticipatedFilter(admin.SimpleListFilter):
    title = _('Filter')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 's'

    def lookups(self, request, model_admin):

        return (
            ('G', _('بالاتر از ۱۰')),
            ('B', _('پایینتر از ۱۰')),
            ('M', _('موجودی بیشتر از 70')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'G':
            return queryset.filter(
                stu_id__in=
                        Participated.objects.raw("""
                            SELECT stu_id
                            FROM participated 
                            WHERE mark >= 10
                            """
                            )
            )
        if self.value() == 'B':
            return queryset.filter(
                stu_id__in=
                        Participated.objects.raw("""
                            SELECT stu_id
                            FROM participated 
                            WHERE mark < 10
                            """
                            )
            )
        if self.value() == 'M':
            return queryset.filter(
                stu_id__in=
                        Participated.objects.raw("""
                            SELECT stu_id
                            FROM participated 
                            natural join students
                            WHERE balance > 70
                            """,[])
                    )
                
@admin.register(Participated)
class ParticipatedAdmin(admin.ModelAdmin):
    list_display = ['stu_id','quiz_id','mark','sql_username']

    def sql_username(self, obj):
        p = Students.objects.raw(f"""
        SELECT *
        FROM students
        Where stu_id = '{obj.stu_id}'
        limit 1
        """)[0]
        return f"{p.username}"


    # action_form = XForm
    list_filter = [ParticipatedFilter]
    actions = ['help_under_ten','help_stu']
    
    @admin.action(description="""
        نمره ۹.۹۹
        """)
    def help_under_ten(self,request,qeryset):
        with connection.cursor() as c:
            c.execute("""
            UPDATE participated
            SET mark = 9.99
            WHERE mark IS NOT NULL 
                AND mark < 10
            """)
    @admin.action(description="""
        نمودار
        """)
    def help_stu(self,request,qeryset):
        with connection.cursor() as c:
            c.execute("""
            UPDATE participated
            SET mark = mark + 1
            WHERE mark BETWEEN 10 AND 19
            """)
