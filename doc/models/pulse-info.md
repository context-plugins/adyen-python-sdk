
# Pulse Info

## Structure

`PulseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `processing_type` | [`ProcessingTypeEnum`](../../doc/models/processing-type-enum.md) | Required | The type of transactions processed over this payment method.<br>Allowed values:<br><br>- **pos** for in-person payments.<br>- **billpay** for subscription payments, both the initial payment and the later recurring payments. These transactions have `recurringProcessingModel` **Subscription**.<br>- **ecom** for all other card not present transactions. This includes non-recurring transactions and transactions with `recurringProcessingModel` **CardOnFile** or **UnscheduledCardOnFile**. |
| `transaction_description` | [`TransactionDescriptionInfo1`](../../doc/models/transaction-description-info-1.md) | Optional | Information regarding the transaction description.<br><br>> You cannot configure the transaction description in the test environment. |

## Example

```python
from adyen.models.processing_type_enum import ProcessingTypeEnum
from adyen.models.pulse_info import PulseInfo
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum

pulse_info = PulseInfo(
    processing_type=ProcessingTypeEnum.BILLPAY,
    transaction_description=TransactionDescriptionInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

