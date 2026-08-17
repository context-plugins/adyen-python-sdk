
# Healthcare 2

Healthcare auto-substantiation amounts for FSA/HSA card transactions. The amounts are used to qualify for reduced interchange rates on healthcare-eligible cards.

## Structure

`Healthcare2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dental_value` | `int` | Optional | The dental amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000 |
| `other_medical_value` | `int` | Optional | The other medical amount not covered by the specific categories, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000 |
| `prescription_value` | `int` | Optional | The prescription/Rx amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000 |
| `total_healthcare_value` | `int` | Required | The total healthcare amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000 |
| `vision_prescription_value` | `int` | Optional | The vision/optical prescription amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000 |

## Example

```python
from adyen.models.healthcare_2 import Healthcare2

healthcare_2 = Healthcare2(
    total_healthcare_value=84,
    dental_value=32,
    other_medical_value=50,
    prescription_value=240,
    vision_prescription_value=66
)
```

