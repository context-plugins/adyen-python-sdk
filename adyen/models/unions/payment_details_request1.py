from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..ideal_payment_details_request import IdealPaymentDetailsRequest, IdealPaymentDetailsRequestDict

PaymentDetailsRequest1: TypeAlias = Annotated[IdealPaymentDetailsRequest, Field(discriminator="method")]

PaymentDetailsRequest1Dict: TypeAlias = IdealPaymentDetailsRequestDict
