from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentFlow(str, Enum):
    """The sales channel used for the payment., The sales channel. Possible values: **Ecommerce**, **POS**."""

    ECOMMERCE = "Ecommerce"
    POS = "POS"

    __str__ = str.__str__


PaymentFlowOrStr: TypeAlias = Annotated[PaymentFlow | str, open_enum_validator(PaymentFlow)]
