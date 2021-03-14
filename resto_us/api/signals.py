from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from api.transactions.models import transaction,UserDealSubscription
from api.restraunt.models import restraunt_standards
from django.conf import settings


@receiver(post_save, sender=transaction)
def updateSubscription(sender, instance, created, **kwargs):
    if created:
        user = instance.users_id
        try:
            user_deal = UserDealSubscription.objects.get(users_id=user,subscription__restraunt_id=instance.restraunt_id)
            try:
                message = EmailMessage(
                    'Transaction Notification',
                    'You have Done a Transaction at ' + instance.restraunt_id.name  + ' on ' + instance.created_at + ' of ' + instance.description,
                    settings.EMAIL_HOST_USER,
                    [user.email]
                )
                message.send()
            except:
                pass
            if instance.trans_amt >= user_deal.subscription.value_of_meal:
                user_deal.meals_had += 1
                user_deal.meals_remaining -= 1
                if user_deal.meals_remaining == 0:
                    user_deal.is_expired =True
                else:
                    user_deal.is_expired = False
                user_deal.save()
        except UserDealSubscription.DoesNotExist:
            pass
