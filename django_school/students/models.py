from django.db import models
from django.conf import settings
from quizzes.models import Quiz,Subject

class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user__is_staff=True)

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='quizzes.TakenQuiz')
    interests = models.ManyToManyField(Subject, related_name='interested_students')
    classroom = models.ForeignKey('classroom.ClassRoom', on_delete=models.CASCADE)

    objects = models.Manager() # The default manager.
    active_objects = StudentManager() # The Only Active Students manager.

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username


