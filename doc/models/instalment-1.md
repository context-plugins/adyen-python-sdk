
# Instalment 1

Information related an instalment transaction. To request an instalment to the issuer, or to make individual instalments of a payment transaction.

## Structure

`Instalment1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `instalment_type` | [`InstalmentTypeEnum`](../../doc/models/instalment-type-enum.md) | Optional | Type of instalment transaction. For requesting an instalment payment transaction.<br>Possible values:<br><br>* **DeferredInstalments**<br>* **EqualInstalments**<br>* **InequalInstalments** |
| `sequence_number` | `int` | Optional | Sequence number of the instalment. For an instalment payment transaction, number of the payment, from 1 to TotalNbOfPayments. |
| `plan_id` | `str` | Optional | Identification of an instalment plan.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `period` | `int` | Optional | Period of time with defined unit of time. A period between 2 payment instalments. |
| `period_unit` | [`PeriodUnit1Enum`](../../doc/models/period-unit-1-enum.md) | Optional | Type of instalment transaction.<br>Possible values:<br><br>* **Annual**<br>* **Daily**<br>* **Monthly**<br>* **Weekly** |
| `first_payment_date` | `date` | Optional | First date of a payment. For instalment, the date of the first payments, if not immediate. |
| `total_nb_of_payments` | `int` | Optional | Total number of payments. For instalment, the number of payments, including the first one. |
| `cumulative_amount` | `float` | Optional | Sum of a collection of amounts. Total amount of the payment instalments.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `first_amount` | `float` | Optional | First amount of the payment instalments.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `charges` | `float` | Optional | Charges related to a transaction. Charge related to the payment instalments.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |

## Example

```python
from adyen.models.instalment_1 import Instalment1
from adyen.models.instalment_type_enum import InstalmentTypeEnum
from adyen.models.period_unit_1_enum import PeriodUnit1Enum

instalment_1 = Instalment1(
    instalment_type=InstalmentTypeEnum.INEQUALINSTALMENTS,
    sequence_number=246,
    plan_id='PlanID0',
    period=210,
    period_unit=PeriodUnit1Enum.MONTHLY
)
```

