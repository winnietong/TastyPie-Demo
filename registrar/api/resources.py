from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.cache import SimpleCache
from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.fields import ToManyField, ToOneField
from tastypie.resources import ModelResource
from registrar.models import Student, Class, StudentProject


class BareClassResource(ModelResource):
    class Meta:
        queryset = Class.objects.all()
        resource_name = "bare_class"


class StudentResource(ModelResource):
    # full = False prevents from being an infinite loop
    klass = ToOneField(BareClassResource, 'klass', full=True)

    class Meta:
        queryset = Student.objects.all()
        resource_name = "student"
        allowed_methods = ['get', 'post', 'put', 'delete']
        ordering = ['first_name']
        always_return_data = True
        authentication = Authentication()
        authorization = Authorization()

        # cache = SimpleCache(timeout=6000)


class ClassResource(ModelResource):
    # ToOneField for one to one.
    # ToManyField for everything else.
    # full=False returns resource's URI instead
    students = ToManyField(StudentResource, 'students', full=False)


    class Meta:
        queryset = Class.objects.all()
        resource_name = "class"
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True

        # Filtering allows you to look at things like this
        # http://127.0.0.1:8000/api/v1/class/?start_date__gt=2014-01-01&format=json
        filtering = {
            'students': ALL_WITH_RELATIONS,
            'title': ['contains', 'icontains'],
            'start_date': ['gt',]
            # Other options include:
            # ['exact', 'range', 'gt', 'gte', 'lt', 'lte']
        }


class StudentProjectResource(ModelResource):
    student = ToOneField(StudentResource, 'student', full=False)

    class Meta:
        queryset = StudentProject.objects.all()
        resource_name = "projects"
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = Authentication()
        authorization = Authorization()
        # always_return_data = True
