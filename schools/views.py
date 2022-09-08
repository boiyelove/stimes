from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article, Tag, Category, Comment, School
from .forms import ArticleForm, SchoolForm, LectureForm, EventForm

# Create your views here.

def get_file(f):
	with open (f, 'r') as docf:
		read_data = list(docf)
	return read_data


def create_school(request):
	form = SchoolForm(request.POST or None)
	context = {"form" : form}
	template = "form.html"
	return render (request, template, context)

def get_schools(request):
	objlist = School.objects.all()
	context = {"form" : objlist}
	template = "listhtml"
	return render (request, template, context)

def create_lecture(request):
	form = LectureForm(request.POST or None)
	context = {"form" : form}
	template = "form.html"
	return render (request, template, context)


def get_lectures(request):
	objlist = Lecture.objects.all()
	context = {"form" : objlist}
	template = "listhtml"
	return render (request, template, context)


def create_event(request):
	form = EventForm(request.POST or None)
	context = {"form" : form}
	template = "form.html"
	return render (request, template, context)

def get_events(request):
	objlist = Event.objects.all()
	context = {"form" : objlist}
	template = "listhtml"
	return render (request, template, context)




def school_home(request):
	context = {}
	template = 'login.html'
	return render (request, template, context)

def year_archive(request, year):
	a_list = Article.objects.filter(pub_date__year=year)
	context = {'year': year,
				'aritcle_list': a_list
					}
	return render(request, 'news/year_archive.html', context)

def get_posts(request, user):
	post_list = Posts.objects.all().order_by(-pub_date)
	template = 'posts/post_list.html'
	context = {'posts' : postlist,}
	return render(request, template, context)

def create_article(request):
	form = ArticleForm(request.POST)
	if form.is_bound:
		if form.is_valid():
			content, created = Article.objects.get_or_create(content=form.cleaned_data['story'],
				reporter = request.User)
			headline = Article.objects.create(headline=form.clead_data['headline'])

			if not created:
				Article.tag_set.clear()
			tag_names = form.cleaned_data('tag').split()
			for tag_name in tag_names:
				tag, dummy = Tag.objects.get_or_create(name=tag_name)
				Article.tag_set.add(tag)
			Article.save()
			return HttpResponseRedirect('/thanks/')
	context = {'form': form}
	template = 'schools/article_form.html'
	return render(request, template, context)


def test_template(request):
	context = {}
	template = "start.html"
	return render(request, template, context)
def month_archive(request):
	pass

def article_detail(request):
	pass
def create_category(request):
	pass
def create_comment(request):
	pass
def get_feeds(request):
	pass
def get_dept(request):
	pass

def get_course(request):
	pass

def create_faculty(request):
	pass
def create_department(request):
	pass
def create_material(request):
	pass
def create_course(request):
	pass

def check_school_type():
	pass
def check_location():
	pass
def check_ancronym():
	pass
def construct_name():
	pass