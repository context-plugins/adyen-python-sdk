from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.post_accept_dispute_error import PostAcceptDisputeErrorBody, post_accept_dispute_error_mapper
from ..errors.post_account_holder_balance_error import (
    PostAccountHolderBalanceErrorBody,
    post_account_holder_balance_error_mapper,
)
from ..errors.post_account_holder_transaction_list_error import (
    PostAccountHolderTransactionListErrorBody,
    post_account_holder_transaction_list_error_mapper,
)
from ..errors.post_assign_terminals_error import PostAssignTerminalsErrorBody, post_assign_terminals_error_mapper
from ..errors.post_change_status_error import PostChangeStatusErrorBody, post_change_status_error_mapper
from ..errors.post_check_balance_error import PostCheckBalanceErrorBody, post_check_balance_error_mapper
from ..errors.post_create_notification_configuration_error import (
    PostCreateNotificationConfigurationErrorBody,
    post_create_notification_configuration_error_mapper,
)
from ..errors.post_create_permit_error import PostCreatePermitErrorBody, post_create_permit_error_mapper
from ..errors.post_create_test_card_ranges_error import (
    PostCreateTestCardRangesErrorBody,
    post_create_test_card_ranges_error_mapper,
)
from ..errors.post_debit_account_holder_error import (
    PostDebitAccountHolderErrorBody,
    post_debit_account_holder_error_mapper,
)
from ..errors.post_defend_dispute_error import PostDefendDisputeErrorBody, post_defend_dispute_error_mapper
from ..errors.post_delete_dispute_defense_document_error import (
    PostDeleteDisputeDefenseDocumentErrorBody,
    post_delete_dispute_defense_document_error_mapper,
)
from ..errors.post_delete_notification_configurations_error import (
    PostDeleteNotificationConfigurationsErrorBody,
    post_delete_notification_configurations_error_mapper,
)
from ..errors.post_disable_error import PostDisableErrorBody, post_disable_error_mapper
from ..errors.post_disable_permit_error import PostDisablePermitErrorBody, post_disable_permit_error_mapper
from ..errors.post_find_terminal_error import PostFindTerminalErrorBody, post_find_terminal_error_mapper
from ..errors.post_get3_ds_availability_error import (
    PostGet3DsAvailabilityErrorBody,
    post_get3_ds_availability_error_mapper,
)
from ..errors.post_get_cost_estimate_error import PostGetCostEstimateErrorBody, post_get_cost_estimate_error_mapper
from ..errors.post_get_notification_configuration_error import (
    PostGetNotificationConfigurationErrorBody,
    post_get_notification_configuration_error_mapper,
)
from ..errors.post_get_notification_configuration_list_error import (
    PostGetNotificationConfigurationListErrorBody,
    post_get_notification_configuration_list_error_mapper,
)
from ..errors.post_get_stores_under_account_error import (
    PostGetStoresUnderAccountErrorBody,
    post_get_stores_under_account_error_mapper,
)
from ..errors.post_get_terminal_details_error import (
    PostGetTerminalDetailsErrorBody,
    post_get_terminal_details_error_mapper,
)
from ..errors.post_get_terminals_under_account_error import (
    PostGetTerminalsUnderAccountErrorBody,
    post_get_terminals_under_account_error_mapper,
)
from ..errors.post_issue_error import PostIssueErrorBody, post_issue_error_mapper
from ..errors.post_list_recurring_details_error import (
    PostListRecurringDetailsErrorBody,
    post_list_recurring_details_error_mapper,
)
from ..errors.post_load_error import PostLoadErrorBody, post_load_error_mapper
from ..errors.post_merge_balance_error import PostMergeBalanceErrorBody, post_merge_balance_error_mapper
from ..errors.post_notify_shopper_error import PostNotifyShopperErrorBody, post_notify_shopper_error_mapper
from ..errors.post_payout_account_holder_error import (
    PostPayoutAccountHolderErrorBody,
    post_payout_account_holder_error_mapper,
)
from ..errors.post_refund_funds_transfer_error import (
    PostRefundFundsTransferErrorBody,
    post_refund_funds_transfer_error_mapper,
)
from ..errors.post_refund_not_paid_out_transfers_error import (
    PostRefundNotPaidOutTransfersErrorBody,
    post_refund_not_paid_out_transfers_error_mapper,
)
from ..errors.post_request_subject_erasure_error import (
    PostRequestSubjectErasureErrorBody,
    post_request_subject_erasure_error_mapper,
)
from ..errors.post_retrieve_applicable_defense_reasons_error import (
    PostRetrieveApplicableDefenseReasonsErrorBody,
    post_retrieve_applicable_defense_reasons_error_mapper,
)
from ..errors.post_schedule_account_updater_error import (
    PostScheduleAccountUpdaterErrorBody,
    post_schedule_account_updater_error_mapper,
)
from ..errors.post_setup_beneficiary_error import PostSetupBeneficiaryErrorBody, post_setup_beneficiary_error_mapper
from ..errors.post_supply_defense_document_error import (
    PostSupplyDefenseDocumentErrorBody,
    post_supply_defense_document_error_mapper,
)
from ..errors.post_test_notification_configuration_error import (
    PostTestNotificationConfigurationErrorBody,
    post_test_notification_configuration_error_mapper,
)
from ..errors.post_transfer_funds_error import PostTransferFundsErrorBody, post_transfer_funds_error_mapper
from ..errors.post_update_notification_configuration_error import (
    PostUpdateNotificationConfigurationErrorBody,
    post_update_notification_configuration_error_mapper,
)
from ..errors.post_void_transaction_error import PostVoidTransactionErrorBody, post_void_transaction_error_mapper
from ..models.accept_dispute_request import AcceptDisputeRequest, AcceptDisputeRequestDict
from ..models.accept_dispute_response import AcceptDisputeResponse
from ..models.account_holder_balance_response import AccountHolderBalanceResponse
from ..models.account_holder_transaction_list_request import (
    AccountHolderTransactionListRequest,
    AccountHolderTransactionListRequestDict,
)
from ..models.account_holder_transaction_list_response import AccountHolderTransactionListResponse
from ..models.assign_terminals_request import AssignTerminalsRequest, AssignTerminalsRequestDict
from ..models.assign_terminals_response import AssignTerminalsResponse
from ..models.certificate_loading_response import CertificateLoadingResponse
from ..models.close_account_holder_request import CloseAccountHolderRequest, CloseAccountHolderRequestDict
from ..models.cost_estimate_request import CostEstimateRequest, CostEstimateRequestDict
from ..models.cost_estimate_response import CostEstimateResponse
from ..models.create_notification_configuration_request import (
    CreateNotificationConfigurationRequest,
    CreateNotificationConfigurationRequestDict,
)
from ..models.create_permit_request import CreatePermitRequest, CreatePermitRequestDict
from ..models.create_permit_result import CreatePermitResult
from ..models.create_session_request import CreateSessionRequest, CreateSessionRequestDict
from ..models.create_test_card_ranges_request import CreateTestCardRangesRequest, CreateTestCardRangesRequestDict
from ..models.create_test_card_ranges_result import CreateTestCardRangesResult
from ..models.debit_account_holder_request import DebitAccountHolderRequest, DebitAccountHolderRequestDict
from ..models.debit_account_holder_response import DebitAccountHolderResponse
from ..models.defend_dispute_request import DefendDisputeRequest, DefendDisputeRequestDict
from ..models.defend_dispute_response import DefendDisputeResponse
from ..models.defense_reasons_request import DefenseReasonsRequest, DefenseReasonsRequestDict
from ..models.defense_reasons_response import DefenseReasonsResponse
from ..models.delete_defense_document_request import DeleteDefenseDocumentRequest, DeleteDefenseDocumentRequestDict
from ..models.delete_defense_document_response import DeleteDefenseDocumentResponse
from ..models.delete_notification_configuration_request import (
    DeleteNotificationConfigurationRequest,
    DeleteNotificationConfigurationRequestDict,
)
from ..models.disable_permit_request import DisablePermitRequest, DisablePermitRequestDict
from ..models.disable_permit_result import DisablePermitResult
from ..models.disable_request import DisableRequest, DisableRequestDict
from ..models.disable_result import DisableResult
from ..models.find_terminal_request import FindTerminalRequest, FindTerminalRequestDict
from ..models.find_terminal_response import FindTerminalResponse
from ..models.generic_response import GenericResponse
from ..models.get_notification_configuration_list_response import GetNotificationConfigurationListResponse
from ..models.get_notification_configuration_request import (
    GetNotificationConfigurationRequest,
    GetNotificationConfigurationRequestDict,
)
from ..models.get_notification_configuration_response import GetNotificationConfigurationResponse
from ..models.get_stores_under_account_request import GetStoresUnderAccountRequest, GetStoresUnderAccountRequestDict
from ..models.get_stores_under_account_response import GetStoresUnderAccountResponse
from ..models.get_terminal_details_request import GetTerminalDetailsRequest, GetTerminalDetailsRequestDict
from ..models.get_terminal_details_response import GetTerminalDetailsResponse
from ..models.get_terminals_under_account_request import (
    GetTerminalsUnderAccountRequest,
    GetTerminalsUnderAccountRequestDict,
)
from ..models.get_terminals_under_account_response import GetTerminalsUnderAccountResponse
from ..models.notify_shopper_request import NotifyShopperRequest, NotifyShopperRequestDict
from ..models.notify_shopper_result import NotifyShopperResult
from ..models.payout_account_holder_request import PayoutAccountHolderRequest, PayoutAccountHolderRequestDict
from ..models.payout_account_holder_response import PayoutAccountHolderResponse
from ..models.recurring_details_request import RecurringDetailsRequest, RecurringDetailsRequestDict
from ..models.recurring_details_result import RecurringDetailsResult
from ..models.refund_funds_transfer_request import RefundFundsTransferRequest, RefundFundsTransferRequestDict
from ..models.refund_funds_transfer_response import RefundFundsTransferResponse
from ..models.refund_not_paid_out_transfers_request import (
    RefundNotPaidOutTransfersRequest,
    RefundNotPaidOutTransfersRequestDict,
)
from ..models.schedule_account_updater_request import ScheduleAccountUpdaterRequest, ScheduleAccountUpdaterRequestDict
from ..models.schedule_account_updater_result import ScheduleAccountUpdaterResult
from ..models.setup_beneficiary_request import SetupBeneficiaryRequest, SetupBeneficiaryRequestDict
from ..models.stored_value_balance_check_request import (
    StoredValueBalanceCheckRequest,
    StoredValueBalanceCheckRequestDict,
)
from ..models.stored_value_balance_check_response import StoredValueBalanceCheckResponse
from ..models.stored_value_balance_merge_request import (
    StoredValueBalanceMergeRequest,
    StoredValueBalanceMergeRequestDict,
)
from ..models.stored_value_balance_merge_response import StoredValueBalanceMergeResponse
from ..models.stored_value_issue_request import StoredValueIssueRequest, StoredValueIssueRequestDict
from ..models.stored_value_issue_response import StoredValueIssueResponse
from ..models.stored_value_load_request import StoredValueLoadRequest, StoredValueLoadRequestDict
from ..models.stored_value_load_response import StoredValueLoadResponse
from ..models.stored_value_status_change_request import (
    StoredValueStatusChangeRequest,
    StoredValueStatusChangeRequestDict,
)
from ..models.stored_value_status_change_response import StoredValueStatusChangeResponse
from ..models.stored_value_void_request import StoredValueVoidRequest, StoredValueVoidRequestDict
from ..models.stored_value_void_response import StoredValueVoidResponse
from ..models.subject_erasure_by_psp_reference_request import (
    SubjectErasureByPspReferenceRequest,
    SubjectErasureByPspReferenceRequestDict,
)
from ..models.subject_erasure_response import SubjectErasureResponse
from ..models.supply_defense_document_request import SupplyDefenseDocumentRequest, SupplyDefenseDocumentRequestDict
from ..models.supply_defense_document_response import SupplyDefenseDocumentResponse
from ..models.test_notification_configuration_request import (
    TestNotificationConfigurationRequest,
    TestNotificationConfigurationRequestDict,
)
from ..models.test_notification_configuration_response import TestNotificationConfigurationResponse
from ..models.three_dsavailability_request import ThreeDsavailabilityRequest, ThreeDsavailabilityRequestDict
from ..models.three_dsavailability_response import ThreeDsavailabilityResponse
from ..models.transfer_funds_request import TransferFundsRequest, TransferFundsRequestDict
from ..models.transfer_funds_response import TransferFundsResponse
from ..models.update_notification_configuration_request import (
    UpdateNotificationConfigurationRequest,
    UpdateNotificationConfigurationRequestDict,
)
from ..server.server import Server


