from django.shortcuts import render
from testapp.models import School,Student
from rest_framework import viewsets
from testapp.serializers import SchoolSerializer,StudentSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class SchoolViewSets(viewsets.ModelViewSet):
      queryset=School.objects.all()
      serializer_class=SchoolSerializer

    #companies/{companyId}/employees
      @action(detail=True, methods=['get'])
      def students(self,request,pk=None):
          try:
            school=School.objects.get(pk=pk)
            std=Student.objects.filter(school=school)
            stds_serializer=StudentSerializer(stds,many=True,context={'request':request})
            return Response(emps_serializer.data)
          except Exception as e:
              print(e)
              return Response({
                'message':'Company might not exits !! Error '
            })


class StudentViewSets(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class LoginAPI(viewsets.ModelViewSet):
    def post(self,request):
        try:
            data=request.data
            serializer=LoginSerializer(data=data)
            if serializer.is_valid():
                 email = serializer.data['email']
                 password = serializer.data['password']

                 user = authenticate(email=email,password=password)

                 if user is None:

                     return Responce({
                             'status'  : 400,
                             'message' : 'invalid password',
                             'data' : {}
                       })

                 refresh = RefreshToken.for_user(user)

                 return {
                      'refresh': str(refresh),
                      'access': str(refresh.access_token),
                  }

            return Responce({
                     'status'  : 400,
                     'message' : 'something went wrong',
                     'data' : serializer.errors
               })

        except Exception as e:
             print(e)
