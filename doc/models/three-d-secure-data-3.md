
# Three D Secure Data 3

Authentication data from a [merchant plug-in (MPI)](https://en.wikipedia.org/wiki/Merchant_plug-in) like Mastercard SecureCode, Visa Secure, or Cartes Bancaires. Required for cardholder-initiated transaction (CIT) adjustments.

## Structure

`ThreeDSecureData3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication_response` | [`AuthenticationResponseEnum`](../../doc/models/authentication-response-enum.md) | Optional | In 3D Secure 2, this is the `transStatus` from the challenge result. If the transaction was frictionless, omit this parameter. |
| `cavv` | `str` | Optional | The cardholder authentication value (base64 encoded, 20 bytes in a decoded form). |
| `cavv_algorithm` | `str` | Optional | The CAVV algorithm used. Include this only for 3D Secure 1. |
| `challenge_cancel` | [`ChallengeCancelEnum`](../../doc/models/challenge-cancel-enum.md) | Optional | Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. For possible values, refer to [3D Secure API reference](https://docs.adyen.com/online-payments/3d-secure/api-reference#mpidata). |
| `directory_response` | [`DirectoryResponseEnum`](../../doc/models/directory-response-enum.md) | Optional | In 3D Secure 2, this is the `transStatus` from the `ARes`. |
| `ds_trans_id` | `str` | Optional | Supported for 3D Secure 2. The unique transaction identifier assigned by the Directory Server (DS) to identify a single transaction. |
| `eci` | `str` | Optional | The electronic commerce indicator. |
| `risk_score` | `str` | Optional | Risk score calculated by Directory Server (DS). Required for Cartes Bancaires integrations. |
| `three_ds_version` | `str` | Optional | The version of the 3D Secure protocol. |
| `token_authentication_verification_value` | `str` | Optional | Network token authentication verification value (TAVV). The network token cryptogram. |
| `trans_status_reason` | `str` | Optional | Provides information on why the `transStatus` field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values). |
| `xid` | `str` | Optional | Supported for 3D Secure 1. The transaction identifier (Base64-encoded, 20 bytes in a decoded form). |

## Example

```python
from adyen.models.authentication_response_enum import AuthenticationResponseEnum
from adyen.models.challenge_cancel_enum import ChallengeCancelEnum
from adyen.models.directory_response_enum import DirectoryResponseEnum
from adyen.models.three_d_secure_data_3 import ThreeDSecureData3

three_d_secure_data_3 = ThreeDSecureData3(
    authentication_response=AuthenticationResponseEnum.U,
    cavv='cavv0',
    cavv_algorithm='cavvAlgorithm0',
    challenge_cancel=ChallengeCancelEnum.ENUM_06,
    directory_response=DirectoryResponseEnum.U
)
```

