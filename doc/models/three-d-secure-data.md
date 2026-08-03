
# Three D Secure Data

Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires).

*This model accepts additional fields of type Any.*

## Structure

`ThreeDSecureData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication_response` | [`AuthenticationResponse`](../../doc/models/authentication-response.md) | Optional | - |
| `cavv` | `str` | Optional | The cardholder authentication value (base64 encoded, 20 bytes in a decoded form). |
| `cavv_algorithm` | `str` | Optional | The CAVV algorithm used. Include this only for 3D Secure 1. |
| `challenge_cancel` | [`ChallengeCancel`](../../doc/models/challenge-cancel.md) | Optional | - |
| `directory_response` | [`DirectoryResponse`](../../doc/models/directory-response.md) | Optional | - |
| `ds_trans_id` | `str` | Optional | Supported for 3D Secure 2. The unique transaction identifier assigned by the Directory Server (DS) to identify a single transaction. |
| `eci` | `str` | Optional | The electronic commerce indicator. |
| `risk_score` | `str` | Optional | Risk score calculated by Directory Server (DS). Required for Cartes Bancaires integrations. |
| `three_ds_version` | `str` | Optional | The version of the 3D Secure protocol. |
| `token_authentication_verification_value` | `str` | Optional | Network token authentication verification value (TAVV). The network token cryptogram. |
| `trans_status_reason` | `str` | Optional | Provides information on why the `transStatus` field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values). |
| `xid` | `str` | Optional | Supported for 3D Secure 1. The transaction identifier (Base64-encoded, 20 bytes in a decoded form). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.authentication_response import AuthenticationResponse
from adyen.models.challenge_cancel import ChallengeCancel
from adyen.models.directory_response import DirectoryResponse
from adyen.models.three_d_secure_data import ThreeDSecureData

three_d_secure_data = ThreeDSecureData(
    authentication_response=AuthenticationResponse.U,
    cavv='cavv4',
    cavv_algorithm='cavvAlgorithm4',
    challenge_cancel=ChallengeCancel.ENUM_05,
    directory_response=DirectoryResponse.D,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

