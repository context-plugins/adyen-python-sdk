
# Payment Method Upi Apps

*This model accepts additional fields of type Any.*

## Structure

`PaymentMethodUpiApps`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_identifier_info` | [`AppIdentifierInfo`](../../doc/models/app-identifier-info.md) | Optional | - |
| `id` | `str` | Required | The unique identifier of this app, to submit in requests to /payments. |
| `name` | `str` | Required | A localized name of the app. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.app_identifier_info import AppIdentifierInfo
from adyen.models.payment_method_upi_apps import PaymentMethodUpiApps

payment_method_upi_apps = PaymentMethodUpiApps(
    id='id0',
    name='name0',
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
```

