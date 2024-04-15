from django.db import models
class Class(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    teacher = models.CharField(max_length=20)
    def __str__(self):
        return f"course name : {self.title} teacher is : {self.teacher} , description {self.description[:10]}"
