
# Payments App Dto

*This model accepts additional fields of type Any.*

## Structure

`PaymentsAppDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `installation_id` | `str` | Required | The unique identifier of the Payments App instance. |
| `merchant_account_code` | `str` | Required | The account code associated with the Payments App instance. |
| `merchant_store_code` | `str` | Optional | The store code associated with the Payments App instance. |
| `status` | `str` | Required | The status of the Payments App instance. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payments_app_dto import PaymentsAppDto

payments_app_dto = PaymentsAppDto(
    installation_id='installationId6',
    merchant_account_code='merchantAccountCode2',
    status='status2',
    merchant_store_code='merchantStoreCode2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

