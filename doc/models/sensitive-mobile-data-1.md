
# Sensitive Mobile Data 1

Sensitive information related to the mobile phone.
If unprotected mobile data.

## Structure

`SensitiveMobileData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msisdn` | `int` | Required | Mobile Subscriber Integrated Service Digital Network (i.e. mobile phone number of the SIM card). Country, National Destination Code, and Subscriber Number. |
| `imsi` | `int` | Optional | International Mobile Subscriber Identity. Unique number associated with the mobile phone user, containing the Mobile Country Code (MCC), the Mobile Network Code (MNC), and the Mobile Identification Number (MSIN) |
| `imei` | `int` | Optional | International Mobile Equipment Identity. Unique number associated with the mobile phone device. |

## Example

```python
from adyen.models.sensitive_mobile_data_1 import SensitiveMobileData1

sensitive_mobile_data_1 = SensitiveMobileData1(
    msisdn=254,
    imsi=230,
    imei=138
)
```

