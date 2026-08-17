
# Stored Value Account Status

## Structure

`StoredValueAccountStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stored_value_account_id` | [`StoredValueAccountID`](../../doc/models/stored-value-account-id.md) | Required | Identification of the stored value account or the stored value card and the associated product sold by the Sale System for stored value requests. |
| `current_balance` | `float` | Optional | If relevant and known.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |

## Example

```python
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.stored_value_account_id import StoredValueAccountID
from adyen.models.stored_value_account_status import StoredValueAccountStatus
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum

stored_value_account_status = StoredValueAccountStatus(
    stored_value_account_id=StoredValueAccountID(
        stored_value_account_type=StoredValueAccountType1Enum.PHONECARD,
        entry_mode=[
            EntryModeEnum.MAGSTRIPE,
            EntryModeEnum.SCANNED
        ],
        identification_type=IdentificationType11Enum.PHONENUMBER,
        stored_value_id='StoredValueID8',
        stored_value_provider='StoredValueProvider4',
        owner_name='OwnerName0',
        expiry_date=4
    ),
    current_balance=249.1
)
```

