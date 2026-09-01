from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StorePaymentMethodMode(str, Enum):
    """Indicates if the details of the payment method will be stored for the shopper. Possible values:
    * **disabled** – No details will be stored (default).
    * **askForConsent** – If the ``shopperReference`` is provided, the Drop-in/Component shows a checkbox where the
        shopper can select to store their payment details for card payments.
    * **enabled** – If the ``shopperReference`` is provided, the details will be stored without asking the shopper for
        consent."""

    ASK_FOR_CONSENT = "askForConsent"
    DISABLED = "disabled"
    ENABLED = "enabled"

    __str__ = str.__str__


StorePaymentMethodModeOrStr: TypeAlias = Annotated[
    StorePaymentMethodMode | str, open_enum_validator(StorePaymentMethodMode)
]
