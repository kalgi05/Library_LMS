from django.db import models

class Student(models.Model):
  enrollment = models.CharField(max_length=12, primary_key=True)
  name = models.CharField(max_length=35)
  email = models.EmailField(max_length=50, unique=True)
  password = models.CharField(max_length=200)
  mobile = models.CharField(max_length=10, unique=True)
  dob = models.DateField()
  branch = models.CharField(
        max_length=5,
        choices={
            ('BCA', "BCA"),
            ('MCA', "MCA"),
            ('BBA', "BBA"),
            ('MBA', "MBA"),
            ('iMCA', "iMCA"),
        },
        default='Select Your Branch',
  )
  gender = models.CharField(
    max_length=6,
    choices={
      ('Male', "Male"),
      ('Female', "Female"),
    },
    default='Select Your Gender',
    )
  total_issues = models.IntegerField(default=0)
  current_issues = models.IntegerField(default=0)
  present = models.BooleanField(default = False)
  intime = models.DateTimeField(null=True)
  outtime = models.DateTimeField(null=True)
  panenlty = models.IntegerField(default=0)
  approved = models.BooleanField(default = False)
#   idcard = models.ImageField(upload_to='../LMS/IDs/')
  @staticmethod
  def get_student_by_enrollment(enrollment):
    try:
      return Student.objects.get(enrollment=enrollment)
    except:
      return False