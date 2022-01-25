# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior    
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Department(models.Model):
    dep_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'department'


class Enroll(models.Model):
    stu = models.ForeignKey('Students', models.DO_NOTHING)
    quiz = models.OneToOneField('Quizzes', models.DO_NOTHING, primary_key=True)
    order_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enroll'
        unique_together = (('quiz', 'stu'),)


class Flashcard(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    is_question_md = models.BooleanField(blank=True, null=True)
    is_answer_md = models.BooleanField(blank=True, null=True)
    hint = models.TextField(blank=True, null=True)
    categoryid = models.ForeignKey('FlashcardCategory', models.DO_NOTHING, db_column='categoryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flashcard'


class FlashcardCategory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'flashcard_category'


class Participated(models.Model):
    stu = models.OneToOneField('Students', models.DO_NOTHING, primary_key=True)
    quiz = models.ForeignKey('Quizzes', models.DO_NOTHING)
    mark = models.FloatField()

    class Meta:
        managed = False
        db_table = 'participated'
        unique_together = (('stu', 'quiz'),)


class Professors(models.Model):
    prof_id = models.FloatField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professors'


class Questions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sujectid = models.CharField(db_column='sujectID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    question = models.CharField(max_length=256)
    wrong_answers = models.CharField(max_length=256, blank=True, null=True)
    correct_answer = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class QuizQuestion(models.Model):
    quiz = models.OneToOneField('Quizzes', models.DO_NOTHING, primary_key=True)
    question = models.ForeignKey(Questions, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'quiz_question'


class QuizSubject(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    prof = models.ForeignKey(Professors, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quiz_subject'


class Quizzes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField(blank=True, null=True)
    began_at = models.DateField(blank=True, null=True)
    end_at = models.DateField(blank=True, null=True)
    quiz_subject = models.ForeignKey(QuizSubject, models.DO_NOTHING, blank=True, null=True)      

    class Meta:
        managed = False
        db_table = 'quizzes'


class StudentCategory(models.Model):
    stu = models.ForeignKey('Students', models.DO_NOTHING)
    category = models.OneToOneField(FlashcardCategory, models.DO_NOTHING, primary_key=True)      

    class Meta:
        managed = False
        db_table = 'student_category'
        unique_together = (('category', 'stu'),)


class Students(models.Model):
    stu_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128, blank=True, null=True)
    balance = models.FloatField()

    class Meta:
        managed = False
        db_table = 'students'