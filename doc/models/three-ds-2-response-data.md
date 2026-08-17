
# Three DS 2 Response Data

## Structure

`ThreeDS2ResponseData`

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

## Example

```python
from adyen.models.three_ds_2_response_data import ThreeDS2ResponseData

three_ds_2_response_data = ThreeDS2ResponseData(
    acs_challenge_mandated='acsChallengeMandated4',
    acs_operator_id='acsOperatorID6',
    acs_reference_number='acsReferenceNumber6',
    acs_signed_content='acsSignedContent0',
    acs_trans_id='acsTransID4'
)
```

