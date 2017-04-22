from django.db import models

# Create your models here.

class Student(models.Model):
	full_name = models.CharField("Full Name", max_length=80)
	age = models.PositiveIntegerField("Age")
	room_number = models.CharField("Room No.", max_length=20, help_text="For example: A20")
	hostel = models.CharField("Hostel", max_length=80)
	hometown = models.CharField("Hometown", max_length=80)

	class Meta:
		verbose_name = "Student"
		verbose_name_plural = "Students"

	def __str__(self):
		return self.full_name