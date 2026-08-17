
# Bank Account Identification Type Requirement

## Structure

`BankAccountIdentificationTypeRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_identification_types` | [`List[BankAccountIdentificationTypeEnum]`](../../doc/models/bank-account-identification-type-enum.md) | Optional | List of bank account identification types: eg.; [iban , numberAndBic] |
| `description` | `str` | Optional | Specifies the bank account details for a particular route per required field in this object depending on the country of the bank account and the currency of the transfer. |
| `mtype` | `str` | Required, Constant | **bankAccountIdentificationTypeRequirement**<br><br>**Value**: `"bankAccountIdentificationTypeRequirement"` |

## Example

```python
from adyen.models.bank_account_identification_type_enum import BankAccountIdentificationTypeEnum
from adyen.models.bank_account_identification_type_requirement import BankAccountIdentificationTypeRequirement

bank_account_identification_type_requirement = BankAccountIdentificationTypeRequirement(
    bank_account_identification_types=[
        BankAccountIdentificationTypeEnum.SELOCAL,
        BankAccountIdentificationTypeEnum.SGLOCAL,
        BankAccountIdentificationTypeEnum.UKLOCAL
    ],
    description='description0'
)
```

