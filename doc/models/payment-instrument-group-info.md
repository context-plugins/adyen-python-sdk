
# Payment Instrument Group Info

*This model accepts additional fields of type Any.*

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
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_instrument_group_info import PaymentInstrumentGroupInfo

payment_instrument_group_info = PaymentInstrumentGroupInfo(
    balance_platform='balancePlatform8',
    tx_variant='txVariant4',
    description='description6',
    properties={
        'key0': 'properties4'
    },
    reference='reference8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

