
# Instalment 1

Information related an instalment transaction. To request an instalment to the issuer, or to make individual instalments of a payment transaction.

*This model accepts additional fields of type Any.*

## Structure

`Instalment1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `instalment_type` | [`InstalmentType`](../../doc/models/instalment-type.md) | Optional | - |
| `sequence_number` | `int` | Optional | Sequence number of the instalment. For an instalment payment transaction, number of the payment, from 1 to TotalNbOfPayments. |
| `plan_id` | `str` | Optional | Identification of an instalment plan.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `period` | `int` | Optional | Period of time with defined unit of time. A period between 2 payment instalments. |
| `period_unit` | [`PeriodUnit1`](../../doc/models/period-unit-1.md) | Optional | - |
| `first_payment_date` | `date` | Optional | First date of a payment. For instalment, the date of the first payments, if not immediate. |
| `total_nb_of_payments` | `int` | Optional | Total number of payments. For instalment, the number of payments, including the first one. |
| `cumulative_amount` | `float` | Optional | Sum of a collection of amounts. Total amount of the payment instalments.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `first_amount` | `float` | Optional | First amount of the payment instalments.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `charges` | `float` | Optional | Charges related to a transaction. Charge related to the payment instalments.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.instalment_1 import Instalment1
from adyen.models.instalment_type import InstalmentType
from adyen.models.period_unit_1 import PeriodUnit1

instalment_1 = Instalment1(
    instalment_type=InstalmentType.INEQUALINSTALMENTS,
    sequence_number=246,
    plan_id='PlanID0',
    period=210,
    period_unit=PeriodUnit1.MONTHLY,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

