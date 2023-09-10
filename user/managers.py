from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_student(self,user_name,email,password=None):
        student = self.model(
            user_name    = user_name,
            email        = email
        )
        student.set_password(password)
        student.save(using = self._db)
        return student
    

    def create_teacher(self,user_name,email,password=None):
        teacher = self.model(
            user_name = user_name,
            email=email
        )
        teacher.set_password(password)
        teacher.save(using = self._db)
        return teacher

    def create_superuser(self,user_name,email,password=None):
        admin = self.model(
            user_name    = user_name,
            email        = email
        )
        admin.set_password(password)
        admin.is_admin  = True
        admin.is_staff  = True
        admin.save(using = self._db)
        return admin