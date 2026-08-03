
# Moto

*This model accepts additional fields of type Any.*

## Structure

`Moto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_moto` | `bool` | Optional | Enable MOTO transactions. |
| `max_amount` | `int` | Optional | The maximum amount for MOTO transactions. You need to set the currency for this amount using the [`standalone.currencyCode`](https://docs.adyen.com/api-explorer/Management/1/patch/companies/(companyId)/terminalSettings#request-standalone-currencyCode) parameter. Do not enable standalone, unless you are using a standalone solution. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.moto import Moto

moto = Moto(
    enable_moto=False,
    max_amount=152,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

