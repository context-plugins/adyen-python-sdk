
# Additional Data Ratepay

## Structure

`AdditionalDataRatepay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ratepay_installment_amount` | `str` | Optional | Amount the customer has to pay each month. |
| `ratepay_interest_rate` | `str` | Optional | Interest rate of this installment. |
| `ratepay_last_installment_amount` | `str` | Optional | Amount of the last installment. |
| `ratepay_payment_firstday` | `str` | Optional | Calendar day of the first payment. |
| `ratepaydata_delivery_date` | `str` | Optional | Date the merchant delivered the goods to the customer. |
| `ratepaydata_due_date` | `str` | Optional | Date by which the customer must settle the payment. |
| `ratepaydata_invoice_date` | `str` | Optional | Invoice date, defined by the merchant. If not included, the invoice date is set to the delivery date. |
| `ratepaydata_invoice_id` | `str` | Optional | Identification name or number for the invoice, defined by the merchant. |

## Example

```python
from adyen.models.additional_data_ratepay import AdditionalDataRatepay

additional_data_ratepay = AdditionalDataRatepay(
    ratepay_installment_amount='ratepay.installmentAmount4',
    ratepay_interest_rate='ratepay.interestRate0',
    ratepay_last_installment_amount='ratepay.lastInstallmentAmount2',
    ratepay_payment_firstday='ratepay.paymentFirstday6',
    ratepaydata_delivery_date='ratepaydata.deliveryDate6'
)
```

