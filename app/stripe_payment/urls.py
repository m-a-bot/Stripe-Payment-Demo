from django.urls import include, path

from .views import (
    CancelPaymentPageView,
    GetStripeSessionIdView,
    ItemPageView,
    SuccessPaymentPageView,
)

"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path("item/<int:id>/", ItemPageView.as_view(), name="item-page"),
    path(
        "buy/<int:id>/",
        GetStripeSessionIdView.as_view(),
        name="get-stripe-session-id",
    ),
    path(
        "success/",
        SuccessPaymentPageView.as_view(),
        name="success-payment-page",
    ),
    path(
        "cancel/", CancelPaymentPageView.as_view(), name="cancel-payment-page"
    ),
]
