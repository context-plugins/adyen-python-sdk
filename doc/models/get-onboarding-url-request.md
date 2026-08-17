
# Get Onboarding Url Request

## Structure

`GetOnboardingUrlRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The account holder code you provided when you created the account holder. |
| `collect_information` | [`CollectInformation1`](../../doc/models/collect-information-1.md) | Optional | Contains indicators whether the page should only collect information for specific [KYC checks](https://docs.adyen.com/classic-platforms/verification-checks). By default, the page collects information for all KYC checks that apply to the [legal entity type](https://docs.adyen.com/classic-platforms/account-holders-and-accounts#legal-entity-types). |
| `edit_mode` | `bool` | Optional | Indicates if editing checks is allowed even if all the checks have passed. |
| `mobile_o_auth_callback_url` | `str` | Optional | The URL to which the account holder is redirected after completing an OAuth authentication with a bank through Trustly/PayMyBank. |
| `platform_name` | `str` | Optional | The platform name which will show up in the welcome page. |
| `return_url` | `str` | Optional | The URL where the account holder will be redirected back to after they complete the onboarding, or if their session times out. Maximum length of 500 characters. If you don't provide this, the account holder will be redirected back to the default return URL configured in your platform account. |
| `shopper_locale` | `str` | Optional | The language to be used in the page, specified by a combination of a language and country code. For example, **pt-BR**.<br><br>If not specified in the request or if the language is not supported, the page uses the browser language. If the browser language is not supported, the page uses **en-US** by default.<br><br>For a list of supported languages, refer to [Change the page language](https://docs.adyen.com/classic-platforms/hosted-onboarding-page/customize-experience#change-page-language). |
| `show_pages` | [`ShowPages2`](../../doc/models/show-pages-2.md) | Optional | Contains indicators whether specific pages must be shown to the account holder. |

## Example

```python
from adyen.models.collect_information_1 import CollectInformation1
from adyen.models.get_onboarding_url_request import GetOnboardingUrlRequest

get_onboarding_url_request = GetOnboardingUrlRequest(
    account_holder_code='accountHolderCode4',
    collect_information=CollectInformation1(
        bank_details=False,
        business_details=False,
        individual_details=False,
        legal_arrangement_details=False,
        pci_questionnaire=False
    ),
    edit_mode=False,
    mobile_o_auth_callback_url='mobileOAuthCallbackUrl2',
    platform_name='platformName6',
    return_url='returnUrl8'
)
```

