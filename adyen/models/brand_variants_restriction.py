from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BrandVariantsRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[str]] = UNSET
    """List of card brand variants.

    Possible values:

    - **mc**, **mccredit**, **mccommercialcredit_b2b**, **mcdebit**, **mcbusinessdebit**, **mcbusinessworlddebit**,
        **mcprepaid**, **mcmaestro**

     - **visa**, **visacredit**, **visadebit**, **visaprepaid**.

    You can specify a rule for a generic variant. For example, to create a rule for all Mastercard payment instruments,
    use **mc**. The rule is applied to all payment instruments under **mc**, such as **mcbusinessdebit** and
    **mcdebit**."""


class BrandVariantsRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[list[str]]
