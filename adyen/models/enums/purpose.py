from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Purpose(str, Enum):
    """Specifies the reason for creating the rule.

    Possible values:
    * **fraud**: the rule is created to regulate fraudulent activity.
    * **policy**: the rule is created to ensure that the transaction adheres to your business' policies. For example, if
        your business has policies about the Merchant Category Codes (MCCs) allowed on a transaction, you can create a
        rule to block transactions that have specific MCCs."""

    COMPLIANCE = "compliance"
    FRAUD = "fraud"
    INTERNAL_POLICY = "internalPolicy"
    POLICY = "policy"
    SYSTEM = "system"

    __str__ = str.__str__


PurposeOrStr: TypeAlias = Annotated[Purpose | str, open_enum_validator(Purpose)]
