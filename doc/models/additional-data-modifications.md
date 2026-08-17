
# Additional Data Modifications

## Structure

`AdditionalDataModifications`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `installment_payment_data_selected_installment_option` | `str` | Optional | This is the installment option selected by the shopper. It is required only if specified by the user. |

## Example

```python
from adyen.models.additional_data_modifications import AdditionalDataModifications

additional_data_modifications = AdditionalDataModifications(
    installment_payment_data_selected_installment_option='installmentPaymentData.selectedInstallmentOption2'
)
```

