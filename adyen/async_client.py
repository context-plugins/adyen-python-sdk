from __future__ import annotations

from functools import cached_property
from types import TracebackType
from typing import Any
from uuid import UUID, uuid4

from typing_extensions import Self

from .apis.account_company_level import AsyncAccountCompanyLevel
from .apis.account_holders import AsyncAccountHolders
from .apis.account_merchant_level import AsyncAccountMerchantLevel
from .apis.account_store_level import AsyncAccountStoreLevel
from .apis.account_verification import AsyncAccountVerification
from .apis.accounts import AsyncAccounts
from .apis.allowed_origins_company_level import AsyncAllowedOriginsCompanyLevel
from .apis.allowed_origins_merchant_level import AsyncAllowedOriginsMerchantLevel
from .apis.android_files_company_level import AsyncAndroidFilesCompanyLevel
from .apis.api_credentials_company_level import AsyncApiCredentialsCompanyLevel
from .apis.api_credentials_merchant_level import AsyncApiCredentialsMerchantLevel
from .apis.api_key_company_level import AsyncApiKeyCompanyLevel
from .apis.api_key_merchant_level import AsyncApiKeyMerchantLevel
from .apis.authorized_card_users import AsyncAuthorizedCardUsers
from .apis.balance_accounts import AsyncBalanceAccounts
from .apis.balance_transfers import AsyncBalanceTransfers
from .apis.balances import AsyncBalances
from .apis.balances_overview import AsyncBalancesOverview
from .apis.bank_account_validation import AsyncBankAccountValidation
from .apis.business_lines_api import AsyncBusinessLinesApi
from .apis.capital import AsyncCapital
from .apis.card_orders import AsyncCardOrders
from .apis.cash_out_api import AsyncCashOutApi
from .apis.client_key_company_level import AsyncClientKeyCompanyLevel
from .apis.client_key_merchant_level import AsyncClientKeyMerchantLevel
from .apis.custom_payout_schedules_sweeps import AsyncCustomPayoutSchedulesSweeps
from .apis.direct_debit_mandates import AsyncDirectDebitMandates
from .apis.dispute_attachments import AsyncDisputeAttachments
from .apis.documents import AsyncDocuments
from .apis.donation_campaigns import AsyncDonationCampaigns
from .apis.donations import AsyncDonations
from .apis.dynamic_offers import AsyncDynamicOffers
from .apis.general import AsyncGeneral
from .apis.grant_accounts import AsyncGrantAccounts
from .apis.grant_offers_api import AsyncGrantOffersApi
from .apis.grants_api import AsyncGrantsApi
from .apis.hosted_onboarding import AsyncHostedOnboarding
from .apis.hosted_onboarding_page import AsyncHostedOnboardingPage
from .apis.i_deal_profiles import AsyncIDealProfiles
from .apis.initialization import AsyncInitialization
from .apis.instant_payouts import AsyncInstantPayouts
from .apis.legal_entities import AsyncLegalEntities
from .apis.manage_card_pin import AsyncManageCardPin
from .apis.manage_sca_devices import AsyncManageScaDevices
from .apis.managed_payout_schedules import AsyncManagedPayoutSchedules
from .apis.modifications import AsyncModifications
from .apis.my_api_credential import AsyncMyApiCredential
from .apis.network_tokens import AsyncNetworkTokens
from .apis.orders import AsyncOrders
from .apis.payment_instrument_groups import AsyncPaymentInstrumentGroups
from .apis.payment_instruments import AsyncPaymentInstruments
from .apis.payment_links import AsyncPaymentLinks
from .apis.payment_methods_merchant_level import AsyncPaymentMethodsMerchantLevel
from .apis.payments import AsyncPayments
from .apis.payments_app import AsyncPaymentsApp
from .apis.payout_settings_merchant_level import AsyncPayoutSettingsMerchantLevel
from .apis.pci_compliance_questionnaire_page import AsyncPciComplianceQuestionnairePage
from .apis.pci_questionnaires import AsyncPciQuestionnaires
from .apis.platform import AsyncPlatform
from .apis.raise_disputes import AsyncRaiseDisputes
from .apis.rates import AsyncRates
from .apis.recurring_api import AsyncRecurringApi
from .apis.recurring_top_ups import AsyncRecurringTopUps
from .apis.reviewing import AsyncReviewing
from .apis.sca_association_management import AsyncScaAssociationManagement
from .apis.sca_device_management import AsyncScaDeviceManagement
from .apis.session_authentication import AsyncSessionAuthentication
from .apis.split_configuration_merchant_level import AsyncSplitConfigurationMerchantLevel
from .apis.tax_e_delivery_consent import AsyncTaxEDeliveryConsent
from .apis.terminal_actions_company_level import AsyncTerminalActionsCompanyLevel
from .apis.terminal_actions_terminal_level import AsyncTerminalActionsTerminalLevel
from .apis.terminal_orders_company_level import AsyncTerminalOrdersCompanyLevel
from .apis.terminal_orders_merchant_level import AsyncTerminalOrdersMerchantLevel
from .apis.terminal_settings_company_level import AsyncTerminalSettingsCompanyLevel
from .apis.terminal_settings_merchant_level import AsyncTerminalSettingsMerchantLevel
from .apis.terminal_settings_store_level import AsyncTerminalSettingsStoreLevel
from .apis.terminal_settings_terminal_level import AsyncTerminalSettingsTerminalLevel
from .apis.terminals_terminal_level import AsyncTerminalsTerminalLevel
from .apis.terms_of_service import AsyncTermsOfService
from .apis.transaction_rules import AsyncTransactionRules
from .apis.transactions import AsyncTransactions
from .apis.transfer_instruments import AsyncTransferInstruments
from .apis.transfer_limits_balance_account_level import AsyncTransferLimitsBalanceAccountLevel
from .apis.transfer_limits_balance_platform_level import AsyncTransferLimitsBalancePlatformLevel
from .apis.transfer_routes import AsyncTransferRoutes
from .apis.transfers import AsyncTransfers
from .apis.users_company_level import AsyncUsersCompanyLevel
from .apis.users_merchant_level import AsyncUsersMerchantLevel
from .apis.utility import AsyncUtility
from .apis.verification import AsyncVerification
from .apis.webhooks_company_level import AsyncWebhooksCompanyLevel
from .apis.webhooks_merchant_level import AsyncWebhooksMerchantLevel
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseAdyenClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    ApiKeyQueryScheme,
    ApiResult,
    AsyncAnySchemes,
    AsyncHttpClient,
    AsyncHttpx2Client,
    AsyncRawClient,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    RawError,
    RequestOptionsOrDict,
    RetryOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    no_auth,
    param,
    raw_error_response,
    unwrap,
)
from .models.abort_request import AbortRequest, AbortRequestDict
from .models.admin_request import AdminRequest, AdminRequestDict
from .models.admin_response import AdminResponse
from .models.balance_inquiry_request import BalanceInquiryRequest, BalanceInquiryRequestDict
from .models.balance_inquiry_response import BalanceInquiryResponse
from .models.card_acquisition_request import CardAcquisitionRequest, CardAcquisitionRequestDict
from .models.card_acquisition_response import CardAcquisitionResponse
from .models.card_reader_apdurequest import CardReaderApdurequest, CardReaderApdurequestDict
from .models.card_reader_apduresponse import CardReaderApduresponse
from .models.diagnosis_request import DiagnosisRequest, DiagnosisRequestDict
from .models.diagnosis_response import DiagnosisResponse
from .models.display_request import DisplayRequest, DisplayRequestDict
from .models.display_response import DisplayResponse
from .models.enable_service_request import EnableServiceRequest, EnableServiceRequestDict
from .models.enable_service_response import EnableServiceResponse
from .models.get_totals_request import GetTotalsRequest, GetTotalsRequestDict
from .models.get_totals_response import GetTotalsResponse
from .models.input_request import InputRequest, InputRequestDict
from .models.input_response import InputResponse
from .models.login_request import LoginRequest, LoginRequestDict
from .models.login_response import LoginResponse
from .models.logout_request import LogoutRequest, LogoutRequestDict
from .models.logout_response import LogoutResponse
from .models.payment_request2 import PaymentRequest2, PaymentRequest2Dict
from .models.payment_response4 import PaymentResponse4
from .models.print_request import PrintRequest, PrintRequestDict
from .models.print_response import PrintResponse
from .models.reconciliation_request import ReconciliationRequest, ReconciliationRequestDict
from .models.reconciliation_response import ReconciliationResponse
from .models.reversal_request import ReversalRequest, ReversalRequestDict
from .models.reversal_response import ReversalResponse
from .models.stored_value_request import StoredValueRequest, StoredValueRequestDict
from .models.stored_value_response import StoredValueResponse
from .models.transaction_status_request import TransactionStatusRequest, TransactionStatusRequestDict
from .models.transaction_status_response import TransactionStatusResponse
from .server.server import Server
from .server.server_config import ServerConfigOrDict


