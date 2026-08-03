
# Payments App Response

*This model accepts additional fields of type Any.*

## Structure

`PaymentsAppResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payments_apps` | [`List[PaymentsAppDto]`](../../doc/models/payments-app-dto.md) | Required | List of Payments Apps. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payments_app_dto import PaymentsAppDto
from adyen.models.payments_app_response import PaymentsAppResponse

payments_app_response = PaymentsAppResponse(
    payments_apps=[
        PaymentsAppDto(
            installation_id='installationId8',
            merchant_account_code='merchantAccountCode4',
            status='status4',
            merchant_store_code='merchantStoreCode4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

