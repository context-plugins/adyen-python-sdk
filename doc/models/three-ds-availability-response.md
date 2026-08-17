
# Three DS Availability Response

## Structure

`ThreeDSAvailabilityResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bin_details` | [`BinDetail1`](../../doc/models/bin-detail-1.md) | Optional | Bin Group Details |
| `ds_public_keys` | [`List[DSPublicKeyDetail]`](../../doc/models/ds-public-key-detail.md) | Optional | List of Directory Server (DS) public keys. |
| `three_ds_1_supported` | `bool` | Optional | Indicator if 3D Secure 1 is supported. |
| `three_ds_2_card_range_details` | [`List[ThreeDS2CardRangeDetail]`](../../doc/models/three-ds-2-card-range-detail.md) | Optional | List of brand and card range pairs. |
| `three_ds_2_supported` | `bool` | Optional | Indicator if 3D Secure 2 is supported. |

## Example

```python
from adyen.models.bin_detail_1 import BinDetail1
from adyen.models.ds_public_key_detail import DSPublicKeyDetail
from adyen.models.three_ds_2_card_range_detail import ThreeDS2CardRangeDetail
from adyen.models.three_ds_availability_response import ThreeDSAvailabilityResponse

three_ds_availability_response = ThreeDSAvailabilityResponse(
    bin_details=BinDetail1(
        issuer_country='issuerCountry8'
    ),
    ds_public_keys=[
        DSPublicKeyDetail(
            brand='brand6',
            directory_server_id='directoryServerId6',
            from_sdk_version='fromSDKVersion8',
            public_key='publicKey0',
            root_certificates='rootCertificates4'
        )
    ],
    three_ds_1_supported=False,
    three_ds_2_card_range_details=[
        ThreeDS2CardRangeDetail(
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
            ]
        )
    ],
    three_ds_2_supported=False
)
```

