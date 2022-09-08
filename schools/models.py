import datetime
from django.utils import timezone
from django.conf import settings
from cities_light.models import City, Region, Country
from django.db import models

# Create your models here.

building_type = (("LT", "LECTURE THEARTER"),
                 ("OFFICE", "OFFICE"),
                 ("HALL","HALL"),
                 ("LAB", "LABORATORY"),
                 )
school_type = (("FED", "FEDERAL"),
               ("PRI", "PRIVATE"),
               ("STA", "STATE"),
               )

tertiary_type = (("UNI", "UNIVERSITY"),
                 ("POL", "POLYTECHNIC"),
                 ("COL", "COLLEGE"),
                 )
persp = (("FRONT", "FRONT"),
              ("RIGHT", "RIGHT"),
              ("LEFT", "LEFT"),
              ("BACK", "BACK"),
              )

categ = (("FAC", "FACULTY"),
		("DEP", "DEPARTMENT"),
        )






class Article(models.Model):
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, blank = True, null = True)
    # image1 = models.ImageField(upload_toblank = True, Null=True)
    # image1 = models.ImageField(blank =True, Null =True)
    # image1 = models.ImageField(blank = True, Null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    edited_at = models.DateTimeField(auto_now = True)
    pub_date = models.DateTimeField()
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


    def limit_pub_date_choices():
        return {'pub_date__lte': datetime.date.ustcnow()}

    def was_published_recently(self):
            return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_filed = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published_recently'

    def __str__(self):
        return self.headline


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    articles = models.ManyToManyField('Article')  
    created_at = models.DateTimeField(auto_now_add = True)
    edited_at = models.DateTimeField(auto_now = True)
    pub_date = models.DateTimeField()
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


    def limit_pub_date_choices():
        return {'pub_date__lte': datetime.date.ustcnow()}

    def was_published_recently(self):
            return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_filed = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published_recently'     

    def __str__(self):
        return self.name

event_type_choices = (
("Appearance or Signing"),
("Attraction"),
("Camp, Trip or Retreat"),
("Concert or Performance"),
("Conference"),
("Convention"),
("Course, Training or Workshop"),
("Dinner or Gala"),
("Festival or Fair"),
("Game or Competition"),
("Meeting or Networking Event"),
("Other"),
("Party or Social Gathering"),
("Race or Endurance Event"),
("Rally"),
("Screening"),
("Seminar or Talk"),
("Tour"),
("Tournament"),
("Tradeshow, Consumer Show or Expo"),
)

class Category(models.Model):
    name = models.CharField(max_length = 20)
    desc = models.CharField(max_length=120)
    parent = models.ForeignKey("self", null = True, blank = True)
    tags = models.ForeignKey('Tag')
    created_at = models.DateTimeField(auto_now_add = True)
    edited_at = models.DateTimeField(auto_now = True)
    pub_date = models.DateTimeField()
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


    def limit_pub_date_choices():
        return {'pub_date__lte': datetime.date.ustcnow()}

    def was_published_recently(self):
            return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_filed = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published_recently'

    def __str__(self):
        if self.parent:
            return (self.parent, self.name)
        return self.name

class Comment(models.Model):
        body = models.TextField()
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, blank = True, null = True)
        post = models.ForeignKey('Article', on_delete = models.SET_NULL, blank = True, null = True)

        def __str__(self):
            return self.body

