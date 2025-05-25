from django.shortcuts import render 
from .forms import FeedbackForm

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        
        if form.is_valid(): 
            form.save()
            return render(request, 'feedback/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

