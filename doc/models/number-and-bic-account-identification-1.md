
# Number and Bic Account Identification 1

*This model accepts additional fields of type Any.*

## Structure

`NumberAndBicAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The bank account number, without separators or whitespace. The length and format depends on the bank or country.<br><br>**Constraints**: *Maximum Length*: `34` |
| `additional_bank_identification` | [`AdditionalBankIdentification`](../../doc/models/additional-bank-identification.md) | Optional | - |
| `bic` | `str` | Required | The bank's 8- or 11-character BIC or SWIFT code.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `11` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_bank_identification import AdditionalBankIdentification
from adyen.models.additional_bank_identification_type import AdditionalBankIdentificationType
from adyen.models.bank_account_identification import NumberAndBicAccountIdentification1

number_and_bic_account_identification_1 = NumberAndBicAccountIdentification1(
    account_number='accountNumber0',
    bic='bic4',
    additional_bank_identification=AdditionalBankIdentification(
        code='code2',
        mtype=AdditionalBankIdentificationType.GBSORTCODE,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    mtype='numberAndBic',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

