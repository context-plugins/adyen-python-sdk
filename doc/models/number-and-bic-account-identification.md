
# Number and Bic Account Identification

## Structure

`NumberAndBicAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The bank account number, without separators or whitespace. The length and format depends on the bank or country.<br><br>**Constraints**: *Maximum Length*: `34` |
| `additional_bank_identification` | [`AdditionalBankIdentification1`](../../doc/models/additional-bank-identification-1.md) | Optional | Additional identification codes of the bank. Some banks may require these identifiers for cross-border transfers. |
| `bic` | `str` | Required | The bank's 8- or 11-character BIC or SWIFT code.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `11` |
| `mtype` | `str` | Required, Constant | **numberAndBic**<br><br>**Value**: `"numberAndBic"` |

## Example

```python
from adyen.models.additional_bank_identification_1 import AdditionalBankIdentification1
from adyen.models.number_and_bic_account_identification import NumberAndBicAccountIdentification
from adyen.models.type_510_enum import Type510Enum

number_and_bic_account_identification = NumberAndBicAccountIdentification(
    account_number='accountNumber0',
    bic='bic4',
    additional_bank_identification=AdditionalBankIdentification1(
        code='code2',
        mtype=Type510Enum.GBSORTCODE
    )
)
```

