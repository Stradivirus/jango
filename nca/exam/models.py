from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    choice_a = models.CharField(max_length=100)
    choice_b = models.CharField(max_length=100)
    choice_c = models.CharField(max_length=100)
    choice_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)  # 문자열 답변을 저장할 수 있도록 변경

    def __str__(self):
        return self.question_text
