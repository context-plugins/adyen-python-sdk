from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Surcharge(SdkBaseModel):
    value: int
    """The `surcharge <https://docs.adyen.com/online-payments/surcharge/>`__ amount to apply to the transaction, in
    `minor units <https://docs.adyen.com/development-resources/currency-codes>`__. When you apply surcharge, include the
    surcharge in the ``amount.value`` field.

    Review our `Surcharge compliance guide <https://docs.adyen.com/development-resources/surcharge-compliance/>`__ to
    learn about how to comply with regulatory requirements when applying surcharge."""


class SurchargeDict(TypedDict):
    value: int
