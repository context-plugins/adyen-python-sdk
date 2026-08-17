
# Payment Method

## Structure

`PaymentMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apps` | [`List[PaymentMethodUPIApps]`](../../doc/models/payment-method-upi-apps.md) | Optional | A list of apps for this payment method. |
| `brand` | `str` | Optional | Brand for the selected gift card. For example: plastix, hmclub. |
| `brands` | `List[str]` | Optional | List of possible brands. For example: visa, mc. |
| `configuration` | `Dict[str, str]` | Optional | The configuration of the payment method. |
| `funding_source` | [`FundingSource9Enum`](../../doc/models/funding-source-9-enum.md) | Optional | The funding source of the payment method. |
| `group` | [`PaymentMethodGroup2`](../../doc/models/payment-method-group-2.md) | Optional | The group where this payment method belongs to. |
| `input_details` | [`List[InputDetail]`](../../doc/models/input-detail.md) | Optional | All input details to be provided to complete the payment with this payment method. |
| `issuers` | [`List[PaymentMethodIssuer]`](../../doc/models/payment-method-issuer.md) | Optional | A list of issuers for this payment method. |
| `name` | `str` | Optional | The displayable name of this payment method. |
| `promoted` | `bool` | Optional | Indicates whether this payment method should be promoted or not. |
| `mtype` | `str` | Optional | The unique payment method code. |

## Example

```python
from adyen.models.app_identifier_info_1 import AppIdentifierInfo1
from adyen.models.funding_source_9_enum import FundingSource9Enum
from adyen.models.payment_method import PaymentMethod
from adyen.models.payment_method_upi_apps import PaymentMethodUPIApps

payment_method = PaymentMethod(
    apps=[
        PaymentMethodUPIApps(
            id='id6',
            name='name6',
            app_identifier_info=AppIdentifierInfo1(
                android_package_id='androidPackageId8',
                ios_scheme='iosScheme8'
            )
        ),
        PaymentMethodUPIApps(
            id='id6',
            name='name6',
            app_identifier_info=AppIdentifierInfo1(
                android_package_id='androidPackageId8',
                ios_scheme='iosScheme8'
            )
        )
    ],
    brand='brand4',
    brands=[
        'brands1'
    ],
    configuration={
        'key0': 'configuration6',
        'key1': 'configuration7',
        'key2': 'configuration8'
    },
    funding_source=FundingSource9Enum.PREPAID
)
```

