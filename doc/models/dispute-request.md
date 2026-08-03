
# Dispute Request

*This model accepts additional fields of type Any.*

## Structure

`DisputeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Your description for the dispute.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `disputed_amount` | [`DisputedAmount`](../../doc/models/disputed-amount.md) | Optional | - |
| `duplicate_info` | [`DuplicateInfo`](../../doc/models/duplicate-info.md) | Optional | - |
| `fraud_info` | [`FraudInfo`](../../doc/models/fraud-info.md) | Optional | - |
| `not_delivered_info` | [`NotDeliveredInfo`](../../doc/models/not-delivered-info.md) | Optional | - |
| `other_info` | [`OtherInfo`](../../doc/models/other-info.md) | Optional | - |
| `status` | [`DisputeStatus1`](../../doc/models/dispute-status-1.md) | Optional | - |
| `transaction_id` | `str` | Required | The unique reference of the transaction for which you are raising the dispute.<br><br>**Constraints**: *Minimum Length*: `1` |
| `mtype` | `str` | Required | The type of the dispute.<br><br>Possible values: **duplicate**, **fraud**, **notDelivered**, **other**.<br><br>**Note:** The **other** dispute `type` is currently in beta testing. Do not create or submit any disputes for this dispute `type` at this time. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.dispute_request import DisputeRequest
from adyen.models.disputed_amount import DisputedAmount
from adyen.models.duplicate_info import DuplicateInfo
from adyen.models.fraud_info import FraudInfo
from adyen.models.not_delivered_info import NotDeliveredInfo
from adyen.models.product_type_2 import ProductType2

dispute_request = DisputeRequest(
    transaction_id='transactionId6',
    mtype='type4',
    description='description4',
    disputed_amount=DisputedAmount(
        currency='currency0',
        value=162,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    duplicate_info=DuplicateInfo(
        duplicate_transaction_id='duplicateTransactionId4',
        same_card=False,
        same_issuer=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    fraud_info=FraudInfo(
        card_does_not_belong_to_cardholder=False,
        card_was_counterfeited=False,
        description_of_issue='descriptionOfIssue2',
        report_only=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    not_delivered_info=NotDeliveredInfo(
        description_of_issue='descriptionOfIssue6',
        last_expected_date=dateutil.parser.parse('2016-03-13').date(),
        what_was_not_delivered=ProductType2.GOODS,
        agreed_delivery_location='agreedDeliveryLocation4',
        date_of_cancellation=dateutil.parser.parse('2016-03-13').date(),
        delivered_to_wrong_location=False,
        did_cardholder_return=False,
        is_delivery_late=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

