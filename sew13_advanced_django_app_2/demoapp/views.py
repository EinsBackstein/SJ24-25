from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from .models import Person

# Create your views here.

def index_demo(request):
    return HttpResponse("<h1>Hello Django!</h1>")

# 1.) the index view returns all people with the index template
# def person_index(request):
#     people = Person.objects.all()  # get all Person opjects from the database
#     # return the rendered template page with the passed parameter people
#     if request.method == 'POST':
#         selected_person_id = request.POST.get('selected_person')
#         if selected_person_id:
#             if 'details' in request.POST:
#                 return redirect('person_details_route', person_id=selected_person_id)
#             elif 'edit' in request.POST:
#                 return redirect('person_edit_route', person_id=selected_person_id)
#             elif 'delete' in request.POST:
#                 return redirect('person_delete_route', person_id=selected_person_id)

#     return render(request, 'person/index.html', {'people': people})

def person_index(request):
    #people_list = Person.objects.all()  # don't use the unsorted list
    people_list = Person.objects.all().order_by('lastname')  # use a sorted queryset for pagination
    page = request.GET.get('page', 1) # read the acutal page or use 1 as default
    paginator = Paginator(people_list, 10)  # Show 10 people per page

    try:
        people = paginator.page(page) # a certain page
    except PageNotAnInteger:
        people = paginator.page(1) # the first page
    except EmptyPage:
        people = paginator.page(paginator.num_pages) # the last page

    return render(request, 'person/index.html', {'people': people}) # pass the paginator object to the template


# 2.) the details view returns one person with the detail template
def person_details(request, person_id):
    try:
        # try to get the Person object with the person_id
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        # if the Person object was not found raise a 404 Http error
        raise Http404('Person not found')
    # return the rendered template page with the passed parameter person
    return render(request, 'person/details.html', {'person': person})

# 3.) the create() function returns an empty form to enter the new person data
def person_create(request):
    return render(request, 'person/create.html')


# 4.) the store() function stores the new person and redirects back to the person_index_route
def person_store(request):
    try:
        p = Person()
        p.firstname = request.POST.get('firstname')
        p.lastname = request.POST.get('lastname')
        p.age = request.POST.get('age')
        p.sex = request.POST.get('sex')
        p.description = request.POST.get('description')
        p.save()
        return redirect('person_index_route')
    except Exception as ex:
        return HttpResponseBadRequest(ex)

# 5.) the edit() function reads the person object with the given id from the database 
def person_edit(request, person_id):
    try:
        # try to get the Person object with the person_id
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        # if the Person object was not found raise a 404 Http error
        raise Http404('Person not found')
    return render(request, 'person/edit.html', {'person': person})

# 6.) the upate() function updates the person object with the given id and the request data in the database
def person_update(request, person_id):
    try:
        p = Person.objects.get(id=person_id)
        p.firstname = request.POST.get('firstname')
        p.lastname = request.POST.get('lastname')
        p.age = request.POST.get('age')
        p.sex = request.POST.get('sex')
        p.description = request.POST.get('description')
        p.save()
    except Person.DoesNotExist:
        raise Http404('Person not found')
    except Exception as ex:
        return HttpResponseBadRequest(ex)
    return redirect('person_index_route')

# 7.) delete a person object by the given id
def person_delete(request, person_id):
    try:
        # try to get the Person object with the person_id
        person = Person.objects.get(id=person_id)
        person.delete()
    except Person.DoesNotExist:
        # if the Person object was not found raise a 404 Http error
        raise Http404('Person not found')
    except Exception as ex:
        return HttpResponseBadRequest(ex)
    return redirect('person_index_route')

@login_required
def person_create(request):
    departments = Department.objects.all()
    sex_choices = Person.SEX_CHOICES
    return render(request, 'person/create.html', {'departments': departments, 'sex_choices': sex_choices})
