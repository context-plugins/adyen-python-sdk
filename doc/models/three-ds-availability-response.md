
# Three Ds Availability Response

*This model accepts additional fields of type Any.*

## Structure

`ThreeDsAvailabilityResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bin_details` | [`BinDetail`](../../doc/models/bin-detail.md) | Optional | - |
| `ds_public_keys` | [`List[DsPublicKeyDetail]`](../../doc/models/ds-public-key-detail.md) | Optional | List of Directory Server (DS) public keys. |
| `three_ds_1_supported` | `bool` | Optional | Indicator if 3D Secure 1 is supported. |
| `three_ds_2_card_range_details` | [`List[ThreeDs2CardRangeDetail]`](../../doc/models/three-ds-2-card-range-detail.md) | Optional | List of brand and card range pairs. |
| `three_ds_2_supported` | `bool` | Optional | Indicator if 3D Secure 2 is supported. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bin_detail import BinDetail
from adyen.models.ds_public_key_detail import DsPublicKeyDetail
from adyen.models.three_ds_2_card_range_detail import ThreeDs2CardRangeDetail
from adyen.models.three_ds_availability_response import ThreeDsAvailabilityResponse

three_ds_availability_response = ThreeDsAvailabilityResponse(
    bin_details=BinDetail(
        issuer_country='issuerCountry8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    ds_public_keys=[
        DsPublicKeyDetail(
            brand='brand6',
            directory_server_id='directoryServerId6',
            from_sdk_version='fromSDKVersion8',
            public_key='publicKey0',
            root_certificates='rootCertificates4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    three_ds_1_supported=False,
    three_ds_2_card_range_details=[
        ThreeDs2CardRangeDetail(
            acs_info_ind=[
                'acsInfoInd1',
                'acsInfoInd0',
                'acsInfoInd9'
            ],
            brand_code='brandCode6',
            end_range='endRange2',
            start_range='startRange0',
            three_ds_2_versions=[
                'threeDS2Versions9'
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    three_ds_2_supported=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

