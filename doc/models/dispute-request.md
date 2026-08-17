
# Dispute Request

## Structure

`DisputeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Your description for the dispute.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `disputed_amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The amount for which you dispute the transaction. The disputed amount cannot be greater than the transaction amount. If you do not provide an amount, the entire transaction amount will be disputed. |
| `duplicate_info` | [`DuplicateInfo1`](../../doc/models/duplicate-info-1.md) | Optional | Additional information for raising a dispute of `type` **duplicate**. Required for disputes of `type` **duplicate**. |
| `fraud_info` | [`FraudInfo1`](../../doc/models/fraud-info-1.md) | Optional | Additional information for raising a dispute of `type` **fraud**. Required for disputes of `type` **fraud**. |
| `not_delivered_info` | [`NotDeliveredInfo1`](../../doc/models/not-delivered-info-1.md) | Optional | Additional information for raising a dispute of `type` **notDelivered**. Required for disputes of `type` **notDelivered**. |
| `other_info` | [`OtherInfo3`](../../doc/models/other-info-3.md) | Optional | Additional information for raising a dispute of `type` **other**. Required for disputes of `type` **other**.<br><br>**Note:** The **other** dispute `type` is currently in beta testing. Do not create or submit any disputes for this dispute `type` at this time. |
| `status` | [`DisputeStatus1Enum`](../../doc/models/dispute-status-1-enum.md) | Optional | The current status of the dispute.<br><br>When you create a dispute, you can only set the `status` to **draft**. When you update a dispute, you can set the `status` to **submitted** or **closed**.<br><br>Possible values: **draft**, **submitted**, **closed**, **won**, **chargeback**, **secondPresentment**. |
| `transaction_id` | `str` | Required | The unique reference of the transaction for which you are raising the dispute.<br><br>**Constraints**: *Minimum Length*: `1` |
| `mtype` | `str` | Required | The type of the dispute.<br><br>Possible values: **duplicate**, **fraud**, **notDelivered**, **other**.<br><br>**Note:** The **other** dispute `type` is currently in beta testing. Do not create or submit any disputes for this dispute `type` at this time. |

## Example

```python
import dateutil.parser

from adyen.models.amount_17 import Amount17
from adyen.models.dispute_request import DisputeRequest
from adyen.models.duplicate_info_1 import DuplicateInfo1
from adyen.models.fraud_info_1 import FraudInfo1
from adyen.models.not_delivered_info_1 import NotDeliveredInfo1
from adyen.models.product_type_21_enum import ProductType21Enum

dispute_request = DisputeRequest(
    transaction_id='transactionId6',
    mtype='type4',
    description='description4',
    disputed_amount=Amount17(
        currency='currency0',
        value=162
    ),
    duplicate_info=DuplicateInfo1(
        duplicate_transaction_id='duplicateTransactionId4',
        same_card=False,
        same_issuer=False
    ),
    fraud_info=FraudInfo1(
        card_does_not_belong_to_cardholder=False,
        card_was_counterfeited=False,
        description_of_issue='descriptionOfIssue2',
        report_only=False
    ),
    not_delivered_info=NotDeliveredInfo1(
        description_of_issue='descriptionOfIssue6',
        last_expected_date=dateutil.parser.parse('2016-03-13').date(),
        what_was_not_delivered=ProductType21Enum.GOODS,
        agreed_delivery_location='agreedDeliveryLocation4',
        date_of_cancellation=dateutil.parser.parse('2016-03-13').date(),
        delivered_to_wrong_location=False,
        did_cardholder_return=False,
        is_delivery_late=False
    )
)
```

