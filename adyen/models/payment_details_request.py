from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .details_request_authentication_data1 import (
    DetailsRequestAuthenticationData1,
    DetailsRequestAuthenticationData1Dict,
)
from .payment_completion_details1 import PaymentCompletionDetails1, PaymentCompletionDetails1Dict


class PaymentDetailsRequest(SdkBaseModel):
    authentication_data: Optional[DetailsRequestAuthenticationData1] = Field(default=UNSET, alias="authenticationData")
    """Data for 3DS authentication."""

    details: PaymentCompletionDetails1
    """Use this collection to submit the details that were returned as a result of the ``/payments`` call."""

    payment_data: Optional[str] = Field(default=UNSET, alias="paymentData")
    """Encoded payment data. For `authorizing a payment after using 3D Secure 2 Authentication-only
    <https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only/#authorise-the-payment-with-adyen>`__:

    If you received ``resultCode``: **AuthenticationNotRequired** in the ``/payments`` response, use the
    ``threeDSPaymentData`` from the same response.

    If you received ``resultCode``: **AuthenticationFinished** in the ``/payments`` response, use the
    ``action.paymentData`` from the same response."""

    three_ds_authentication_only: Optional[bool] = Field(default=UNSET, alias="threeDSAuthenticationOnly")
    """Change the ``authenticationOnly`` indicator originally set in the ``/payments`` request. Only needs to be set if
    you want to modify the value set previously."""


class PaymentDetailsRequestDict(TypedDict):
    authentication_data: NotRequired[DetailsRequestAuthenticationData1Dict]
    details: PaymentCompletionDetails1Dict
    payment_data: NotRequired[str]
    three_ds_authentication_only: NotRequired[bool]
