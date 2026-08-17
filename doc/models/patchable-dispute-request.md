
# Patchable Dispute Request

## Structure

`PatchableDisputeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `duplicate_info` | [PatchableDuplicateInfo](../../doc/models/patchable-duplicate-info.md) \| None | Optional | This is a container for one-of cases. |
| `fraud_info` | [PatchableFraudInfo](../../doc/models/patchable-fraud-info.md) \| None | Optional | This is a container for one-of cases. |
| `not_delivered_info` | [PatchableNotDeliveredInfo](../../doc/models/patchable-not-delivered-info.md) \| None | Optional | This is a container for one-of cases. |
| `other_info` | [PatchableOtherInfo](../../doc/models/patchable-other-info.md) \| None | Optional | This is a container for one-of cases. |
| `status` | [DisputeStatus](../../doc/models/dispute-status-enum.md) \| None | Optional | This is a container for one-of cases. |

## Example

```python
import dateutil.parser

from adyen.models.dispute_status_enum import DisputeStatusEnum
from adyen.models.patchable_dispute_request import PatchableDisputeRequest
from adyen.models.patchable_duplicate_info import PatchableDuplicateInfo
from adyen.models.patchable_fraud_info import PatchableFraudInfo
from adyen.models.patchable_not_delivered_info import PatchableNotDeliveredInfo
from adyen.models.patchable_other_info import PatchableOtherInfo
from adyen.models.product_type_11_enum import ProductType11Enum
from adyen.models.sub_type_11_enum import SubType11Enum

patchable_dispute_request = PatchableDisputeRequest(
    duplicate_info=PatchableDuplicateInfo(
        duplicate_transaction_id='duplicateTransactionId6',
        same_card=False,
        same_issuer=False
    ),
    fraud_info=PatchableFraudInfo(
        card_does_not_belong_to_cardholder=False,
        card_was_counterfeited=False,
        description_of_issue='descriptionOfIssue6',
        report_only=False
    ),
    not_delivered_info=PatchableNotDeliveredInfo(
        agreed_delivery_location='agreedDeliveryLocation2',
        date_of_cancellation=dateutil.parser.parse('2016-03-13').date(),
        delivered_to_wrong_location=False,
        description_of_issue='descriptionOfIssue2',
        did_cardholder_return=False
    ),
    other_info=PatchableOtherInfo(
        description_of_issue='descriptionOfIssue6',
        sub_type=SubType11Enum.COUNTERFEIT,
        what_was_purchased=ProductType11Enum.GOODS
    ),
    status=DisputeStatusEnum.CLOSED
)
```

