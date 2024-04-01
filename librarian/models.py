# from typing import Iterable
from django.db import models
from students.models import Student
import datetime
import random

class Books(models.Model):
  
  
  inc = 0o0001
  bookId = models.CharField(max_length=12, primary_key=True)
  bName = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  publisher = models.CharField(max_length=25)
  edition = models.IntegerField()
  category = models.CharField(
        max_length=20,
        choices={
            ('Computer Science', "Computer Science"),
            ('Management', "Management"),
            ('Database', "Database"),
            ('Journal', "Journal"),
        },
        default='Select the Category',
  )
  Price = models.FloatField()
  PubYear = models.IntegerField()
  totAvail = models.IntegerField()
  totIssued = models.IntegerField()
  totQuant = models.IntegerField()
  
  def insertBook(self):
    if self.category == "Computer Science":
      ch = 'CS'
    elif self.category == "Management":
      ch = 'MG'
    elif self.category == "Database":
      ch = 'DB'
    elif self.category == "Journal":
      ch = 'JN'
        
    self.bookId = str(datetime.date.today().year-2000)+"BK"+ch+str(random.randint(0o0001, 9999))
    self.totIssued = int(self.totQuant) - int(self.totAvail)
    #  print(self.bookId)
    #  print(self.totIssued)
    self.save()
    return self.bookId
  
class Issues(models.Model):
  issueId = models.CharField(max_length=12, primary_key=True)
  StudentId = models.ForeignKey(Student, on_delete=models.CASCADE)
  BookId = models.ForeignKey(Books, on_delete=models.CASCADE)
  issueDate = models.DateField(default=datetime.date.today)
  returnDate = models.DateField(null = True)
  panelty = models.IntegerField(default = 0)
  completed = models.BooleanField(default= False)
  def save(self):
     self.returnDate = self.issueDate + datetime.timedelta(days=7)
     return super().save()


# class Payment(models.Model):
#     event_date = models.DateField()
#     payment_due_date = models.DateField()

#     class Meta:
#         ordering = ["payment_due_date"]

#     def save(self, *args, **kwargs):
#         if self.payment_due_date is None:
#             self.payment_due_date = self.event_date.date() + datetime.timedelta(days=2)
#         super(Payment, self).save(*args, **kwargs)




#   @staticmethod
#   def get_student_by_enrollment(enrollment):
#     try:
#       return Student.objects.get(enrollment=enrollment)
#     except:
#       return False