from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict
from .platform_chargeback_logic import PlatformChargebackLogic, PlatformChargebackLogicDict
from .split import Split, SplitDict
from .three_dsecure_data import ThreeDsecureData, ThreeDsecureDataDict


class VoidPendingRefundRequest(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be required for a particular modification request.

    The additionalData object consists of entries, each of which includes the key and value."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account that is used to process the payment."""

    modification_amount: Optional[Amount] = Field(default=UNSET, alias="modificationAmount")
    """The amount that needs to be captured/refunded. Required for ``/capture`` and ``/refund``, not allowed for
    ``/cancel``. The ``currency`` must match the currency used in authorisation, the ``value`` must be smaller than or
    equal to the authorised amount."""

    mpi_data: Optional[ThreeDsecureData] = Field(default=UNSET, alias="mpiData")
    """Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires)."""

    original_merchant_reference: Optional[str] = Field(default=UNSET, alias="originalMerchantReference")
    """The original merchant reference to cancel."""

    original_reference: Optional[str] = Field(default=UNSET, alias="originalReference")
    """The original pspReference of the payment to modify. This reference is returned in:
    * authorisation response
    * authorisation notification"""

    platform_chargeback_logic: Optional[PlatformChargebackLogic] = Field(default=UNSET, alias="platformChargebackLogic")
    """Defines how to book chargebacks when using `Adyen for Platforms
    <https://docs.adyen.com/adyen-for-platforms-model>`__."""

    reference: Optional[str] = UNSET
    """Your reference for the payment modification. This reference is visible in Customer Area and in reports. Maximum
    length: 80 characters."""

    splits: Optional[list[Split]] = UNSET
    """An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms.
    For more information, see how to split payments for `platforms
    <https://docs.adyen.com/platforms/automatic-split-configuration/>`__."""

    tender_reference: Optional[str] = Field(default=UNSET, alias="tenderReference")
    """The transaction reference provided by the PED. For point-of-sale integrations only."""

    unique_terminal_id: Optional[str] = Field(default=UNSET, alias="uniqueTerminalId")
    """Unique terminal ID for the PED that originally processed the request. For point-of-sale integrations only."""


class VoidPendingRefundRequestDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    merchant_account: str
    modification_amount: NotRequired[AmountDict]
    mpi_data: NotRequired[ThreeDsecureDataDict]
    original_merchant_reference: NotRequired[str]
    original_reference: NotRequired[str]
    platform_chargeback_logic: NotRequired[PlatformChargebackLogicDict]
    reference: NotRequired[str]
    splits: NotRequired[list[SplitDict]]
    tender_reference: NotRequired[str]
    unique_terminal_id: NotRequired[str]
