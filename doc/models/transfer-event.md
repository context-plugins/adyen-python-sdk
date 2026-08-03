
# Transfer Event

*This model accepts additional fields of type Any.*

## Structure

`TransferEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Optional | - |
| `amount_adjustments` | [`List[AmountAdjustment]`](../../doc/models/amount-adjustment.md) | Optional | The amount adjustments in this transfer. Only applicable for [issuing](https://docs.adyen.com/issuing/) integrations. |
| `arn` | `str` | Optional | Scheme unique arn identifier useful for tracing captures, chargebacks, refunds, etc. |
| `booking_date` | `datetime` | Optional | The date when the transfer request was sent. |
| `estimated_arrival_time` | `datetime` | Optional | The estimated time when the beneficiary should have access to the funds. |
| `events_data` | List[[InterchangeData](../../doc/models/interchange-data.md) \| [IssuingTransactionData](../../doc/models/issuing-transaction-data.md) \| [MerchantPurchaseData](../../doc/models/merchant-purchase-data.md)] \| None | Optional | This is List of a container for one-of cases. |
| `external_reason` | [`ExternalReason`](../../doc/models/external-reason.md) | Optional | - |
| `id` | `str` | Optional | The unique identifier of the transfer event. |
| `modification` | [`Modification`](../../doc/models/modification.md) | Optional | - |
| `mutations` | [`List[BalanceMutation]`](../../doc/models/balance-mutation.md) | Optional | The list of balance mutations per event. |
| `original_amount` | [`OriginalAmount`](../../doc/models/original-amount.md) | Optional | - |
| `reason` | [`Reason2`](../../doc/models/reason-2.md) | Optional | - |
| `status` | [`Status25`](../../doc/models/status-25.md) | Optional | - |
| `tracing_data` | [UKFpsTracingData](../../doc/models/uk-fps-tracing-data.md) \| [USAchTracingData](../../doc/models/us-ach-tracing-data.md) \| None | Optional | This is a container for one-of cases. |
| `tracking_data` | [ConfirmationTrackingData](../../doc/models/confirmation-tracking-data.md) \| [EstimationTrackingData](../../doc/models/estimation-tracking-data.md) \| [InternalReviewTrackingData](../../doc/models/internal-review-tracking-data.md) \| None | Optional | This is a container for one-of cases. |
| `transaction_id` | `str` | Optional | The id of the transaction that is related to this accounting event. Only sent for events of type **accounting** where the balance changes. |
| `mtype` | [`Type74`](../../doc/models/type-74.md) | Optional | - |
| `update_date` | `datetime` | Optional | The date when the tracking status was updated. |
| `value_date` | `datetime` | Optional | The date when the funds are expected to be deducted from or credited to the balance account. This date can be in either the past or future. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.amount_adjustment import AmountAdjustment
from adyen.models.amount_adjustment_type import AmountAdjustmentType
from adyen.models.transfer_event import TransferEvent

transfer_event = TransferEvent(
    amount=Amount5(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    amount_adjustments=[
        AmountAdjustment(
            amount=Amount5(
                currency='currency2',
                value=110,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            amount_adjustment_type=AmountAdjustmentType.ATMMARKUP,
            basepoints=170,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AmountAdjustment(
            amount=Amount5(
                currency='currency2',
                value=110,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            amount_adjustment_type=AmountAdjustmentType.ATMMARKUP,
            basepoints=170,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AmountAdjustment(
            amount=Amount5(
                currency='currency2',
                value=110,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            amount_adjustment_type=AmountAdjustmentType.ATMMARKUP,
            basepoints=170,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    arn='arn0',
    booking_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    estimated_arrival_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

