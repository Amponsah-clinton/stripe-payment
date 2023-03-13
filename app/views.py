from django.shortcuts import render
import stripe
from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context
    
def charge(request):
    if request.method =='POST':
        charge = stripe.Charge.create(
            amount = 500,
            currency = 'usd',
            description = 'Django charge',
            source = request.POST['stripeToken'],
        )
        return render(request, 'charge.html')