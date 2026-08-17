
# Account Verification Routes Request

## Structure

`AccountVerificationRoutesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country` | [`AccountVerificationCountry2Enum`](../../doc/models/account-verification-country-2-enum.md) | Required | The location where the third-party individual's bank account is registered. Adyen uses this information to determine an available open banking provider, and to configure the open banking flow for that respective location. |
| `locale` | `str` | Optional | The language to use in the open banking flow UI, specified by a combination of a two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) language code and an [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code.<br><br>This information is used to configure the open banking flow with the same language for a consistent user experience.<br><br>Default value: **en-US** |
| `redirect_url` | `str` | Required | The URL where Adyen redirects the third-party individual after they complete the open banking flow. |
| `state` | `str` | Optional | A value that helps you identify the request in callback handling. You can generate this value on a per-session basis to protect the callback against Cross-Site Request Forgery (CSRF) attacks. This value  must be composed of characters that can be successfully URL-encoded. |

## Example

```python
from adyen.models.account_verification_country_2_enum import AccountVerificationCountry2Enum
from adyen.models.account_verification_routes_request import AccountVerificationRoutesRequest

account_verification_routes_request = AccountVerificationRoutesRequest(
    country=AccountVerificationCountry2Enum.CA,
    redirect_url='redirectUrl8',
    locale='locale6',
    state='state4'
)
```

