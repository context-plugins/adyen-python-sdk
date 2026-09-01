from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .company_links2 import CompanyLinks2, CompanyLinks2Dict
from .data_center import DataCenter, DataCenterDict


class Company2(SdkBaseModel):
    links: Optional[CompanyLinks2] = Field(default=UNSET, alias="_links")
    """References to resources connected with this company."""

    data_centers: Optional[list[DataCenter]] = Field(default=UNSET, alias="dataCenters")
    """List of available data centers.

    Adyen has several data centers around the world.In the URL that you use for making API requests, we recommend you
    use the live URL prefix from the data center closest to your shoppers."""

    description: Optional[str] = UNSET
    """Your description for the company account, maximum 300 characters"""

    id: Optional[str] = UNSET
    """The unique identifier of the company account."""

    name: Optional[str] = UNSET
    """The legal or trading name of the company."""

    reference: Optional[str] = UNSET
    """Your reference to the account"""

    status: Optional[str] = UNSET
    """The status of the company account.

    Possible values:

    * **Active**: Users can log in. Processing and payout capabilities depend on the status of the merchant account.
    * **Inactive**: Users can log in. Payment processing and payouts are disabled.
    * **Closed**: The company account is closed and this cannot be reversed. Users cannot log in. Payment processing and
        payouts are disabled."""


class Company2Dict(TypedDict):
    links: NotRequired[CompanyLinks2 | CompanyLinks2Dict]
    data_centers: NotRequired[list[DataCenter | DataCenterDict]]
    description: NotRequired[str]
    id: NotRequired[str]
    name: NotRequired[str]
    reference: NotRequired[str]
    status: NotRequired[str]
