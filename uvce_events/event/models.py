from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # participants = models.IntegerField(default=0)
    start_date = models.DateField(null=False)
    start_time = models.TimeField(null=False)
    registration_deadline = models.TimeField(null=True)
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank = False, default = User)


    def __str__(self):
        return self.title


    # def registration_open(self):
    #     now = timezone.now()
    #     print(f"Now: {now}, Registration Deadline: {self.registration_deadline}, Deadline TZ: {self.registration_deadline.tzinfo}")
    #     result = self.registration_deadline > now
    #     print(f"Is Registration Open: {result}")
    #     return result

BRANCH_CHOICES =( 
    ("Computer Science", "Computer Science"), 
    ("Information Science", "Information Science"), 
    ("Electrical and Electronics", "Electrical and Electronics"), 
    ("Elecronics and Communication", "Elecronics and Communication"), 
    ("Mechanical", "Mechanical"),
    ("Civil", "Civil"),

) 

YEAR_CHOICES =(
    (1, 'first'),
    (2, 'second'),
    (3, 'third'),
    (4, 'fourth'),
    (5, 'fifth'),
)
class Student_Register(models.Model):
    name = models.CharField(max_length=30)
    roll_number = models.CharField(max_length = 10)
    email_address = models.CharField(max_length=40)
    branch = models.CharField(max_length=30, choices = BRANCH_CHOICES, verbose_name = "Select Branch" ) 
    year = models.IntegerField(choices = YEAR_CHOICES, verbose_name="Select Year" )


    def __str__(self):
        return self.name
    