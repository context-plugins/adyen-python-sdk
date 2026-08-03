
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| merchant_account | `str` | *Default*: `"merchantAccountDefaultValue"` |
| device_id | `str` | *Default*: `"deviceIdDefaultValue"` |
| environment | [`Environment`](../README.md#environments) | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT", "GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](../doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](../doc/logging-configuration.md) | The SDK logging configuration for API calls |
| api_key_auth_credentials | [`ApiKeyAuthCredentials`](auth/custom-header-signature.md) | The credential object for Custom Header Signature |
| basic_auth_credentials | [`BasicAuthCredentials`](auth/basic-authentication.md) | The credential object for Basic Authentication |
| client_key_credentials | [`ClientKeyCredentials`](auth/custom-query-parameter.md) | The credential object for Custom Query Parameter |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
import logging

from adyen.adyen_client import AdyenClient
from adyen.configuration import Environment
from adyen.http.auth.api_key_auth import ApiKeyAuthCredentials
from adyen.http.auth.basic_auth import BasicAuthCredentials
from adyen.http.auth.client_key import ClientKeyCredentials
from adyen.logging.configuration.api_logging_configuration import LoggingConfiguration
from adyen.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from adyen.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration

client = AdyenClient(
    api_key_auth_credentials=ApiKeyAuthCredentials(
        x_api_key='X-API-Key'
    ),
    basic_auth_credentials=BasicAuthCredentials(
        username='Username',
        password='Password'
    ),
    client_key_credentials=ClientKeyCredentials(
        client_key='clientKey'
    ),
    environment=Environment.PRODUCTION,
    merchant_account='merchantAccountDefaultValue',
    device_id='deviceIdDefaultValue',
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)
```

## Environment-Based Client Initialization

```python
from adyen.adyen_client import AdyenClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = AdyenClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## Adyen Client

The gateway for the SDK. This class acts as a factory for the Apis and also holds the configuration of the SDK.

## Apis

| Name | Description |
|  --- | --- |
| payments | Gets PaymentsApi |
| i_deal_profiles | Gets IdealProfilesApi |
| account_holders | Gets AccountHoldersApi |
| accounts | Gets AccountsApi |
| verification | Gets VerificationApi |
| balances_overview | Gets BalancesOverviewApi |
| balance_transfers | Gets BalanceTransfersApi |
| platform | Gets PlatformApi |
| balance_accounts | Gets BalanceAccountsApi |
| balances | Gets BalancesApi |
| managed_payout_schedules | Gets ManagedPayoutSchedulesApi |
| custom_payout_schedules_sweeps | Gets CustomPayoutSchedulesSweepsApi |
| authorized_card_users | Gets AuthorizedCardUsersApi |
| recurring_top_ups | Gets RecurringTopUpsApi |
| payment_instruments | Gets PaymentInstrumentsApi |
| payment_instrument_groups | Gets PaymentInstrumentGroupsApi |
| transaction_rules | Gets TransactionRulesApi |
| bank_account_validation | Gets BankAccountValidationApi |
| network_tokens | Gets NetworkTokensApi |
| grant_accounts | Gets GrantAccountsApi |
| grant_offers | Gets GrantOffersApi |
| card_orders | Gets CardOrdersApi |
| direct_debit_mandates | Gets DirectDebitMandatesApi |
| manage_card_pin | Gets ManageCardPinApi |
| transfer_routes | Gets TransferRoutesApi |
| sca_device_management | Gets ScaDeviceManagementApi |
| transfer_limits_balance_account_level | Gets TransferLimitsBalanceAccountLevelApi |
| transfer_limits_balance_platform_level | Gets TransferLimitsBalancePlatformLevelApi |
| manage_sca_devices | Gets ManageScaDevicesApi |
| sca_association_management | Gets ScaAssociationManagementApi |
| general | Gets GeneralApi |
| dynamic_offers | Gets DynamicOffersApi |
| grants | Gets GrantsApi |
| donations | Gets DonationsApi |
| payment_links | Gets PaymentLinksApi |
| modifications | Gets ModificationsApi |
| recurring | Gets RecurringApi |
| orders | Gets OrdersApi |
| utility | Gets UtilityApi |
| cloud_endpoints_and_connection | Gets CloudEndpointsAndConnectionApi |
| rates | Gets RatesApi |
| hosted_onboarding_page | Gets HostedOnboardingPageApi |
| pci_compliance_questionnaire_page | Gets PciComplianceQuestionnairePageApi |
| legal_entities | Gets LegalEntitiesApi |
| transfer_instruments | Gets TransferInstrumentsApi |
| business_lines | Gets BusinessLinesApi |
| documents | Gets DocumentsApi |
| terms_of_service | Gets TermsOfServiceApi |
| pci_questionnaires | Gets PciQuestionnairesApi |
| tax_e_delivery_consent | Gets TaxEDeliveryConsentApi |
| hosted_onboarding | Gets HostedOnboardingApi |
| account_company_level | Gets AccountCompanyLevelApi |
| account_merchant_level | Gets AccountMerchantLevelApi |
| account_store_level | Gets AccountStoreLevelApi |
| payout_settings_merchant_level | Gets PayoutSettingsMerchantLevelApi |
| users_company_level | Gets UsersCompanyLevelApi |
| users_merchant_level | Gets UsersMerchantLevelApi |
| my_api_credential | Gets MyApiCredentialApi |
| api_credentials_company_level | Gets ApiCredentialsCompanyLevelApi |
| api_credentials_merchant_level | Gets ApiCredentialsMerchantLevelApi |
| api_key_company_level | Gets ApiKeyCompanyLevelApi |
| api_key_merchant_level | Gets ApiKeyMerchantLevelApi |
| client_key_company_level | Gets ClientKeyCompanyLevelApi |
| client_key_merchant_level | Gets ClientKeyMerchantLevelApi |
| allowed_origins_company_level | Gets AllowedOriginsCompanyLevelApi |
| allowed_origins_merchant_level | Gets AllowedOriginsMerchantLevelApi |
| webhooks_company_level | Gets WebhooksCompanyLevelApi |
| webhooks_merchant_level | Gets WebhooksMerchantLevelApi |
| payment_methods_merchant_level | Gets PaymentMethodsMerchantLevelApi |
| terminals_terminal_level | Gets TerminalsTerminalLevelApi |
| terminal_actions_company_level | Gets TerminalActionsCompanyLevelApi |
| terminal_actions_terminal_level | Gets TerminalActionsTerminalLevelApi |
| terminal_orders_company_level | Gets TerminalOrdersCompanyLevelApi |
| terminal_orders_merchant_level | Gets TerminalOrdersMerchantLevelApi |
| terminal_settings_company_level | Gets TerminalSettingsCompanyLevelApi |
| terminal_settings_merchant_level | Gets TerminalSettingsMerchantLevelApi |
| terminal_settings_store_level | Gets TerminalSettingsStoreLevelApi |
| terminal_settings_terminal_level | Gets TerminalSettingsTerminalLevelApi |
| android_files_company_level | Gets AndroidFilesCompanyLevelApi |
| split_configuration_merchant_level | Gets SplitConfigurationMerchantLevelApi |
| donation_campaigns | Gets DonationCampaignsApi |
| account_verification | Gets AccountVerificationApi |
| payments_app | Gets PaymentsAppApi |
| initialization | Gets InitializationApi |
| reviewing | Gets ReviewingApi |
| instant_payouts | Gets InstantPayoutsApi |
| dispute_attachments | Gets DisputeAttachmentsApi |
| raise_disputes | Gets RaiseDisputesApi |
| session_authentication | Gets SessionAuthenticationApi |
| transfers | Gets TransfersApi |
| transactions | Gets TransactionsApi |
| capital | Gets CapitalApi |
| cash_out | Gets CashOutApi |
| api | Gets Api |

