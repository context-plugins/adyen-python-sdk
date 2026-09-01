from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .amounts_resp1 import AmountsResp1, AmountsResp1Dict
from .captured_signature1 import CapturedSignature1, CapturedSignature1Dict
from .currency_conversion import CurrencyConversion, CurrencyConversionDict
from .enums.authentication_method1 import AuthenticationMethod1OrStr
from .enums.payment_type1 import PaymentType1OrStr
from .instalment1 import Instalment1, Instalment1Dict
from .payment_acquirer_data import PaymentAcquirerData, PaymentAcquirerDataDict
from .payment_instrument_data import PaymentInstrumentData, PaymentInstrumentDataDict


class PaymentResult1(SdkBaseModel):
    payment_type: Optional[PaymentType1OrStr] = Field(default=UNSET, alias="PaymentType")
    """Type of payment transaction. Elements requested by the Sale System that are related to the payment only. Possible
    values:
    * **CashAdvance**
    * **CashDeposit**
    * **Completion**
    * **FirstReservation**
    * **Instalment**
    * **IssuerInstalment**
    * **Normal**
    * **OneTimeReservation**
    * **PaidOut**
    * **Recurring**
    * **Refund**
    * **UpdateReservation**"""

    payment_instrument_data: Optional[PaymentInstrumentData] = Field(default=UNSET, alias="PaymentInstrumentData")
    """Data related to the instrument of payment for the transaction. Sent in the result of the payment transaction. For
    a card, it could also be sent in the ``CardAcquisition`` response, to be processed by the Sale System."""

    amounts_resp: Optional[AmountsResp1] = Field(default=UNSET, alias="AmountsResp")
    """Various amounts related to the payment response from the POI System. Amounts approved by the POI and the Acquirer
    for the payment and loyalty transaction, containing:
      * The authorised amount to be paid.
      * The amount of the rebates.
      * The amount of financial fees.
      * The cash back part of the requested amount for a payment with cash back.
      * The tip part of the requested amount for a payment with tip."""

    instalment: Optional[Instalment1] = Field(default=UNSET, alias="Instalment")
    """Information related an instalment transaction. To request an instalment to the issuer, or to make individual
    instalments of a payment transaction."""

    currency_conversion: Optional[list[CurrencyConversion]] = Field(default=UNSET, alias="CurrencyConversion")
    """Information related to a currency conversion. A currency conversion occurred in the payment, and the merchant
    needs to know information related to this conversion (e.g. to print on the sale receipt)."""

    merchant_override_flag: Optional[bool] = Field(default=UNSET, alias="MerchantOverrideFlag")
    """Indicates that the Merchant forced the result of the payment to successful. Allows the Sale System to be sure
    that the payment has been forced."""

    captured_signature: Optional[CapturedSignature1] = Field(default=UNSET, alias="CapturedSignature")
    """Numeric value of a handwritten signature. Contains the value of a handwritten signature, e.g. the signature of a
    cardholder on the merchant payment receipt. Only one format of the signature is allowed:
      * The size of the pad area where the signature is written, given with the maximum abscissa and ordinate values.
      * The sequence of coordinates where the pen changes direction or lift."""

    protected_signature: Optional[str] = Field(default=UNSET, alias="ProtectedSignature")
    """Numeric value of a handwritten signature. Contains the value of a handwritten signature, e.g. the signature of a
    cardholder on the merchant payment receipt. The format before encryption is the encoded data structure
    CapturedSignature. The data structure before encryption includes the start and end tags for an XML encoding, the
    identifier and length bytes for an ASN.1 encoding, and the complete member ProtectedSignature for a JSON
    encoding."""

    customer_language: Optional[str] = Field(default=UNSET, alias="CustomerLanguage")
    """The language of the customer that was used on the terminal screen or in text printed by the terminal. Format:
    two-character `ISO 639:2023 <https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes>`__ format."""

    online_flag: Optional[bool] = Field(default=UNSET, alias="OnlineFlag")
    """Indicate that the payment transaction processing has required the approval of a host. Allows the Sale System to
    know if the payment was online or offline."""

    authentication_method: Optional[list[AuthenticationMethod1OrStr]] = Field(
        default=UNSET, alias="AuthenticationMethod"
    )
    """Method for customer authentication. Allows the Sale System informed about customer authentication for the payment
    transaction. Possible values:
    * **Bypass**
    * **ManualVerification**
    * **MerchantAuthentication**
    * **OfflinePIN**
    * **OnlinePIN**
    * **PaperSignature**
    * **SecureCertificate**
    * **SecureNoCertificate**
    * **SecuredChannel**
    * **SignatureCapture**
    * **UnknownMethod**"""

    validity_date: Optional[Date] = Field(default=UNSET, alias="ValidityDate")
    """End of the validity period for the reservation, for the first reservation, and the reservation updates as
    well."""

    payment_acquirer_data: Optional[PaymentAcquirerData] = Field(default=UNSET, alias="PaymentAcquirerData")
    """Data related to the response from the payment Acquirer."""


class PaymentResult1Dict(TypedDict):
    payment_type: NotRequired[PaymentType1OrStr]
    payment_instrument_data: NotRequired[PaymentInstrumentData | PaymentInstrumentDataDict]
    amounts_resp: NotRequired[AmountsResp1 | AmountsResp1Dict]
    instalment: NotRequired[Instalment1 | Instalment1Dict]
    currency_conversion: NotRequired[list[CurrencyConversion | CurrencyConversionDict]]
    merchant_override_flag: NotRequired[bool]
    captured_signature: NotRequired[CapturedSignature1 | CapturedSignature1Dict]
    protected_signature: NotRequired[str]
    customer_language: NotRequired[str]
    online_flag: NotRequired[bool]
    authentication_method: NotRequired[list[AuthenticationMethod1OrStr]]
    validity_date: NotRequired[Date]
    payment_acquirer_data: NotRequired[PaymentAcquirerData | PaymentAcquirerDataDict]
