from django.db import models
from apps.accounts.models import ProfileModel
# Create your models here.


class concertModel(models.Model):
    class Meta:
        verbose_name="مدل کنسرت"
        verbose_name_plural="مدل کنسرت"
    Name=models.CharField(max_length=100,verbose_name="نام کنسرت")
    SingerName=models.CharField(max_length=100,verbose_name="نام خواننده")
    lenght=models.IntegerField(verbose_name="طول برنامه")
    Poster=models.ImageField(upload_to="concertImages/",verbose_name="پوستر")
    def __str__(self) -> str:
        return self.SingerName
    
class locationModel(models.Model):
    class Meta:
        verbose_name="مکان"
        verbose_name_plural="مکان ها"
    Name=models.CharField(max_length=100,verbose_name="نام محل")
    Address=models.CharField(max_length=500,default="تهران - برج میلاد",verbose_name="آدرس")
    Phone=models.CharField(max_length=11,verbose_name="تلفن")
    capacity=models.IntegerField(verbose_name="ظرفیت")

    def __str__(self) -> str:
        return self.SingerName
    
class timeModel(models.Model):
    class Meta:
        verbose_name="سانس"
        verbose_name_plural="سانس ها"
    concertModel=models.ForeignKey(concertModel,on_delete=models.PROTECT)
    locationModel=models.ForeignKey(locationModel,on_delete=models.PROTECT)
    StartDateTime=models.DateTimeField(verbose_name="تایم شروع")
    Seat=models.IntegerField(verbose_name="شماره صندلی")
    Start=1
    End=2
    Cancle=3
    Sales=4
    status_choices=(
        (Start,"فروش بلیط آغاز شده است"),
        (End,"پایان"),
        (Sales,"در حال فروش..."),
        (Cancle,'کنسل شده'),
    )
    Status=models.IntegerField(choices=status_choices,default=1,verbose_name="وضعیت")


    def __str__(self) -> str:
        return f"Time: {self.StartDateTime} Concert Name : {self.concertModel.Name} location: {self.locationModel.Name} " 


class ticketModel(models.Model):
    class Meta:
        verbose_name="بلیت"
        verbose_name_plural="بلیت ها"
    ProfileModel=models.ForeignKey(ProfileModel,on_delete=models.PROTECT)
    timeModel=models.ForeignKey(timeModel,on_delete=models.PROTECT)
    ticketImage=models.ImageField(upload_to="TicketImages/",verbose_name="تصویر بلیت")
    Name=models.CharField(max_length=100,verbose_name="نام بلیت")
    Price=models.IntegerField(verbose_name="بهای بلیت")

    def __str__(self):
        return "TicketInfo: Profile: {} ConcertInfo : {}".format(timeModel.__str__())

