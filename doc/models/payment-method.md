
# Payment Method

*This model accepts additional fields of type Any.*

## Structure

`PaymentMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apps` | [`List[PaymentMethodUpiApps]`](../../doc/models/payment-method-upi-apps.md) | Optional | A list of apps for this payment method. |
| `brand` | `str` | Optional | Brand for the selected gift card. For example: plastix, hmclub. |
| `brands` | `List[str]` | Optional | List of possible brands. For example: visa, mc. |
| `configuration` | `Dict[str, str]` | Optional | The configuration of the payment method. |
| `funding_source` | [`FundingSource`](../../doc/models/funding-source.md) | Optional | - |
| `group` | [`PaymentMethodGroup`](../../doc/models/payment-method-group.md) | Optional | - |
| `input_details` | [`List[InputDetail]`](../../doc/models/input-detail.md) | Optional | All input details to be provided to complete the payment with this payment method. |
| `issuers` | [`List[PaymentMethodIssuer]`](../../doc/models/payment-method-issuer.md) | Optional | A list of issuers for this payment method. |
| `name` | `str` | Optional | The displayable name of this payment method. |
| `promoted` | `bool` | Optional | Indicates whether this payment method should be promoted or not. |
| `mtype` | `str` | Optional | The unique payment method code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.app_identifier_info import AppIdentifierInfo
from adyen.models.funding_source import FundingSource
from adyen.models.payment_method import PaymentMethod
from adyen.models.payment_method_upi_apps import PaymentMethodUpiApps

payment_method = PaymentMethod(
    apps=[
        PaymentMethodUpiApps(
            id='id6',
            name='name6',
            app_identifier_info=AppIdentifierInfo(
                android_package_id='androidPackageId8',
                ios_scheme='iosScheme8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        PaymentMethodUpiApps(
            id='id6',
            name='name6',
            app_identifier_info=AppIdentifierInfo(
                android_package_id='androidPackageId8',
                ios_scheme='iosScheme8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
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
    funding_source=FundingSource.PREPAID,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

