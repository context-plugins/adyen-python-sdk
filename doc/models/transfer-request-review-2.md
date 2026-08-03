
# Transfer Request Review 2

Contains information required for triggering transfer reviews.

*This model accepts additional fields of type Any.*

## Structure

`TransferRequestReview2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number_of_approvals_required` | `int` | Optional | Specifies the number of [approvals](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers/approve) required to process the transfer. |
| `sca_on_approval` | `bool` | Optional | Specifies whether you will initiate Strong Customer Authentication (SCA) in thePOST [/transfers/approve](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers/approve) request.<br><br>Only applies to transfers made with an Adyen [business account](https://docs.adyen.com/platforms/business-accounts). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.transfer_request_review_2 import TransferRequestReview2

transfer_request_review_2 = TransferRequestReview2(
    number_of_approvals_required=244,
    sca_on_approval=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

