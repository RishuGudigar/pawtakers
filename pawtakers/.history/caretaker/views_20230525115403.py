from django.shortcuts import render, redirect, get_object_or_404,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import ListView,View
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.urls import reverse




# @login_required
# def add_user(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('caretaker:success', user_id=user.id)
#         else:
#              return render(request,'failed.html')
#     else:
#         form = UserProfileForm()
#     return render(request, 'add_user.html', {'form': form})


# def add_user(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         aadhar_number = request.POST.get('aadhar_number')
#         phone_number = request.POST.get('phone_number')
#         address = request.POST.get('address')
#         description = request.POST.get('service_description')
#         date_of_birth =request.POST.get('date_of_birth')
#         gender=request.POST.get('gender')
#         # Create and save the caretaker object
#         caretaker = UserProfile.objects.create(name=name,phone_number=phone_number, aadhar_number=aadhar_number, address=address, description=description,date_of_birth=date_of_birth,gender=gender)
#         caretaker.save()

#         # Redirect to success page
#         return render(request, 'success.html')
#     else:
#         return render(request, 'info_extractor.html')
# @login_required
# def add_user(request):
#     if request.method == 'POST':
#         # Get the current user
#         # user = request.user

#         # Get the data from the form
#         name = request.POST.get('name')
#         aadhar_number = request.POST.get('aadhar_number')
#         phone_number = request.POST.get('phone_number')
#         address = request.POST.get('address')
#         description = request.POST.get('service_description')
#         date_of_birth =request.POST.get('date_of_birth')
#         gender=request.POST.get('gender')

#         # Create a new Caretaker instance and link it to the current user
#         UserProfile= UserProfile.objects.create(
#             user=request.user.username,
#             name=name,
#             aadhar_number=aadhar_number,
#             phone_number=phone_number,
#             address=address,
#             description=description,
#             date_of_birth=date_of_birth,
#             gender=gender
#         )

#         # Redirect to the profile page
#         return redirect('profile.html')
#     else:
#         return render(request, 'add_user.html')



def display(request):
     profiles = UserProfile.objects.all()
     
     selected_city = request.GET.get('city')
     if selected_city:
          profiles = profiles.filter(city=selected_city)
     
     cities = UserProfile.objects.values_list('city', flat=True).distinct()
     
     context = {
          'profiles': profiles,
          'cities': cities,
          'selected_city': selected_city,
     }
     
     return render(request, 'home.html', context)


def index(request):
          return render(request,'index.html')


class ProfileView(View):
     def get(self,request,pk,*args, **kwargs):
          profile=UserProfile.objects.get(pk=pk)
          user= profile.user
          
          context ={
               'user' : user,
               'profile' :profile,
               

          }

          return render(request,'profile.html',context)

class Data(View):
     def get(self,request,*args, **kwargs):
          form = UserProfileForm()

          context ={
               'form':form,
               
          }
          
          return render(request,'form.html',context)
     

     def post(self,request,*args, **kwargs):
          form=UserProfileForm(request.POST,request.FILES)

          if form.is_valid():
               new_post = form.save(commit=False)
               new_post.user = request.user
               pk = new_post.pk
               new_post.save()
               return HttpResponseRedirect('/display')
     
          return render(request,'profile.html')
     

class ProfileEditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
     model=UserProfile
      fields = ['name','image','phone_number','backup_phonenumber','description','services_description','form_number','first_line','second_line','city','state','postal_code']