class School(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()
    ancronym = models.CharField(max_length = 10)
    logo = models.ImageField(upload_to='img/school/logo', null=True)
    # country = models.ForeignKey(Country)
    # region = models.ForeignKey(Region, limit_choices_to=limit_region_by_country())
    # cat = models.CharField(max_length = 15, choices = tertiary_type, default='UNIVERSITY')
    # stype = models.CharField(max_length = 15, choices = school_type)
    # founded = models.DateTimeField(null=True, blank=True)
    # story = models.TextField(null=True, blank=True)
    # email = models.EmailField(default='admin@stimes.org')
    # website = models.URLField(max_length=120, default = 'www.stimes.org')

    # class Meta:
    #     unique_together =    ('self.name' , 'self.region')
    created_at = models.DateTimeField(auto_now_add = True)
    edited_at = models.DateTimeField(auto_now = True)
    pub_date = models.DateTimeField()
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


    def limit_pub_date_choices():
        return {'pub_date__lte': datetime.date.ustcnow()}

    def was_published_recently(self):
            return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_filed = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published_recently'


    # def limit_region_by_country(self):
    # 	country = self.country
    # 	region = country.region_set.all()
    # 	return region


    # def __str__(self):
    #     return (self.name, self.region)



# class SchoolImage(models.Model):
#     building = models.ForeignKey("Building", on_delete = models.SET_NULL, blank = True, null = True)
#     image = models.ImageField(upload_to = 'img/school/buiding')
#     desc = models.CharField(max_length=60)


# class Building(models.Model):
#     school = models.ForeignKey("School")
#     name = models.CharField(max_length=120)
#     slug = models.SlugField()
#     category = models.CharField(max_length = 10, choices = building_type, default='LECTURE THEATER')
#     seat_size = models.PositiveSmallIntegerField(null = True, blank=True)
#     image = models.ImageField(upload_to = 'img/school/building')
#     description = models.TextField(max_length = 200)


class Faculty(models.Model):
    school = models.ForeignKey("School", on_delete = models.SET_NULL, blank = True, null = True)
    # category = models.CharField(max_length = 2, choices = limit_fac_cat(), default='Faculty')
    name = models.CharField(max_length =12)
    desc = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add = True)
    edited_at = models.DateTimeField(auto_now = True)
    pub_date = models.DateTimeField()
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


    def limit_pub_date_choices():
        return {'pub_date__lte': datetime.date.ustcnow()}

    def was_published_recently(self):
            return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_filed = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published_recently'

    def limit_fac_cat(self):
    	parent_name = self.parent.name
    	parent_categ =self.parent.categ
    	if parent_name == self.name:
    		pass
    	elif parent_categ == self.categ == "fac":
    		pass
    	return 




class Department(models.Model):
    faculty = models.ForeignKey("Faculty", on_delete = models.SET_NULL, blank = True, null = True)
    name = models.CharField(max_length = 20)
    desc = models.CharField(max_length=60)


class Course(models.Model):
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 160)
    dept = models.ForeignKey("Department", on_delete =  models.SET_NULL, null = True, blank = True)
    school = models.ForeignKey("School") 
    created_at = models.DateTimeField(auto_now_add = True)
    pub_date = models.DateTimeField()
    active = models.BooleanField(default=True)



class Lecture(models.Model):
    course = models.ForeignKey("Course", on_delete = models.SET_NULL, null = True, blank = True)
    school = models.CharField(max_length = 50)
    # venue = models.ForeignKey("Building", models.SET_NULL, null = True, blank = True)
    start_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    end_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    lecturer = models.CharField(max_length=50, null = True, blank = True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)



class Material(models.Model):
    desc = models.TextField()
    link = models.URLField(null= True, blank =True)
    course = models.ManyToManyField(Course, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    edited_at = models.DateTimeField(auto_now = True)
    pub_date = models.DateTimeField()
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


    def limit_pub_date_choices():
        return {'pub_date__lte': datetime.date.ustcnow()}

    def was_published_recently(self):
            return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_filed = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published_recently'    


class Week_Schedule(models.Model):
    course = models.OneToOneField("Course", null=True)
    monday = models.DurationField(blank = True, null = True)
    tuesday = models.DurationField(blank = True, null = True)
    wednesday =models.DurationField(blank = True, null = True)
    thursday = models.DurationField(blank = True, null = True)
    friday = models.DurationField(blank = True, null = True)
    saturday = models.DurationField(blank = True, null = True)
    sunday = models.DurationField(blank = True, null = True)

    
    
