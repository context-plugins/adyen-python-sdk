from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount29 import Amount29, Amount29Dict
from .application_info import ApplicationInfo, ApplicationInfoDict
from .enums.adjust_auth_type import AdjustAuthTypeOrStr
from .enums.industry_usage1 import IndustryUsage1OrStr
from .line_item import LineItem, LineItemDict
from .split import Split, SplitDict
from .three_dsecure_data3 import ThreeDsecureData3, ThreeDsecureData3Dict


class PaymentAmountUpdateRequest(SdkBaseModel):
    adjust_auth_type: Optional[AdjustAuthTypeOrStr] = Field(default=UNSET, alias="adjustAuthType")
    """The type of adjustment. Possible values:

    * **cardholderInitiatedTransaction**

    * **merchantInitiatedTransaction**"""

    adjust_authorisation_data: Optional[str] = Field(default=UNSET, alias="adjustAuthorisationData")
    """The required data to make a `synchronous authorization adjustment
    <https://docs.adyen.com/online-payments/adjust-authorisation>`__. Pass the corresponding value from the
    ``/payments`` response or webhook message."""

    amount: Amount29
    """The updated amount. The ``currency`` must match the currency used in authorisation."""

    application_info: Optional[ApplicationInfo] = Field(default=UNSET, alias="applicationInfo")
    """Information about your application. For more details, see `Building Adyen solutions
    <https://docs.adyen.com/development-resources/building-adyen-solutions>`__."""

    industry_usage: Optional[IndustryUsage1OrStr] = Field(default=UNSET, alias="industryUsage")
    """The reason for the amount update. Possible values:
    * **delayedCharge**
    * **noShow**
    * **installment**"""

    line_items: Optional[list[LineItem]] = Field(default=UNSET, alias="lineItems")
    """Price and product information of the refunded items, required for `partial refunds
    <https://docs.adyen.com/online-payments/refund#refund-a-payment>`__.
    > This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay,
        Walley, and Zip."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account that is used to process the payment."""

    mpi_data: Optional[ThreeDsecureData3] = Field(default=UNSET, alias="mpiData")
    """Authentication data from a `merchant plug-in (MPI) <https://en.wikipedia.org/wiki/Merchant_plug-in>`__ like
    Mastercard SecureCode, Visa Secure, or Cartes Bancaires. Required for cardholder-initiated transaction (CIT)
    adjustments."""

    reference: Optional[str] = UNSET
    """Your reference for the amount update request. Maximum length: 80 characters."""

    splits: Optional[list[Split]] = UNSET
    """An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms.
    For more information, see how to process payments for `marketplaces
    <https://docs.adyen.com/marketplaces/process-payments>`__ or `platforms
    <https://docs.adyen.com/platforms/process-payments>`__."""


class PaymentAmountUpdateRequestDict(TypedDict):
    adjust_auth_type: NotRequired[AdjustAuthTypeOrStr]
    adjust_authorisation_data: NotRequired[str]
    amount: Amount29Dict
    application_info: NotRequired[ApplicationInfoDict]
    industry_usage: NotRequired[IndustryUsage1OrStr]
    line_items: NotRequired[list[LineItemDict]]
    merchant_account: str
    mpi_data: NotRequired[ThreeDsecureData3Dict]
    reference: NotRequired[str]
    splits: NotRequired[list[SplitDict]]
