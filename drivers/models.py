from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.validators import RegexValidator
# from rider.models import Rider_profile


# Create your models here.
class Driver_profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length=200, blank =True)
    location = models.CharField(max_length = 50, blank =True)
    phone_number =models.IntegerField(blank = True, null = True)
    profile_pic = models.ImageField(upload_to = 'profile_pic/', blank=True, null= True)
    car_model = models.CharField(max_length = 30, blank = True)
    car_number_plates = models.CharField(max_length = 30, blank = True)
    car_capacity = models.IntegerField(default = 0)
    car_image = models.ImageField(upload_to ='car_images/', blank =True, null =True)
    car_color = models.CharField(max_length = 30, blank =True)
    current_location = models.CharField(max_length = 10)
    destination = models.CharField(max_length = 30, blank = True, null = True)




@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Driver_profile.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_user_profile(sender,instance, **kwargs):
    instance.driver_profile.save()


# class DriverReview(models.Model):
#     rider_profile = models.ForeignKey(Rider_profile, on_delete=models.CASCADE)
#     driver_profile = models.ForeignKey(Driver_profile, on_delete=models.CASCADE)
#     review = models.TextField(max_length=500)



#     @classmethod
#     def get_reviews(cls, driver_profile_id):
#         driver_reviews = DriverReview.objects.filter(driver_profile = driver_profile_id)
#         return driver_reviews


class TripPlan(models.Model):
    driver_profile = models.ForeignKey(Driver_profile,on_delete=models.CASCADE )
    current_location = models.CharField(max_length = 30)
    destination = models.CharField(max_length = 30)
