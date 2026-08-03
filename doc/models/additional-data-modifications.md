
# Additional Data Modifications

*This model accepts additional fields of type Any.*

## Structure

`AdditionalDataModifications`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `installment_payment_data_selected_installment_option` | `str` | Optional | This is the installment option selected by the shopper. It is required only if specified by the user. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_data_modifications import AdditionalDataModifications

additional_data_modifications = AdditionalDataModifications(
    installment_payment_data_selected_installment_option='installmentPaymentData.selectedInstallmentOption2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

