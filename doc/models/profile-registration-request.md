
# Profile Registration Request

## Structure

`ProfileRegistrationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier of the account holder.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `150` |
| `payment_instrument_ids` | `List[str]` | Required | The unique identifiers of the payment instruments to be associated with the iDEAL profile.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `100`, *Minimum Length*: `1`, *Maximum Length*: `150` |

## Example

```python
from adyen.models.profile_registration_request import ProfileRegistrationRequest

profile_registration_request = ProfileRegistrationRequest(
    account_holder_id='AH00000000000000000000000',
    payment_instrument_ids=[
        'PI00000000000000000000000',
        'PI11111111111111111111111'
    ]
)
```

