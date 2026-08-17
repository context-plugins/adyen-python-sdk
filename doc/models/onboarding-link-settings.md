
# Onboarding Link Settings

## Structure

`OnboardingLinkSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accepted_countries` | `List[str]` | Optional | The list of countries the user can choose from in hosted onboarding when `editPrefilledCountry` is allowed.<br><br>The value must be in the two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code format.<br><br>The array is empty by default, allowing all [countries and regions supported by hosted onboarding](https://docs.adyen.com/platforms/onboard-users/#hosted-onboarding). |
| `allow_bank_account_format_selection` | `bool` | Optional | Default value: **false**<br><br>Indicates if the user can select the format for their payout account (if applicable). |
| `allow_debug_ui` | `bool` | Optional | Default value: **true**<br><br>Indicates whether the debug user interface (UI) is enabled. The debug UI provides information for your support staff to diagnose and resolve user issues during onboarding. It can be accessed using a keyboard shortcut. |
| `allow_intra_region_cross_border_payout` | `bool` | Optional | Default value: **false**<br><br>Indicates if the user can select a payout account in a different EU/EEA location (including Switzerland and the UK) than the location of their legal entity. |
| `change_legal_entity_type` | `bool` | Optional | Default value: **true**<br><br>Indicates if the user can change their legal entity type. |
| `edit_prefilled_country` | `bool` | Optional | Default value: **true**<br><br>Indicates if the user can change the country of their legal entity's address, for example the registered address of an organization. |
| `enforce_legal_age` | `bool` | Optional | Default value: **false**<br><br>Indicates if only users above the age of 18 can be onboarded. |
| `hide_onboarding_introduction_individual` | `bool` | Optional | Default value: **true**<br><br>Indicates whether the introduction screen is hidden for the user of the individual legal entity type.<br>The introduction screen provides brief instructions for the subsequent steps in the hosted onboarding process. |
| `hide_onboarding_introduction_organization` | `bool` | Optional | Default value: **true**<br><br>Indicates whether the introduction screen is hidden for the user of the organization legal entity type.<br>The introduction screen provides brief instructions for the subsequent steps in the hosted onboarding process. |
| `hide_onboarding_introduction_sole_proprietor` | `bool` | Optional | Default value: **true**<br><br>Indicates whether the introduction screen is hidden for the user of the sole proprietorship legal entity type.<br>The introduction screen provides brief instructions for the subsequent steps in the hosted onboarding process. |
| `hide_onboarding_introduction_trust` | `bool` | Optional | Default value: **true**<br><br>Indicates whether the introduction screen is hidden for the user of the trust legal entity type.<br>The introduction screen provides brief instructions for the subsequent steps in the hosted onboarding process. |
| `instant_bank_verification` | `bool` | Optional | Default value: **true**<br><br>Indicates if the user can initiate the verification process through open banking providers, like Plaid or Tink. |
| `require_pci_sign_ecom_moto` | `bool` | Optional | Default value: **false**<br><br>Indicates if the user is required to sign a PCI questionnaires for the **ecomMoto** sales channel type. |
| `require_pci_sign_ecommerce` | `bool` | Optional | Default value: **false**<br><br>Indicates if the user is required to sign a PCI questionnaires for the **eCommerce** sales channel type. |
| `require_pci_sign_pos` | `bool` | Optional | Default value: **false**<br><br>Indicates if the user is required to sign a PCI questionnaires for the **pos** sales channel type. |
| `require_pci_sign_pos_moto` | `bool` | Optional | Default value: **false**<br><br>Indicates if the user is required to sign a PCI questionnaires for the **posMoto** sales channel type. |
| `transfer_instrument_limit` | `int` | Optional | The maximum number of transfer instruments the user can create. |

## Example

```python
from adyen.models.onboarding_link_settings import OnboardingLinkSettings

onboarding_link_settings = OnboardingLinkSettings(
    accepted_countries=[
        'acceptedCountries1',
        'acceptedCountries2'
    ],
    allow_bank_account_format_selection=False,
    allow_debug_ui=False,
    allow_intra_region_cross_border_payout=False,
    change_legal_entity_type=False
)
```

