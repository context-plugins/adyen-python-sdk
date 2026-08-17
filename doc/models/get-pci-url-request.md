
# Get Pci Url Request

## Structure

`GetPciUrlRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The account holder code you provided when you created the account holder. |
| `return_url` | `str` | Optional | The URL where the account holder will be redirected back to after they fill out the questionnaire, or if their session times out. Maximum length of 500 characters. |

## Example

```python
from adyen.models.get_pci_url_request import GetPciUrlRequest

get_pci_url_request = GetPciUrlRequest(
    account_holder_code='accountHolderCode6',
    return_url='returnUrl8'
)
```

