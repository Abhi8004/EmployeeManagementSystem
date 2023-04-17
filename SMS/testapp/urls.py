from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from testapp.views import SchoolViewSets,StudentViewSets

router=routers.DefaultRouter()
router.register(r'school', SchoolViewSets)
router.register(r'student', StudentViewSets)
#router.register(r'login', LoginAPI)

urlpatterns = [
    #path('login/', UserLoginView.as_view(), name='login'),
    #path('register/', UserRegistrationView.as_view(), name='register'),
    path('', include(router.urls)),
]


#companies/{companyId}/employees
