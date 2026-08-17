
# Transfer Event

## Structure

`TransferEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The original journal amount. Only applicable for [issuing](https://docs.adyen.com/issuing/) integrations. |
| `amount_adjustments` | [`List[AmountAdjustment]`](../../doc/models/amount-adjustment.md) | Optional | The amount adjustments in this transfer. Only applicable for [issuing](https://docs.adyen.com/issuing/) integrations. |
| `arn` | `str` | Optional | Scheme unique arn identifier useful for tracing captures, chargebacks, refunds, etc. |
| `booking_date` | `datetime` | Optional | The date when the transfer request was sent. |
| `estimated_arrival_time` | `datetime` | Optional | The estimated time when the beneficiary should have access to the funds. |
| `events_data` | List[[InterchangeData](../../doc/models/interchange-data.md) \| [IssuingTransactionData](../../doc/models/issuing-transaction-data.md) \| [MerchantPurchaseData](../../doc/models/merchant-purchase-data.md)] \| None | Optional | This is List of a container for one-of cases. |
| `external_reason` | [`ExternalReason1`](../../doc/models/external-reason-1.md) | Optional | The external reason for the transfer status. |
| `id` | `str` | Optional | The unique identifier of the transfer event. |
| `modification` | [`Modification2`](../../doc/models/modification-2.md) | Optional | The payment modification. Only applicable for [returned internal transfers](https://docs.adyen.com/platforms/internal-fund-transfers/internal-transfer-webhooks/#returned-internal-transfer). |
| `mutations` | [`List[BalanceMutation]`](../../doc/models/balance-mutation.md) | Optional | The list of balance mutations per event. |
| `original_amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The amount in the original currency. Only applicable for [issuing](https://docs.adyen.com/issuing/) integrations. |
| `reason` | [`Reason1Enum`](../../doc/models/reason-1-enum.md) | Optional | The reason for the transfer status. |
| `status` | [`Status24Enum`](../../doc/models/status-24-enum.md) | Optional | The status of the transfer event. |
| `tracing_data` | [UKFpsTracingData](../../doc/models/uk-fps-tracing-data.md) \| [USAchTracingData](../../doc/models/us-ach-tracing-data.md) \| None | Optional | This is a container for one-of cases. |
| `tracking_data` | [ConfirmationTrackingData](../../doc/models/confirmation-tracking-data.md) \| [EstimationTrackingData](../../doc/models/estimation-tracking-data.md) \| [InternalReviewTrackingData](../../doc/models/internal-review-tracking-data.md) \| None | Optional | This is a container for one-of cases. |
| `transaction_id` | `str` | Optional | The id of the transaction that is related to this accounting event. Only sent for events of type **accounting** where the balance changes. |
| `mtype` | [`Type73Enum`](../../doc/models/type-73-enum.md) | Optional | The type of the transfer event. Possible values: **accounting**, **tracking**. |
| `update_date` | `datetime` | Optional | The date when the tracking status was updated. |
| `value_date` | `datetime` | Optional | The date when the funds are expected to be deducted from or credited to the balance account. This date can be in either the past or future. |

## Example

```python
import dateutil.parser

from adyen.models.amount_17 import Amount17
from adyen.models.amount_adjustment import AmountAdjustment
from adyen.models.amount_adjustment_type_enum import AmountAdjustmentTypeEnum
from adyen.models.transfer_event import TransferEvent

transfer_event = TransferEvent(
    amount=Amount17(
        currency='currency2',
        value=110
    ),
    amount_adjustments=[
        AmountAdjustment(
            amount=Amount17(
                currency='currency2',
                value=110
            ),
            amount_adjustment_type=AmountAdjustmentTypeEnum.ATMMARKUP,
            basepoints=170
        ),
        AmountAdjustment(
            amount=Amount17(
                currency='currency2',
                value=110
            ),
            amount_adjustment_type=AmountAdjustmentTypeEnum.ATMMARKUP,
            basepoints=170
        ),
        AmountAdjustment(
            amount=Amount17(
                currency='currency2',
                value=110
            ),
            amount_adjustment_type=AmountAdjustmentTypeEnum.ATMMARKUP,
            basepoints=170
        )
    ],
    arn='arn0',
    booking_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    estimated_arrival_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

