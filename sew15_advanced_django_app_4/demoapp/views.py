from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from .models import Person,Department
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
import magic
from django.core.exceptions import ValidationError
from django.db.models import Count


# Create your views here.

def index_demo(request):
    return HttpResponse("<h1>Hello Django!</h1>")

@login_required
# 1.) the index view returns all people with the index template
def person_index(request):
    people_list = Person.objects.all().order_by('lastname')  # use a sorted queryset for pagination
    # read the acutal page or use 1 as default
    page = request.GET.get('page', 1)
    paginator = Paginator(people_list, 10)  # Show 10 people per page

    try:
        people = paginator.page(page)  # a certain page
    except PageNotAnInteger:
        people = paginator.page(1)  # the first page
    except EmptyPage:
        people = paginator.page(paginator.num_pages)  # the last page

    selected_person_id = None
    if request.method == 'POST':
        print(request.POST)
        selected_person_id = request.POST.get('selected_person')

    if selected_person_id:
        if 'details' in request.POST:
            return redirect('person_details_route', person_id=selected_person_id)
        elif 'edit' in request.POST:
            return redirect('person_edit_route', person_id=selected_person_id)
        elif 'delete' in request.POST:
            return redirect('person_delete_route', person_id=selected_person_id)
    departments = Department.objects.annotate(num_people=Count('people')).order_by('shortname')
    for person in people:
        for department in departments:
            if person.department == department:
                person.department.count = department.num_people
                print(person.department.count)
    # pass the paginator object to the template
    return render(request, 'person/index.html', {'people': people, 'departments': Department.objects.all()})


@login_required
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

@login_required
# 3.) the create() function returns an empty form to enter the new person data
def person_create(request):
    return render(request, 'person/create.html')

@login_required
# 4.) the store() function stores the new person and redirects back to the person_index_route
def person_store(request):
    # Validate file type
    picture = request.FILES.get('picture')
    if picture:
        validate_image(picture)
    try:
        p = Person()
        p.firstname = request.POST.get('firstname')
        p.lastname = request.POST.get('lastname')
        p.age = request.POST.get('age')
        p.sex = request.POST.get('sex')
        p.description = request.POST.get('description')
        p.picture = picture
        # Try to save the associated department
        try:
            id = request.POST.get('department')
            d = Department.objects.get(id=id)
            p.department = d
        except Department.DoesNotExist:
            p.department = None
        p.save()
        return redirect('person_index_route')
    except Exception as ex:
        return HttpResponseBadRequest(ex)



@login_required
# 5.) the edit() function reads the person object with the given id from the database 
def person_edit(request, person_id):
    try:
        # try to get the Person object with the person_id
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        # if the Person object was not found raise a 404 Http error
        raise Http404('Person not found')
    return render(request, 'person/edit.html', {'person': person})

@login_required
# 6.) the upate() function updates the person object with the given id and the request data in the database
def person_update(request, person_id):
    # Validate file type
    picture = request.FILES.get('picture')
    if picture:
        validate_image(picture)    
    try:
        p = Person.objects.get(id=person_id)
        p.firstname = request.POST.get('firstname')
        p.lastname = request.POST.get('lastname')
        p.age = request.POST.get('age')
        p.sex = request.POST.get('sex')
        p.description = request.POST.get('description')   
        pic = request.FILES.get('picture') # Change the picture if needed
        if pic:
            p.picture = pic
        p.save()
    except Person.DoesNotExist:
        raise Http404('Person not found')
    except Exception as ex:
        return HttpResponseBadRequest(ex)
    return redirect('person_index_route')


@login_required
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


def validate_image(file):
    mime = magic.Magic()
    file_signature = mime.from_buffer(file.read(1024))
    image_signatures = ['JPEG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP']
    if not any(signature in file_signature for signature in image_signatures):
        raise ValidationError('File is not an image.') 

