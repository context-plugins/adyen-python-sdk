
# Three DS 2 Result

The ThreeDS2Result that was returned in the final CRes., The result of the 3D Secure 2 authentication.

## Structure

`ThreeDS2Result`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication_value` | `str` | Optional | The `authenticationValue` value as defined in the 3D Secure 2 specification. |
| `cavv_algorithm` | `str` | Optional | The algorithm used by the ACS to calculate the authentication value, only for Cartes Bancaires integrations. |
| `challenge_cancel` | [`ChallengeCancelEnum`](../../doc/models/challenge-cancel-enum.md) | Optional | Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. For possible values, refer to [3D Secure API reference](https://docs.adyen.com/online-payments/3d-secure/api-reference#mpidata). |
| `ds_trans_id` | `str` | Optional | The `dsTransID` value as defined in the 3D Secure 2 specification. |
| `eci` | `str` | Optional | The `eci` value as defined in the 3D Secure 2 specification. |
| `exemption_indicator` | [`ExemptionIndicatorEnum`](../../doc/models/exemption-indicator-enum.md) | Optional | Indicates the exemption type that was applied by the issuer to the authentication, if exemption applied.<br>Allowed values:<br><br>* `lowValue`<br>* `secureCorporate`<br>* `trustedBeneficiary`<br>* `transactionRiskAnalysis` |
| `message_version` | `str` | Optional | The `messageVersion` value as defined in the 3D Secure 2 specification. |
| `risk_score` | `str` | Optional | Risk score calculated by Cartes Bancaires Directory Server (DS). |
| `three_ds_requestor_challenge_ind` | [`ThreeDSRequestorChallengeIndEnum`](../../doc/models/three-ds-requestor-challenge-ind-enum.md) | Optional | Indicates whether a challenge is requested for this transaction. Possible values:<br><br>* **01** — No preference<br>* **02** — No challenge requested<br>* **03** — Challenge requested (3DS Requestor preference)<br>* **04** — Challenge requested (Mandate)<br>* **05** — No challenge (transactional risk analysis is already performed)<br>* **06** — Data Only |
| `three_ds_server_trans_id` | `str` | Optional | The `threeDSServerTransID` value as defined in the 3D Secure 2 specification. |
| `timestamp` | `str` | Optional | The `timestamp` value of the 3D Secure 2 authentication. |
| `trans_status` | `str` | Optional | The `transStatus` value as defined in the 3D Secure 2 specification. |
| `trans_status_reason` | `str` | Optional | Provides information on why the `transStatus` field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values). |
| `white_list_status` | `str` | Optional | The `whiteListStatus` value as defined in the 3D Secure 2 specification. |

## Example

```python
from adyen.models.challenge_cancel_enum import ChallengeCancelEnum
from adyen.models.three_ds_2_result import ThreeDS2Result

three_ds_2_result = ThreeDS2Result(
    authentication_value='authenticationValue2',
    cavv_algorithm='cavvAlgorithm4',
    challenge_cancel=ChallengeCancelEnum.ENUM_04,
    ds_trans_id='dsTransID6',
    eci='eci0'
)
```

