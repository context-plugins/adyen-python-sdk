from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.types_with_error import TypesWithErrorOrStr
from .management_payment_method import ManagementPaymentMethod, ManagementPaymentMethodDict
from .pagination_links1 import PaginationLinks1, PaginationLinks1Dict


class PaymentMethodResponse(SdkBaseModel):
    links: Optional[PaginationLinks1] = Field(default=UNSET, alias="_links")
    """Pagination references."""

    data: Optional[list[ManagementPaymentMethod]] = UNSET
    """The list of supported payment methods and their details."""

    items_total: int = Field(alias="itemsTotal")
    """Total number of items."""

    pages_total: int = Field(alias="pagesTotal")
    """Total number of pages."""

    types_with_errors: Optional[list[TypesWithErrorOrStr]] = Field(default=UNSET, alias="typesWithErrors")
    """The payment method types that were not successfully requested and their corresponding errors."""


class PaymentMethodResponseDict(TypedDict):
    links: NotRequired[PaginationLinks1Dict]
    data: NotRequired[list[ManagementPaymentMethodDict]]
    items_total: int
    pages_total: int
    types_with_errors: NotRequired[list[TypesWithErrorOrStr]]