class General:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GeneralWithRawResponse(client, server, auth)

    def post_accept_dispute(
        self,
        *,
        body: AcceptDisputeRequest | AcceptDisputeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AcceptDisputeResponse:
        """Accepts a specific dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_accept_dispute(body=body, request_options=request_options))

    def post_account_holder_balance(
        self,
        *,
        body: CloseAccountHolderRequest | CloseAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountHolderBalanceResponse:
        """Returns the account balances of an account holder. An account's balances are organized according by
        currencies. This mean that an account may have multiple balances: one for each currency.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_account_holder_balance(body=body, request_options=request_options))

    def post_account_holder_transaction_list(
        self,
        *,
        body: AccountHolderTransactionListRequest | AccountHolderTransactionListRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountHolderTransactionListResponse:
        """Returns a list of transactions for an account holder's accounts. You can specify the accounts and transaction
        statuses to be included on the list. The call returns a maximum of 50 transactions for each account. To retrieve
        all transactions, you must make another call with the 'page' value incremented. Transactions are listed in
        chronological order, with the most recent transaction first.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_account_holder_transaction_list(body=body, request_options=request_options)
        )

    def post_assign_terminals(
        self,
        *,
        body: AssignTerminalsRequest | AssignTerminalsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AssignTerminalsResponse:
        """Assigns one or more payment terminals to a merchant account or a store. You can also use this endpoint to
        reassign terminals between merchant accounts or stores, and to unassign a terminal and return it to company
        inventory.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_assign_terminals(body=body, request_options=request_options))

    def post_change_status(
        self,
        *,
        body: StoredValueStatusChangeRequest | StoredValueStatusChangeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredValueStatusChangeResponse:
        """Changes the status of the provided payment method to the specified status.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Internal Server Error - the
                server could not process the request. ``error`` is ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_change_status(body=body, request_options=request_options))

    def post_check_balance(
        self,
        *,
        body: StoredValueBalanceCheckRequest | StoredValueBalanceCheckRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredValueBalanceCheckResponse:
        """Checks the balance of the provided payment method.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Internal Server Error - the
                server could not process the request. ``error`` is ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_check_balance(body=body, request_options=request_options))

    def post_create_notification_configuration(
        self,
        *,
        body: CreateNotificationConfigurationRequest | CreateNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetNotificationConfigurationResponse:
        """Creates a subscription to notifications informing you of events on your platform. After the subscription is
        created, the events specified in the configuration will be sent to the URL specified in the configuration.
        Subscriptions must be configured on a per-event basis (as opposed to, for example, a per-account holder basis),
        so all event notifications of a marketplace and of a given type will be sent to the same endpoint(s). A
        marketplace may have multiple endpoints if desired; an event notification may be sent to as many or as few
        different endpoints as configured.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_create_notification_configuration(body=body, request_options=request_options)
        )

    def post_create_permit(
        self,
        *,
        body: CreatePermitRequest | CreatePermitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreatePermitResult:
        """Create permits for a recurring contract, including support for defining restrictions.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_create_permit(body=body, request_options=request_options))

    def post_create_test_card_ranges(
        self,
        *,
        body: CreateTestCardRangesRequest | CreateTestCardRangesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTestCardRangesResult:
        """Creates one or more test card ranges.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_create_test_card_ranges(body=body, request_options=request_options))

    def post_debit_account_holder(
        self,
        *,
        body: DebitAccountHolderRequest | DebitAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DebitAccountHolderResponse:
        """Sends a direct debit request to an account holder's bank account. If the direct debit is successful, the
        funds are settled in the accounts specified in the split instructions. Adyen sends the result of the direct
        debit in a https://docs.adyen.com/api-explorer/#/NotificationService/latest/post/DIRECT_DEBIT_INITIATED
        notification webhook.

        To learn more about direct debits, see `Top up accounts
        <https://docs.adyen.com/classic-platforms/top-up-accounts>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_debit_account_holder(body=body, request_options=request_options))

    def post_defend_dispute(
        self,
        *,
        body: DefendDisputeRequest | DefendDisputeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DefendDisputeResponse:
        """Defends a specific dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_defend_dispute(body=body, request_options=request_options))

    def post_delete_dispute_defense_document(
        self,
        *,
        body: DeleteDefenseDocumentRequest | DeleteDefenseDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeleteDefenseDocumentResponse:
        """Deletes a specific dispute defense document that was supplied earlier.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_delete_dispute_defense_document(body=body, request_options=request_options)
        )

    def post_delete_notification_configurations(
        self,
        *,
        body: DeleteNotificationConfigurationRequest | DeleteNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Deletes an existing notification subscription configuration. After the subscription is deleted, no further
        event notifications will be sent to the URL defined in the subscription.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_delete_notification_configurations(body=body, request_options=request_options)
        )

    def post_disable(
        self,
        *,
        body: DisableRequest | DisableRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DisableResult:
        """Disables stored payment details to stop charging a shopper with this particular recurring detail ID.

        For more information, refer to `Disable stored details
        <https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/tokenization/disable-stored-details>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_disable(body=body, request_options=request_options))

    def post_disable_permit(
        self,
        *,
        body: DisablePermitRequest | DisablePermitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DisablePermitResult:
        """Disable a permit that was previously linked to a recurringDetailReference.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_disable_permit(body=body, request_options=request_options))

    def post_find_terminal(
        self,
        *,
        body: FindTerminalRequest | FindTerminalRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FindTerminalResponse:
        """Returns the company account, merchant account, or store that a payment terminal is assigned to.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_find_terminal(body=body, request_options=request_options))

    def post_get3ds_availability(
        self,
        *,
        body: ThreeDsavailabilityRequest | ThreeDsavailabilityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ThreeDsavailabilityResponse:
        """Verifies whether 3D Secure is available for the specified BIN or card brand. For 3D Secure 2, this endpoint
        also returns device fingerprinting keys.

        For more information, refer to `3D Secure 2 <https://docs.adyen.com/online-payments/3d-secure/native-3ds2>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_get3ds_availability(body=body, request_options=request_options))

    def post_get_cost_estimate(
        self,
        *,
        body: CostEstimateRequest | CostEstimateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CostEstimateResponse:
        """>This API is available only for merchants operating in Australia, the EU, and the UK.

        Use the Adyen Cost Estimation API to pre-calculate interchange and scheme fee costs. Knowing these costs prior
        actual payment authorisation gives you an opportunity to charge those costs to the cardholder, if necessary.

        To retrieve this information, make the call to the ``/getCostEstimate`` endpoint. The response to this call
        contains the amount of the interchange and scheme fees charged by the network for this transaction, and also
        which surcharging policy is possible (based on current regulations).

        > Since not all information is known in advance (for example, if the cardholder will successfully authenticate
            via 3D Secure or if you also plan to provide additional Level 2/3 data), the returned amounts are based on a
            set of assumption criteria you define in the ``assumptions`` parameter.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_get_cost_estimate(body=body, request_options=request_options))

    def post_get_notification_configuration(
        self,
        *,
        body: GetNotificationConfigurationRequest | GetNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetNotificationConfigurationResponse:
        """Returns the details of the configuration of a notification subscription.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_get_notification_configuration(body=body, request_options=request_options)
        )

    def post_get_notification_configuration_list(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GetNotificationConfigurationListResponse:
        """Returns the details of the configurations of all of the notification subscriptions in the platform of the
        executing user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_get_notification_configuration_list(body=body, request_options=request_options)
        )

    def post_get_stores_under_account(
        self,
        *,
        body: GetStoresUnderAccountRequest | GetStoresUnderAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetStoresUnderAccountResponse:
        """Returns a list of stores associated with a company account or a merchant account, including the status of
        each store.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_get_stores_under_account(body=body, request_options=request_options))

    def post_get_terminal_details(
        self,
        *,
        body: GetTerminalDetailsRequest | GetTerminalDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetTerminalDetailsResponse:
        """Returns the details of a payment terminal, including where the terminal is assigned to. The response returns
        the same details that are provided in the terminal list in your Customer Area and in the Terminal Fleet report.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_get_terminal_details(body=body, request_options=request_options))

    def post_get_terminals_under_account(
        self,
        *,
        body: GetTerminalsUnderAccountRequest | GetTerminalsUnderAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetTerminalsUnderAccountResponse:
        """Returns a list of payment terminals associated with a company account, merchant account, or store. The
        response shows whether the terminals are in the inventory, or in-store (ready for boarding or already boarded).

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_get_terminals_under_account(body=body, request_options=request_options)
        )

    def post_issue(
        self,
        *,
        body: StoredValueIssueRequest | StoredValueIssueRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredValueIssueResponse:
        """Issues a new card of the given payment method.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Internal Server Error - the
                server could not process the request. ``error`` is ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_issue(body=body, request_options=request_options))

    def post_list_recurring_details(
        self,
        *,
        body: RecurringDetailsRequest | RecurringDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringDetailsResult:
        """Lists the stored payment details for a shopper, if there are any available. The recurring detail ID can be
        used with a regular authorisation request to charge the shopper. A summary of the payment detail is returned for
        presentation to the shopper.

        For more information, refer to `Retrieve stored details
        <https://docs.adyen.com/classic-integration/recurring-payments/retrieve-stored-details/>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_list_recurring_details(body=body, request_options=request_options))

    def post_load(
        self,
        *,
        body: StoredValueLoadRequest | StoredValueLoadRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredValueLoadResponse:
        """Loads the payment method with the specified funds.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Internal Server Error - the
                server could not process the request. ``error`` is ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_load(body=body, request_options=request_options))

    def post_merge_balance(
        self,
        *,
        body: StoredValueBalanceMergeRequest | StoredValueBalanceMergeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredValueBalanceMergeResponse:
        """Increases the balance of the paymentmethod by the full amount left on the source paymentmethod

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Internal Server Error - the
                server could not process the request. ``error`` is ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_merge_balance(body=body, request_options=request_options))

    def post_notify_shopper(
        self,
        *,
        body: NotifyShopperRequest | NotifyShopperRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NotifyShopperResult:
        """Sends a request to the issuer so they can inform the shopper about the upcoming recurring payment. This
        endpoint is used only for local acquiring in India. For more information, refer to `Recurring card payments in
        India <https://docs.adyen.com/payment-methods/cards/cards-recurring-india>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_notify_shopper(body=body, request_options=request_options))

    def post_payout_account_holder(
        self,
        *,
        body: PayoutAccountHolderRequest | PayoutAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayoutAccountHolderResponse:
        """Pays out a specified amount from an account to the bank account of account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_payout_account_holder(body=body, request_options=request_options))

    def post_refund_funds_transfer(
        self,
        *,
        body: RefundFundsTransferRequest | RefundFundsTransferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RefundFundsTransferResponse:
        """Refunds funds transferred from one account to another. Both accounts must be in the same platform, but can
        have different account holders.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_refund_funds_transfer(body=body, request_options=request_options))

    def post_refund_not_paid_out_transfers(
        self,
        *,
        body: RefundNotPaidOutTransfersRequest | RefundNotPaidOutTransfersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Refunds all the transactions of an account that have taken place since the most recent payout. This request
        is on a account basis (as opposed to a payment basis), so only the portion of the payment that was made to the
        specified account is refunded. The commissions, fees, and payments to other accounts remain in the accounts to
        which they were sent as designated by the original payment's split details.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_refund_not_paid_out_transfers(body=body, request_options=request_options)
        )

    def post_request_subject_erasure(
        self,
        *,
        body: SubjectErasureByPspReferenceRequest | SubjectErasureByPspReferenceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubjectErasureResponse:
        """Sends the PSP reference containing the shopper data that should be deleted.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_request_subject_erasure(body=body, request_options=request_options))

    def post_retrieve_applicable_defense_reasons(
        self,
        *,
        body: DefenseReasonsRequest | DefenseReasonsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DefenseReasonsResponse:
        """Returns a list of all applicable defense reasons to defend a specific dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_retrieve_applicable_defense_reasons(body=body, request_options=request_options)
        )

    def post_schedule_account_updater(
        self,
        *,
        body: ScheduleAccountUpdaterRequest | ScheduleAccountUpdaterRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduleAccountUpdaterResult:
        """When making the API call, you can submit either the credit card information, or the recurring detail
        reference and the shopper reference:
        * If the card information is provided, all the sub-fields for ``card`` are mandatory.
        * If the recurring detail reference is provided, the fields for ``shopperReference`` and
            ``selectedRecurringDetailReference`` are mandatory.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_schedule_account_updater(body=body, request_options=request_options))

    def post_sessions3(
        self,
        *,
        body: CreateSessionRequest | CreateSessionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CertificateLoadingResponse:
        """Establishes a secure communications session between the POS Mobile SDK and the Adyen payments platform,
        through mutual authentication. The request sends a setup token that identifies the SDK and the device. The
        response returns a session token that the SDK can use to authenticate responses received from the Adyen payments
        platform. >This request applies to **mobile in-person** transactions. You cannot use this request to create
        online payments sessions.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.post_sessions3(body=body, request_options=request_options))

    def post_setup_beneficiary(
        self,
        *,
        body: SetupBeneficiaryRequest | SetupBeneficiaryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Defines a benefactor and a beneficiary relationship between two accounts. At the time of
        benefactor/beneficiary setup, the funds in the benefactor account are transferred to the beneficiary account,
        and any further payments to the benefactor account are automatically sent to the beneficiary account. A series
        of benefactor/beneficiaries may not exceed four beneficiaries and may not have a cycle in it.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_setup_beneficiary(body=body, request_options=request_options))

    def post_supply_defense_document(
        self,
        *,
        body: SupplyDefenseDocumentRequest | SupplyDefenseDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SupplyDefenseDocumentResponse:
        """Supplies a specific dispute defense document.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_supply_defense_document(body=body, request_options=request_options))

    def post_test_notification_configuration(
        self,
        *,
        body: TestNotificationConfigurationRequest | TestNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TestNotificationConfigurationResponse:
        """Tests an existing notification subscription configuration. For each event type specified, a test notification
        will be generated and sent to the URL configured in the subscription specified.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_test_notification_configuration(body=body, request_options=request_options)
        )

    def post_transfer_funds(
        self,
        *,
        body: TransferFundsRequest | TransferFundsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferFundsResponse:
        """Transfers funds from one account to another account. Both accounts must be in the same platform, but can have
        different account holders. The transfer must include a transfer code, which should be determined by the
        platform, in compliance with local regulations.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.post_transfer_funds(body=body, request_options=request_options))

    def post_update_notification_configuration(
        self,
        *,
        body: UpdateNotificationConfigurationRequest | UpdateNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetNotificationConfigurationResponse:
        """Updates an existing notification subscription configuration. If you are updating the event types, you must
        provide all event types, otherwise the previous event type configuration will be overwritten.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_update_notification_configuration(body=body, request_options=request_options)
        )

    def post_void_transaction(
        self,
        *,
        body: StoredValueVoidRequest | StoredValueVoidRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredValueVoidResponse:
        """Voids the referenced stored value transaction.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Internal Server Error - the
                server could not process the request. ``error`` is ``ServiceError | RawError``."""
        return unwrap(self._with_raw_response.post_void_transaction(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> GeneralWithRawResponse:
        return self._with_raw_response


class AsyncGeneral:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGeneralWithRawResponse(client, server, auth)

    async def post_accept_dispute(
        self,
        *,
        body: AcceptDisputeRequest | AcceptDisputeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AcceptDisputeResponse:
        """Accepts a specific dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(await self._with_raw_response.post_accept_dispute(body=body, request_options=request_options))

    async def post_account_holder_balance(
        self,
        *,
        body: CloseAccountHolderRequest | CloseAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountHolderBalanceResponse:
        """Returns the account balances of an account holder. An account's balances are organized according by
        currencies. This mean that an account may have multiple balances: one for each currency.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_account_holder_balance(body=body, request_options=request_options)
        )

    async def post_account_holder_transaction_list(
        self,
        *,
        body: AccountHolderTransactionListRequest | AccountHolderTransactionListRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountHolderTransactionListResponse:
        """Returns a list of transactions for an account holder's accounts. You can specify the accounts and transaction
        statuses to be included on the list. The call returns a maximum of 50 transactions for each account. To retrieve
        all transactions, you must make another call with the 'page' value incremented. Transactions are listed in
        chronological order, with the most recent transaction first.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_account_holder_transaction_list(
                body=body, request_options=request_options
            ),
        )

    async def post_assign_terminals(
        self,
        *,
        body: AssignTerminalsRequest | AssignTerminalsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AssignTerminalsResponse:
        """Assigns one or more payment terminals to a merchant account or a store. You can also use this endpoint to
        reassign terminals between merchant accounts or stores, and to unassign a terminal and return it to company
        inventory.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(await self._with_raw_response.post_assign_terminals(body=body, request_options=request_options))

    async def post_change_status(
        self,
        *,
        body: StoredValueStatusChangeRequest | StoredValueStatusChangeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredValueStatusChangeResponse:
        """Changes the status of the provided payment method to the specified status.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Internal Server Error - the
                server could not process the request. ``error`` is ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_change_status(body=body, request_options=request_options))

    async def post_check_balance(
        self,
        *,
        body: StoredValueBalanceCheckRequest | StoredValueBalanceCheckRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredValueBalanceCheckResponse:
        """Checks the balance of the provided payment method.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Internal Server Error - the
                server could not process the request. ``error`` is ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_check_balance(body=body, request_options=request_options))

    async def post_create_notification_configuration(
        self,
        *,
        body: CreateNotificationConfigurationRequest | CreateNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetNotificationConfigurationResponse:
        """Creates a subscription to notifications informing you of events on your platform. After the subscription is
        created, the events specified in the configuration will be sent to the URL specified in the configuration.
        Subscriptions must be configured on a per-event basis (as opposed to, for example, a per-account holder basis),
        so all event notifications of a marketplace and of a given type will be sent to the same endpoint(s). A
        marketplace may have multiple endpoints if desired; an event notification may be sent to as many or as few
        different endpoints as configured.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_create_notification_configuration(
                body=body, request_options=request_options
            ),
        )

    async def post_create_permit(
        self,
        *,
        body: CreatePermitRequest | CreatePermitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreatePermitResult:
        """Create permits for a recurring contract, including support for defining restrictions.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_create_permit(body=body, request_options=request_options))

    async def post_create_test_card_ranges(
        self,
        *,
        body: CreateTestCardRangesRequest | CreateTestCardRangesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTestCardRangesResult:
        """Creates one or more test card ranges.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_create_test_card_ranges(body=body, request_options=request_options)
        )

    async def post_debit_account_holder(
        self,
        *,
        body: DebitAccountHolderRequest | DebitAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DebitAccountHolderResponse:
        """Sends a direct debit request to an account holder's bank account. If the direct debit is successful, the
        funds are settled in the accounts specified in the split instructions. Adyen sends the result of the direct
        debit in a https://docs.adyen.com/api-explorer/#/NotificationService/latest/post/DIRECT_DEBIT_INITIATED
        notification webhook.

        To learn more about direct debits, see `Top up accounts
        <https://docs.adyen.com/classic-platforms/top-up-accounts>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_debit_account_holder(body=body, request_options=request_options)
        )

    async def post_defend_dispute(
        self,
        *,
        body: DefendDisputeRequest | DefendDisputeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DefendDisputeResponse:
        """Defends a specific dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(await self._with_raw_response.post_defend_dispute(body=body, request_options=request_options))

    async def post_delete_dispute_defense_document(
        self,
        *,
        body: DeleteDefenseDocumentRequest | DeleteDefenseDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeleteDefenseDocumentResponse:
        """Deletes a specific dispute defense document that was supplied earlier.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_delete_dispute_defense_document(
                body=body, request_options=request_options
            ),
        )

    async def post_delete_notification_configurations(
        self,
        *,
        body: DeleteNotificationConfigurationRequest | DeleteNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Deletes an existing notification subscription configuration. After the subscription is deleted, no further
        event notifications will be sent to the URL defined in the subscription.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_delete_notification_configurations(
                body=body, request_options=request_options
            ),
        )

    async def post_disable(
        self,
        *,
        body: DisableRequest | DisableRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DisableResult:
        """Disables stored payment details to stop charging a shopper with this particular recurring detail ID.

        For more information, refer to `Disable stored details
        <https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/tokenization/disable-stored-details>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_disable(body=body, request_options=request_options))

    async def post_disable_permit(
        self,
        *,
        body: DisablePermitRequest | DisablePermitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DisablePermitResult:
        """Disable a permit that was previously linked to a recurringDetailReference.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_disable_permit(body=body, request_options=request_options))

    async def post_find_terminal(
        self,
        *,
        body: FindTerminalRequest | FindTerminalRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FindTerminalResponse:
        """Returns the company account, merchant account, or store that a payment terminal is assigned to.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(await self._with_raw_response.post_find_terminal(body=body, request_options=request_options))

    async def post_get3ds_availability(
        self,
        *,
        body: ThreeDsavailabilityRequest | ThreeDsavailabilityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ThreeDsavailabilityResponse:
        """Verifies whether 3D Secure is available for the specified BIN or card brand. For 3D Secure 2, this endpoint
        also returns device fingerprinting keys.

        For more information, refer to `3D Secure 2 <https://docs.adyen.com/online-payments/3d-secure/native-3ds2>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_get3ds_availability(body=body, request_options=request_options)
        )

    async def post_get_cost_estimate(
        self,
        *,
        body: CostEstimateRequest | CostEstimateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CostEstimateResponse:
        """>This API is available only for merchants operating in Australia, the EU, and the UK.

        Use the Adyen Cost Estimation API to pre-calculate interchange and scheme fee costs. Knowing these costs prior
        actual payment authorisation gives you an opportunity to charge those costs to the cardholder, if necessary.

        To retrieve this information, make the call to the ``/getCostEstimate`` endpoint. The response to this call
        contains the amount of the interchange and scheme fees charged by the network for this transaction, and also
        which surcharging policy is possible (based on current regulations).

        > Since not all information is known in advance (for example, if the cardholder will successfully authenticate
            via 3D Secure or if you also plan to provide additional Level 2/3 data), the returned amounts are based on a
            set of assumption criteria you define in the ``assumptions`` parameter.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_get_cost_estimate(body=body, request_options=request_options))

    async def post_get_notification_configuration(
        self,
        *,
        body: GetNotificationConfigurationRequest | GetNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetNotificationConfigurationResponse:
        """Returns the details of the configuration of a notification subscription.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_get_notification_configuration(
                body=body, request_options=request_options
            ),
        )

    async def post_get_notification_configuration_list(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GetNotificationConfigurationListResponse:
        """Returns the details of the configurations of all of the notification subscriptions in the platform of the
        executing user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_get_notification_configuration_list(
                body=body, request_options=request_options
            ),
        )

    async def post_get_stores_under_account(
        self,
        *,
        body: GetStoresUnderAccountRequest | GetStoresUnderAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetStoresUnderAccountResponse:
        """Returns a list of stores associated with a company account or a merchant account, including the status of
        each store.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_get_stores_under_account(body=body, request_options=request_options)
        )

    async def post_get_terminal_details(
        self,
        *,
        body: GetTerminalDetailsRequest | GetTerminalDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetTerminalDetailsResponse:
        """Returns the details of a payment terminal, including where the terminal is assigned to. The response returns
        the same details that are provided in the terminal list in your Customer Area and in the Terminal Fleet report.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_get_terminal_details(body=body, request_options=request_options)
        )

    async def post_get_terminals_under_account(
        self,
        *,
        body: GetTerminalsUnderAccountRequest | GetTerminalsUnderAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetTerminalsUnderAccountResponse:
        """Returns a list of payment terminals associated with a company account, merchant account, or store. The
        response shows whether the terminals are in the inventory, or in-store (ready for boarding or already boarded).

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_get_terminals_under_account(body=body, request_options=request_options)
        )

    async def post_issue(
        self,
        *,
        body: StoredValueIssueRequest | StoredValueIssueRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredValueIssueResponse:
        """Issues a new card of the given payment method.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Internal Server Error - the
                server could not process the request. ``error`` is ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_issue(body=body, request_options=request_options))

    async def post_list_recurring_details(
        self,
        *,
        body: RecurringDetailsRequest | RecurringDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringDetailsResult:
        """Lists the stored payment details for a shopper, if there are any available. The recurring detail ID can be
        used with a regular authorisation request to charge the shopper. A summary of the payment detail is returned for
        presentation to the shopper.

        For more information, refer to `Retrieve stored details
        <https://docs.adyen.com/classic-integration/recurring-payments/retrieve-stored-details/>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_list_recurring_details(body=body, request_options=request_options)
        )

    async def post_load(
        self,
        *,
        body: StoredValueLoadRequest | StoredValueLoadRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredValueLoadResponse:
        """Loads the payment method with the specified funds.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Internal Server Error - the
                server could not process the request. ``error`` is ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_load(body=body, request_options=request_options))

    async def post_merge_balance(
        self,
        *,
        body: StoredValueBalanceMergeRequest | StoredValueBalanceMergeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredValueBalanceMergeResponse:
        """Increases the balance of the paymentmethod by the full amount left on the source paymentmethod

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Internal Server Error - the
                server could not process the request. ``error`` is ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_merge_balance(body=body, request_options=request_options))

    async def post_notify_shopper(
        self,
        *,
        body: NotifyShopperRequest | NotifyShopperRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NotifyShopperResult:
        """Sends a request to the issuer so they can inform the shopper about the upcoming recurring payment. This
        endpoint is used only for local acquiring in India. For more information, refer to `Recurring card payments in
        India <https://docs.adyen.com/payment-methods/cards/cards-recurring-india>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_notify_shopper(body=body, request_options=request_options))

    async def post_payout_account_holder(
        self,
        *,
        body: PayoutAccountHolderRequest | PayoutAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayoutAccountHolderResponse:
        """Pays out a specified amount from an account to the bank account of account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_payout_account_holder(body=body, request_options=request_options)
        )

    async def post_refund_funds_transfer(
        self,
        *,
        body: RefundFundsTransferRequest | RefundFundsTransferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RefundFundsTransferResponse:
        """Refunds funds transferred from one account to another. Both accounts must be in the same platform, but can
        have different account holders.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_refund_funds_transfer(body=body, request_options=request_options)
        )

    async def post_refund_not_paid_out_transfers(
        self,
        *,
        body: RefundNotPaidOutTransfersRequest | RefundNotPaidOutTransfersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Refunds all the transactions of an account that have taken place since the most recent payout. This request
        is on a account basis (as opposed to a payment basis), so only the portion of the payment that was made to the
        specified account is refunded. The commissions, fees, and payments to other accounts remain in the accounts to
        which they were sent as designated by the original payment's split details.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_refund_not_paid_out_transfers(body=body, request_options=request_options)
        )

    async def post_request_subject_erasure(
        self,
        *,
        body: SubjectErasureByPspReferenceRequest | SubjectErasureByPspReferenceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubjectErasureResponse:
        """Sends the PSP reference containing the shopper data that should be deleted.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_request_subject_erasure(body=body, request_options=request_options)
        )

    async def post_retrieve_applicable_defense_reasons(
        self,
        *,
        body: DefenseReasonsRequest | DefenseReasonsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DefenseReasonsResponse:
        """Returns a list of all applicable defense reasons to defend a specific dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_retrieve_applicable_defense_reasons(
                body=body, request_options=request_options
            ),
        )

    async def post_schedule_account_updater(
        self,
        *,
        body: ScheduleAccountUpdaterRequest | ScheduleAccountUpdaterRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduleAccountUpdaterResult:
        """When making the API call, you can submit either the credit card information, or the recurring detail
        reference and the shopper reference:
        * If the card information is provided, all the sub-fields for ``card`` are mandatory.
        * If the recurring detail reference is provided, the fields for ``shopperReference`` and
            ``selectedRecurringDetailReference`` are mandatory.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_schedule_account_updater(body=body, request_options=request_options)
        )

    async def post_sessions3(
        self,
        *,
        body: CreateSessionRequest | CreateSessionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CertificateLoadingResponse:
        """Establishes a secure communications session between the POS Mobile SDK and the Adyen payments platform,
        through mutual authentication. The request sends a setup token that identifies the SDK and the device. The
        response returns a session token that the SDK can use to authenticate responses received from the Adyen payments
        platform. >This request applies to **mobile in-person** transactions. You cannot use this request to create
        online payments sessions.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.post_sessions3(body=body, request_options=request_options))

    async def post_setup_beneficiary(
        self,
        *,
        body: SetupBeneficiaryRequest | SetupBeneficiaryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Defines a benefactor and a beneficiary relationship between two accounts. At the time of
        benefactor/beneficiary setup, the funds in the benefactor account are transferred to the beneficiary account,
        and any further payments to the benefactor account are automatically sent to the beneficiary account. A series
        of benefactor/beneficiaries may not exceed four beneficiaries and may not have a cycle in it.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(await self._with_raw_response.post_setup_beneficiary(body=body, request_options=request_options))

    async def post_supply_defense_document(
        self,
        *,
        body: SupplyDefenseDocumentRequest | SupplyDefenseDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SupplyDefenseDocumentResponse:
        """Supplies a specific dispute defense document.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_supply_defense_document(body=body, request_options=request_options)
        )

    async def post_test_notification_configuration(
        self,
        *,
        body: TestNotificationConfigurationRequest | TestNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TestNotificationConfigurationResponse:
        """Tests an existing notification subscription configuration. For each event type specified, a test notification
        will be generated and sent to the URL configured in the subscription specified.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_test_notification_configuration(
                body=body, request_options=request_options
            ),
        )

    async def post_transfer_funds(
        self,
        *,
        body: TransferFundsRequest | TransferFundsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferFundsResponse:
        """Transfers funds from one account to another account. Both accounts must be in the same platform, but can have
        different account holders. The transfer must include a transfer code, which should be determined by the
        platform, in compliance with local regulations.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(await self._with_raw_response.post_transfer_funds(body=body, request_options=request_options))

    async def post_update_notification_configuration(
        self,
        *,
        body: UpdateNotificationConfigurationRequest | UpdateNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetNotificationConfigurationResponse:
        """Updates an existing notification subscription configuration. If you are updating the event types, you must
        provide all event types, otherwise the previous event type configuration will be overwritten.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_update_notification_configuration(
                body=body, request_options=request_options
            ),
        )

    async def post_void_transaction(
        self,
        *,
        body: StoredValueVoidRequest | StoredValueVoidRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredValueVoidResponse:
        """Voids the referenced stored value transaction.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Internal Server Error - the
                server could not process the request. ``error`` is ``ServiceError | RawError``."""
        return unwrap(await self._with_raw_response.post_void_transaction(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncGeneralWithRawResponse:
        return self._with_raw_response


class GeneralWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_accept_dispute(
        self,
        *,
        body: AcceptDisputeRequest | AcceptDisputeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AcceptDisputeResponse, PostAcceptDisputeErrorBody]:
        """Accepts a specific dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default22("/acceptDispute"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AcceptDisputeRequest | AcceptDisputeRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AcceptDisputeResponse],
            error_mapper=post_accept_dispute_error_mapper,
            request_options=request_options,
        )

    def post_account_holder_balance(
        self,
        *,
        body: CloseAccountHolderRequest | CloseAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountHolderBalanceResponse, PostAccountHolderBalanceErrorBody]:
        """Returns the account balances of an account holder. An account's balances are organized according by
        currencies. This mean that an account may have multiple balances: one for each currency.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/accountHolderBalance"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CloseAccountHolderRequest | CloseAccountHolderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AccountHolderBalanceResponse],
            error_mapper=post_account_holder_balance_error_mapper,
            request_options=request_options,
        )

    def post_account_holder_transaction_list(
        self,
        *,
        body: AccountHolderTransactionListRequest | AccountHolderTransactionListRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountHolderTransactionListResponse, PostAccountHolderTransactionListErrorBody]:
        """Returns a list of transactions for an account holder's accounts. You can specify the accounts and transaction
        statuses to be included on the list. The call returns a maximum of 50 transactions for each account. To retrieve
        all transactions, you must make another call with the 'page' value incremented. Transactions are listed in
        chronological order, with the most recent transaction first.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/accountHolderTransactionList"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountHolderTransactionListRequest | AccountHolderTransactionListRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AccountHolderTransactionListResponse],
            error_mapper=post_account_holder_transaction_list_error_mapper,
            request_options=request_options,
        )

    def post_assign_terminals(
        self,
        *,
        body: AssignTerminalsRequest | AssignTerminalsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AssignTerminalsResponse, PostAssignTerminalsErrorBody]:
        """Assigns one or more payment terminals to a merchant account or a store. You can also use this endpoint to
        reassign terminals between merchant accounts or stores, and to unassign a terminal and return it to company
        inventory.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default28("/assignTerminals"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AssignTerminalsRequest | AssignTerminalsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AssignTerminalsResponse],
            error_mapper=post_assign_terminals_error_mapper,
            request_options=request_options,
        )

    def post_change_status(
        self,
        *,
        body: StoredValueStatusChangeRequest | StoredValueStatusChangeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredValueStatusChangeResponse, PostChangeStatusErrorBody]:
        """Changes the status of the provided payment method to the specified status.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/changeStatus"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueStatusChangeRequest | StoredValueStatusChangeRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StoredValueStatusChangeResponse],
            error_mapper=post_change_status_error_mapper,
            request_options=request_options,
        )

    def post_check_balance(
        self,
        *,
        body: StoredValueBalanceCheckRequest | StoredValueBalanceCheckRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredValueBalanceCheckResponse, PostCheckBalanceErrorBody]:
        """Checks the balance of the provided payment method.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/checkBalance"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueBalanceCheckRequest | StoredValueBalanceCheckRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StoredValueBalanceCheckResponse],
            error_mapper=post_check_balance_error_mapper,
            request_options=request_options,
        )

    def post_create_notification_configuration(
        self,
        *,
        body: CreateNotificationConfigurationRequest | CreateNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetNotificationConfigurationResponse, PostCreateNotificationConfigurationErrorBody]:
        """Creates a subscription to notifications informing you of events on your platform. After the subscription is
        created, the events specified in the configuration will be sent to the URL specified in the configuration.
        Subscriptions must be configured on a per-event basis (as opposed to, for example, a per-account holder basis),
        so all event notifications of a marketplace and of a given type will be sent to the same endpoint(s). A
        marketplace may have multiple endpoints if desired; an event notification may be sent to as many or as few
        different endpoints as configured.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/createNotificationConfiguration"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateNotificationConfigurationRequest | CreateNotificationConfigurationRequestDict | None](
                body
            ),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetNotificationConfigurationResponse],
            error_mapper=post_create_notification_configuration_error_mapper,
            request_options=request_options,
        )

    def post_create_permit(
        self,
        *,
        body: CreatePermitRequest | CreatePermitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreatePermitResult, PostCreatePermitErrorBody]:
        """Create permits for a recurring contract, including support for defining restrictions.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/createPermit"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreatePermitRequest | CreatePermitRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreatePermitResult],
            error_mapper=post_create_permit_error_mapper,
            request_options=request_options,
        )

    def post_create_test_card_ranges(
        self,
        *,
        body: CreateTestCardRangesRequest | CreateTestCardRangesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTestCardRangesResult, PostCreateTestCardRangesErrorBody]:
        """Creates one or more test card ranges.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/createTestCardRanges"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTestCardRangesRequest | CreateTestCardRangesRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateTestCardRangesResult],
            error_mapper=post_create_test_card_ranges_error_mapper,
            request_options=request_options,
        )

    def post_debit_account_holder(
        self,
        *,
        body: DebitAccountHolderRequest | DebitAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DebitAccountHolderResponse, PostDebitAccountHolderErrorBody]:
        """Sends a direct debit request to an account holder's bank account. If the direct debit is successful, the
        funds are settled in the accounts specified in the split instructions. Adyen sends the result of the direct
        debit in a https://docs.adyen.com/api-explorer/#/NotificationService/latest/post/DIRECT_DEBIT_INITIATED
        notification webhook.

        To learn more about direct debits, see `Top up accounts
        <https://docs.adyen.com/classic-platforms/top-up-accounts>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/debitAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DebitAccountHolderRequest | DebitAccountHolderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[DebitAccountHolderResponse],
            error_mapper=post_debit_account_holder_error_mapper,
            request_options=request_options,
        )

    def post_defend_dispute(
        self,
        *,
        body: DefendDisputeRequest | DefendDisputeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DefendDisputeResponse, PostDefendDisputeErrorBody]:
        """Defends a specific dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default22("/defendDispute"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DefendDisputeRequest | DefendDisputeRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[DefendDisputeResponse],
            error_mapper=post_defend_dispute_error_mapper,
            request_options=request_options,
        )

    def post_delete_dispute_defense_document(
        self,
        *,
        body: DeleteDefenseDocumentRequest | DeleteDefenseDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeleteDefenseDocumentResponse, PostDeleteDisputeDefenseDocumentErrorBody]:
        """Deletes a specific dispute defense document that was supplied earlier.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default22("/deleteDisputeDefenseDocument"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteDefenseDocumentRequest | DeleteDefenseDocumentRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[DeleteDefenseDocumentResponse],
            error_mapper=post_delete_dispute_defense_document_error_mapper,
            request_options=request_options,
        )

    def post_delete_notification_configurations(
        self,
        *,
        body: DeleteNotificationConfigurationRequest | DeleteNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostDeleteNotificationConfigurationsErrorBody]:
        """Deletes an existing notification subscription configuration. After the subscription is deleted, no further
        event notifications will be sent to the URL defined in the subscription.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/deleteNotificationConfigurations"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteNotificationConfigurationRequest | DeleteNotificationConfigurationRequestDict | None](
                body
            ),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_delete_notification_configurations_error_mapper,
            request_options=request_options,
        )

    def post_disable(
        self,
        *,
        body: DisableRequest | DisableRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DisableResult, PostDisableErrorBody]:
        """Disables stored payment details to stop charging a shopper with this particular recurring detail ID.

        For more information, refer to `Disable stored details
        <https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/tokenization/disable-stored-details>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/disable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisableRequest | DisableRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[DisableResult],
            error_mapper=post_disable_error_mapper,
            request_options=request_options,
        )

    def post_disable_permit(
        self,
        *,
        body: DisablePermitRequest | DisablePermitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DisablePermitResult, PostDisablePermitErrorBody]:
        """Disable a permit that was previously linked to a recurringDetailReference.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/disablePermit"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisablePermitRequest | DisablePermitRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[DisablePermitResult],
            error_mapper=post_disable_permit_error_mapper,
            request_options=request_options,
        )

    def post_find_terminal(
        self,
        *,
        body: FindTerminalRequest | FindTerminalRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FindTerminalResponse, PostFindTerminalErrorBody]:
        """Returns the company account, merchant account, or store that a payment terminal is assigned to.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default28("/findTerminal"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FindTerminalRequest | FindTerminalRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[FindTerminalResponse],
            error_mapper=post_find_terminal_error_mapper,
            request_options=request_options,
        )

    def post_get3ds_availability(
        self,
        *,
        body: ThreeDsavailabilityRequest | ThreeDsavailabilityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ThreeDsavailabilityResponse, PostGet3DsAvailabilityErrorBody]:
        """Verifies whether 3D Secure is available for the specified BIN or card brand. For 3D Secure 2, this endpoint
        also returns device fingerprinting keys.

        For more information, refer to `3D Secure 2 <https://docs.adyen.com/online-payments/3d-secure/native-3ds2>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default4("/get3dsAvailability"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ThreeDsavailabilityRequest | ThreeDsavailabilityRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ThreeDsavailabilityResponse],
            error_mapper=post_get3_ds_availability_error_mapper,
            request_options=request_options,
        )

    def post_get_cost_estimate(
        self,
        *,
        body: CostEstimateRequest | CostEstimateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CostEstimateResponse, PostGetCostEstimateErrorBody]:
        """>This API is available only for merchants operating in Australia, the EU, and the UK.

        Use the Adyen Cost Estimation API to pre-calculate interchange and scheme fee costs. Knowing these costs prior
        actual payment authorisation gives you an opportunity to charge those costs to the cardholder, if necessary.

        To retrieve this information, make the call to the ``/getCostEstimate`` endpoint. The response to this call
        contains the amount of the interchange and scheme fees charged by the network for this transaction, and also
        which surcharging policy is possible (based on current regulations).

        > Since not all information is known in advance (for example, if the cardholder will successfully authenticate
            via 3D Secure or if you also plan to provide additional Level 2/3 data), the returned amounts are based on a
            set of assumption criteria you define in the ``assumptions`` parameter.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default4("/getCostEstimate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CostEstimateRequest | CostEstimateRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CostEstimateResponse],
            error_mapper=post_get_cost_estimate_error_mapper,
            request_options=request_options,
        )

    def post_get_notification_configuration(
        self,
        *,
        body: GetNotificationConfigurationRequest | GetNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetNotificationConfigurationResponse, PostGetNotificationConfigurationErrorBody]:
        """Returns the details of the configuration of a notification subscription.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/getNotificationConfiguration"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetNotificationConfigurationRequest | GetNotificationConfigurationRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetNotificationConfigurationResponse],
            error_mapper=post_get_notification_configuration_error_mapper,
            request_options=request_options,
        )

    def post_get_notification_configuration_list(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetNotificationConfigurationListResponse, PostGetNotificationConfigurationListErrorBody]:
        """Returns the details of the configurations of all of the notification subscriptions in the platform of the
        executing user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/getNotificationConfigurationList"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetNotificationConfigurationListResponse],
            error_mapper=post_get_notification_configuration_list_error_mapper,
            request_options=request_options,
        )

    def post_get_stores_under_account(
        self,
        *,
        body: GetStoresUnderAccountRequest | GetStoresUnderAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetStoresUnderAccountResponse, PostGetStoresUnderAccountErrorBody]:
        """Returns a list of stores associated with a company account or a merchant account, including the status of
        each store.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default28("/getStoresUnderAccount"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetStoresUnderAccountRequest | GetStoresUnderAccountRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetStoresUnderAccountResponse],
            error_mapper=post_get_stores_under_account_error_mapper,
            request_options=request_options,
        )

    def post_get_terminal_details(
        self,
        *,
        body: GetTerminalDetailsRequest | GetTerminalDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetTerminalDetailsResponse, PostGetTerminalDetailsErrorBody]:
        """Returns the details of a payment terminal, including where the terminal is assigned to. The response returns
        the same details that are provided in the terminal list in your Customer Area and in the Terminal Fleet report.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default28("/getTerminalDetails"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetTerminalDetailsRequest | GetTerminalDetailsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetTerminalDetailsResponse],
            error_mapper=post_get_terminal_details_error_mapper,
            request_options=request_options,
        )

    def post_get_terminals_under_account(
        self,
        *,
        body: GetTerminalsUnderAccountRequest | GetTerminalsUnderAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetTerminalsUnderAccountResponse, PostGetTerminalsUnderAccountErrorBody]:
        """Returns a list of payment terminals associated with a company account, merchant account, or store. The
        response shows whether the terminals are in the inventory, or in-store (ready for boarding or already boarded).

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default28("/getTerminalsUnderAccount"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetTerminalsUnderAccountRequest | GetTerminalsUnderAccountRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetTerminalsUnderAccountResponse],
            error_mapper=post_get_terminals_under_account_error_mapper,
            request_options=request_options,
        )

    def post_issue(
        self,
        *,
        body: StoredValueIssueRequest | StoredValueIssueRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredValueIssueResponse, PostIssueErrorBody]:
        """Issues a new card of the given payment method.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/issue"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueIssueRequest | StoredValueIssueRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StoredValueIssueResponse],
            error_mapper=post_issue_error_mapper,
            request_options=request_options,
        )

    def post_list_recurring_details(
        self,
        *,
        body: RecurringDetailsRequest | RecurringDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringDetailsResult, PostListRecurringDetailsErrorBody]:
        """Lists the stored payment details for a shopper, if there are any available. The recurring detail ID can be
        used with a regular authorisation request to charge the shopper. A summary of the payment detail is returned for
        presentation to the shopper.

        For more information, refer to `Retrieve stored details
        <https://docs.adyen.com/classic-integration/recurring-payments/retrieve-stored-details/>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/listRecurringDetails"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RecurringDetailsRequest | RecurringDetailsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[RecurringDetailsResult],
            error_mapper=post_list_recurring_details_error_mapper,
            request_options=request_options,
        )

    def post_load(
        self,
        *,
        body: StoredValueLoadRequest | StoredValueLoadRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredValueLoadResponse, PostLoadErrorBody]:
        """Loads the payment method with the specified funds.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/load"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueLoadRequest | StoredValueLoadRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StoredValueLoadResponse],
            error_mapper=post_load_error_mapper,
            request_options=request_options,
        )

    def post_merge_balance(
        self,
        *,
        body: StoredValueBalanceMergeRequest | StoredValueBalanceMergeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredValueBalanceMergeResponse, PostMergeBalanceErrorBody]:
        """Increases the balance of the paymentmethod by the full amount left on the source paymentmethod

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/mergeBalance"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueBalanceMergeRequest | StoredValueBalanceMergeRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StoredValueBalanceMergeResponse],
            error_mapper=post_merge_balance_error_mapper,
            request_options=request_options,
        )

    def post_notify_shopper(
        self,
        *,
        body: NotifyShopperRequest | NotifyShopperRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NotifyShopperResult, PostNotifyShopperErrorBody]:
        """Sends a request to the issuer so they can inform the shopper about the upcoming recurring payment. This
        endpoint is used only for local acquiring in India. For more information, refer to `Recurring card payments in
        India <https://docs.adyen.com/payment-methods/cards/cards-recurring-india>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/notifyShopper"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[NotifyShopperRequest | NotifyShopperRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[NotifyShopperResult],
            error_mapper=post_notify_shopper_error_mapper,
            request_options=request_options,
        )

    def post_payout_account_holder(
        self,
        *,
        body: PayoutAccountHolderRequest | PayoutAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayoutAccountHolderResponse, PostPayoutAccountHolderErrorBody]:
        """Pays out a specified amount from an account to the bank account of account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/payoutAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PayoutAccountHolderRequest | PayoutAccountHolderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PayoutAccountHolderResponse],
            error_mapper=post_payout_account_holder_error_mapper,
            request_options=request_options,
        )

    def post_refund_funds_transfer(
        self,
        *,
        body: RefundFundsTransferRequest | RefundFundsTransferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RefundFundsTransferResponse, PostRefundFundsTransferErrorBody]:
        """Refunds funds transferred from one account to another. Both accounts must be in the same platform, but can
        have different account holders.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/refundFundsTransfer"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundFundsTransferRequest | RefundFundsTransferRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[RefundFundsTransferResponse],
            error_mapper=post_refund_funds_transfer_error_mapper,
            request_options=request_options,
        )

    def post_refund_not_paid_out_transfers(
        self,
        *,
        body: RefundNotPaidOutTransfersRequest | RefundNotPaidOutTransfersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostRefundNotPaidOutTransfersErrorBody]:
        """Refunds all the transactions of an account that have taken place since the most recent payout. This request
        is on a account basis (as opposed to a payment basis), so only the portion of the payment that was made to the
        specified account is refunded. The commissions, fees, and payments to other accounts remain in the accounts to
        which they were sent as designated by the original payment's split details.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/refundNotPaidOutTransfers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundNotPaidOutTransfersRequest | RefundNotPaidOutTransfersRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_refund_not_paid_out_transfers_error_mapper,
            request_options=request_options,
        )

    def post_request_subject_erasure(
        self,
        *,
        body: SubjectErasureByPspReferenceRequest | SubjectErasureByPspReferenceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubjectErasureResponse, PostRequestSubjectErasureErrorBody]:
        """Sends the PSP reference containing the shopper data that should be deleted.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/requestSubjectErasure"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubjectErasureByPspReferenceRequest | SubjectErasureByPspReferenceRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SubjectErasureResponse],
            error_mapper=post_request_subject_erasure_error_mapper,
            request_options=request_options,
        )

    def post_retrieve_applicable_defense_reasons(
        self,
        *,
        body: DefenseReasonsRequest | DefenseReasonsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DefenseReasonsResponse, PostRetrieveApplicableDefenseReasonsErrorBody]:
        """Returns a list of all applicable defense reasons to defend a specific dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default22("/retrieveApplicableDefenseReasons"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DefenseReasonsRequest | DefenseReasonsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[DefenseReasonsResponse],
            error_mapper=post_retrieve_applicable_defense_reasons_error_mapper,
            request_options=request_options,
        )

    def post_schedule_account_updater(
        self,
        *,
        body: ScheduleAccountUpdaterRequest | ScheduleAccountUpdaterRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduleAccountUpdaterResult, PostScheduleAccountUpdaterErrorBody]:
        """When making the API call, you can submit either the credit card information, or the recurring detail
        reference and the shopper reference:
        * If the card information is provided, all the sub-fields for ``card`` are mandatory.
        * If the recurring detail reference is provided, the fields for ``shopperReference`` and
            ``selectedRecurringDetailReference`` are mandatory.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/scheduleAccountUpdater"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduleAccountUpdaterRequest | ScheduleAccountUpdaterRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ScheduleAccountUpdaterResult],
            error_mapper=post_schedule_account_updater_error_mapper,
            request_options=request_options,
        )

    def post_sessions3(
        self,
        *,
        body: CreateSessionRequest | CreateSessionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CertificateLoadingResponse, RawError]:
        """Establishes a secure communications session between the POS Mobile SDK and the Adyen payments platform,
        through mutual authentication. The request sends a setup token that identifies the SDK and the device. The
        response returns a session token that the SDK can use to authenticate responses received from the Adyen payments
        platform. >This request applies to **mobile in-person** transactions. You cannot use this request to create
        online payments sessions.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default27("/sessions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSessionRequest | CreateSessionRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CertificateLoadingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def post_setup_beneficiary(
        self,
        *,
        body: SetupBeneficiaryRequest | SetupBeneficiaryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostSetupBeneficiaryErrorBody]:
        """Defines a benefactor and a beneficiary relationship between two accounts. At the time of
        benefactor/beneficiary setup, the funds in the benefactor account are transferred to the beneficiary account,
        and any further payments to the benefactor account are automatically sent to the beneficiary account. A series
        of benefactor/beneficiaries may not exceed four beneficiaries and may not have a cycle in it.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/setupBeneficiary"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetupBeneficiaryRequest | SetupBeneficiaryRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_setup_beneficiary_error_mapper,
            request_options=request_options,
        )

    def post_supply_defense_document(
        self,
        *,
        body: SupplyDefenseDocumentRequest | SupplyDefenseDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SupplyDefenseDocumentResponse, PostSupplyDefenseDocumentErrorBody]:
        """Supplies a specific dispute defense document.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default22("/supplyDefenseDocument"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SupplyDefenseDocumentRequest | SupplyDefenseDocumentRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SupplyDefenseDocumentResponse],
            error_mapper=post_supply_defense_document_error_mapper,
            request_options=request_options,
        )

    def post_test_notification_configuration(
        self,
        *,
        body: TestNotificationConfigurationRequest | TestNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TestNotificationConfigurationResponse, PostTestNotificationConfigurationErrorBody]:
        """Tests an existing notification subscription configuration. For each event type specified, a test notification
        will be generated and sent to the URL configured in the subscription specified.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/testNotificationConfiguration"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TestNotificationConfigurationRequest | TestNotificationConfigurationRequestDict | None](
                body
            ),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TestNotificationConfigurationResponse],
            error_mapper=post_test_notification_configuration_error_mapper,
            request_options=request_options,
        )

    def post_transfer_funds(
        self,
        *,
        body: TransferFundsRequest | TransferFundsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferFundsResponse, PostTransferFundsErrorBody]:
        """Transfers funds from one account to another account. Both accounts must be in the same platform, but can have
        different account holders. The transfer must include a transfer code, which should be determined by the
        platform, in compliance with local regulations.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/transferFunds"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferFundsRequest | TransferFundsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransferFundsResponse],
            error_mapper=post_transfer_funds_error_mapper,
            request_options=request_options,
        )

    def post_update_notification_configuration(
        self,
        *,
        body: UpdateNotificationConfigurationRequest | UpdateNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetNotificationConfigurationResponse, PostUpdateNotificationConfigurationErrorBody]:
        """Updates an existing notification subscription configuration. If you are updating the event types, you must
        provide all event types, otherwise the previous event type configuration will be overwritten.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/updateNotificationConfiguration"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateNotificationConfigurationRequest | UpdateNotificationConfigurationRequestDict | None](
                body
            ),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetNotificationConfigurationResponse],
            error_mapper=post_update_notification_configuration_error_mapper,
            request_options=request_options,
        )

    def post_void_transaction(
        self,
        *,
        body: StoredValueVoidRequest | StoredValueVoidRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredValueVoidResponse, PostVoidTransactionErrorBody]:
        """Voids the referenced stored value transaction.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/voidTransaction"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueVoidRequest | StoredValueVoidRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StoredValueVoidResponse],
            error_mapper=post_void_transaction_error_mapper,
            request_options=request_options,
        )


class AsyncGeneralWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_accept_dispute(
        self,
        *,
        body: AcceptDisputeRequest | AcceptDisputeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AcceptDisputeResponse, PostAcceptDisputeErrorBody]:
        """Accepts a specific dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default22("/acceptDispute"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AcceptDisputeRequest | AcceptDisputeRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[AcceptDisputeResponse],
            error_mapper=post_accept_dispute_error_mapper,
            request_options=request_options,
        )

    async def post_account_holder_balance(
        self,
        *,
        body: CloseAccountHolderRequest | CloseAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountHolderBalanceResponse, PostAccountHolderBalanceErrorBody]:
        """Returns the account balances of an account holder. An account's balances are organized according by
        currencies. This mean that an account may have multiple balances: one for each currency.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/accountHolderBalance"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CloseAccountHolderRequest | CloseAccountHolderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[AccountHolderBalanceResponse],
            error_mapper=post_account_holder_balance_error_mapper,
            request_options=request_options,
        )

    async def post_account_holder_transaction_list(
        self,
        *,
        body: AccountHolderTransactionListRequest | AccountHolderTransactionListRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountHolderTransactionListResponse, PostAccountHolderTransactionListErrorBody]:
        """Returns a list of transactions for an account holder's accounts. You can specify the accounts and transaction
        statuses to be included on the list. The call returns a maximum of 50 transactions for each account. To retrieve
        all transactions, you must make another call with the 'page' value incremented. Transactions are listed in
        chronological order, with the most recent transaction first.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/accountHolderTransactionList"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountHolderTransactionListRequest | AccountHolderTransactionListRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[AccountHolderTransactionListResponse],
            error_mapper=post_account_holder_transaction_list_error_mapper,
            request_options=request_options,
        )

    async def post_assign_terminals(
        self,
        *,
        body: AssignTerminalsRequest | AssignTerminalsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AssignTerminalsResponse, PostAssignTerminalsErrorBody]:
        """Assigns one or more payment terminals to a merchant account or a store. You can also use this endpoint to
        reassign terminals between merchant accounts or stores, and to unassign a terminal and return it to company
        inventory.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default28("/assignTerminals"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AssignTerminalsRequest | AssignTerminalsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[AssignTerminalsResponse],
            error_mapper=post_assign_terminals_error_mapper,
            request_options=request_options,
        )

    async def post_change_status(
        self,
        *,
        body: StoredValueStatusChangeRequest | StoredValueStatusChangeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredValueStatusChangeResponse, PostChangeStatusErrorBody]:
        """Changes the status of the provided payment method to the specified status.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/changeStatus"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueStatusChangeRequest | StoredValueStatusChangeRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[StoredValueStatusChangeResponse],
            error_mapper=post_change_status_error_mapper,
            request_options=request_options,
        )

    async def post_check_balance(
        self,
        *,
        body: StoredValueBalanceCheckRequest | StoredValueBalanceCheckRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredValueBalanceCheckResponse, PostCheckBalanceErrorBody]:
        """Checks the balance of the provided payment method.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/checkBalance"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueBalanceCheckRequest | StoredValueBalanceCheckRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[StoredValueBalanceCheckResponse],
            error_mapper=post_check_balance_error_mapper,
            request_options=request_options,
        )

    async def post_create_notification_configuration(
        self,
        *,
        body: CreateNotificationConfigurationRequest | CreateNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetNotificationConfigurationResponse, PostCreateNotificationConfigurationErrorBody]:
        """Creates a subscription to notifications informing you of events on your platform. After the subscription is
        created, the events specified in the configuration will be sent to the URL specified in the configuration.
        Subscriptions must be configured on a per-event basis (as opposed to, for example, a per-account holder basis),
        so all event notifications of a marketplace and of a given type will be sent to the same endpoint(s). A
        marketplace may have multiple endpoints if desired; an event notification may be sent to as many or as few
        different endpoints as configured.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/createNotificationConfiguration"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateNotificationConfigurationRequest | CreateNotificationConfigurationRequestDict | None](
                body
            ),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GetNotificationConfigurationResponse],
            error_mapper=post_create_notification_configuration_error_mapper,
            request_options=request_options,
        )

    async def post_create_permit(
        self,
        *,
        body: CreatePermitRequest | CreatePermitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreatePermitResult, PostCreatePermitErrorBody]:
        """Create permits for a recurring contract, including support for defining restrictions.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/createPermit"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreatePermitRequest | CreatePermitRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CreatePermitResult],
            error_mapper=post_create_permit_error_mapper,
            request_options=request_options,
        )

    async def post_create_test_card_ranges(
        self,
        *,
        body: CreateTestCardRangesRequest | CreateTestCardRangesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTestCardRangesResult, PostCreateTestCardRangesErrorBody]:
        """Creates one or more test card ranges.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/createTestCardRanges"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTestCardRangesRequest | CreateTestCardRangesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CreateTestCardRangesResult],
            error_mapper=post_create_test_card_ranges_error_mapper,
            request_options=request_options,
        )

    async def post_debit_account_holder(
        self,
        *,
        body: DebitAccountHolderRequest | DebitAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DebitAccountHolderResponse, PostDebitAccountHolderErrorBody]:
        """Sends a direct debit request to an account holder's bank account. If the direct debit is successful, the
        funds are settled in the accounts specified in the split instructions. Adyen sends the result of the direct
        debit in a https://docs.adyen.com/api-explorer/#/NotificationService/latest/post/DIRECT_DEBIT_INITIATED
        notification webhook.

        To learn more about direct debits, see `Top up accounts
        <https://docs.adyen.com/classic-platforms/top-up-accounts>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/debitAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DebitAccountHolderRequest | DebitAccountHolderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[DebitAccountHolderResponse],
            error_mapper=post_debit_account_holder_error_mapper,
            request_options=request_options,
        )

    async def post_defend_dispute(
        self,
        *,
        body: DefendDisputeRequest | DefendDisputeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DefendDisputeResponse, PostDefendDisputeErrorBody]:
        """Defends a specific dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default22("/defendDispute"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DefendDisputeRequest | DefendDisputeRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[DefendDisputeResponse],
            error_mapper=post_defend_dispute_error_mapper,
            request_options=request_options,
        )

    async def post_delete_dispute_defense_document(
        self,
        *,
        body: DeleteDefenseDocumentRequest | DeleteDefenseDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeleteDefenseDocumentResponse, PostDeleteDisputeDefenseDocumentErrorBody]:
        """Deletes a specific dispute defense document that was supplied earlier.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default22("/deleteDisputeDefenseDocument"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteDefenseDocumentRequest | DeleteDefenseDocumentRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[DeleteDefenseDocumentResponse],
            error_mapper=post_delete_dispute_defense_document_error_mapper,
            request_options=request_options,
        )

    async def post_delete_notification_configurations(
        self,
        *,
        body: DeleteNotificationConfigurationRequest | DeleteNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostDeleteNotificationConfigurationsErrorBody]:
        """Deletes an existing notification subscription configuration. After the subscription is deleted, no further
        event notifications will be sent to the URL defined in the subscription.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/deleteNotificationConfigurations"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteNotificationConfigurationRequest | DeleteNotificationConfigurationRequestDict | None](
                body
            ),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GenericResponse],
            error_mapper=post_delete_notification_configurations_error_mapper,
            request_options=request_options,
        )

    async def post_disable(
        self,
        *,
        body: DisableRequest | DisableRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DisableResult, PostDisableErrorBody]:
        """Disables stored payment details to stop charging a shopper with this particular recurring detail ID.

        For more information, refer to `Disable stored details
        <https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/tokenization/disable-stored-details>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/disable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisableRequest | DisableRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[DisableResult],
            error_mapper=post_disable_error_mapper,
            request_options=request_options,
        )

    async def post_disable_permit(
        self,
        *,
        body: DisablePermitRequest | DisablePermitRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DisablePermitResult, PostDisablePermitErrorBody]:
        """Disable a permit that was previously linked to a recurringDetailReference.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/disablePermit"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisablePermitRequest | DisablePermitRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[DisablePermitResult],
            error_mapper=post_disable_permit_error_mapper,
            request_options=request_options,
        )

    async def post_find_terminal(
        self,
        *,
        body: FindTerminalRequest | FindTerminalRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FindTerminalResponse, PostFindTerminalErrorBody]:
        """Returns the company account, merchant account, or store that a payment terminal is assigned to.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default28("/findTerminal"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FindTerminalRequest | FindTerminalRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[FindTerminalResponse],
            error_mapper=post_find_terminal_error_mapper,
            request_options=request_options,
        )

    async def post_get3ds_availability(
        self,
        *,
        body: ThreeDsavailabilityRequest | ThreeDsavailabilityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ThreeDsavailabilityResponse, PostGet3DsAvailabilityErrorBody]:
        """Verifies whether 3D Secure is available for the specified BIN or card brand. For 3D Secure 2, this endpoint
        also returns device fingerprinting keys.

        For more information, refer to `3D Secure 2 <https://docs.adyen.com/online-payments/3d-secure/native-3ds2>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default4("/get3dsAvailability"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ThreeDsavailabilityRequest | ThreeDsavailabilityRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[ThreeDsavailabilityResponse],
            error_mapper=post_get3_ds_availability_error_mapper,
            request_options=request_options,
        )

    async def post_get_cost_estimate(
        self,
        *,
        body: CostEstimateRequest | CostEstimateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CostEstimateResponse, PostGetCostEstimateErrorBody]:
        """>This API is available only for merchants operating in Australia, the EU, and the UK.

        Use the Adyen Cost Estimation API to pre-calculate interchange and scheme fee costs. Knowing these costs prior
        actual payment authorisation gives you an opportunity to charge those costs to the cardholder, if necessary.

        To retrieve this information, make the call to the ``/getCostEstimate`` endpoint. The response to this call
        contains the amount of the interchange and scheme fees charged by the network for this transaction, and also
        which surcharging policy is possible (based on current regulations).

        > Since not all information is known in advance (for example, if the cardholder will successfully authenticate
            via 3D Secure or if you also plan to provide additional Level 2/3 data), the returned amounts are based on a
            set of assumption criteria you define in the ``assumptions`` parameter.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default4("/getCostEstimate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CostEstimateRequest | CostEstimateRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CostEstimateResponse],
            error_mapper=post_get_cost_estimate_error_mapper,
            request_options=request_options,
        )

    async def post_get_notification_configuration(
        self,
        *,
        body: GetNotificationConfigurationRequest | GetNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetNotificationConfigurationResponse, PostGetNotificationConfigurationErrorBody]:
        """Returns the details of the configuration of a notification subscription.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/getNotificationConfiguration"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetNotificationConfigurationRequest | GetNotificationConfigurationRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GetNotificationConfigurationResponse],
            error_mapper=post_get_notification_configuration_error_mapper,
            request_options=request_options,
        )

    async def post_get_notification_configuration_list(
        self, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetNotificationConfigurationListResponse, PostGetNotificationConfigurationListErrorBody]:
        """Returns the details of the configurations of all of the notification subscriptions in the platform of the
        executing user.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/getNotificationConfigurationList"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GetNotificationConfigurationListResponse],
            error_mapper=post_get_notification_configuration_list_error_mapper,
            request_options=request_options,
        )

    async def post_get_stores_under_account(
        self,
        *,
        body: GetStoresUnderAccountRequest | GetStoresUnderAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetStoresUnderAccountResponse, PostGetStoresUnderAccountErrorBody]:
        """Returns a list of stores associated with a company account or a merchant account, including the status of
        each store.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default28("/getStoresUnderAccount"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetStoresUnderAccountRequest | GetStoresUnderAccountRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GetStoresUnderAccountResponse],
            error_mapper=post_get_stores_under_account_error_mapper,
            request_options=request_options,
        )

    async def post_get_terminal_details(
        self,
        *,
        body: GetTerminalDetailsRequest | GetTerminalDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetTerminalDetailsResponse, PostGetTerminalDetailsErrorBody]:
        """Returns the details of a payment terminal, including where the terminal is assigned to. The response returns
        the same details that are provided in the terminal list in your Customer Area and in the Terminal Fleet report.

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default28("/getTerminalDetails"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetTerminalDetailsRequest | GetTerminalDetailsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GetTerminalDetailsResponse],
            error_mapper=post_get_terminal_details_error_mapper,
            request_options=request_options,
        )

    async def post_get_terminals_under_account(
        self,
        *,
        body: GetTerminalsUnderAccountRequest | GetTerminalsUnderAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetTerminalsUnderAccountResponse, PostGetTerminalsUnderAccountErrorBody]:
        """Returns a list of payment terminals associated with a company account, merchant account, or store. The
        response shows whether the terminals are in the inventory, or in-store (ready for boarding or already boarded).

        >From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate
        the management of your terminal fleet, use our `Management API
        <https://docs.adyen.com/api-explorer/Management/latest/overview>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default28("/getTerminalsUnderAccount"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetTerminalsUnderAccountRequest | GetTerminalsUnderAccountRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GetTerminalsUnderAccountResponse],
            error_mapper=post_get_terminals_under_account_error_mapper,
            request_options=request_options,
        )

    async def post_issue(
        self,
        *,
        body: StoredValueIssueRequest | StoredValueIssueRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredValueIssueResponse, PostIssueErrorBody]:
        """Issues a new card of the given payment method.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/issue"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueIssueRequest | StoredValueIssueRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[StoredValueIssueResponse],
            error_mapper=post_issue_error_mapper,
            request_options=request_options,
        )

    async def post_list_recurring_details(
        self,
        *,
        body: RecurringDetailsRequest | RecurringDetailsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringDetailsResult, PostListRecurringDetailsErrorBody]:
        """Lists the stored payment details for a shopper, if there are any available. The recurring detail ID can be
        used with a regular authorisation request to charge the shopper. A summary of the payment detail is returned for
        presentation to the shopper.

        For more information, refer to `Retrieve stored details
        <https://docs.adyen.com/classic-integration/recurring-payments/retrieve-stored-details/>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/listRecurringDetails"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RecurringDetailsRequest | RecurringDetailsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[RecurringDetailsResult],
            error_mapper=post_list_recurring_details_error_mapper,
            request_options=request_options,
        )

    async def post_load(
        self,
        *,
        body: StoredValueLoadRequest | StoredValueLoadRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredValueLoadResponse, PostLoadErrorBody]:
        """Loads the payment method with the specified funds.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/load"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueLoadRequest | StoredValueLoadRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[StoredValueLoadResponse],
            error_mapper=post_load_error_mapper,
            request_options=request_options,
        )

    async def post_merge_balance(
        self,
        *,
        body: StoredValueBalanceMergeRequest | StoredValueBalanceMergeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredValueBalanceMergeResponse, PostMergeBalanceErrorBody]:
        """Increases the balance of the paymentmethod by the full amount left on the source paymentmethod

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/mergeBalance"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueBalanceMergeRequest | StoredValueBalanceMergeRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[StoredValueBalanceMergeResponse],
            error_mapper=post_merge_balance_error_mapper,
            request_options=request_options,
        )

    async def post_notify_shopper(
        self,
        *,
        body: NotifyShopperRequest | NotifyShopperRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NotifyShopperResult, PostNotifyShopperErrorBody]:
        """Sends a request to the issuer so they can inform the shopper about the upcoming recurring payment. This
        endpoint is used only for local acquiring in India. For more information, refer to `Recurring card payments in
        India <https://docs.adyen.com/payment-methods/cards/cards-recurring-india>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/notifyShopper"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[NotifyShopperRequest | NotifyShopperRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[NotifyShopperResult],
            error_mapper=post_notify_shopper_error_mapper,
            request_options=request_options,
        )

    async def post_payout_account_holder(
        self,
        *,
        body: PayoutAccountHolderRequest | PayoutAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayoutAccountHolderResponse, PostPayoutAccountHolderErrorBody]:
        """Pays out a specified amount from an account to the bank account of account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/payoutAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PayoutAccountHolderRequest | PayoutAccountHolderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[PayoutAccountHolderResponse],
            error_mapper=post_payout_account_holder_error_mapper,
            request_options=request_options,
        )

    async def post_refund_funds_transfer(
        self,
        *,
        body: RefundFundsTransferRequest | RefundFundsTransferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RefundFundsTransferResponse, PostRefundFundsTransferErrorBody]:
        """Refunds funds transferred from one account to another. Both accounts must be in the same platform, but can
        have different account holders.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/refundFundsTransfer"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundFundsTransferRequest | RefundFundsTransferRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[RefundFundsTransferResponse],
            error_mapper=post_refund_funds_transfer_error_mapper,
            request_options=request_options,
        )

    async def post_refund_not_paid_out_transfers(
        self,
        *,
        body: RefundNotPaidOutTransfersRequest | RefundNotPaidOutTransfersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostRefundNotPaidOutTransfersErrorBody]:
        """Refunds all the transactions of an account that have taken place since the most recent payout. This request
        is on a account basis (as opposed to a payment basis), so only the portion of the payment that was made to the
        specified account is refunded. The commissions, fees, and payments to other accounts remain in the accounts to
        which they were sent as designated by the original payment's split details.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/refundNotPaidOutTransfers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundNotPaidOutTransfersRequest | RefundNotPaidOutTransfersRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GenericResponse],
            error_mapper=post_refund_not_paid_out_transfers_error_mapper,
            request_options=request_options,
        )

    async def post_request_subject_erasure(
        self,
        *,
        body: SubjectErasureByPspReferenceRequest | SubjectErasureByPspReferenceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubjectErasureResponse, PostRequestSubjectErasureErrorBody]:
        """Sends the PSP reference containing the shopper data that should be deleted.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default6("/requestSubjectErasure"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubjectErasureByPspReferenceRequest | SubjectErasureByPspReferenceRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[SubjectErasureResponse],
            error_mapper=post_request_subject_erasure_error_mapper,
            request_options=request_options,
        )

    async def post_retrieve_applicable_defense_reasons(
        self,
        *,
        body: DefenseReasonsRequest | DefenseReasonsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DefenseReasonsResponse, PostRetrieveApplicableDefenseReasonsErrorBody]:
        """Returns a list of all applicable defense reasons to defend a specific dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default22("/retrieveApplicableDefenseReasons"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DefenseReasonsRequest | DefenseReasonsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[DefenseReasonsResponse],
            error_mapper=post_retrieve_applicable_defense_reasons_error_mapper,
            request_options=request_options,
        )

    async def post_schedule_account_updater(
        self,
        *,
        body: ScheduleAccountUpdaterRequest | ScheduleAccountUpdaterRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduleAccountUpdaterResult, PostScheduleAccountUpdaterErrorBody]:
        """When making the API call, you can submit either the credit card information, or the recurring detail
        reference and the shopper reference:
        * If the card information is provided, all the sub-fields for ``card`` are mandatory.
        * If the recurring detail reference is provided, the fields for ``shopperReference`` and
            ``selectedRecurringDetailReference`` are mandatory.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default2("/scheduleAccountUpdater"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduleAccountUpdaterRequest | ScheduleAccountUpdaterRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[ScheduleAccountUpdaterResult],
            error_mapper=post_schedule_account_updater_error_mapper,
            request_options=request_options,
        )

    async def post_sessions3(
        self,
        *,
        body: CreateSessionRequest | CreateSessionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CertificateLoadingResponse, RawError]:
        """Establishes a secure communications session between the POS Mobile SDK and the Adyen payments platform,
        through mutual authentication. The request sends a setup token that identifies the SDK and the device. The
        response returns a session token that the SDK can use to authenticate responses received from the Adyen payments
        platform. >This request applies to **mobile in-person** transactions. You cannot use this request to create
        online payments sessions.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default27("/sessions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSessionRequest | CreateSessionRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CertificateLoadingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def post_setup_beneficiary(
        self,
        *,
        body: SetupBeneficiaryRequest | SetupBeneficiaryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostSetupBeneficiaryErrorBody]:
        """Defines a benefactor and a beneficiary relationship between two accounts. At the time of
        benefactor/beneficiary setup, the funds in the benefactor account are transferred to the beneficiary account,
        and any further payments to the benefactor account are automatically sent to the beneficiary account. A series
        of benefactor/beneficiaries may not exceed four beneficiaries and may not have a cycle in it.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/setupBeneficiary"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetupBeneficiaryRequest | SetupBeneficiaryRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GenericResponse],
            error_mapper=post_setup_beneficiary_error_mapper,
            request_options=request_options,
        )

    async def post_supply_defense_document(
        self,
        *,
        body: SupplyDefenseDocumentRequest | SupplyDefenseDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SupplyDefenseDocumentResponse, PostSupplyDefenseDocumentErrorBody]:
        """Supplies a specific dispute defense document.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default22("/supplyDefenseDocument"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SupplyDefenseDocumentRequest | SupplyDefenseDocumentRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[SupplyDefenseDocumentResponse],
            error_mapper=post_supply_defense_document_error_mapper,
            request_options=request_options,
        )

    async def post_test_notification_configuration(
        self,
        *,
        body: TestNotificationConfigurationRequest | TestNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TestNotificationConfigurationResponse, PostTestNotificationConfigurationErrorBody]:
        """Tests an existing notification subscription configuration. For each event type specified, a test notification
        will be generated and sent to the URL configured in the subscription specified.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/testNotificationConfiguration"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TestNotificationConfigurationRequest | TestNotificationConfigurationRequestDict | None](
                body
            ),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TestNotificationConfigurationResponse],
            error_mapper=post_test_notification_configuration_error_mapper,
            request_options=request_options,
        )

    async def post_transfer_funds(
        self,
        *,
        body: TransferFundsRequest | TransferFundsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferFundsResponse, PostTransferFundsErrorBody]:
        """Transfers funds from one account to another account. Both accounts must be in the same platform, but can have
        different account holders. The transfer must include a transfer code, which should be determined by the
        platform, in compliance with local regulations.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default16("/transferFunds"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferFundsRequest | TransferFundsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TransferFundsResponse],
            error_mapper=post_transfer_funds_error_mapper,
            request_options=request_options,
        )

    async def post_update_notification_configuration(
        self,
        *,
        body: UpdateNotificationConfigurationRequest | UpdateNotificationConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetNotificationConfigurationResponse, PostUpdateNotificationConfigurationErrorBody]:
        """Updates an existing notification subscription configuration. If you are updating the event types, you must
        provide all event types, otherwise the previous event type configuration will be overwritten.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/updateNotificationConfiguration"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateNotificationConfigurationRequest | UpdateNotificationConfigurationRequestDict | None](
                body
            ),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GetNotificationConfigurationResponse],
            error_mapper=post_update_notification_configuration_error_mapper,
            request_options=request_options,
        )

    async def post_void_transaction(
        self,
        *,
        body: StoredValueVoidRequest | StoredValueVoidRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredValueVoidResponse, PostVoidTransactionErrorBody]:
        """Voids the referenced stored value transaction.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/voidTransaction"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StoredValueVoidRequest | StoredValueVoidRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[StoredValueVoidResponse],
            error_mapper=post_void_transaction_error_mapper,
            request_options=request_options,
        )
