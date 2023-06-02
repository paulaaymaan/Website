from django.http import HttpResponseNotFound,HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Survey,DietPlan

# Create your views here.

def Home_page(request):
    return render(request, 'app1/Home.html')

def sign_in_page(request):
    if request.method == 'POST':
      username=request.POST.get('Uname')
      password=request.POST.get('Pass') 
      user=authenticate(request,username=username,password=password)
      if user is not None:
         login(request,user)
         return render (request ,'app1/profile.html')
         
      else:
         return HttpResponse("User Name or Password is incorrect")

    return render(request, 'app1/sign_in.html')

def sign_up_page(request):
    if request.method == 'POST':
      UserName=request.POST.get('UserName')
      Email=request.POST.get('Email')
      Password=request.POST.get("Password")
      my_User=User.objects.create_user(UserName,Email,Password)
      my_User.save()
      return render(request,'app1/gender.html')
  
    return render(request, 'app1/sign_up.html')

def logout_fun(request):
   logout(request)
   return redirect('Home')


#def plan_page(request):
 #   return render(request, 'app1/plan.html')

@login_required
def survey_page(request):
    if request.method == 'POST':
        age = request.POST['age']
        weight = request.POST['weight']
        height = request.POST['height']
        desired_weight = request.POST['desired_weight']
        survey = Survey(user=request.user, age=age, weight=weight, height=height, desired_weight=desired_weight)
        survey.save()
        
        return redirect('profile')
    else:
        return render(request, 'app1/survey.html')
    
   # return render(request, 'app1/survey.html')
   
@login_required
def surveys(request):
    surveys = Survey.objects.all()
    return render(request, 'surveys.html', {'surveys': surveys})


@login_required(login_url='Home')
def gender_page(request):
    return render(request, 'app1/gender.html')



def page1_page(request):
  return render(request, 'app1/page1.html')



@login_required
def profile(request):
    #survey=request.POST.get('survey')
    #return render(request, 'app1/profile.html')
    # survey = get_object_or_404(Survey, pk=id),
    survey = Survey.objects.filter(user=request.user)
    print(survey[survey.count()-1].age)
    print(survey.count()-1)
    survey_last=survey[survey.count()-1]
    
   # survey = Survey.objects.filter(user=request.user)
    weight_diff = survey[survey.count()-1].weight - survey[survey.count()-1].desired_weight
    print(survey[survey.count()-1].weight)
    diet_plans=DietPlan.objects.all()
    if weight_diff > 20:
        diet_plan =diet_plans[0]
    else:
        diet_plan = diet_plans[1]
    
    
    
        
    return render(request, 'app1/profile.html', {"survey_last": survey_last,
                                                  "diet_plan": diet_plan
                                                  
                                                })
    
    
def plan(request):
    return render(request, 'app1/plan.html')

    
