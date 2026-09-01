from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResponseAdditionalData3Dsecure(SdkBaseModel):
    card_holder_info: Optional[str] = Field(default=UNSET, alias="cardHolderInfo")
    """Information provided by the issuer to the cardholder. If this field is present, you need to display this
    information to the cardholder."""

    cavv: Optional[str] = UNSET
    """The Cardholder Authentication Verification Value (CAVV) for the 3D Secure authentication session, as a
    Base64-encoded 20-byte array."""

    cavv_algorithm: Optional[str] = Field(default=UNSET, alias="cavvAlgorithm")
    """The CAVV algorithm used."""

    sca_exemption_requested: Optional[str] = Field(default=UNSET, alias="scaExemptionRequested")
    """Shows the `exemption type
    <https://docs.adyen.com/payments-fundamentals/psd2-sca-compliance-and-implementation-guide#specifypreferenceinyourapirequest>`__
    that Adyen requested for the payment.

     Possible values:
    * **lowValue**
    * **secureCorporate**
    * **trustedBeneficiary**
    * **transactionRiskAnalysis**"""

    threeds2_card_enrolled: Optional[bool] = Field(default=UNSET, alias="threeds2.cardEnrolled")
    """Indicates whether a card is enrolled for 3D Secure 2."""


class ResponseAdditionalData3DsecureDict(TypedDict):
    card_holder_info: NotRequired[str]
    cavv: NotRequired[str]
    cavv_algorithm: NotRequired[str]
    sca_exemption_requested: NotRequired[str]
    threeds2_card_enrolled: NotRequired[bool]
