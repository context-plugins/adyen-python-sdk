
# Payment Method UPI Apps

## Structure

`PaymentMethodUPIApps`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_identifier_info` | [`AppIdentifierInfo1`](../../doc/models/app-identifier-info-1.md) | Optional | The app identifier information containing iOS scheme and Android package ID. |
| `id` | `str` | Required | The unique identifier of this app, to submit in requests to /payments. |
| `name` | `str` | Required | A localized name of the app. |

## Example

```python
from adyen.models.app_identifier_info_1 import AppIdentifierInfo1
from adyen.models.payment_method_upi_apps import PaymentMethodUPIApps

payment_method_upi_apps = PaymentMethodUPIApps(
    id='id0',
    name='name0',
    app_identifier_info=AppIdentifierInfo1(
        android_package_id='androidPackageId8',
        ios_scheme='iosScheme8'
    )
)
```

