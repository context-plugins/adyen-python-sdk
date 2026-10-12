from __future__ import annotations

from functools import cached_property
from types import TracebackType
from typing import Any
from uuid import UUID, uuid4

from typing_extensions import Self

from .apis.account_company_level import AccountCompanyLevel
from .apis.account_holders import AccountHolders
from .apis.account_merchant_level import AccountMerchantLevel
from .apis.account_store_level import AccountStoreLevel
from .apis.account_verification import AccountVerification
from .apis.accounts import Accounts
from .apis.allowed_origins_company_level import AllowedOriginsCompanyLevel
from .apis.allowed_origins_merchant_level import AllowedOriginsMerchantLevel
from .apis.android_files_company_level import AndroidFilesCompanyLevel
from .apis.api_credentials_company_level import ApiCredentialsCompanyLevel
from .apis.api_credentials_merchant_level import ApiCredentialsMerchantLevel
from .apis.api_key_company_level import ApiKeyCompanyLevel
from .apis.api_key_merchant_level import ApiKeyMerchantLevel
from .apis.authorized_card_users import AuthorizedCardUsers
from .apis.balance_accounts import BalanceAccounts
from .apis.balance_transfers import BalanceTransfers
from .apis.balances import Balances
from .apis.balances_overview import BalancesOverview
from .apis.bank_account_validation import BankAccountValidation
from .apis.business_lines_api import BusinessLinesApi
from .apis.capital import Capital
from .apis.card_orders import CardOrders
from .apis.cash_out_api import CashOutApi
from .apis.client_key_company_level import ClientKeyCompanyLevel
from .apis.client_key_merchant_level import ClientKeyMerchantLevel
from .apis.custom_payout_schedules_sweeps import CustomPayoutSchedulesSweeps
from .apis.direct_debit_mandates import DirectDebitMandates
from .apis.dispute_attachments import DisputeAttachments
from .apis.documents import Documents
from .apis.donation_campaigns import DonationCampaigns
from .apis.donations import Donations
from .apis.dynamic_offers import DynamicOffers
from .apis.general import General
from .apis.grant_accounts import GrantAccounts
from .apis.grant_offers_api import GrantOffersApi
from .apis.grants_api import GrantsApi
from .apis.hosted_onboarding import HostedOnboarding
from .apis.hosted_onboarding_page import HostedOnboardingPage
from .apis.i_deal_profiles import IDealProfiles
from .apis.initialization import Initialization
from .apis.instant_payouts import InstantPayouts
from .apis.legal_entities import LegalEntities
from .apis.manage_card_pin import ManageCardPin
from .apis.manage_sca_devices import ManageScaDevices
from .apis.managed_payout_schedules import ManagedPayoutSchedules
from .apis.modifications import Modifications
from .apis.my_api_credential import MyApiCredential
from .apis.network_tokens import NetworkTokens
from .apis.orders import Orders
from .apis.payment_instrument_groups import PaymentInstrumentGroups
from .apis.payment_instruments import PaymentInstruments
from .apis.payment_links import PaymentLinks
from .apis.payment_methods_merchant_level import PaymentMethodsMerchantLevel
from .apis.payments import Payments
from .apis.payments_app import PaymentsApp
from .apis.payout_settings_merchant_level import PayoutSettingsMerchantLevel
from .apis.pci_compliance_questionnaire_page import PciComplianceQuestionnairePage
from .apis.pci_questionnaires import PciQuestionnaires
from .apis.platform import Platform
from .apis.raise_disputes import RaiseDisputes
from .apis.rates import Rates
from .apis.recurring_api import RecurringApi
from .apis.recurring_top_ups import RecurringTopUps
from .apis.reviewing import Reviewing
from .apis.sca_association_management import ScaAssociationManagement
from .apis.sca_device_management import ScaDeviceManagement
from .apis.session_authentication import SessionAuthentication
from .apis.split_configuration_merchant_level import SplitConfigurationMerchantLevel
from .apis.tax_e_delivery_consent import TaxEDeliveryConsent
from .apis.terminal_actions_company_level import TerminalActionsCompanyLevel
from .apis.terminal_actions_terminal_level import TerminalActionsTerminalLevel
from .apis.terminal_orders_company_level import TerminalOrdersCompanyLevel
from .apis.terminal_orders_merchant_level import TerminalOrdersMerchantLevel
from .apis.terminal_settings_company_level import TerminalSettingsCompanyLevel
from .apis.terminal_settings_merchant_level import TerminalSettingsMerchantLevel
from .apis.terminal_settings_store_level import TerminalSettingsStoreLevel
from .apis.terminal_settings_terminal_level import TerminalSettingsTerminalLevel
from .apis.terminals_terminal_level import TerminalsTerminalLevel
from .apis.terms_of_service import TermsOfService
from .apis.transaction_rules import TransactionRules
from .apis.transactions import Transactions
from .apis.transfer_instruments import TransferInstruments
from .apis.transfer_limits_balance_account_level import TransferLimitsBalanceAccountLevel
from .apis.transfer_limits_balance_platform_level import TransferLimitsBalancePlatformLevel
from .apis.transfer_routes import TransferRoutes
from .apis.transfers import Transfers
from .apis.users_company_level import UsersCompanyLevel
from .apis.users_merchant_level import UsersMerchantLevel
from .apis.utility import Utility
from .apis.verification import Verification
from .apis.webhooks_company_level import WebhooksCompanyLevel
from .apis.webhooks_merchant_level import WebhooksMerchantLevel
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseAdyenClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AnySchemes,
    ApiKeyHeaderScheme,
    ApiKeyQueryScheme,
    ApiResult,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    HttpClient,
    Httpx2Client,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RetryOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
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


