
# Detailsoftokensthatarenotstoredwith Adyen

*This model accepts additional fields of type Any.*

## Structure

`DetailsoftokensthatarenotstoredwithAdyen`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `expiry_month` | `str` | Optional | The card expiry month. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `expiry_year` | `str` | Optional | The card expiry year. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `holder_name` | `str` | Optional | The name of the card holder.<br><br>**Constraints**: *Maximum Length*: `15000` |
| `number` | `str` | Optional | The card number. Only collect raw card data if you are [fully PCI compliant](https://docs.adyen.com/development-resources/pci-dss-compliance-guide). |
| `stored_payment_method_id` | `str` | Required | Identifier used to fetch the token from the external service<br><br>**Constraints**: *Maximum Length*: `64` |
| `subtype` | [`Subtype3`](../../doc/models/subtype-3.md) | Required | The external service from which to fetch the token. Supported only for specific companies. Contact Adyen if you want to use this feature. |
| `mtype` | [`Type67`](../../doc/models/type-67.md) | Required | The type of token. Allowed value: **externalToken**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.detailsoftokensthatarenotstoredwith_adyen import DetailsoftokensthatarenotstoredwithAdyen
from adyen.models.subtype_3 import Subtype3
from adyen.models.type_67 import Type67

detailsoftokensthatarenotstoredwith_adyen = DetailsoftokensthatarenotstoredwithAdyen(
    stored_payment_method_id='storedPaymentMethodId0',
    subtype=Subtype3.HILTON,
    mtype=Type67.EXTERNALTOKEN,
    checkout_attempt_id='checkoutAttemptId2',
    expiry_month='expiryMonth0',
    expiry_year='expiryYear0',
    holder_name='holderName2',
    number='number4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

