from django.db import models

# Create your models here.


class FlashcardCategory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.id}, {self.name}"
    class Meta:
        managed = False
        db_table = 'flashcard_category'

    

class Flashcard(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    is_question_md = models.BooleanField(blank=True, null=True)
    is_answer_md = models.BooleanField(blank=True, null=True)
    hint = models.TextField(blank=True, null=True)
    categoryid = models.ForeignKey('FlashcardCategory', models.DO_NOTHING, db_column='categoryID')  # Field name made lowercase.

    def __str__(self) -> str:
        return f"{self.id}, {self.question}"
    class Meta:
        managed = False
        db_table = 'flashcard'

#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
#----------------------------------------------

class Students(models.Model):
    stu_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128, blank=True, null=True)
    balance = models.FloatField()

    def __str__(self) -> str:
        return f"{self.stu_id}, {self.username}"
    class Meta:
        managed = False
        db_table = 'students'

class StudentCategory(models.Model):
    category = models.ForeignKey(FlashcardCategory, models.DO_NOTHING)
    stu = models.OneToOneField('Students', models.DO_NOTHING, primary_key=True)

    def __str__(self) -> str:
        return f"{self.category}, {self.stu}"
    class Meta:
        managed = False
        db_table = 'student_category'
        unique_together = (('stu', 'category'), ('category', 'stu'),)

#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
#----------------------------------------------



class Department(models.Model):
    dep_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.dep_id}-{self.name}"
    class Meta:
        managed = False
        db_table = 'department'


class Professors(models.Model):
    prof_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.prof_id}, {self.username}"
    class Meta:
        managed = False
        db_table = 'professors'

#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
#----------------------------------------------

class QuizzesSubject(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.id}, {self.name}"
    class Meta:
        managed = False
        db_table = 'quizzes_subject'


class Quizzes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField(blank=True, null=True)
    began_at = models.DateField(blank=True, null=True)
    end_at = models.DateField(blank=True, null=True)
    quiz_subject = models.ForeignKey(QuizzesSubject, models.DO_NOTHING)
    prof = models.ForeignKey(Professors, models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.id}, {self.name}"
    class Meta:
        managed = False
        db_table = 'quizzes'


class Questions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.CharField(max_length=256)
    wrong_answers_1 = models.CharField(max_length=256, blank=True, null=True)
    correct_answer = models.CharField(max_length=256, blank=True, null=True)
    quiz = models.ForeignKey('Quizzes', models.DO_NOTHING, blank=True, null=True)
    wrong_answers_2 = models.CharField(max_length=256, blank=True, null=True)
    wrong_answers_3 = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.id}"
    class Meta:
        managed = False
        db_table = 'questions'


#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
#----------------------------------------------

class Enroll(models.Model):
    quiz = models.ForeignKey('Quizzes', models.DO_NOTHING)
    order_id = models.BigIntegerField(primary_key=True)
    stu = models.ForeignKey('Students', models.DO_NOTHING)
    
    def __str__(self) -> str:
        return f"{self.order_id}, {self.stu}, {self.quiz}"
    class Meta:
        managed = False
        db_table = 'enroll'
        unique_together = (('quiz', 'stu'),)


class Participated(models.Model):
    stu = models.OneToOneField('Students', models.DO_NOTHING, primary_key=True)
    mark = models.FloatField(blank=True, null=True)
    quiz = models.ForeignKey('Quizzes', models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.stu_id}, {self.quiz_id}, {self.mark}"
    class Meta:
        managed = False
        db_table = 'participated'
        unique_together = (('stu_id', 'quiz_id'),)
