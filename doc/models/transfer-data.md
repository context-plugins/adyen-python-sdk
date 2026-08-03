
# Transfer Data

*This model accepts additional fields of type Any.*

## Structure

`TransferData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`ResourceReference`](../../doc/models/resource-reference.md) | Optional | - |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Required | - |
| `balance_account` | [`ResourceReference`](../../doc/models/resource-reference.md) | Optional | - |
| `balance_platform` | `str` | Optional | The unique identifier of the balance platform. |
| `balances` | [`List[BalanceMutation]`](../../doc/models/balance-mutation.md) | Optional | The list of the latest balance statuses in the transfer. |
| `category` | [`Category3`](../../doc/models/category-3.md) | Required | - |
| `category_data` | [BankCategoryData](../../doc/models/bank-category-data.md) \| [InternalCategoryData](../../doc/models/internal-category-data.md) \| [IssuedCard](../../doc/models/issued-card.md) \| [PlatformPayment](../../doc/models/platform-payment.md) \| None | Optional | This is a container for one-of cases. |
| `counterparty` | [`TransferNotificationCounterParty`](../../doc/models/transfer-notification-counter-party.md) | Optional | - |
| `created_at` | `datetime` | Optional | The date and time when the transfer was created, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |
| `creation_date` | `datetime` | Optional | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |
| `description` | `str` | Optional | Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.<br><br>Supported characters: **[a-z] [A-Z] [0-9] / - ?** **: ( ) . , ' + Space**<br><br>Supported characters for **regular** and **fast** transfers to a US counterparty: **[a-z] [A-Z] [0-9] & $ % # @** **~ = + - _ ' " ! ?** |
| `direct_debit_information` | [`DirectDebitInformation`](../../doc/models/direct-debit-information.md) | Optional | - |
| `direction` | [`Direction`](../../doc/models/direction.md) | Optional | - |
| `event_id` | `str` | Optional | The unique identifier of the latest transfer event. Included only when the `category` is **issuedCard**. |
| `events` | [`List[TransferEvent]`](../../doc/models/transfer-event.md) | Optional | The list of events leading up to the current status of the transfer. |
| `execution_date` | [`ExecutionDate`](../../doc/models/execution-date.md) | Optional | - |
| `external_reason` | [`ExternalReason`](../../doc/models/external-reason.md) | Optional | - |
| `id` | `str` | Optional | The ID of the resource. |
| `network_reason` | [`NetworkReason`](../../doc/models/network-reason.md) | Optional | - |
| `payment_instrument` | [`PaymentInstrument2`](../../doc/models/payment-instrument-2.md) | Optional | - |
| `reason` | [`Reason21`](../../doc/models/reason-21.md) | Optional | - |
| `reference` | `str` | Optional | Your reference for the transfer, used internally within your platform. If you don't provide this in the request, Adyen generates a unique reference.<br><br>**Constraints**: *Maximum Length*: `80` |
| `reference_for_beneficiary` | `str` | Optional | A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of funds.<br><br>Supported characters: **a-z**, **A-Z**, **0-9**.The maximum length depends on the `category`.<br><br>- **internal**: 80 characters<br><br>- **bank**: 35 characters when transferring to an IBAN, 15 characters for others. |
| `review` | [`TransferReview`](../../doc/models/transfer-review.md) | Optional | - |
| `sequence_number` | `int` | Optional | The sequence number of the transfer webhook. The numbers start from 1 and increase with each new webhook for a specific transfer.<br><br>The sequence number can help you restore the correct sequence of events even if they arrive out of order. |
| `status` | [`Status53`](../../doc/models/status-53.md) | Required | - |
| `tracing` | [UKFpsTracingData](../../doc/models/uk-fps-tracing-data.md) \| [USAchTracingData](../../doc/models/us-ach-tracing-data.md) \| None | Optional | This is a container for one-of cases. |
| `tracking` | [ConfirmationTrackingData](../../doc/models/confirmation-tracking-data.md) \| [EstimationTrackingData](../../doc/models/estimation-tracking-data.md) \| [InternalReviewTrackingData](../../doc/models/internal-review-tracking-data.md) \| None | Optional | This is a container for one-of cases. |
| `transaction_rules_result` | [`TransactionRulesResult`](../../doc/models/transaction-rules-result.md) | Optional | - |
| `mtype` | [`Type83`](../../doc/models/type-83.md) | Optional | - |
| `ultimate_party` | [`UltimatePartyIdentification`](../../doc/models/ultimate-party-identification.md) | Optional | - |
| `updated_at` | `datetime` | Optional | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.balance_mutation import BalanceMutation
from adyen.models.bank_category_data import BankCategoryData
from adyen.models.category_3 import Category3
from adyen.models.priority import Priority
from adyen.models.resource_reference import ResourceReference
from adyen.models.status_53 import Status53
from adyen.models.transfer_data import TransferData
from adyen.models.type_312 import Type312

transfer_data = TransferData(
    amount=Amount5(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    category=Category3.INTERNAL,
    status=Status53.CHARGEBACKREVERSED,
    account_holder=ResourceReference(
        description='description0',
        id='id0',
        reference='reference4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    balance_account=ResourceReference(
        description='description2',
        id='id2',
        reference='reference2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    balance_platform='balancePlatform2',
    balances=[
        BalanceMutation(
            balance=224,
            currency='currency0',
            received=214,
            reserved=158,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        BalanceMutation(
            balance=224,
            currency='currency0',
            received=214,
            reserved=158,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        BalanceMutation(
            balance=224,
            currency='currency0',
            received=214,
            reserved=158,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    category_data=BankCategoryData(
        priority=Priority.INSTANT,
        mtype=Type312.BANK,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

