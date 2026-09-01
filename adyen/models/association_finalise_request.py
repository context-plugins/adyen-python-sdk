from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .association_delegated_authentication_data1 import (
    AssociationDelegatedAuthenticationData1,
    AssociationDelegatedAuthenticationData1Dict,
)


class AssociationFinaliseRequest(SdkBaseModel):
    ids: list[str]
    """The list of unique identifiers of the resources that you are associating with the SCA device.

    Maximum: 5 strings."""

    strong_customer_authentication: AssociationDelegatedAuthenticationData1 = Field(
        alias="strongCustomerAuthentication"
    )
    """Contains authentication information required to associate the resource with the SCA device."""

    type_: Literal["PaymentInstrument"] = Field(default="PaymentInstrument", alias="type")
    """The type of resource that you are associating with the SCA device.

    Possible value: **PaymentInstrument**"""


class AssociationFinaliseRequestDict(TypedDict):
    ids: list[str]
    strong_customer_authentication: (
        AssociationDelegatedAuthenticationData1 | AssociationDelegatedAuthenticationData1Dict
    )
    type_: NotRequired[Literal["PaymentInstrument"]]
