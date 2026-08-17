
# Three DS 2 Card Range Detail

## Structure

`ThreeDS2CardRangeDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acs_info_ind` | `List[str]` | Optional | Provides additional information to the 3DS Server.<br>Possible values:<br><br>- 01 (Authentication is available at ACS)<br>- 02 (Attempts supported by ACS or DS)<br>- 03 (Decoupled authentication supported)<br>- 04 (Whitelisting supported) |
| `brand_code` | `str` | Optional | Card brand. |
| `end_range` | `str` | Optional | BIN end range. |
| `start_range` | `str` | Optional | BIN start range. |
| `three_ds_2_versions` | `List[str]` | Optional | Supported 3D Secure protocol versions |
| `three_ds_method_url` | `str` | Optional | In a 3D Secure 2 browser-based flow, this is the URL where you should send the device fingerprint to. |

## Example

```python
from adyen.models.three_ds_2_card_range_detail import ThreeDS2CardRangeDetail

three_ds_2_card_range_detail = ThreeDS2CardRangeDetail(
    acs_info_ind=[
        'acsInfoInd5',
        'acsInfoInd6'
    ],
    brand_code='brandCode2',
    end_range='endRange4',
    start_range='startRange4',
    three_ds_2_versions=[
        'threeDS2Versions3'
    ]
)
```

