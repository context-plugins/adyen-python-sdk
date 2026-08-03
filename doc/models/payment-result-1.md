
# Payment Result 1

*This model accepts additional fields of type Any.*

## Structure

`PaymentResult1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_type` | [`PaymentType1`](../../doc/models/payment-type-1.md) | Optional | - |
| `payment_instrument_data` | [`PaymentInstrumentData2`](../../doc/models/payment-instrument-data-2.md) | Optional | - |
| `amounts_resp` | [`AmountsResp`](../../doc/models/amounts-resp.md) | Optional | - |
| `instalment` | [`Instalment`](../../doc/models/instalment.md) | Optional | - |
| `currency_conversion` | [`List[CurrencyConversion]`](../../doc/models/currency-conversion.md) | Optional | Information related to a currency conversion. A currency conversion occurred in the payment, and the merchant needs to know information related to this conversion (e.g. to print on the sale receipt). |
| `merchant_override_flag` | `bool` | Optional | Indicates that the Merchant forced the result of the payment to successful. Allows the Sale System to be sure that the payment has been forced.<br><br>**Default**: `False` |
| `captured_signature` | [`CapturedSignature`](../../doc/models/captured-signature.md) | Optional | - |
| `protected_signature` | `str` | Optional | Numeric value of a handwritten signature. Contains the value of a handwritten signature, e.g. the signature of a cardholder on the merchant payment receipt. The format before encryption is the encoded data structure CapturedSignature. The data structure before encryption includes the start and end tags for an XML encoding, the identifier and length bytes for an ASN.1 encoding, and the complete member ProtectedSignature for a JSON encoding. |
| `customer_language` | `str` | Optional | The language of the customer that was used on the terminal screen or in text printed by the terminal. Format: two-character [ISO 639:2023](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.<br><br>**Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `online_flag` | `bool` | Optional | Indicate that the payment transaction processing has required the approval of a host. Allows the Sale System to know if the payment was online or offline.<br><br>**Default**: `True` |
| `authentication_method` | [`List[AuthenticationMethod1]`](../../doc/models/authentication-method-1.md) | Optional | Method for customer authentication. Allows the Sale System informed about customer authentication for the payment transaction.<br>Possible values:<br><br>* **Bypass**<br>* **ManualVerification**<br>* **MerchantAuthentication**<br>* **OfflinePIN**<br>* **OnlinePIN**<br>* **PaperSignature**<br>* **SecureCertificate**<br>* **SecureNoCertificate**<br>* **SecuredChannel**<br>* **SignatureCapture**<br>* **UnknownMethod** |
| `validity_date` | `date` | Optional | End of the validity period for the reservation, for the first reservation, and the reservation updates as well. |
| `payment_acquirer_data` | [`PaymentAcquirerData1`](../../doc/models/payment-acquirer-data-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amounts_resp import AmountsResp
from adyen.models.card_data_2 import CardData2
from adyen.models.check_data_2 import CheckData2
from adyen.models.converted_amount import ConvertedAmount
from adyen.models.currency_conversion import CurrencyConversion
from adyen.models.entry_mode import EntryMode
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation import Geolocation
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.instalment import Instalment
from adyen.models.instalment_type import InstalmentType
from adyen.models.mobile_data_2 import MobileData2
from adyen.models.payment_instrument_data_2 import PaymentInstrumentData2
from adyen.models.payment_instrument_type_11 import PaymentInstrumentType11
from adyen.models.payment_result_1 import PaymentResult1
from adyen.models.payment_type_1 import PaymentType1
from adyen.models.period_unit_1 import PeriodUnit1
from adyen.models.stored_value_account_id_2 import StoredValueAccountId2
from adyen.models.stored_value_account_type_1 import StoredValueAccountType1
from adyen.models.track_data_2 import TrackData2
from adyen.models.track_format_1 import TrackFormat1
from adyen.models.utm_coordinates import UtmCoordinates

payment_result_1 = PaymentResult1(
    payment_type=PaymentType1.RECURRING,
    payment_instrument_data=PaymentInstrumentData2(
        payment_instrument_type=PaymentInstrumentType11.CASH,
        protected_card_data='ProtectedCardData8',
        card_data=CardData2(
            payment_brand='PaymentBrand0',
            masked_pan='MaskedPan0',
            payment_account_ref='PaymentAccountRef8',
            entry_mode=[
                EntryMode.MANUAL,
                EntryMode.KEYED
            ],
            card_country_code=3,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        check_data=CheckData2(
            bank_id='BankID0',
            account_number='AccountNumber6',
            check_number='CheckNumber2',
            track_data=TrackData2(
                track_value='TrackValue6',
                track_numb=3,
                track_format=TrackFormat1.JISII,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            check_card_number='CheckCardNumber6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        mobile_data=MobileData2(
            mobile_country_code=3,
            mobile_network_code=3,
            masked_msisdn=22,
            geolocation=Geolocation(
                geographic_coordinates=GeographicCoordinates(
                    latitude='Latitude4',
                    longitude='Longitude2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                utm_coordinates=UtmCoordinates(
                    utm_zone='UTMZone6',
                    utm_eastward='UTMEastward0',
                    utm_northward='UTMNorthward0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            protected_mobile_data='ProtectedMobileData0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        stored_value_account_id=StoredValueAccountId2(
            stored_value_account_type=StoredValueAccountType1.PHONECARD,
            entry_mode=[
                EntryMode.MAGSTRIPE,
                EntryMode.SCANNED
            ],
            identification_type=IdentificationType11.PHONENUMBER,
            stored_value_id='StoredValueID8',
            stored_value_provider='StoredValueProvider4',
            owner_name='OwnerName0',
            expiry_date=4,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    amounts_resp=AmountsResp(
        authorized_amount=133.28,
        currency='Currency0',
        total_rebates_amount=120.04,
        total_fees_amount=181.08,
        cash_back_amount=206.58,
        tip_amount=86.96,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    instalment=Instalment(
        instalment_type=InstalmentType.DEFERREDINSTALMENTS,
        sequence_number=106,
        plan_id='PlanID4',
        period=70,
        period_unit=PeriodUnit1.MONTHLY,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    currency_conversion=[
        CurrencyConversion(
            converted_amount=ConvertedAmount(
                amount_value=81.82,
                currency='Currency0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            customer_approved_flag=False,
            rate=175.8,
            markup=100.86,
            commission=197.78,
            declaration='Declaration4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CurrencyConversion(
            converted_amount=ConvertedAmount(
                amount_value=81.82,
                currency='Currency0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            customer_approved_flag=False,
            rate=175.8,
            markup=100.86,
            commission=197.78,
            declaration='Declaration4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CurrencyConversion(
            converted_amount=ConvertedAmount(
                amount_value=81.82,
                currency='Currency0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            customer_approved_flag=False,
            rate=175.8,
            markup=100.86,
            commission=197.78,
            declaration='Declaration4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    merchant_override_flag=False,
    online_flag=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

