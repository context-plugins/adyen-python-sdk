
# Response Additional Data Installments

*This model accepts additional fields of type Any.*

## Structure

`ResponseAdditionalDataInstallments`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `installment_payment_data_installment_type` | `str` | Optional | Type of installment. The value of `installmentType` should be **IssuerFinanced**. |
| `installment_payment_data_option_item_nr_annual_percentage_rate` | `str` | Optional | Annual interest rate. |
| `installment_payment_data_option_item_nr_first_installment_amount` | `str` | Optional | First Installment Amount in minor units. |
| `installment_payment_data_option_item_nr_installment_fee` | `str` | Optional | Installment fee amount in minor units. |
| `installment_payment_data_option_item_nr_interest_rate` | `str` | Optional | Interest rate for the installment period. |
| `installment_payment_data_option_item_nr_maximum_number_of_installments` | `str` | Optional | Maximum number of installments possible for this payment. |
| `installment_payment_data_option_item_nr_minimum_number_of_installments` | `str` | Optional | Minimum number of installments possible for this payment. |
| `installment_payment_data_option_item_nr_number_of_installments` | `str` | Optional | Total number of installments possible for this payment. |
| `installment_payment_data_option_item_nr_subsequent_installment_amount` | `str` | Optional | Subsequent Installment Amount in minor units. |
| `installment_payment_data_option_item_nr_total_amount_due` | `str` | Optional | Total amount in minor units. |
| `installment_payment_data_payment_options` | `str` | Optional | Possible values:<br><br>* PayInInstallmentsOnly<br>* PayInFullOnly<br>* PayInFullOrInstallments |
| `installments_value` | `str` | Optional | The number of installments that the payment amount should be charged with.<br><br>Example: 5<br><br>> Only relevant for card payments in countries that support installments. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.response_additional_data_installments import ResponseAdditionalDataInstallments

response_additional_data_installments = ResponseAdditionalDataInstallments(
    installment_payment_data_installment_type='installmentPaymentData.installmentType2',
    installment_payment_data_option_item_nr_annual_percentage_rate=Liquid error: Value cannot be null. (Parameter 'key'),
    installment_payment_data_option_item_nr_first_installment_amount=Liquid error: Value cannot be null. (Parameter 'key'),
    installment_payment_data_option_item_nr_installment_fee=Liquid error: Value cannot be null. (Parameter 'key'),
    installment_payment_data_option_item_nr_interest_rate=Liquid error: Value cannot be null. (Parameter 'key'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

