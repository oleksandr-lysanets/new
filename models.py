from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()
    correct_answer = models.CharField(max_length=200)
    wrong_answer1 = models.CharField(max_length=200)
    wrong_answer2 = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Quiz(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.topic.name} - {self.question.text}"

