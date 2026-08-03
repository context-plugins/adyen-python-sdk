
# Update Payment Link Request

*This model accepts additional fields of type Any.*

## Structure

`UpdatePaymentLinkRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`Status28`](../../doc/models/status-28.md) | Required | Status of the payment link. Possible values:<br><br>* **expired** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.status_28 import Status28
from adyen.models.update_payment_link_request import UpdatePaymentLinkRequest

update_payment_link_request = UpdatePaymentLinkRequest(
    status=Status28.EXPIRED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

