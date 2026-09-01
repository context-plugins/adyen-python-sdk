from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Name(SdkBaseModel):
    """Name of the person., The shopper's full name., the name of the person, The name of the shopper., The shopper's
    full name., The shopper's name.

    When the ``entityType`` is ``Company``, the ``shopperName.lastName`` must contain the company name., The shopper's
    name.

    In case the ``entityType`` is ``Company``, the ``shopperName.lastName`` must contain the company name.

    > This field is required to update the existing ``shopperName`` associated with a recurring contract., Name of the
        person., The user's full name.

    Allowed length: 1—80 characters., The user's full name., The name of the contact."""

    first_name: str = Field(alias="firstName")
    """The first name."""

    last_name: str = Field(alias="lastName")
    """The last name."""


class NameDict(TypedDict):
    first_name: str
    last_name: str
