from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OnboardingLinkSettings2(SdkBaseModel):
    """Key-value pairs indicating the settings for the hosted onboarding page. The key represents a specific setting."""

    accepted_countries: Optional[list[str]] = Field(default=UNSET, alias="acceptedCountries")
    """The list of countries the user can choose from in hosted onboarding when ``editPrefilledCountry`` is allowed.

    The value must be in the two-character `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__
    country code format.

    The array is empty by default, allowing all `countries and regions supported by hosted onboarding
    <https://docs.adyen.com/platforms/onboard-users/#hosted-onboarding>`__."""

    allow_bank_account_format_selection: Optional[bool] = Field(default=UNSET, alias="allowBankAccountFormatSelection")
    """Default value: **false**

    Indicates if the user can select the format for their payout account (if applicable)."""

    allow_debug_ui: Optional[bool] = Field(default=UNSET, alias="allowDebugUi")
    """Default value: **true**

    Indicates whether the debug user interface (UI) is enabled. The debug UI provides information for your support staff
    to diagnose and resolve user issues during onboarding. It can be accessed using a keyboard shortcut."""

    allow_intra_region_cross_border_payout: Optional[bool] = Field(
        default=UNSET, alias="allowIntraRegionCrossBorderPayout"
    )
    """Default value: **false**

    Indicates if the user can select a payout account in a different EU/EEA location (including Switzerland and the UK)
    than the location of their legal entity."""

    change_legal_entity_type: Optional[bool] = Field(default=UNSET, alias="changeLegalEntityType")
    """Default value: **true**

    Indicates if the user can change their legal entity type."""

    edit_prefilled_country: Optional[bool] = Field(default=UNSET, alias="editPrefilledCountry")
    """Default value: **true**

    Indicates if the user can change the country of their legal entity's address, for example the registered address of
    an organization."""

    enforce_legal_age: Optional[bool] = Field(default=UNSET, alias="enforceLegalAge")
    """Default value: **false**

    Indicates if only users above the age of 18 can be onboarded."""

    hide_onboarding_introduction_individual: Optional[bool] = Field(
        default=UNSET, alias="hideOnboardingIntroductionIndividual"
    )
    """Default value: **true**

    Indicates whether the introduction screen is hidden for the user of the individual legal entity type. The
    introduction screen provides brief instructions for the subsequent steps in the hosted onboarding process."""

    hide_onboarding_introduction_organization: Optional[bool] = Field(
        default=UNSET, alias="hideOnboardingIntroductionOrganization"
    )
    """Default value: **true**

    Indicates whether the introduction screen is hidden for the user of the organization legal entity type. The
    introduction screen provides brief instructions for the subsequent steps in the hosted onboarding process."""

    hide_onboarding_introduction_sole_proprietor: Optional[bool] = Field(
        default=UNSET, alias="hideOnboardingIntroductionSoleProprietor"
    )
    """Default value: **true**

    Indicates whether the introduction screen is hidden for the user of the sole proprietorship legal entity type. The
    introduction screen provides brief instructions for the subsequent steps in the hosted onboarding process."""

    hide_onboarding_introduction_trust: Optional[bool] = Field(default=UNSET, alias="hideOnboardingIntroductionTrust")
    """Default value: **true**

    Indicates whether the introduction screen is hidden for the user of the trust legal entity type. The introduction
    screen provides brief instructions for the subsequent steps in the hosted onboarding process."""

    instant_bank_verification: Optional[bool] = Field(default=UNSET, alias="instantBankVerification")
    """Default value: **true**

    Indicates if the user can initiate the verification process through open banking providers, like Plaid or Tink."""

    require_pci_sign_ecom_moto: Optional[bool] = Field(default=UNSET, alias="requirePciSignEcomMoto")
    """Default value: **false**

    Indicates if the user is required to sign a PCI questionnaires for the **ecomMoto** sales channel type."""

    require_pci_sign_ecommerce: Optional[bool] = Field(default=UNSET, alias="requirePciSignEcommerce")
    """Default value: **false**

    Indicates if the user is required to sign a PCI questionnaires for the **eCommerce** sales channel type."""

    require_pci_sign_pos: Optional[bool] = Field(default=UNSET, alias="requirePciSignPos")
    """Default value: **false**

    Indicates if the user is required to sign a PCI questionnaires for the **pos** sales channel type."""

    require_pci_sign_pos_moto: Optional[bool] = Field(default=UNSET, alias="requirePciSignPosMoto")
    """Default value: **false**

    Indicates if the user is required to sign a PCI questionnaires for the **posMoto** sales channel type."""

    transfer_instrument_limit: Optional[int] = Field(default=UNSET, alias="transferInstrumentLimit")
    """The maximum number of transfer instruments the user can create."""


class OnboardingLinkSettings2Dict(TypedDict):
    accepted_countries: NotRequired[list[str]]
    allow_bank_account_format_selection: NotRequired[bool]
    allow_debug_ui: NotRequired[bool]
    allow_intra_region_cross_border_payout: NotRequired[bool]
    change_legal_entity_type: NotRequired[bool]
    edit_prefilled_country: NotRequired[bool]
    enforce_legal_age: NotRequired[bool]
    hide_onboarding_introduction_individual: NotRequired[bool]
    hide_onboarding_introduction_organization: NotRequired[bool]
    hide_onboarding_introduction_sole_proprietor: NotRequired[bool]
    hide_onboarding_introduction_trust: NotRequired[bool]
    instant_bank_verification: NotRequired[bool]
    require_pci_sign_ecom_moto: NotRequired[bool]
    require_pci_sign_ecommerce: NotRequired[bool]
    require_pci_sign_pos: NotRequired[bool]
    require_pci_sign_pos_moto: NotRequired[bool]
    transfer_instrument_limit: NotRequired[int]
