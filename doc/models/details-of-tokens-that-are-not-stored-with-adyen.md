
# Details of Tokens that Are Not Stored with Adyen

## Structure

`DetailsOfTokensThatAreNotStoredWithAdyen`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `expiry_month` | `str` | Optional | The card expiry month. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `expiry_year` | `str` | Optional | The card expiry year. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `holder_name` | `str` | Optional | The name of the card holder.<br><br>**Constraints**: *Maximum Length*: `15000` |
| `number` | `str` | Optional | The card number. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `stored_payment_method_id` | `str` | Required | Identifier used to fetch the token from the external service<br><br>**Constraints**: *Maximum Length*: `64` |
| `subtype` | `str` | Required, Constant | The external service from which to fetch the token. Supported only for specific companies. Contact Adyen if you want to use this feature.<br><br>**Value**: `"hilton"` |
| `mtype` | `str` | Required, Constant | The type of token. Allowed value: **externalToken**.<br><br>**Value**: `"externalToken"` |

## Example

```python
from adyen.models.details_of_tokens_that_are_not_stored_with_adyen import DetailsOfTokensThatAreNotStoredWithAdyen

details_of_tokens_that_are_not_stored_with_adyen = DetailsOfTokensThatAreNotStoredWithAdyen(
    stored_payment_method_id='storedPaymentMethodId0',
    checkout_attempt_id='checkoutAttemptId2',
    expiry_month='expiryMonth0',
    expiry_year='expiryYear0',
    holder_name='holderName2',
    number='number4'
)
```

