from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting
from .forms import MeetingForm, ResourceForm

# Create your views here.
def index(request):
    return render(request, 'club/index.html')
    
def resources(request):
    resource_list = Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list':resource_list})

def meetings(request):
    meeting_list = Meeting.objects.all()
    return render(request, 'club/meeting_list.html', {'meetings': meeting_list})

def meeting_details(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meeting_details.html', {'meeting': meeting})

def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

def newResource(request):
    form=ResourceForm

    if request.method=='POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})