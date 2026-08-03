
# Three Ds 2 Response Data 1

Response of the 3D Secure 2 authentication.

*This model accepts additional fields of type Any.*

## Structure

`ThreeDs2ResponseData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acs_challenge_mandated` | `str` | Optional | - |
| `acs_operator_id` | `str` | Optional | - |
| `acs_reference_number` | `str` | Optional | - |
| `acs_signed_content` | `str` | Optional | - |
| `acs_trans_id` | `str` | Optional | - |
| `acs_url` | `str` | Optional | - |
| `authentication_type` | `str` | Optional | - |
| `card_holder_info` | `str` | Optional | - |
| `cavv_algorithm` | `str` | Optional | - |
| `challenge_indicator` | `str` | Optional | - |
| `ds_reference_number` | `str` | Optional | - |
| `ds_trans_id` | `str` | Optional | - |
| `exemption_indicator` | `str` | Optional | - |
| `message_version` | `str` | Optional | - |
| `risk_score` | `str` | Optional | - |
| `sdk_ephem_pub_key` | `str` | Optional | - |
| `three_ds_server_trans_id` | `str` | Optional | - |
| `trans_status` | `str` | Optional | - |
| `trans_status_reason` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.three_ds_2_response_data_1 import ThreeDs2ResponseData1

three_ds_2_response_data_1 = ThreeDs2ResponseData1(
    acs_challenge_mandated='acsChallengeMandated4',
    acs_operator_id='acsOperatorID6',
    acs_reference_number='acsReferenceNumber6',
    acs_signed_content='acsSignedContent0',
    acs_trans_id='acsTransID6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

