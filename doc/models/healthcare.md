
# Healthcare

*This model accepts additional fields of type Any.*

## Structure

`Healthcare`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dental_value` | `int` | Optional | The dental amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000 |
| `other_medical_value` | `int` | Optional | The other medical amount not covered by the specific categories, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000 |
| `prescription_value` | `int` | Optional | The prescription/Rx amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000 |
| `total_healthcare_value` | `int` | Required | The total healthcare amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000 |
| `vision_prescription_value` | `int` | Optional | The vision/optical prescription amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.healthcare import Healthcare

healthcare = Healthcare(
    total_healthcare_value=16,
    dental_value=132,
    other_medical_value=150,
    prescription_value=116,
    vision_prescription_value=166,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

