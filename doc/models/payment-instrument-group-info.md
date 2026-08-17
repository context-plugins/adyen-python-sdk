
# Payment Instrument Group Info

## Structure

`PaymentInstrumentGroupInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_platform` | `str` | Required | The unique identifier of the [balance platform](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id) to which the payment instrument group belongs. |
| `description` | `str` | Optional | Your description for the payment instrument group.<br><br>**Constraints**: *Maximum Length*: `300` |
| `properties` | `Dict[str, str]` | Optional | Properties of the payment instrument group. |
| `reference` | `str` | Optional | Your reference for the payment instrument group.<br><br>**Constraints**: *Maximum Length*: `150` |
| `tx_variant` | `str` | Required | The tx variant of the payment instrument group. |

## Example

```python
from adyen.models.payment_instrument_group_info import PaymentInstrumentGroupInfo

payment_instrument_group_info = PaymentInstrumentGroupInfo(
    balance_platform='balancePlatform8',
    tx_variant='txVariant4',
    description='description6',
    properties={
        'key0': 'properties4'
    },
    reference='reference8'
)
```

