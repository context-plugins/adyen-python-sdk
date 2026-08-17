
# Connectivity

## Structure

`Connectivity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `simcard_status` | [`SimcardStatusEnum`](../../doc/models/simcard-status-enum.md) | Optional | Indicates the status of the SIM card in the payment terminal. Can be updated and received only at terminal level, and only for models that support cellular connectivity.<br><br>Possible values:<br><br>* **ACTIVATED**: the SIM card is activated. Cellular connectivity may still need to be enabled on the terminal itself, in the **Network** settings.<br>* **INVENTORY**: the SIM card is not activated. The terminal can't use cellular connectivity. |
| `terminal_ip_address_url` | [`EventUrl3`](../../doc/models/event-url-3.md) | Optional | The list of local and public URLs to send notifications to when using local integrations. |

## Example

```python
from adyen.models.connectivity import Connectivity
from adyen.models.event_url_3 import EventUrl3
from adyen.models.simcard_status_enum import SimcardStatusEnum
from adyen.models.url import Url

connectivity = Connectivity(
    simcard_status=SimcardStatusEnum.ACTIVATED,
    terminal_ip_address_url=EventUrl3(
        event_local_urls=[
            Url(
                encrypted=False,
                password='password4',
                url='url4',
                username='username0'
            )
        ],
        event_public_urls=[
            Url(
                encrypted=False,
                password='password8',
                url='url8',
                username='username4'
            ),
            Url(
                encrypted=False,
                password='password8',
                url='url8',
                username='username4'
            )
        ]
    )
)
```

