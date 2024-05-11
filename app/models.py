from django.db import models



# Create your models here.
class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
    
class University(BaseModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}-{self.title}"
    


class Sponsor(BaseModel):
    class HomiyChoices(models.TextChoices):
        YANGI = 'yangi', 'Yangi'
        MODERATSIYA = 'moderatsiya', 'Moderatsiyada'
        TASDIQLANGAN = 'tasdiqlangan', 'Tasdiqlangan'
        ATMEN = 'atmen', 'Atmen'
    status =  models.CharField(max_length=100,
                              choices=HomiyChoices.choices,
                              default=HomiyChoices.YANGI)
    
    class SponsorType(models.TextChoices):
        YURIDIK = 'yuridik', 'Yuridik'
        JISMONIY = 'jismoniy', 'Jismoniy'
    sponsr_type =  models.CharField(max_length=100,
                              choices=SponsorType.choices,
                              default=SponsorType.JISMONIY)
    
    class PaymentType(models.TextChoices):
        NAQD = 'naqd', 'Naqd'
        PLASTIK = 'plastik', 'Plastik'
    payment_type =  models.CharField(max_length=100,
                              choices=PaymentType.choices,
                              default=PaymentType.PLASTIK)
    
    
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    organization = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id}-{self.full_name}"
    
    
    


class Student(BaseModel):
    class TalabaChoices(models.TextChoices):
        BAKALAVR = 'bakalvr', 'Bakalvr'
        MAGISTR = 'magistr', 'Magistr'
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    x = models.DecimalField(max_digits=10,decimal_places=2)
    otm = models.ForeignKey(University, on_delete=models.PROTECT)
    Talaba_turi =  models.CharField(max_length=100,
                              choices=TalabaChoices.choices,
                              default=TalabaChoices.BAKALAVR)
    def __str__(self):
        return f"{self.id}-{self.full_name}"
    
class SponsorStudent(BaseModel):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.PROTECT, related_name='Sponsor_Student')
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='Sponsor_Student')

    
