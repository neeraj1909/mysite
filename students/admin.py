from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
	model = Student

	list_display = [
		"full_name",
		"age",
		"hometown"
	]

	list_filter = [
		"age",
	]

	search_fields = [
		"full_name",
		"hometown",
		"hostel",
	]

admin.site.register(Student, StudentAdmin)
# Register your models here.
