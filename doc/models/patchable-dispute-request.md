
# Patchable Dispute Request

*This model accepts additional fields of type Any.*

## Structure

`PatchableDisputeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `duplicate_info` | [PatchableDuplicateInfo](../../doc/models/patchable-duplicate-info.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `fraud_info` | [PatchableFraudInfo](../../doc/models/patchable-fraud-info.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `not_delivered_info` | [PatchableNotDeliveredInfo](../../doc/models/patchable-not-delivered-info.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `other_info` | [PatchableOtherInfo](../../doc/models/patchable-other-info.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `status` | [DisputeStatus](../../doc/models/dispute-status.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.dispute_status import DisputeStatus
from adyen.models.patchable_dispute_request import PatchableDisputeRequest
from adyen.models.patchable_duplicate_info import PatchableDuplicateInfo
from adyen.models.patchable_fraud_info import PatchableFraudInfo
from adyen.models.patchable_not_delivered_info import PatchableNotDeliveredInfo
from adyen.models.patchable_other_info import PatchableOtherInfo
from adyen.models.product_type_1 import ProductType1
from adyen.models.sub_type_11 import SubType11

patchable_dispute_request = PatchableDisputeRequest(
    duplicate_info=PatchableDuplicateInfo(
        duplicate_transaction_id='duplicateTransactionId6',
        same_card=False,
        same_issuer=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    fraud_info=PatchableFraudInfo(
        card_does_not_belong_to_cardholder=False,
        card_was_counterfeited=False,
        description_of_issue='descriptionOfIssue6',
        report_only=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    not_delivered_info=PatchableNotDeliveredInfo(
        agreed_delivery_location='agreedDeliveryLocation2',
        date_of_cancellation=dateutil.parser.parse('2016-03-13').date(),
        delivered_to_wrong_location=False,
        description_of_issue='descriptionOfIssue2',
        did_cardholder_return=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    other_info=PatchableOtherInfo(
        description_of_issue='descriptionOfIssue6',
        sub_type=SubType11.COUNTERFEIT,
        what_was_purchased=ProductType1.GOODS,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    status=DisputeStatus.CLOSED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

