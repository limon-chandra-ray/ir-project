from django.db import models
from user.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import pre_delete,post_save
from django.shortcuts import get_object_or_404

# Create your models here.

class StudentManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        result =  super().get_queryset(*args, **kwargs)
        return result.filter(role = CustomUser.Role.STUDENT)
class Student(CustomUser):
    base_role = CustomUser.Role.STUDENT
    student = StudentManager()
    class Meta:
        proxy = True
@receiver(post_save,sender = Student)
def create_staff_profile(sender,instance,created,*args, **kwargs):
    if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user = instance)

class StudentProfile(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11,unique=True,null=True,blank=True)
    student_id = models.CharField(max_length=50,unique=True,null=True,blank=True)
    image = models.ImageField(upload_to='student/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.user.email
    def save(self,*args, **kwargs):
        if self.id:
            existing = get_object_or_404(StudentProfile,id = self.id)
            if existing.image != self.image:
                existing.image.delete(save=False)
        super(StudentProfile,self).save(*args, **kwargs)

    @receiver(pre_delete,sender = 'studentTeam.StudentProfile')
    def student_profile_image_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'image':

                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save = False)
    
