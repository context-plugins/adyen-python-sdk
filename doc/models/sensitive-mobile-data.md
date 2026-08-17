
# Sensitive Mobile Data

## Structure

`SensitiveMobileData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msisdn` | `int` | Required | Mobile Subscriber Integrated Service Digital Network (i.e. mobile phone number of the SIM card). Country, National Destination Code, and Subscriber Number. |
| `imsi` | `int` | Optional | International Mobile Subscriber Identity. Unique number associated with the mobile phone user, containing the Mobile Country Code (MCC), the Mobile Network Code (MNC), and the Mobile Identification Number (MSIN) |
| `imei` | `int` | Optional | International Mobile Equipment Identity. Unique number associated with the mobile phone device. |

## Example

```python
from adyen.models.sensitive_mobile_data import SensitiveMobileData

sensitive_mobile_data = SensitiveMobileData(
    msisdn=88,
    imsi=64,
    imei=228
)
```