class AsyncAdyenClient(BaseAdyenClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        server_config: ServerConfigOrDict | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        custom_async_http_client: AsyncHttpClient | None = None,
        api_key_auth: str | None = None,
        basic_auth: BasicAuthCredentialsOrDict | None = None,
        client_key: str | None = None,
    ) -> None:
        super().__init__(server_config=server_config, timeout=timeout, retry_options=retry_options)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpx2Client(timeout=timeout)
            ),
            retry_options=self._retry_options,
            global_headers=[
                param[str]("User-Agent", "AdyenClient/72 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "72"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            api_key_auth=ApiKeyHeaderScheme("X-API-Key", api_key_auth) if api_key_auth is not None else no_auth,
            basic_auth=BasicAuthScheme(BasicAuthCredentials.coerce(basic_auth)) if basic_auth is not None else no_auth,
            client_key=ApiKeyQueryScheme("clientKey", client_key) if client_key is not None else no_auth,
        )

    @cached_property
    def api_credentials_company_level(self) -> AsyncApiCredentialsCompanyLevel:
        return AsyncApiCredentialsCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def api_credentials_merchant_level(self) -> AsyncApiCredentialsMerchantLevel:
        return AsyncApiCredentialsMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def api_key_company_level(self) -> AsyncApiKeyCompanyLevel:
        return AsyncApiKeyCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def api_key_merchant_level(self) -> AsyncApiKeyMerchantLevel:
        return AsyncApiKeyMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def account_company_level(self) -> AsyncAccountCompanyLevel:
        return AsyncAccountCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def account_merchant_level(self) -> AsyncAccountMerchantLevel:
        return AsyncAccountMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def account_store_level(self) -> AsyncAccountStoreLevel:
        return AsyncAccountStoreLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def account_verification(self) -> AsyncAccountVerification:
        return AsyncAccountVerification(self._raw_client, self._server)

    @cached_property
    def account_holders(self) -> AsyncAccountHolders:
        return AsyncAccountHolders(self._raw_client, self._server, self._auth)

    @cached_property
    def accounts(self) -> AsyncAccounts:
        return AsyncAccounts(self._raw_client, self._server, self._auth)

    @cached_property
    def allowed_origins_company_level(self) -> AsyncAllowedOriginsCompanyLevel:
        return AsyncAllowedOriginsCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def allowed_origins_merchant_level(self) -> AsyncAllowedOriginsMerchantLevel:
        return AsyncAllowedOriginsMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def android_files_company_level(self) -> AsyncAndroidFilesCompanyLevel:
        return AsyncAndroidFilesCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def authorized_card_users(self) -> AsyncAuthorizedCardUsers:
        return AsyncAuthorizedCardUsers(self._raw_client, self._server)

    @cached_property
    def balance_accounts(self) -> AsyncBalanceAccounts:
        return AsyncBalanceAccounts(self._raw_client, self._server, self._auth)

    @cached_property
    def balance_transfers(self) -> AsyncBalanceTransfers:
        return AsyncBalanceTransfers(self._raw_client, self._server)

    @cached_property
    def balances(self) -> AsyncBalances:
        return AsyncBalances(self._raw_client, self._server)

    @cached_property
    def balances_overview(self) -> AsyncBalancesOverview:
        return AsyncBalancesOverview(self._raw_client, self._server)

    @cached_property
    def bank_account_validation(self) -> AsyncBankAccountValidation:
        return AsyncBankAccountValidation(self._raw_client, self._server, self._auth)

    @cached_property
    def business_lines_api(self) -> AsyncBusinessLinesApi:
        return AsyncBusinessLinesApi(self._raw_client, self._server, self._auth)

    @cached_property
    def capital(self) -> AsyncCapital:
        return AsyncCapital(self._raw_client, self._server, self._auth)

    @cached_property
    def card_orders(self) -> AsyncCardOrders:
        return AsyncCardOrders(self._raw_client, self._server, self._auth)

    @cached_property
    def cash_out_api(self) -> AsyncCashOutApi:
        return AsyncCashOutApi(self._raw_client, self._server)

    @cached_property
    def client_key_company_level(self) -> AsyncClientKeyCompanyLevel:
        return AsyncClientKeyCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def client_key_merchant_level(self) -> AsyncClientKeyMerchantLevel:
        return AsyncClientKeyMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def custom_payout_schedules_sweeps(self) -> AsyncCustomPayoutSchedulesSweeps:
        return AsyncCustomPayoutSchedulesSweeps(self._raw_client, self._server, self._auth)

    @cached_property
    def direct_debit_mandates(self) -> AsyncDirectDebitMandates:
        return AsyncDirectDebitMandates(self._raw_client, self._server)

    @cached_property
    def dispute_attachments(self) -> AsyncDisputeAttachments:
        return AsyncDisputeAttachments(self._raw_client, self._server)

    @cached_property
    def documents(self) -> AsyncDocuments:
        return AsyncDocuments(self._raw_client, self._server, self._auth)

    @cached_property
    def donation_campaigns(self) -> AsyncDonationCampaigns:
        return AsyncDonationCampaigns(self._raw_client, self._server, self._auth)

    @cached_property
    def donations(self) -> AsyncDonations:
        return AsyncDonations(self._raw_client, self._server, self._auth)

    @cached_property
    def dynamic_offers(self) -> AsyncDynamicOffers:
        return AsyncDynamicOffers(self._raw_client, self._server)

    @cached_property
    def general(self) -> AsyncGeneral:
        return AsyncGeneral(self._raw_client, self._server, self._auth)

    @cached_property
    def grant_accounts(self) -> AsyncGrantAccounts:
        return AsyncGrantAccounts(self._raw_client, self._server, self._auth)

    @cached_property
    def grant_offers_api(self) -> AsyncGrantOffersApi:
        return AsyncGrantOffersApi(self._raw_client, self._server, self._auth)

    @cached_property
    def grants_api(self) -> AsyncGrantsApi:
        return AsyncGrantsApi(self._raw_client, self._server)

    @cached_property
    def hosted_onboarding(self) -> AsyncHostedOnboarding:
        return AsyncHostedOnboarding(self._raw_client, self._server, self._auth)

    @cached_property
    def hosted_onboarding_page(self) -> AsyncHostedOnboardingPage:
        return AsyncHostedOnboardingPage(self._raw_client, self._server, self._auth)

    @cached_property
    def initialization(self) -> AsyncInitialization:
        return AsyncInitialization(self._raw_client, self._server, self._auth)

    @cached_property
    def instant_payouts(self) -> AsyncInstantPayouts:
        return AsyncInstantPayouts(self._raw_client, self._server, self._auth)

    @cached_property
    def legal_entities(self) -> AsyncLegalEntities:
        return AsyncLegalEntities(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_sca_devices(self) -> AsyncManageScaDevices:
        return AsyncManageScaDevices(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_card_pin(self) -> AsyncManageCardPin:
        return AsyncManageCardPin(self._raw_client, self._server, self._auth)

    @cached_property
    def managed_payout_schedules(self) -> AsyncManagedPayoutSchedules:
        return AsyncManagedPayoutSchedules(self._raw_client, self._server)

    @cached_property
    def modifications(self) -> AsyncModifications:
        return AsyncModifications(self._raw_client, self._server, self._auth)

    @cached_property
    def my_api_credential(self) -> AsyncMyApiCredential:
        return AsyncMyApiCredential(self._raw_client, self._server, self._auth)

    @cached_property
    def network_tokens(self) -> AsyncNetworkTokens:
        return AsyncNetworkTokens(self._raw_client, self._server, self._auth)

    @cached_property
    def orders(self) -> AsyncOrders:
        return AsyncOrders(self._raw_client, self._server, self._auth)

    @cached_property
    def pci_compliance_questionnaire_page(self) -> AsyncPciComplianceQuestionnairePage:
        return AsyncPciComplianceQuestionnairePage(self._raw_client, self._server, self._auth)

    @cached_property
    def pci_questionnaires(self) -> AsyncPciQuestionnaires:
        return AsyncPciQuestionnaires(self._raw_client, self._server, self._auth)

    @cached_property
    def payment_instrument_groups(self) -> AsyncPaymentInstrumentGroups:
        return AsyncPaymentInstrumentGroups(self._raw_client, self._server, self._auth)

    @cached_property
    def payment_instruments(self) -> AsyncPaymentInstruments:
        return AsyncPaymentInstruments(self._raw_client, self._server, self._auth)

    @cached_property
    def payment_links(self) -> AsyncPaymentLinks:
        return AsyncPaymentLinks(self._raw_client, self._server, self._auth)

    @cached_property
    def payment_methods_merchant_level(self) -> AsyncPaymentMethodsMerchantLevel:
        return AsyncPaymentMethodsMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def payments(self) -> AsyncPayments:
        return AsyncPayments(self._raw_client, self._server, self._auth)

    @cached_property
    def payments_app(self) -> AsyncPaymentsApp:
        return AsyncPaymentsApp(self._raw_client, self._server)

    @cached_property
    def payout_settings_merchant_level(self) -> AsyncPayoutSettingsMerchantLevel:
        return AsyncPayoutSettingsMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def platform(self) -> AsyncPlatform:
        return AsyncPlatform(self._raw_client, self._server, self._auth)

    @cached_property
    def raise_disputes(self) -> AsyncRaiseDisputes:
        return AsyncRaiseDisputes(self._raw_client, self._server)

    @cached_property
    def rates(self) -> AsyncRates:
        return AsyncRates(self._raw_client, self._server)

    @cached_property
    def recurring_api(self) -> AsyncRecurringApi:
        return AsyncRecurringApi(self._raw_client, self._server, self._auth)

    @cached_property
    def recurring_top_ups(self) -> AsyncRecurringTopUps:
        return AsyncRecurringTopUps(self._raw_client, self._server)

    @cached_property
    def reviewing(self) -> AsyncReviewing:
        return AsyncReviewing(self._raw_client, self._server, self._auth)

    @cached_property
    def sca_association_management(self) -> AsyncScaAssociationManagement:
        return AsyncScaAssociationManagement(self._raw_client, self._server)

    @cached_property
    def sca_device_management(self) -> AsyncScaDeviceManagement:
        return AsyncScaDeviceManagement(self._raw_client, self._server)

    @cached_property
    def session_authentication(self) -> AsyncSessionAuthentication:
        return AsyncSessionAuthentication(self._raw_client, self._server)

    @cached_property
    def split_configuration_merchant_level(self) -> AsyncSplitConfigurationMerchantLevel:
        return AsyncSplitConfigurationMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def tax_e_delivery_consent(self) -> AsyncTaxEDeliveryConsent:
        return AsyncTaxEDeliveryConsent(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_actions_company_level(self) -> AsyncTerminalActionsCompanyLevel:
        return AsyncTerminalActionsCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_actions_terminal_level(self) -> AsyncTerminalActionsTerminalLevel:
        return AsyncTerminalActionsTerminalLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_orders_company_level(self) -> AsyncTerminalOrdersCompanyLevel:
        return AsyncTerminalOrdersCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_orders_merchant_level(self) -> AsyncTerminalOrdersMerchantLevel:
        return AsyncTerminalOrdersMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_settings_company_level(self) -> AsyncTerminalSettingsCompanyLevel:
        return AsyncTerminalSettingsCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_settings_merchant_level(self) -> AsyncTerminalSettingsMerchantLevel:
        return AsyncTerminalSettingsMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_settings_store_level(self) -> AsyncTerminalSettingsStoreLevel:
        return AsyncTerminalSettingsStoreLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_settings_terminal_level(self) -> AsyncTerminalSettingsTerminalLevel:
        return AsyncTerminalSettingsTerminalLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminals_terminal_level(self) -> AsyncTerminalsTerminalLevel:
        return AsyncTerminalsTerminalLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terms_of_service(self) -> AsyncTermsOfService:
        return AsyncTermsOfService(self._raw_client, self._server, self._auth)

    @cached_property
    def transaction_rules(self) -> AsyncTransactionRules:
        return AsyncTransactionRules(self._raw_client, self._server, self._auth)

    @cached_property
    def transactions(self) -> AsyncTransactions:
        return AsyncTransactions(self._raw_client, self._server, self._auth)

    @cached_property
    def transfer_instruments(self) -> AsyncTransferInstruments:
        return AsyncTransferInstruments(self._raw_client, self._server, self._auth)

    @cached_property
    def transfer_limits_balance_account_level(self) -> AsyncTransferLimitsBalanceAccountLevel:
        return AsyncTransferLimitsBalanceAccountLevel(self._raw_client, self._server)

    @cached_property
    def transfer_limits_balance_platform_level(self) -> AsyncTransferLimitsBalancePlatformLevel:
        return AsyncTransferLimitsBalancePlatformLevel(self._raw_client, self._server)

    @cached_property
    def transfer_routes(self) -> AsyncTransferRoutes:
        return AsyncTransferRoutes(self._raw_client, self._server, self._auth)

    @cached_property
    def transfers(self) -> AsyncTransfers:
        return AsyncTransfers(self._raw_client, self._server, self._auth)

    @cached_property
    def users_company_level(self) -> AsyncUsersCompanyLevel:
        return AsyncUsersCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def users_merchant_level(self) -> AsyncUsersMerchantLevel:
        return AsyncUsersMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def utility(self) -> AsyncUtility:
        return AsyncUtility(self._raw_client, self._server, self._auth)

    @cached_property
    def verification(self) -> AsyncVerification:
        return AsyncVerification(self._raw_client, self._server, self._auth)

    @cached_property
    def webhooks_company_level(self) -> AsyncWebhooksCompanyLevel:
        return AsyncWebhooksCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def webhooks_merchant_level(self) -> AsyncWebhooksMerchantLevel:
        return AsyncWebhooksMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def i_deal_profiles(self) -> AsyncIDealProfiles:
        return AsyncIDealProfiles(self._raw_client, self._server)

    @cached_property
    def with_raw_response(self) -> AsyncApiWithRawResponse:
        return AsyncApiWithRawResponse(self._raw_client, self._server, self._auth)

    async def abort_request(
        self,
        *,
        body: AbortRequest | AbortRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Body of the Abort Request message. It conveys Information requested for identification of the message request
        carrying the transaction to abort. A message to display on the CustomerError Device could be sent by the Sale
        System (DisplayOutput).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A successful ``AbortRequest`` returns a response with a **200 OK** HTTP status code and no body.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.abort_request(body=body, request_options=request_options))

    async def admin_request(
        self,
        *,
        body: AdminRequest | AdminRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminResponse:
        """Empty. Content of the Custom Admin Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            It conveys the result of the Custom Admin. Content of the Custom Admin Response message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.admin_request(body=body, request_options=request_options))

    async def balance_inquiry_request(
        self,
        *,
        body: BalanceInquiryRequest | BalanceInquiryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceInquiryResponse:
        """It conveys Information related to the account for which a Balance Inquiry is requested. Content of the
        Balance Inquiry Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Content of the Balance Inquiry Response message. It conveys the balance and the identification of the
            associated payment, loyalty or stored value account.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.balance_inquiry_request(body=body, request_options=request_options))

    async def card_acquisition_request(
        self,
        *,
        body: CardAcquisitionRequest | CardAcquisitionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CardAcquisitionResponse:
        """It conveys Information related to the payment and loyalty cards to read and analyse. This message pair is
        usually followed by a message pair (e.g. payment or loyalty) which refers to this Card Acquisition message pair.
        Content of the Card Acquisition Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            It conveys Information related to the payment and loyalty cards read and processed by the POI System and
            entered by the Customer. Content of the Card Acquisition Response message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.card_acquisition_request(body=body, request_options=request_options))

    async def card_reader_apdu_request(
        self,
        *,
        body: CardReaderApdurequest | CardReaderApdurequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CardReaderApduresponse:
        """It contains the APDU request to send to the chip of the card, and a possible invitation message to display on
        the CashierInterface or the CustomerInterface. Content of the Card Reader APDU Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Content of the Card Reader APDU Response message. It contains the result of the requested service, APDU
            response sent by the chip of the card in response to the APDU request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.card_reader_apdu_request(body=body, request_options=request_options))

    async def diagnosis_request(
        self,
        *,
        body: DiagnosisRequest | DiagnosisRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DiagnosisResponse:
        """It conveys Information related to the target POI for which the diagnosis is requested. Content of the
        Diagnosis Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            It conveys the result of the requested diagnosis and a possible message to display on a logical device.
            Content of the Diagnosis Response message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.diagnosis_request(body=body, request_options=request_options))

    async def display_request(
        self,
        *,
        body: DisplayRequest | DisplayRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DisplayResponse:
        """It conveys the data to display and the way to process the display. It contains the complete content to
        display. It might contain an operation (the DisplayOutput element) per Display Device type. Content of the
        Display Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            It conveys the result of the display, parallel to the message request, except if response not required and
            absent. Content of the Display Response message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.display_request(body=body, request_options=request_options))

    async def enable_service_request(
        self,
        *,
        body: EnableServiceRequest | EnableServiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EnableServiceResponse:
        """It conveys the services that will be enabled for the POI Terminal without the request of the Sale System, and
        a possible invitation for the Customer to start the services. Content of the Enable Service Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            It conveys the result of the Enable Service processing. Content of the Enable Service Response message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.enable_service_request(body=body, request_options=request_options))

    async def get_totals_request(
        self,
        *,
        body: GetTotalsRequest | GetTotalsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetTotalsResponse:
        """It conveys information from the Sale System related to the scope and the format of the totals to be computed
        by the POI System. Content of the Get Totals Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Content of the Reconciliation Response message. It conveys Information related to the Reconciliation
            transaction processed by the POI System.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.get_totals_request(body=body, request_options=request_options))

    async def input_request(
        self,
        *,
        body: InputRequest | InputRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InputResponse:
        """Content of the ``InputRequest`` message. It conveys the data to display and how to process it. In addition to
        the display on the Input Device, it might contain an operation (the ``DisplayOutput`` element) per Display
        Device type.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            It conveys the result of the input or the result of the outputs, parallel to the message request, except if
            response not required and absent. Content of the Input Response message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.input_request(body=body, request_options=request_options))

    async def login_request(
        self,
        *,
        body: LoginRequest | LoginRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LoginResponse:
        """It conveys information related to the session (period between a Login and the following Logout) to process.
        Content of the ``LoginRequest`` message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            It conveys Information related to the Login to process. Content of the Login Response message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.login_request(body=body, request_options=request_options))

    async def logout_request(
        self,
        *,
        body: LogoutRequest | LogoutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LogoutResponse:
        """Empty. Content of the Logout Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            It conveys the result of the Logout. Content of the Logout Response message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.logout_request(body=body, request_options=request_options))

    async def payment_request(
        self,
        *,
        body: PaymentRequest2 | PaymentRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentResponse4:
        """Request sent to terminal to initiate payment. It conveys Information related to the Payment transaction to
        process. Content of the ``PaymentRequest`` message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            It conveys Information related to the Payment transaction processed by the POI System. Content of the
            Payment Response message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.payment_request(body=body, request_options=request_options))

    async def print_request(
        self,
        *,
        body: PrintRequest | PrintRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PrintResponse:
        """Content of the Print Request message. It conveys the complete data to print and how to process the print.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            It conveys the result of the print, parallel to the message request, except if response not required and
            absent. Content of the Print Response message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.print_request(body=body, request_options=request_options))

    async def reconciliation_request(
        self,
        *,
        body: ReconciliationRequest | ReconciliationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReconciliationResponse:
        """Content of the Reconciliation Request message. It conveys Information related to the Reconciliation requested
        by the Sale System.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            It conveys Information related to the Reconciliation transaction processed by the POI System. Content of the
            Reconciliation Response message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.reconciliation_request(body=body, request_options=request_options))

    async def reversal_request(
        self,
        *,
        body: ReversalRequest | ReversalRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReversalResponse:
        """It conveys Information related to the reversal of a previous payment or a loyalty transaction. Content of the
        Reversal Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            It conveys Information related to the reversal processed by the POI System. Content of the Reversal Response
            message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.reversal_request(body=body, request_options=request_options))

    async def stored_value_request(
        self,
        *,
        body: StoredValueRequest | StoredValueRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredValueResponse:
        """It conveys Information related to the Stored Value transaction to process. Content of the Stored Value
        Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            It conveys Information related to the Stored Value transaction processed by the POI System. Content of the
            Stored Value Response message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self.with_raw_response.stored_value_request(body=body, request_options=request_options))

    async def transaction_status_request(
        self,
        *,
        body: TransactionStatusRequest | TransactionStatusRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransactionStatusResponse:
        """Content of the TransactionStatus Request message. It conveys Information requested for status of the last or
        current Payment, Loyalty or Reversal transaction.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Content of the TransactionStatus Response message. It conveys Information related to the status of the last
            or current Payment, Loyalty or Reversal transaction.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self.with_raw_response.transaction_status_request(body=body, request_options=request_options)
        )

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


class AsyncApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def abort_request(
        self,
        *,
        body: AbortRequest | AbortRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, RawError]:
        """Body of the Abort Request message. It conveys Information requested for identification of the message request
        carrying the transaction to abort. A message to display on the CustomerError Device could be sent by the Sale
        System (DisplayOutput).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/abort"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AbortRequest | AbortRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_request(
        self,
        *,
        body: AdminRequest | AdminRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminResponse, RawError]:
        """Empty. Content of the Custom Admin Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/admin"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminRequest | AdminRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[AdminResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def balance_inquiry_request(
        self,
        *,
        body: BalanceInquiryRequest | BalanceInquiryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceInquiryResponse, RawError]:
        """It conveys Information related to the account for which a Balance Inquiry is requested. Content of the
        Balance Inquiry Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/balanceinquiry"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceInquiryRequest | BalanceInquiryRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[BalanceInquiryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def card_acquisition_request(
        self,
        *,
        body: CardAcquisitionRequest | CardAcquisitionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CardAcquisitionResponse, RawError]:
        """It conveys Information related to the payment and loyalty cards to read and analyse. This message pair is
        usually followed by a message pair (e.g. payment or loyalty) which refers to this Card Acquisition message pair.
        Content of the Card Acquisition Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/cardacquisition"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CardAcquisitionRequest | CardAcquisitionRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CardAcquisitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def card_reader_apdu_request(
        self,
        *,
        body: CardReaderApdurequest | CardReaderApdurequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CardReaderApduresponse, RawError]:
        """It contains the APDU request to send to the chip of the card, and a possible invitation message to display on
        the CashierInterface or the CustomerInterface. Content of the Card Reader APDU Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/cardreaderapdu"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CardReaderApdurequest | CardReaderApdurequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CardReaderApduresponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def diagnosis_request(
        self,
        *,
        body: DiagnosisRequest | DiagnosisRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DiagnosisResponse, RawError]:
        """It conveys Information related to the target POI for which the diagnosis is requested. Content of the
        Diagnosis Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/diagnosis"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DiagnosisRequest | DiagnosisRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[DiagnosisResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def display_request(
        self,
        *,
        body: DisplayRequest | DisplayRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DisplayResponse, RawError]:
        """It conveys the data to display and the way to process the display. It contains the complete content to
        display. It might contain an operation (the DisplayOutput element) per Display Device type. Content of the
        Display Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/display"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisplayRequest | DisplayRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[DisplayResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def enable_service_request(
        self,
        *,
        body: EnableServiceRequest | EnableServiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EnableServiceResponse, RawError]:
        """It conveys the services that will be enabled for the POI Terminal without the request of the Sale System, and
        a possible invitation for the Customer to start the services. Content of the Enable Service Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/enableservice"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[EnableServiceRequest | EnableServiceRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[EnableServiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_totals_request(
        self,
        *,
        body: GetTotalsRequest | GetTotalsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetTotalsResponse, RawError]:
        """It conveys information from the Sale System related to the scope and the format of the totals to be computed
        by the POI System. Content of the Get Totals Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/gettotals"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetTotalsRequest | GetTotalsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GetTotalsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def input_request(
        self,
        *,
        body: InputRequest | InputRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InputResponse, RawError]:
        """Content of the ``InputRequest`` message. It conveys the data to display and how to process it. In addition to
        the display on the Input Device, it might contain an operation (the ``DisplayOutput`` element) per Display
        Device type.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/input"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InputRequest | InputRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[InputResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def login_request(
        self,
        *,
        body: LoginRequest | LoginRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LoginResponse, RawError]:
        """It conveys information related to the session (period between a Login and the following Logout) to process.
        Content of the ``LoginRequest`` message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/login"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LoginRequest | LoginRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[LoginResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def logout_request(
        self,
        *,
        body: LogoutRequest | LogoutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LogoutResponse, RawError]:
        """Empty. Content of the Logout Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/logout"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LogoutRequest | LogoutRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[LogoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def payment_request(
        self,
        *,
        body: PaymentRequest2 | PaymentRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentResponse4, RawError]:
        """Request sent to terminal to initiate payment. It conveys Information related to the Payment transaction to
        process. Content of the ``PaymentRequest`` message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/payment"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentRequest2 | PaymentRequest2Dict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[PaymentResponse4],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def print_request(
        self,
        *,
        body: PrintRequest | PrintRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PrintResponse, RawError]:
        """Content of the Print Request message. It conveys the complete data to print and how to process the print.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/print"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PrintRequest | PrintRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[PrintResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def reconciliation_request(
        self,
        *,
        body: ReconciliationRequest | ReconciliationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReconciliationResponse, RawError]:
        """Content of the Reconciliation Request message. It conveys Information related to the Reconciliation requested
        by the Sale System.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/reconciliation"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReconciliationRequest | ReconciliationRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[ReconciliationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def reversal_request(
        self,
        *,
        body: ReversalRequest | ReversalRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReversalResponse, RawError]:
        """It conveys Information related to the reversal of a previous payment or a loyalty transaction. Content of the
        Reversal Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/reversal"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReversalRequest | ReversalRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[ReversalResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stored_value_request(
        self,
        *,
        body: StoredValueRequest | StoredValueRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredValueResponse, RawError]:
        """It conveys Information related to the Stored Value transaction to process. Content of the Stored Value
        Request message.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/storedvalue"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueRequest | StoredValueRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[StoredValueResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def transaction_status_request(
        self,
        *,
        body: TransactionStatusRequest | TransactionStatusRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransactionStatusResponse, RawError]:
        """Content of the TransactionStatus Request message. It conveys Information requested for status of the last or
        current Payment, Loyalty or Reversal transaction.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/transactionstatus"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransactionStatusRequest | TransactionStatusRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TransactionStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


AsyncClient = AsyncAdyenClient
