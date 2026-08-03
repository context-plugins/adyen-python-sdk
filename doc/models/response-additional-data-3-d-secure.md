
# Response Additional Data 3 D Secure

*This model accepts additional fields of type Any.*

## Structure

`ResponseAdditionalData3DSecure`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_holder_info` | `str` | Optional | Information provided by the issuer to the cardholder. If this field is present, you need to display this information to the cardholder. |
| `cavv` | `str` | Optional | The Cardholder Authentication Verification Value (CAVV) for the 3D Secure authentication session, as a Base64-encoded 20-byte array. |
| `cavv_algorithm` | `str` | Optional | The CAVV algorithm used. |
| `sca_exemption_requested` | `str` | Optional | Shows the [exemption type](https://docs.adyen.com/payments-fundamentals/psd2-sca-compliance-and-implementation-guide#specifypreferenceinyourapirequest) that Adyen requested for the payment.<br><br>Possible values:<br><br>* **lowValue**<br>* **secureCorporate**<br>* **trustedBeneficiary**<br>* **transactionRiskAnalysis** |
| `threeds_2_card_enrolled` | `bool` | Optional | Indicates whether a card is enrolled for 3D Secure 2. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.response_additional_data_3_d_secure import ResponseAdditionalData3DSecure

response_additional_data_3_d_secure = ResponseAdditionalData3DSecure(
    card_holder_info='cardHolderInfo0',
    cavv='cavv0',
    cavv_algorithm='cavvAlgorithm0',
    sca_exemption_requested='scaExemptionRequested8',
    threeds_2_card_enrolled=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

