from django.db import models
from user.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import pre_delete,post_save
from django.shortcuts import get_object_or_404

# Create your models here.

class TeacherManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        result =  super().get_queryset(*args, **kwargs)
        return result.filter(role = CustomUser.Role.TEACHER)
class Teacher(CustomUser):
    base_role = CustomUser.Role.TEACHER
    teacher = TeacherManager()
    class Meta:
        proxy = True
@receiver(post_save,sender = Teacher)
def create_staff_profile(sender,instance,created,*args, **kwargs):
    if created and instance.role == "TEACHER":
        TeacherProfile.objects.create(user = instance)

class TeacherProfile(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11,unique=True,null=True,blank=True)
    image = models.ImageField(upload_to='teacher/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.user.email
    def save(self,*args, **kwargs):
        if self.id:
            existing = get_object_or_404(TeacherProfile,id = self.id)
            if existing.image != self.image:
                existing.image.delete(save=False)
        super(TeacherProfile,self).save(*args, **kwargs)

    @receiver(pre_delete,sender = 'teacherTeam.TeacherProfile')
    def teacher_profile_image_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'image':
                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save = False)
    
