from .models import Event, Student_Register
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm, EventForm,SignupForm, Student_Register_Form
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import EventForm, Student_Register_Form



#normal students home page
def homePage(request):
    if request.user.is_authenticated:
        # If authenticated, filter events based on the organizer
        user_events = Event.objects.filter(organizer=request.user)
    else:
        user_events = None  # or any default value you want for non-authenticated users

    events = Event.objects.all()
    participants = Student_Register.objects.count()
    print(participants, flush=True)
 
    context = {
        'events': events,
        'user_events':user_events,
        'now': timezone.now(),
        'participants': participants,
    }

    return render(request, 'event/home.html',context)


# def students(request):
#     events = Event.objects.all()
#     context = {
#         'events': events,
#     }
#     return render(request, 'event/students.html',context)

#register a event
def studentRegister(request):
    form = Student_Register_Form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Student_Register_Form()

    
    context = {
    'form': form,
    }
    
    return render(request, 'event/student_register_form.html', context)


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'event/signup.html', {'form': form})


# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'event/login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('home')


#create event

# def Create_event(request):
#     form = EventForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
#     else:
#         form = EventForm()
#     return render(request, "event/create_event.html", {"form":form})



@login_required
def Create_event(request):
    if request.method == 'POST':
        start_time = request.POST.get('appt')
        start_date = request.POST.get('birthday')
        form = EventForm(request.POST, user=request.user, start_time=start_time, start_date=start_date)
        # form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = EventForm(user=request.user)
        

    return render(request, 'event/create_event.html', {'form': form})



#delete event
def delete(request, id):
  member = Event.objects.get(id=id)
  member.delete()
  return redirect('home')



# #to display specific clubs events 
# def user_profile(request, username):
#     user = get_object_or_404(User, username=username)
#     blogs = Blog.objects.filter(organizer=user)

#     context = {
#         'user_profile': user,
#         'blogs': blogs,
#     }

#     return render(request, 'event/home.html', context)




#club detail and its events

# def club_profile(request, club_id):
#     club = get_object_or_404(User, id=club_id)
#     past_events = Event.objects.filter(club=club, end_date__lt=timezone.now())

#     context = {
#         'club': club,
#         'past_events': past_events,
#     }

#     return render(request, 'event/club_profile.html', context)