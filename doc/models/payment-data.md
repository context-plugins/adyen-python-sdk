
# Payment Data

## Structure

`PaymentData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_type` | [`PaymentType1Enum`](../../doc/models/payment-type-1-enum.md) | Optional | Type of payment transaction. Elements requested by the Sale System that are related to the payment only.<br>Possible values:<br><br>* **CashAdvance**<br>* **CashDeposit**<br>* **Completion**<br>* **FirstReservation**<br>* **Instalment**<br>* **IssuerInstalment**<br>* **Normal**<br>* **OneTimeReservation**<br>* **PaidOut**<br>* **Recurring**<br>* **Refund**<br>* **UpdateReservation** |
| `split_payment_flag` | `bool` | Optional | Indicates if the payment of the Sale transaction is split. Allows the POI to decline payment means that cannot accept split payment.<br><br>**Default**: `False` |
| `requested_validity_date` | `date` | Optional | Requested validity date for the reservation. Allows a specific period for the reservation according to the need of the Merchant for the first reservation and the reservation updates as well. |
| `card_acquisition_reference` | [`TransactionIDType`](../../doc/models/transaction-id-type.md) | Optional | Identification of a transaction for the Sale System or the POI System. |
| `instalment` | [`Instalment1`](../../doc/models/instalment-1.md) | Optional | Information related an instalment transaction. To request an instalment to the issuer, or to make individual instalments of a payment transaction. |
| `payment_instrument_data` | [`PaymentInstrumentData`](../../doc/models/payment-instrument-data.md) | Optional | Data related to the instrument of payment for the transaction.<br>Sent in the result of the payment transaction. For a card, it could also be sent in the `CardAcquisition` response, to be processed by the Sale System. |

## Example

```python
import dateutil.parser

from adyen.models.instalment_1 import Instalment1
from adyen.models.instalment_type_enum import InstalmentTypeEnum
from adyen.models.payment_data import PaymentData
from adyen.models.payment_type_1_enum import PaymentType1Enum
from adyen.models.period_unit_1_enum import PeriodUnit1Enum
from adyen.models.transaction_id_type import TransactionIDType

payment_data = PaymentData(
    payment_type=PaymentType1Enum.CASHADVANCE,
    split_payment_flag=False,
    requested_validity_date=dateutil.parser.parse('2016-03-13').date(),
    card_acquisition_reference=TransactionIDType(
        transaction_id='TransactionID8',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    ),
    instalment=Instalment1(
        instalment_type=InstalmentTypeEnum.DEFERREDINSTALMENTS,
        sequence_number=106,
        plan_id='PlanID4',
        period=70,
        period_unit=PeriodUnit1Enum.MONTHLY
    )
)
```

