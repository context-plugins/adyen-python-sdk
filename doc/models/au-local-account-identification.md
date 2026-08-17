
# AU Local Account Identification

## Structure

`AULocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `9` |
| `bsb_code` | `str` | Required | The 6-digit [Bank State Branch (BSB) code](https://en.wikipedia.org/wiki/Bank_state_branch), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6` |
| `mtype` | `str` | Required, Constant | **auLocal**<br><br>**Value**: `"auLocal"` |

## Example

```python
from adyen.models.au_local_account_identification import AULocalAccountIdentification

au_local_account_identification = AULocalAccountIdentification(
    account_number='accountNumber2',
    bsb_code='bsbCode4'
)
```

