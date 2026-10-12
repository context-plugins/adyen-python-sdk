from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..ideal_payment_details_request import IdealPaymentDetailsRequest, IdealPaymentDetailsRequestDict

PaymentDetailsRequest1: TypeAlias = Annotated[
    Annotated[IdealPaymentDetailsRequest, Tag("ideal")], WireDiscriminator("method")
]

PaymentDetailsRequest1Dict: TypeAlias = IdealPaymentDetailsRequestDict
