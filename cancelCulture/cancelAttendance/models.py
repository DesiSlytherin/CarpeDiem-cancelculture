from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class leavereq(models.Model):
	#username = models.ForeignKey(User, on_delete= models.CASCADE,related_name='req_name')
	Name = models.CharField(max_length=256,null=False,blank=False)
	Register_Number = models.PositiveIntegerField(null=False,blank=False)
	Dept_Choices = (('CSE','CSE'),('IT','IT'),('MECH','MECH'),('ECE','ECE'),('EEE','EEE'))
	Department = models.CharField(max_length=256,null=False,blank=False,choices=Dept_Choices)
	reason_choices = (('Casual','Casual'),('Emergency','Emergency'),('Medical','Medical'),('Others','Others'))
	Reason = models.CharField(max_length=256,null=False,blank=False,choices=reason_choices)
	Initial_Date = models.DateField()
	Final_Date = models.DateField()
	status_chooces = (('Pending','Pending'),('Approved','Approved'),('Rejected','Rejected'))
	Status = models.CharField(max_length=256,null=False,blank=False,choices=status_chooces,default='Pending')
	Attachment = models.FileField(upload_to ='uploads/',null=True,blank=True)

