
# Number and Bic Account Identification 1

## Structure

`NumberAndBicAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The bank account number, without separators or whitespace. The length and format depends on the bank or country.<br><br>**Constraints**: *Maximum Length*: `34` |
| `additional_bank_identification` | [`AdditionalBankIdentification11`](../../doc/models/additional-bank-identification-11.md) | Optional | Additional identification codes of the bank. Some banks may require these identifiers for cross-border transfers. |
| `bic` | `str` | Required | The bank's 8- or 11-character BIC or SWIFT code.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `11` |

## Example

```python
from adyen.models.additional_bank_identification_11 import AdditionalBankIdentification11
from adyen.models.additional_bank_identification_type_enum import AdditionalBankIdentificationTypeEnum
from adyen.models.bank_account_identification import NumberAndBicAccountIdentification1

number_and_bic_account_identification_1 = NumberAndBicAccountIdentification1(
    account_number='accountNumber0',
    bic='bic4',
    additional_bank_identification=AdditionalBankIdentification11(
        code='code2',
        mtype=AdditionalBankIdentificationTypeEnum.GBSORTCODE
    ),
    mtype='numberAndBic'
)
```

