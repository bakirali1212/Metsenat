from dataclasses import fields
from rest_framework.serializers import ModelSerializer
# from pyexpat import model
from django.db.models import Sum
from rest_framework import serializers

from .models import Student,SponsorStudent,Sponsor,University,BaseModel

class SponsorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        exclude = ['update_at','sponsr_type','payment_type','organization']
        
class StudentSerializers(serializers.ModelSerializer):
    # otm = serializers.StringRelatedField(source = 'otm.title')
    sponsor = serializers.SerializerMethodField()

    def get_sponsor(self, obj):

        
        
        student_paid_money = obj.Sponsor_Student.all().aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        return f" {student_paid_money}"

    class Meta:
        model = Student
        exclude = ['update_at','create_at','phone']


class StudentDetailSerializers(serializers.ModelSerializer):
    otm = serializers.StringRelatedField(source = 'otm.title')

    class Meta:
        model = Student
        exclude = ['update_at','create_at']


        


class UniversitySerializers(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'
        
class BaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = '__all__'

class StudentSponsorSerializers(serializers.ModelSerializer):
    sponsor = SponsorSerializers(read_only=True)
    class Meta:
        model = SponsorStudent
        fields = ('__all__')

        def validate(self, attrs):
        
            amount = attrs.get('amount')
            sponsor = attrs.get('sponsor')
            student = attrs.get('student')
            
            student_paid_money = student.Sponsor_Student.all().aggregate(total_amount=Sum('amount'))['total_amount'] or 0
            if student.kontrakt - student_paid_money < amount:
                raise serializers.ValidationError(detail={'error': f"Siz {student.kontrakt - student_paid_money} pul to'lasangiz yetarli"})
            
            sponsor_paid_money = sponsor.Sponsor_Student.all().aggregate(total_amount=Sum('amount'))['total_amount'] or 0
            if sponsor.amount - sponsor_paid_money < amount:
                raise serializers.ValidationError(detail={'error': f"Sizning xisobingizda {sponsor.amount - sponsor_paid_money} pul bor"})


            return attrs
        
class StudentSponsorListSerializers(ModelSerializer):
    sponsor = serializers.StringRelatedField(source = 'sponsor.full_name')
    class Meta:
        model = SponsorStudent
        fields = ('id', 'sponsor', 'amount')