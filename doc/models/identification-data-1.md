
# Identification Data 1

Information about the individual's identification document.

## Structure

`IdentificationData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_number` | `str` | Optional | The card number of the document that was issued (AU only). |
| `expiry_date` | `str` | Optional | The expiry date of the document, in YYYY-MM-DD format. |
| `issuer_country` | `str` | Optional | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the document was issued. For example, **US**. |
| `issuer_state` | `str` | Optional | The state or province where the document was issued (AU only). |
| `national_id_exempt` | `bool` | Optional | Applies only to individuals in the US. Set to **true** if the individual does not have an SSN. To verify their identity, Adyen will require them to upload an ID document. |
| `number` | `str` | Optional | The number in the document. |
| `mtype` | [`Type132Enum`](../../doc/models/type-132-enum.md) | Required | Type of identity data. For individuals, the following types are supported. See our [onboarding guide](https://docs.adyen.com/platforms/onboard-users/onboarding-steps/?onboarding_type=custom) for other supported countries.<br><br>- Australia: **driversLicense**, **passport**<br><br>- Hong Kong: **driversLicense**, **nationalIdNumber**, **passport**<br><br>- New Zealand: **driversLicense**, **passport**<br><br>- Singapore: **driversLicense**, **nationalIdNumber**, **passport**<br><br>- All other supported countries: **nationalIdNumber** |

## Example

```python
from adyen.models.identification_data_1 import IdentificationData1
from adyen.models.type_132_enum import Type132Enum

identification_data_1 = IdentificationData1(
    mtype=Type132Enum.NATIONALIDNUMBER,
    card_number='cardNumber0',
    expiry_date='expiryDate2',
    issuer_country='issuerCountry0',
    issuer_state='issuerState0',
    national_id_exempt=False
)
```

