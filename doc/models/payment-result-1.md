
# Payment Result 1

## Structure

`PaymentResult1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_type` | [`PaymentType1Enum`](../../doc/models/payment-type-1-enum.md) | Optional | Type of payment transaction. Elements requested by the Sale System that are related to the payment only.<br>Possible values:<br><br>* **CashAdvance**<br>* **CashDeposit**<br>* **Completion**<br>* **FirstReservation**<br>* **Instalment**<br>* **IssuerInstalment**<br>* **Normal**<br>* **OneTimeReservation**<br>* **PaidOut**<br>* **Recurring**<br>* **Refund**<br>* **UpdateReservation** |
| `payment_instrument_data` | [`PaymentInstrumentData`](../../doc/models/payment-instrument-data.md) | Optional | Data related to the instrument of payment for the transaction.<br>Sent in the result of the payment transaction. For a card, it could also be sent in the `CardAcquisition` response, to be processed by the Sale System. |
| `amounts_resp` | [`AmountsResp1`](../../doc/models/amounts-resp-1.md) | Optional | Various amounts related to the payment response from the POI System. Amounts approved by the POI and the Acquirer for the payment and loyalty transaction, containing:<br><br>* The authorised amount to be paid.<br>* The amount of the rebates.<br>* The amount of financial fees.<br>* The cash back part of the requested amount for a payment with cash back.<br>* The tip part of the requested amount for a payment with tip. |
| `instalment` | [`Instalment1`](../../doc/models/instalment-1.md) | Optional | Information related an instalment transaction. To request an instalment to the issuer, or to make individual instalments of a payment transaction. |
| `currency_conversion` | [`List[CurrencyConversion]`](../../doc/models/currency-conversion.md) | Optional | Information related to a currency conversion. A currency conversion occurred in the payment, and the merchant needs to know information related to this conversion (e.g. to print on the sale receipt). |
| `merchant_override_flag` | `bool` | Optional | Indicates that the Merchant forced the result of the payment to successful. Allows the Sale System to be sure that the payment has been forced.<br><br>**Default**: `False` |
| `captured_signature` | [`CapturedSignature1`](../../doc/models/captured-signature-1.md) | Optional | Numeric value of a handwritten signature. Contains the value of a handwritten signature, e.g. the signature of a cardholder on the merchant payment receipt. Only one format of the signature is allowed:<br><br>* The size of the pad area where the signature is written, given with the maximum abscissa and ordinate values.<br>* The sequence of coordinates where the pen changes direction or lift. |
| `protected_signature` | `str` | Optional | Numeric value of a handwritten signature. Contains the value of a handwritten signature, e.g. the signature of a cardholder on the merchant payment receipt. The format before encryption is the encoded data structure CapturedSignature. The data structure before encryption includes the start and end tags for an XML encoding, the identifier and length bytes for an ASN.1 encoding, and the complete member ProtectedSignature for a JSON encoding. |
| `customer_language` | `str` | Optional | The language of the customer that was used on the terminal screen or in text printed by the terminal. Format: two-character [ISO 639:2023](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.<br><br>**Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `online_flag` | `bool` | Optional | Indicate that the payment transaction processing has required the approval of a host. Allows the Sale System to know if the payment was online or offline.<br><br>**Default**: `True` |
| `authentication_method` | [`List[AuthenticationMethod1Enum]`](../../doc/models/authentication-method-1-enum.md) | Optional | Method for customer authentication. Allows the Sale System informed about customer authentication for the payment transaction.<br>Possible values:<br><br>* **Bypass**<br>* **ManualVerification**<br>* **MerchantAuthentication**<br>* **OfflinePIN**<br>* **OnlinePIN**<br>* **PaperSignature**<br>* **SecureCertificate**<br>* **SecureNoCertificate**<br>* **SecuredChannel**<br>* **SignatureCapture**<br>* **UnknownMethod** |
| `validity_date` | `date` | Optional | End of the validity period for the reservation, for the first reservation, and the reservation updates as well. |
| `payment_acquirer_data` | [`PaymentAcquirerData`](../../doc/models/payment-acquirer-data.md) | Optional | Data related to the response from the payment Acquirer. |

## Example

```python
from adyen.models.amounts_resp_1 import AmountsResp1
from adyen.models.card_data_1 import CardData1
from adyen.models.check_data_1 import CheckData1
from adyen.models.converted_amount_1 import ConvertedAmount1
from adyen.models.currency_conversion import CurrencyConversion
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation_1 import Geolocation1
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.instalment_1 import Instalment1
from adyen.models.instalment_type_enum import InstalmentTypeEnum
from adyen.models.mobile_data_1 import MobileData1
from adyen.models.payment_instrument_data import PaymentInstrumentData
from adyen.models.payment_instrument_type_11_enum import PaymentInstrumentType11Enum
from adyen.models.payment_result_1 import PaymentResult1
from adyen.models.payment_type_1_enum import PaymentType1Enum
from adyen.models.period_unit_1_enum import PeriodUnit1Enum
from adyen.models.stored_value_account_id import StoredValueAccountID
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum
from adyen.models.track_data_1 import TrackData1
from adyen.models.track_format_1_enum import TrackFormat1Enum
from adyen.models.utm_coordinates import UTMCoordinates

payment_result_1 = PaymentResult1(
    payment_type=PaymentType1Enum.RECURRING,
    payment_instrument_data=PaymentInstrumentData(
        payment_instrument_type=PaymentInstrumentType11Enum.CASH,
        protected_card_data='ProtectedCardData8',
        card_data=CardData1(
            payment_brand='PaymentBrand0',
            masked_pan='MaskedPan0',
            payment_account_ref='PaymentAccountRef8',
            entry_mode=[
                EntryModeEnum.MANUAL,
                EntryModeEnum.KEYED
            ],
            card_country_code=3
        ),
        check_data=CheckData1(
            bank_id='BankID0',
            account_number='AccountNumber6',
            check_number='CheckNumber2',
            track_data=TrackData1(
                track_value='TrackValue6',
                track_numb=3,
                track_format=TrackFormat1Enum.JISII
            ),
            check_card_number='CheckCardNumber6'
        ),
        mobile_data=MobileData1(
            mobile_country_code=3,
            mobile_network_code=3,
            masked_msisdn=22,
            geolocation=Geolocation1(
                geographic_coordinates=GeographicCoordinates(
                    latitude='Latitude4',
                    longitude='Longitude2'
                ),
                utm_coordinates=UTMCoordinates(
                    utm_zone='UTMZone6',
                    utm_eastward='UTMEastward0',
                    utm_northward='UTMNorthward0'
                )
            ),
            protected_mobile_data='ProtectedMobileData0'
        ),
        stored_value_account_id=StoredValueAccountID(
            stored_value_account_type=StoredValueAccountType1Enum.PHONECARD,
            entry_mode=[
                EntryModeEnum.MAGSTRIPE,
                EntryModeEnum.SCANNED
            ],
            identification_type=IdentificationType11Enum.PHONENUMBER,
            stored_value_id='StoredValueID8',
            stored_value_provider='StoredValueProvider4',
            owner_name='OwnerName0',
            expiry_date=4
        )
    ),
    amounts_resp=AmountsResp1(
        authorized_amount=133.28,
        currency='Currency0',
        total_rebates_amount=120.04,
        total_fees_amount=181.08,
        cash_back_amount=206.58,
        tip_amount=86.96
    ),
    instalment=Instalment1(
        instalment_type=InstalmentTypeEnum.DEFERREDINSTALMENTS,
        sequence_number=106,
        plan_id='PlanID4',
        period=70,
        period_unit=PeriodUnit1Enum.MONTHLY
    ),
    currency_conversion=[
        CurrencyConversion(
            converted_amount=ConvertedAmount1(
                amount_value=81.82,
                currency='Currency0'
            ),
            customer_approved_flag=False,
            rate=175.8,
            markup=100.86,
            commission=197.78,
            declaration='Declaration4'
        ),
        CurrencyConversion(
            converted_amount=ConvertedAmount1(
                amount_value=81.82,
                currency='Currency0'
            ),
            customer_approved_flag=False,
            rate=175.8,
            markup=100.86,
            commission=197.78,
            declaration='Declaration4'
        ),
        CurrencyConversion(
            converted_amount=ConvertedAmount1(
                amount_value=81.82,
                currency='Currency0'
            ),
            customer_approved_flag=False,
            rate=175.8,
            markup=100.86,
            commission=197.78,
            declaration='Declaration4'
        )
    ],
    merchant_override_flag=False,
    online_flag=True
)
```

