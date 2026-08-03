
# Payment Details Request

*This model accepts additional fields of type Any.*

## Structure

`PaymentDetailsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `method` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_details_request import PaymentDetailsRequest

payment_details_request = PaymentDetailsRequest(
    method='PaymentDetailsRequest',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

