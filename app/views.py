from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView
from app import serializers
from app import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
import django_filters
from .models import Student
from .serializers import StudentSerializers

from rest_framework.response import Response
from rest_framework import status

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['full_name',]

# Create your views here.

# Sponsor uchun
class  SponsorListAPIView(ListAPIView):
    serializer_class = serializers.SponsorSerializers
    queryset = models.Sponsor.objects.all()
    filter_backends =  [DjangoFilterBackend,SearchFilter]
    filterset_fields = ('status',)
    search_fields = ('full_name',)

class SponsorCreateAPIView(CreateAPIView):
    serializer_class = serializers.SponsorSerializers
    queryset = models.Sponsor.objects.all()
    
class SponsorDestroyAPIView(DestroyAPIView):
    serializer_class = serializers.SponsorSerializers
    queryset = models.Sponsor.objects.all()

class SponsorUpdateAPIView(UpdateAPIView):
    serializer_class = serializers.SponsorSerializers
    queryset = models.Sponsor.objects.all()


# Talaba uchun
class TalabaListAPIView(ListAPIView):
    serializer_class = serializers.StudentSerializers
    queryset = models.Student.objects.all()
    filter_backends =  [DjangoFilterBackend,SearchFilter]
    filterset_fields = ('Talaba_turi', 'otm')
    search_fields = ('full_name',)

class TalabaDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = serializers.StudentDetailSerializers
    queryset = models.Student.objects.all()

class TalabaCreateAPIView(CreateAPIView):
    serializer_class = serializers.StudentSerializers
    queryset = models.Student.objects.all()
    
class TalabaDestroyAPIView(DestroyAPIView):
    serializer_class = serializers.StudentSerializers
    queryset = models.Student.objects.all()

class TalabaUpdateAPIView(UpdateAPIView):
    serializer_class = serializers.StudentSerializers
    queryset = models.Student.objects.all()


# SponsorStudent uchun
class SponsorStudentListAPIView(ListAPIView):
    serializer_class = serializers.StudentSponsorSerializers
    queryset = models.SponsorStudent.objects.all()

class SponsorStudentCreateAPIView(CreateAPIView):
    serializer_class = serializers.StudentSponsorSerializers
    queryset = models.SponsorStudent.objects.all()
    
class SponsorStudentDestroyAPIView(DestroyAPIView):
    serializer_class = serializers.StudentSponsorSerializers
    queryset = models.SponsorStudent.objects.all()

class SponsorStudentUpdateAPIView(UpdateAPIView):
    serializer_class = serializers.StudentSponsorSerializers
    queryset = models.SponsorStudent.objects.all()

class StudentSponsorlistAPIView(ListAPIView):
    
    queryset = models.SponsorStudent.objects.all()
    serializer_class = serializers.StudentSponsorListSerializers
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ('student',)
    # def get(self, request, format=None):
    #     filter = StudentFilter(request.GET, queryset=Student.objects.all())
    #     students = filter.qs
    #     serializer = StudentSerializers(students, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = StudentSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# University uchun

class UniversityCreateAPIView(CreateAPIView):
    serializer_class = serializers.UniversitySerializers
    queryset = models.University.objects.all()

class StaticticAPIView(APIView):

    def get(self, request):
        from django.db.models import Sum
        total_paid_amount = models.SponsorStudent.objects.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        total_required_amount = models.Student.objects.aggregate(total_amount=Sum('contract'))['total_amount'] or 0
        total_unpaid_amount = total_required_amount - total_paid_amount
        return Response(
            data={
                'total_paid_amount' : total_paid_amount,
                'total_required_amount' : total_required_amount,
                'total_unpaid_amount' : total_unpaid_amount
            }
        )

class GraphicAPIView(APIView):

    def get(self, request):
        from datetime import datetime
        this_year = datetime.now().year
        from django.db.models import Sum
        result = []

        for i in range(1,13):
            sponsor_amount = models.Sponsor.objects.filter(
                created_at__month=i,
                created_at__year=this_year,
                status='tasdiqlangan'
            ).aggregate(total=Sum('amount'))['total'] or 0

            student_amount = models.Student.objects.filter(
                created_at__month=i,
                created_at__year=this_year,
            ).aggregate(total=Sum('contract'))['total'] or 0

            result.append({
                "month":i,
                "sponsor_amount":sponsor_amount,
                "student_amount":student_amount
            })

        return Response(result)



