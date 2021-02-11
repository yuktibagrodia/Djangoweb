from django.shortcuts import render, get_object_or_404
from .forms import Useraddquestion
from .models import Note

def newquestion(request):
	if request.method == "POST":
			form = Useraddquestion(request.POST)
			if form.is_valid():
				addquestion = form.save(commit=False)
				addquestion.user = request.user
				addquestion.save()
				return render(request)
			else:
				 pass
	else:
			form = Useraddquestion()
			return render(request)
    