class AdyenClient(BaseAdyenClient[RawClient]):
    def __init__(
        self,
        *,
        server_config: ServerConfigOrDict | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        custom_http_client: HttpClient | None = None,
        api_key_auth: str | None = None,
        basic_auth: BasicAuthCredentialsOrDict | None = None,
        client_key: str | None = None,
    ) -> None:
        super().__init__(server_config=server_config, timeout=timeout, retry_options=retry_options)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else Httpx2Client(timeout=timeout),
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
        self._auth = AuthSchemes(
            api_key_auth=ApiKeyHeaderScheme("X-API-Key", api_key_auth) if api_key_auth is not None else no_auth,
            basic_auth=BasicAuthScheme(BasicAuthCredentials.coerce(basic_auth)) if basic_auth is not None else no_auth,
            client_key=ApiKeyQueryScheme("clientKey", client_key) if client_key is not None else no_auth,
        )

    @cached_property
    def api_credentials_company_level(self) -> ApiCredentialsCompanyLevel:
        return ApiCredentialsCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def api_credentials_merchant_level(self) -> ApiCredentialsMerchantLevel:
        return ApiCredentialsMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def api_key_company_level(self) -> ApiKeyCompanyLevel:
        return ApiKeyCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def api_key_merchant_level(self) -> ApiKeyMerchantLevel:
        return ApiKeyMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def account_company_level(self) -> AccountCompanyLevel:
        return AccountCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def account_merchant_level(self) -> AccountMerchantLevel:
        return AccountMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def account_store_level(self) -> AccountStoreLevel:
        return AccountStoreLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def account_verification(self) -> AccountVerification:
        return AccountVerification(self._raw_client, self._server)

    @cached_property
    def account_holders(self) -> AccountHolders:
        return AccountHolders(self._raw_client, self._server, self._auth)

    @cached_property
    def accounts(self) -> Accounts:
        return Accounts(self._raw_client, self._server, self._auth)

    @cached_property
    def allowed_origins_company_level(self) -> AllowedOriginsCompanyLevel:
        return AllowedOriginsCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def allowed_origins_merchant_level(self) -> AllowedOriginsMerchantLevel:
        return AllowedOriginsMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def android_files_company_level(self) -> AndroidFilesCompanyLevel:
        return AndroidFilesCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def authorized_card_users(self) -> AuthorizedCardUsers:
        return AuthorizedCardUsers(self._raw_client, self._server)

    @cached_property
    def balance_accounts(self) -> BalanceAccounts:
        return BalanceAccounts(self._raw_client, self._server, self._auth)

    @cached_property
    def balance_transfers(self) -> BalanceTransfers:
        return BalanceTransfers(self._raw_client, self._server)

    @cached_property
    def balances(self) -> Balances:
        return Balances(self._raw_client, self._server)

    @cached_property
    def balances_overview(self) -> BalancesOverview:
        return BalancesOverview(self._raw_client, self._server)

    @cached_property
    def bank_account_validation(self) -> BankAccountValidation:
        return BankAccountValidation(self._raw_client, self._server, self._auth)

    @cached_property
    def business_lines_api(self) -> BusinessLinesApi:
        return BusinessLinesApi(self._raw_client, self._server, self._auth)

    @cached_property
    def capital(self) -> Capital:
        return Capital(self._raw_client, self._server, self._auth)

    @cached_property
    def card_orders(self) -> CardOrders:
        return CardOrders(self._raw_client, self._server, self._auth)

    @cached_property
    def cash_out_api(self) -> CashOutApi:
        return CashOutApi(self._raw_client, self._server)

    @cached_property
    def client_key_company_level(self) -> ClientKeyCompanyLevel:
        return ClientKeyCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def client_key_merchant_level(self) -> ClientKeyMerchantLevel:
        return ClientKeyMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def custom_payout_schedules_sweeps(self) -> CustomPayoutSchedulesSweeps:
        return CustomPayoutSchedulesSweeps(self._raw_client, self._server, self._auth)

    @cached_property
    def direct_debit_mandates(self) -> DirectDebitMandates:
        return DirectDebitMandates(self._raw_client, self._server)

    @cached_property
    def dispute_attachments(self) -> DisputeAttachments:
        return DisputeAttachments(self._raw_client, self._server)

    @cached_property
    def documents(self) -> Documents:
        return Documents(self._raw_client, self._server, self._auth)

    @cached_property
    def donation_campaigns(self) -> DonationCampaigns:
        return DonationCampaigns(self._raw_client, self._server, self._auth)

    @cached_property
    def donations(self) -> Donations:
        return Donations(self._raw_client, self._server, self._auth)

    @cached_property
    def dynamic_offers(self) -> DynamicOffers:
        return DynamicOffers(self._raw_client, self._server)

    @cached_property
    def general(self) -> General:
        return General(self._raw_client, self._server, self._auth)

    @cached_property
    def grant_accounts(self) -> GrantAccounts:
        return GrantAccounts(self._raw_client, self._server, self._auth)

    @cached_property
    def grant_offers_api(self) -> GrantOffersApi:
        return GrantOffersApi(self._raw_client, self._server, self._auth)

    @cached_property
    def grants_api(self) -> GrantsApi:
        return GrantsApi(self._raw_client, self._server)

    @cached_property
    def hosted_onboarding(self) -> HostedOnboarding:
        return HostedOnboarding(self._raw_client, self._server, self._auth)

    @cached_property
    def hosted_onboarding_page(self) -> HostedOnboardingPage:
        return HostedOnboardingPage(self._raw_client, self._server, self._auth)

    @cached_property
    def initialization(self) -> Initialization:
        return Initialization(self._raw_client, self._server, self._auth)

    @cached_property
    def instant_payouts(self) -> InstantPayouts:
        return InstantPayouts(self._raw_client, self._server, self._auth)

    @cached_property
    def legal_entities(self) -> LegalEntities:
        return LegalEntities(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_sca_devices(self) -> ManageScaDevices:
        return ManageScaDevices(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_card_pin(self) -> ManageCardPin:
        return ManageCardPin(self._raw_client, self._server, self._auth)

    @cached_property
    def managed_payout_schedules(self) -> ManagedPayoutSchedules:
        return ManagedPayoutSchedules(self._raw_client, self._server)

    @cached_property
    def modifications(self) -> Modifications:
        return Modifications(self._raw_client, self._server, self._auth)

    @cached_property
    def my_api_credential(self) -> MyApiCredential:
        return MyApiCredential(self._raw_client, self._server, self._auth)

    @cached_property
    def network_tokens(self) -> NetworkTokens:
        return NetworkTokens(self._raw_client, self._server, self._auth)

    @cached_property
    def orders(self) -> Orders:
        return Orders(self._raw_client, self._server, self._auth)

    @cached_property
    def pci_compliance_questionnaire_page(self) -> PciComplianceQuestionnairePage:
        return PciComplianceQuestionnairePage(self._raw_client, self._server, self._auth)

    @cached_property
    def pci_questionnaires(self) -> PciQuestionnaires:
        return PciQuestionnaires(self._raw_client, self._server, self._auth)

    @cached_property
    def payment_instrument_groups(self) -> PaymentInstrumentGroups:
        return PaymentInstrumentGroups(self._raw_client, self._server, self._auth)

    @cached_property
    def payment_instruments(self) -> PaymentInstruments:
        return PaymentInstruments(self._raw_client, self._server, self._auth)

    @cached_property
    def payment_links(self) -> PaymentLinks:
        return PaymentLinks(self._raw_client, self._server, self._auth)

    @cached_property
    def payment_methods_merchant_level(self) -> PaymentMethodsMerchantLevel:
        return PaymentMethodsMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def payments(self) -> Payments:
        return Payments(self._raw_client, self._server, self._auth)

    @cached_property
    def payments_app(self) -> PaymentsApp:
        return PaymentsApp(self._raw_client, self._server)

    @cached_property
    def payout_settings_merchant_level(self) -> PayoutSettingsMerchantLevel:
        return PayoutSettingsMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def platform(self) -> Platform:
        return Platform(self._raw_client, self._server, self._auth)

    @cached_property
    def raise_disputes(self) -> RaiseDisputes:
        return RaiseDisputes(self._raw_client, self._server)

    @cached_property
    def rates(self) -> Rates:
        return Rates(self._raw_client, self._server)

    @cached_property
    def recurring_api(self) -> RecurringApi:
        return RecurringApi(self._raw_client, self._server, self._auth)

    @cached_property
    def recurring_top_ups(self) -> RecurringTopUps:
        return RecurringTopUps(self._raw_client, self._server)

    @cached_property
    def reviewing(self) -> Reviewing:
        return Reviewing(self._raw_client, self._server, self._auth)

    @cached_property
    def sca_association_management(self) -> ScaAssociationManagement:
        return ScaAssociationManagement(self._raw_client, self._server)

    @cached_property
    def sca_device_management(self) -> ScaDeviceManagement:
        return ScaDeviceManagement(self._raw_client, self._server)

    @cached_property
    def session_authentication(self) -> SessionAuthentication:
        return SessionAuthentication(self._raw_client, self._server)

    @cached_property
    def split_configuration_merchant_level(self) -> SplitConfigurationMerchantLevel:
        return SplitConfigurationMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def tax_e_delivery_consent(self) -> TaxEDeliveryConsent:
        return TaxEDeliveryConsent(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_actions_company_level(self) -> TerminalActionsCompanyLevel:
        return TerminalActionsCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_actions_terminal_level(self) -> TerminalActionsTerminalLevel:
        return TerminalActionsTerminalLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_orders_company_level(self) -> TerminalOrdersCompanyLevel:
        return TerminalOrdersCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_orders_merchant_level(self) -> TerminalOrdersMerchantLevel:
        return TerminalOrdersMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_settings_company_level(self) -> TerminalSettingsCompanyLevel:
        return TerminalSettingsCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_settings_merchant_level(self) -> TerminalSettingsMerchantLevel:
        return TerminalSettingsMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_settings_store_level(self) -> TerminalSettingsStoreLevel:
        return TerminalSettingsStoreLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal_settings_terminal_level(self) -> TerminalSettingsTerminalLevel:
        return TerminalSettingsTerminalLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terminals_terminal_level(self) -> TerminalsTerminalLevel:
        return TerminalsTerminalLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def terms_of_service(self) -> TermsOfService:
        return TermsOfService(self._raw_client, self._server, self._auth)

    @cached_property
    def transaction_rules(self) -> TransactionRules:
        return TransactionRules(self._raw_client, self._server, self._auth)

    @cached_property
    def transactions(self) -> Transactions:
        return Transactions(self._raw_client, self._server, self._auth)

    @cached_property
    def transfer_instruments(self) -> TransferInstruments:
        return TransferInstruments(self._raw_client, self._server, self._auth)

    @cached_property
    def transfer_limits_balance_account_level(self) -> TransferLimitsBalanceAccountLevel:
        return TransferLimitsBalanceAccountLevel(self._raw_client, self._server)

    @cached_property
    def transfer_limits_balance_platform_level(self) -> TransferLimitsBalancePlatformLevel:
        return TransferLimitsBalancePlatformLevel(self._raw_client, self._server)

    @cached_property
    def transfer_routes(self) -> TransferRoutes:
        return TransferRoutes(self._raw_client, self._server, self._auth)

    @cached_property
    def transfers(self) -> Transfers:
        return Transfers(self._raw_client, self._server, self._auth)

    @cached_property
    def users_company_level(self) -> UsersCompanyLevel:
        return UsersCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def users_merchant_level(self) -> UsersMerchantLevel:
        return UsersMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def utility(self) -> Utility:
        return Utility(self._raw_client, self._server, self._auth)

    @cached_property
    def verification(self) -> Verification:
        return Verification(self._raw_client, self._server, self._auth)

    @cached_property
    def webhooks_company_level(self) -> WebhooksCompanyLevel:
        return WebhooksCompanyLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def webhooks_merchant_level(self) -> WebhooksMerchantLevel:
        return WebhooksMerchantLevel(self._raw_client, self._server, self._auth)

    @cached_property
    def i_deal_profiles(self) -> IDealProfiles:
        return IDealProfiles(self._raw_client, self._server)

    @cached_property
    def with_raw_response(self) -> ApiWithRawResponse:
        return ApiWithRawResponse(self._raw_client, self._server, self._auth)

    def abort_request(
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
        return unwrap(self.with_raw_response.abort_request(body=body, request_options=request_options))

    def admin_request(
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
        return unwrap(self.with_raw_response.admin_request(body=body, request_options=request_options))

    def balance_inquiry_request(
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
        return unwrap(self.with_raw_response.balance_inquiry_request(body=body, request_options=request_options))

    def card_acquisition_request(
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
        return unwrap(self.with_raw_response.card_acquisition_request(body=body, request_options=request_options))

    def card_reader_apdu_request(
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
        return unwrap(self.with_raw_response.card_reader_apdu_request(body=body, request_options=request_options))

    def diagnosis_request(
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
        return unwrap(self.with_raw_response.diagnosis_request(body=body, request_options=request_options))

    def display_request(
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
        return unwrap(self.with_raw_response.display_request(body=body, request_options=request_options))

    def enable_service_request(
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
        return unwrap(self.with_raw_response.enable_service_request(body=body, request_options=request_options))

    def get_totals_request(
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
        return unwrap(self.with_raw_response.get_totals_request(body=body, request_options=request_options))

    def input_request(
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
        return unwrap(self.with_raw_response.input_request(body=body, request_options=request_options))

    def login_request(
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
        return unwrap(self.with_raw_response.login_request(body=body, request_options=request_options))

    def logout_request(
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
        return unwrap(self.with_raw_response.logout_request(body=body, request_options=request_options))

    def payment_request(
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
        return unwrap(self.with_raw_response.payment_request(body=body, request_options=request_options))

    def print_request(
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
        return unwrap(self.with_raw_response.print_request(body=body, request_options=request_options))

    def reconciliation_request(
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
        return unwrap(self.with_raw_response.reconciliation_request(body=body, request_options=request_options))

    def reversal_request(
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
        return unwrap(self.with_raw_response.reversal_request(body=body, request_options=request_options))

    def stored_value_request(
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
        return unwrap(self.with_raw_response.stored_value_request(body=body, request_options=request_options))

    def transaction_status_request(
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
        return unwrap(self.with_raw_response.transaction_status_request(body=body, request_options=request_options))

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


class ApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def abort_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/abort"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AbortRequest | AbortRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/admin"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminRequest | AdminRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AdminResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def balance_inquiry_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/balanceinquiry"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceInquiryRequest | BalanceInquiryRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BalanceInquiryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def card_acquisition_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/cardacquisition"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CardAcquisitionRequest | CardAcquisitionRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CardAcquisitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def card_reader_apdu_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/cardreaderapdu"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CardReaderApdurequest | CardReaderApdurequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CardReaderApduresponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def diagnosis_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/diagnosis"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DiagnosisRequest | DiagnosisRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[DiagnosisResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def display_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/display"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisplayRequest | DisplayRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[DisplayResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def enable_service_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/enableservice"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[EnableServiceRequest | EnableServiceRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[EnableServiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_totals_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/gettotals"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetTotalsRequest | GetTotalsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetTotalsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def input_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/input"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InputRequest | InputRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[InputResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def login_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/login"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LoginRequest | LoginRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[LoginResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def logout_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/logout"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LogoutRequest | LogoutRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[LogoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def payment_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/payment"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentRequest2 | PaymentRequest2Dict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentResponse4],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def print_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/print"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PrintRequest | PrintRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PrintResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def reconciliation_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/reconciliation"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReconciliationRequest | ReconciliationRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ReconciliationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def reversal_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/reversal"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReversalRequest | ReversalRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ReversalResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stored_value_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/storedvalue"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueRequest | StoredValueRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StoredValueResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def transaction_status_request(
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
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default24("/transactionstatus"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransactionStatusRequest | TransactionStatusRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


Client = AdyenClient
