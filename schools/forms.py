from django import forms

class SchoolForm(forms.Form):
	name = forms.CharField(label= 'School name', max_length = '64')
	ancronym = forms.CharField(label='ancronym')
	country = forms.CharField(label='country')

class LectureForm(forms.Form):
	course_code = forms.CharField(label = 'course_code')
	topic = forms.CharField(label='topic')
	venue = forms.CharField(label='venue')
	lecturer = forms.CharField(label='lecturer')
	school = forms.CharField(label='school name')
	instructions = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea)
	title = forms.CharField(label='title')
	tags = forms.CharField(label='tags')

	def create_article(self):
		article = Articles.object.get_or_create(content =  content,
												title = title,
												reporter = request.User)
		if not created:
			article.tag_set.clear()
		tags = form.cleaned_data['tags'].split(',')
		for tag in tags:
			tagin, dummy = Tag.objects.get_or_create(name=tag)
			article.tag_set.add(tagin)
			article.save()
			return HttpResponseRedirect('/page/')
		return article

class EventForm(forms.Form):
	title = forms.CharField(label = 'title')
	start_date = forms.DateField()
	end_date = forms.DateField()
	venue = forms.CharField(label='venue')
	description = forms.CharField(widget=forms.Textarea)