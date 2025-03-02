import os
from logging import getLogger

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY
logger = getLogger(__name__)


class GetStripeSessionIdView(View):

    def get(self, request, id):

        success_url = request.build_absolute_uri(
            reverse("success-payment-page")
        )
        cancel_url = request.build_absolute_uri(reverse("cancel-payment-page"))

        item = Item.objects.get(id=id)
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": item.name,
                        },
                        "unit_amount": item.price,
                    },
                    "quantity": 1,
                }
            ],
            metadata={"item_id": item.id},
            mode="payment",
            success_url=success_url,
            cancel_url=cancel_url,
        )
        return JsonResponse({"id": session.id})


class SuccessPaymentPageView(TemplateView):
    template_name = "stripe_payment/success.html"


class CancelPaymentPageView(TemplateView):
    template_name = "stripe_payment/cancel.html"


class ItemPageView(TemplateView):
    template_name = "stripe_payment/item_buy.html"

    def get_context_data(self, **kwargs):
        item_id = kwargs.get("id")
        item = Item.objects.get(id=item_id)

        context = super().get_context_data(**kwargs)
        context.update(
            {
                "item": item,
                "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
            }
        )

        return context
