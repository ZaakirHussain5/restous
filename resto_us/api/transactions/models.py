from django.db import models
from api.user.models import resto_user
from api.restraunt.models import restraunt,restraunt_standards

def generate_trans_id():
    from django.db.models import Max
    import datetime
    now = datetime.datetime.now()
    uid = transaction.objects.aggregate(Max('id'))
    uid = uid['id__max'] 
    if uid == None:
        uid = 0
    return 'TRANS'+ str(now.year) +'-'+ str(uid+1)

class transaction(models.Model):
    trans_id = models.CharField(max_length=15,default=generate_trans_id)
    users_id = models.ForeignKey(resto_user,on_delete=models.CASCADE)
    restraunt_id = models.ForeignKey(restraunt,on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)
    trans_amt = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    trans_date = models.DateTimeField(auto_now_add=True) 

class UserDealSubscription(models.Model):
    users_id = models.ForeignKey(resto_user,on_delete=models.CASCADE)
    subscription = models.ForeignKey(restraunt_standards,on_delete=models.CASCADE)
    meals_had = models.PositiveIntegerField(default=0)
    meals_remaining = models.PositiveIntegerField(default=0)
    is_expired = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


