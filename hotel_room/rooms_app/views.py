from django.shortcuts import redirect, render
from .models import Hotels,HotelRoom,Reservation
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.shortcuts import render, redirect, get_object_or_404
from .models import HotelRoom
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm


def reservation_success(request):
    messages.success(request,"Successfully booked")

    return redirect(all_bookings)


def make_reservation(request, room_id):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room_id = room_id  # Assuming you pass room_id in the URL
            reservation.guest = request.user  # Assuming you're using authentication
            reservation.save()
            return redirect('reservation_success')  # Redirect to a success page
    else:
        form = ReservationForm()

    return render(request, 'reservation_form.html', {'form': form})
# def make_reservation(request):


#     return render(request, 'bookform.html')
def homepage(request):
    # Retrieve distinct locations from the Hotels model
    locations = Hotels.objects.values('location').distinct()
    owner_number = Hotels.objects.values('owner_number').distinct()

    # Retrieve hotel rooms along with their images
    rooms = HotelRoom.objects.all()

    # Handle form submission
    if 'location' in request.GET:
        selected_location = request.GET['location']
        if selected_location:
            # Filter rooms based on the selected location
            rooms = HotelRoom.objects.filter(hotel__location=selected_location)

    # Pass the list of locations and filtered rooms to the template
    return render(request, 'index.html', {'location': locations, 'rooms': rooms, 'owner_number': owner_number})



#logout for admin and user 
def logoutuser(request):
    if request.method =='GET':
        logout(request)
        messages.success(request,"Logged out successfully")
        print("Logged out successfully")
        return redirect('homepage')
    else:
        print("logout unsuccessfull")
        return redirect('userloginpage')
    

def run_task(request):
    hotel_name = request.GET.get('hotel_name', None)

    if hotel_name:
        # Do something with the hotel_name, such as processing the booking
        # return HttpResponse(f'Booking for hotel: {hotel_name}')

        return HttpResponse(render(request,'bookform.html',{'hotel_name': hotel_name}))
    


def handler404(request):
    return render(request, '404.html', status=404)
        

#about
def aboutpage(request):
    return HttpResponse(render(request,'about.html'))

#contact page
def contactpage(request):
    return HttpResponse(render(request,'contact.html'))

#user sign up
def user_sign_up(request):
    if request.method =="POST":
        user_name = request.POST['username']
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.warning(request,"Password didn't matched")
            return redirect('userloginpage')
        
        try:
            if User.objects.all().get(username=user_name):
                messages.warning(request,"Username Not Available")
                return redirect('userloginpage')
        except:
            pass
            

        new_user = User.objects.create_user(username=user_name,password=password1)
        new_user.is_superuser=False
        new_user.is_staff=False
        new_user.save()
        messages.success(request,"Registration Successfull")
        return redirect("userloginpage")
    return HttpResponse('Access Denied')


#user login and signup page
def user_log_sign_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pswd']

        user = authenticate(username=email,password=password)
     
        
        if user is not None:
            login(request,user)
            messages.success(request,"successful logged in")
            print("Login successfull")
            return redirect('homepage')
        else:
            messages.warning(request,"Incorrect username or password")
            return redirect('userloginpage')

    response = render(request,'user/userlogsign.html')
    return HttpResponse(response)



#staff login and signup page
def staff_log_sign_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        
        if user.is_staff:
            login(request,user)
            return redirect('staffpanel')
        
        else:
            messages.success(request,"Incorrect username or password")
            return redirect('staffloginpage')
    response = render(request,'staff/stafflogsign.html')
    return HttpResponse(response)

#for showing all bookings to staff
@login_required()
def all_bookings(request):
    current_user = get_user(request)

    bookings = Reservation.objects.filter(guest=current_user)


    if not bookings:
        messages.warning(request,"No Bookings Found")
    return HttpResponse(render(request,'allbookings.html',{'bookings':bookings}))


from django.contrib.auth.views import PasswordResetConfirmView

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'your_app/password_reset_confirm.html'
    success_url = '/reset/done/'


from django.contrib.auth.views import PasswordResetCompleteView

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'your_app/password_reset_complete.html'

    
