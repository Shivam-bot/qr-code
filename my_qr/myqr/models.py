from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.


class user_detail(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    dob = models.DateField(blank=True,null=True)
    
    qr = models.ImageField(upload_to="my_qr_code",blank=True,null=True)
    
    def __repr__(self):
        return f"{self.name} {self.dob}"
    
    class Meta:
        db_table = 'User'
        
    def save(self, *args,**kwargs):
        my_qrcode = qrcode.make(f'name:{self.name},dob: {self.dob}')
        canvas = Image.new("RGB",(290,290),'white')
        # draw = ImageDraw.Draw(canvas)
        canvas.paste(my_qrcode)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr.save(fname,File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)