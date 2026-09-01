from __future__ import annotations

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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.get_account_holders_id_balance_accounts_error import (
    GetAccountHoldersIdBalanceAccountsErrorBody,
    get_account_holders_id_balance_accounts_error_mapper,
)
from ..errors.get_account_holders_id_error import GetAccountHoldersIdErrorBody, get_account_holders_id_error_mapper
from ..errors.get_account_holders_id_tax_forms_error import (
    GetAccountHoldersIdTaxFormsErrorBody,
    get_account_holders_id_tax_forms_error_mapper,
)
from ..errors.get_account_holders_id_transaction_rules_error import (
    GetAccountHoldersIdTransactionRulesErrorBody,
    get_account_holders_id_transaction_rules_error_mapper,
)
from ..errors.patch_account_holders_id_error import (
    PatchAccountHoldersIdErrorBody,
    patch_account_holders_id_error_mapper,
)
from ..errors.post_account_holders_error import PostAccountHoldersErrorBody, post_account_holders_error_mapper
from ..errors.post_close_account_holder_error import (
    PostCloseAccountHolderErrorBody,
    post_close_account_holder_error_mapper,
)
from ..errors.post_close_stores_error import PostCloseStoresErrorBody, post_close_stores_error_mapper
from ..errors.post_create_account_holder_error import (
    PostCreateAccountHolderErrorBody,
    post_create_account_holder_error_mapper,
)
from ..errors.post_get_account_holder_error import PostGetAccountHolderErrorBody, post_get_account_holder_error_mapper
from ..errors.post_get_tax_form_error import PostGetTaxFormErrorBody, post_get_tax_form_error_mapper
from ..errors.post_suspend_account_holder_error import (
    PostSuspendAccountHolderErrorBody,
    post_suspend_account_holder_error_mapper,
)
from ..errors.post_un_suspend_account_holder_error import (
    PostUnSuspendAccountHolderErrorBody,
    post_un_suspend_account_holder_error_mapper,
)
from ..errors.post_update_account_holder_error import (
    PostUpdateAccountHolderErrorBody,
    post_update_account_holder_error_mapper,
)
from ..errors.post_update_account_holder_state_error import (
    PostUpdateAccountHolderStateErrorBody,
    post_update_account_holder_state_error_mapper,
)
from ..models.account_holder import AccountHolder
from ..models.account_holder_info import AccountHolderInfo, AccountHolderInfoDict
from ..models.account_holder_update_request import AccountHolderUpdateRequest, AccountHolderUpdateRequestDict
from ..models.close_account_holder_request import CloseAccountHolderRequest, CloseAccountHolderRequestDict
from ..models.close_account_holder_response import CloseAccountHolderResponse
from ..models.close_stores_request import CloseStoresRequest, CloseStoresRequestDict
from ..models.create_account_holder_request import CreateAccountHolderRequest, CreateAccountHolderRequestDict
from ..models.create_account_holder_response import CreateAccountHolderResponse
from ..models.enums.form_type import FormTypeOrStr
from ..models.generic_response import GenericResponse
from ..models.get_account_holder_request import GetAccountHolderRequest, GetAccountHolderRequestDict
from ..models.get_account_holder_response import GetAccountHolderResponse
from ..models.get_account_holder_status_response import GetAccountHolderStatusResponse
from ..models.get_tax_form_request import GetTaxFormRequest, GetTaxFormRequestDict
from ..models.get_tax_form_response import GetTaxFormResponse
from ..models.get_tax_form_response1 import GetTaxFormResponse1
from ..models.paginated_balance_accounts_response import PaginatedBalanceAccountsResponse
from ..models.suspend_account_holder_request import SuspendAccountHolderRequest, SuspendAccountHolderRequestDict
from ..models.suspend_account_holder_response import SuspendAccountHolderResponse
from ..models.tax_form_summary_response import TaxFormSummaryResponse
from ..models.transaction_rules_response import TransactionRulesResponse
from ..models.un_suspend_account_holder_request import UnSuspendAccountHolderRequest, UnSuspendAccountHolderRequestDict
from ..models.un_suspend_account_holder_response import UnSuspendAccountHolderResponse
from ..models.update_account_holder_request import UpdateAccountHolderRequest, UpdateAccountHolderRequestDict
from ..models.update_account_holder_response import UpdateAccountHolderResponse
from ..models.update_account_holder_state_request import (
    UpdateAccountHolderStateRequest,
    UpdateAccountHolderStateRequestDict,
)
from ..server.server import Server


class AccountHolders:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountHoldersWithRawResponse(client, server, auth)

    def get_account_holders_id(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> AccountHolder:
        """Returns an account holder.

        Args:
            id: The unique identifier of the account holder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_account_holders_id(id, request_options=request_options).unwrap()

    def get_account_holders_id_balance_accounts(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedBalanceAccountsResponse:
        """Returns a paginated list of the balance accounts associated with an account holder. To fetch multiple pages,
        use the query parameters.

        For example, to limit the page to 5 balance accounts and skip the first 10, use
        ``/accountHolders/{id}/balanceAccounts?limit=5&offset=10``.

        Args:
            id: The unique identifier of the account holder.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_account_holders_id_balance_accounts(
            id, offset=offset, limit=limit, request_options=request_options
        ).unwrap()

    def get_account_holders_id_tax_form_summary(
        self, id: str, form_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaxFormSummaryResponse:
        """Returns a summary of all tax forms for an account holder.

        Args:
            id: The unique identifier of the account holder.
            form_type: The type of tax form you want a summary for. Accepted values are **US1099k** and **US1099nec**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_account_holders_id_tax_form_summary(
            id, form_type, request_options=request_options
        ).unwrap()

    def get_account_holders_id_tax_forms(
        self,
        id: str,
        form_type: FormTypeOrStr,
        year: int,
        *,
        legal_entity_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetTaxFormResponse1:
        """Generates a tax form for account holders operating in the US. For more information, refer to US tax forms for
        `marketplaces <https://docs.adyen.com/marketplaces/us-tax-forms/>`__ or `platforms
        <https://docs.adyen.com/platforms/us-tax-forms/>`__ .

        Args:
            id: The unique identifier of the account holder.
            form_type: The type of tax form you want to retrieve. Accepted values are **US1099k** and **US1099nec**.
            year: The tax year in **YYYY** format for the tax form you want to retrieve.
            legal_entity_id: The legal entity reference whose tax form you want to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. The requested tax form was not
                available. Unprocessable Entity - a request validation error. Internal Server Error - the server could
                not process the request. ``error`` is ``RestServiceError | RawError``."""
        return self._with_raw_response.get_account_holders_id_tax_forms(
            id, form_type, year, legal_entity_id=legal_entity_id, request_options=request_options
        ).unwrap()

    def get_account_holders_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRulesResponse:
        """Returns a list of transaction rules associated with an account holder.

        Args:
            id: The unique identifier of the account holder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_account_holders_id_transaction_rules(
            id, request_options=request_options
        ).unwrap()

    def patch_account_holders_id(
        self,
        id: str,
        *,
        body: AccountHolderUpdateRequest | AccountHolderUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountHolder:
        """Updates an account holder. When updating an account holder resource, if a parameter is not provided in the
        request, it is left unchanged.

        Args:
            id: The unique identifier of the account holder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_account_holders_id(id, body=body, request_options=request_options).unwrap()

    def post_account_holders(
        self,
        *,
        body: AccountHolderInfo | AccountHolderInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountHolder:
        """Creates an account holder linked to a `legal entity
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_account_holders(body=body, request_options=request_options).unwrap()

    def post_close_account_holder(
        self,
        *,
        body: CloseAccountHolderRequest | CloseAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CloseAccountHolderResponse:
        """Changes the `status of an account holder
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses>`__ to
        **Closed**. This state is final. If an account holder is closed, you can't process transactions, pay out funds,
        or reopen it. If payments are made to an account of an account holder with a **Closed**
        https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status,
        the payments are sent to your liable account.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_close_account_holder(body=body, request_options=request_options).unwrap()

    def post_close_stores(
        self,
        *,
        body: CloseStoresRequest | CloseStoresRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Closes stores associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_close_stores(body=body, request_options=request_options).unwrap()

    def post_create_account_holder(
        self,
        *,
        body: CreateAccountHolderRequest | CreateAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateAccountHolderResponse:
        """Creates an account holder that `represents the sub-merchant's entity
        <https://docs.adyen.com/classic-platforms/account-structure#your-platform>`__ in your platform. The details that
        you need to provide in the request depend on the sub-merchant's legal entity type. For more information, refer
        to `Account holder and accounts
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#legal-entity-types>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_create_account_holder(body=body, request_options=request_options).unwrap()

    def post_get_account_holder(
        self,
        *,
        body: GetAccountHolderRequest | GetAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetAccountHolderResponse:
        """Returns the details of an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_get_account_holder(body=body, request_options=request_options).unwrap()

    def post_get_tax_form(
        self,
        *,
        body: GetTaxFormRequest | GetTaxFormRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetTaxFormResponse:
        """Generates a tax form for account holders operating in the US. For more information, refer to `Providing tax
        forms <https://docs.adyen.com/classic-platforms/tax-forms>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_get_tax_form(body=body, request_options=request_options).unwrap()

    def post_suspend_account_holder(
        self,
        *,
        body: SuspendAccountHolderRequest | SuspendAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SuspendAccountHolderResponse:
        """Changes the `status of an account holder
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses>`__ to
        **Suspended**.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_suspend_account_holder(body=body, request_options=request_options).unwrap()

    def post_un_suspend_account_holder(
        self,
        *,
        body: UnSuspendAccountHolderRequest | UnSuspendAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UnSuspendAccountHolderResponse:
        """Changes the `status of an account holder
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses>`__ from
        **Suspended** to **Inactive**. Account holders can have a **Suspended**
        https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status
        if you suspend them through the https://docs.adyen.com/api-explorer/#/Account/v5/post/suspendAccountHolder
        endpoint or if a verification deadline expires.

        You can only unsuspend account holders if they do not have verification checks with a **FAILED**
        https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_un_suspend_account_holder(
            body=body, request_options=request_options
        ).unwrap()

    def post_update_account_holder(
        self,
        *,
        body: UpdateAccountHolderRequest | UpdateAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateAccountHolderResponse:
        """Updates the ``accountHolderDetails`` and ``processingTier`` of an account holder, and adds bank accounts and
        shareholders.

        When updating ``accountHolderDetails``, parameters that are not included in the request are left unchanged
        except for the following object:

        * ``metadata``: Updating the metadata replaces the entire object. This means that to update an existing
            key-value pair, you must provide the changes, as well as other existing key-value pairs.

        When updating any field in the following objects, you must submit all the fields required for validation:

         * ``address``

        * ``fullPhoneNumber``

        * ``bankAccountDetails.BankAccountDetail``

        * ``businessDetails.shareholders.ShareholderContact``

         For example, to update the ``address.postalCode``, you must also submit the ``address.country``, ``.city``,
            ``.street``, ``.postalCode``, and possibly ``.stateOrProvince`` so that the address can be validated.

        To add a bank account or shareholder, provide the bank account or shareholder details without a
        ``bankAccountUUID`` or a ``shareholderCode``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_update_account_holder(body=body, request_options=request_options).unwrap()

    def post_update_account_holder_state(
        self,
        *,
        body: UpdateAccountHolderStateRequest | UpdateAccountHolderStateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetAccountHolderStatusResponse:
        """Disables or enables the processing or payout state of an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_update_account_holder_state(
            body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AccountHoldersWithRawResponse:
        return self._with_raw_response


class AsyncAccountHolders:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountHoldersWithRawResponse(client, server, auth)

    async def get_account_holders_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountHolder:
        """Returns an account holder.

        Args:
            id: The unique identifier of the account holder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (await self._with_raw_response.get_account_holders_id(id, request_options=request_options)).unwrap()

    async def get_account_holders_id_balance_accounts(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedBalanceAccountsResponse:
        """Returns a paginated list of the balance accounts associated with an account holder. To fetch multiple pages,
        use the query parameters.

        For example, to limit the page to 5 balance accounts and skip the first 10, use
        ``/accountHolders/{id}/balanceAccounts?limit=5&offset=10``.

        Args:
            id: The unique identifier of the account holder.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_account_holders_id_balance_accounts(
                id, offset=offset, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def get_account_holders_id_tax_form_summary(
        self, id: str, form_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaxFormSummaryResponse:
        """Returns a summary of all tax forms for an account holder.

        Args:
            id: The unique identifier of the account holder.
            form_type: The type of tax form you want a summary for. Accepted values are **US1099k** and **US1099nec**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_account_holders_id_tax_form_summary(
                id, form_type, request_options=request_options
            )
        ).unwrap()

    async def get_account_holders_id_tax_forms(
        self,
        id: str,
        form_type: FormTypeOrStr,
        year: int,
        *,
        legal_entity_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetTaxFormResponse1:
        """Generates a tax form for account holders operating in the US. For more information, refer to US tax forms for
        `marketplaces <https://docs.adyen.com/marketplaces/us-tax-forms/>`__ or `platforms
        <https://docs.adyen.com/platforms/us-tax-forms/>`__ .

        Args:
            id: The unique identifier of the account holder.
            form_type: The type of tax form you want to retrieve. Accepted values are **US1099k** and **US1099nec**.
            year: The tax year in **YYYY** format for the tax form you want to retrieve.
            legal_entity_id: The legal entity reference whose tax form you want to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. The requested tax form was not
                available. Unprocessable Entity - a request validation error. Internal Server Error - the server could
                not process the request. ``error`` is ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_account_holders_id_tax_forms(
                id, form_type, year, legal_entity_id=legal_entity_id, request_options=request_options
            )
        ).unwrap()

    async def get_account_holders_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRulesResponse:
        """Returns a list of transaction rules associated with an account holder.

        Args:
            id: The unique identifier of the account holder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_account_holders_id_transaction_rules(id, request_options=request_options)
        ).unwrap()

    async def patch_account_holders_id(
        self,
        id: str,
        *,
        body: AccountHolderUpdateRequest | AccountHolderUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountHolder:
        """Updates an account holder. When updating an account holder resource, if a parameter is not provided in the
        request, it is left unchanged.

        Args:
            id: The unique identifier of the account holder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.patch_account_holders_id(id, body=body, request_options=request_options)
        ).unwrap()

    async def post_account_holders(
        self,
        *,
        body: AccountHolderInfo | AccountHolderInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountHolder:
        """Creates an account holder linked to a `legal entity
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (await self._with_raw_response.post_account_holders(body=body, request_options=request_options)).unwrap()

    async def post_close_account_holder(
        self,
        *,
        body: CloseAccountHolderRequest | CloseAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CloseAccountHolderResponse:
        """Changes the `status of an account holder
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses>`__ to
        **Closed**. This state is final. If an account holder is closed, you can't process transactions, pay out funds,
        or reopen it. If payments are made to an account of an account holder with a **Closed**
        https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status,
        the payments are sent to your liable account.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (
            await self._with_raw_response.post_close_account_holder(body=body, request_options=request_options)
        ).unwrap()

    async def post_close_stores(
        self,
        *,
        body: CloseStoresRequest | CloseStoresRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Closes stores associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (await self._with_raw_response.post_close_stores(body=body, request_options=request_options)).unwrap()

    async def post_create_account_holder(
        self,
        *,
        body: CreateAccountHolderRequest | CreateAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateAccountHolderResponse:
        """Creates an account holder that `represents the sub-merchant's entity
        <https://docs.adyen.com/classic-platforms/account-structure#your-platform>`__ in your platform. The details that
        you need to provide in the request depend on the sub-merchant's legal entity type. For more information, refer
        to `Account holder and accounts
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#legal-entity-types>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (
            await self._with_raw_response.post_create_account_holder(body=body, request_options=request_options)
        ).unwrap()

    async def post_get_account_holder(
        self,
        *,
        body: GetAccountHolderRequest | GetAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetAccountHolderResponse:
        """Returns the details of an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (
            await self._with_raw_response.post_get_account_holder(body=body, request_options=request_options)
        ).unwrap()

    async def post_get_tax_form(
        self,
        *,
        body: GetTaxFormRequest | GetTaxFormRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetTaxFormResponse:
        """Generates a tax form for account holders operating in the US. For more information, refer to `Providing tax
        forms <https://docs.adyen.com/classic-platforms/tax-forms>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (await self._with_raw_response.post_get_tax_form(body=body, request_options=request_options)).unwrap()

    async def post_suspend_account_holder(
        self,
        *,
        body: SuspendAccountHolderRequest | SuspendAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SuspendAccountHolderResponse:
        """Changes the `status of an account holder
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses>`__ to
        **Suspended**.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (
            await self._with_raw_response.post_suspend_account_holder(body=body, request_options=request_options)
        ).unwrap()

    async def post_un_suspend_account_holder(
        self,
        *,
        body: UnSuspendAccountHolderRequest | UnSuspendAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UnSuspendAccountHolderResponse:
        """Changes the `status of an account holder
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses>`__ from
        **Suspended** to **Inactive**. Account holders can have a **Suspended**
        https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status
        if you suspend them through the https://docs.adyen.com/api-explorer/#/Account/v5/post/suspendAccountHolder
        endpoint or if a verification deadline expires.

        You can only unsuspend account holders if they do not have verification checks with a **FAILED**
        https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (
            await self._with_raw_response.post_un_suspend_account_holder(body=body, request_options=request_options)
        ).unwrap()

    async def post_update_account_holder(
        self,
        *,
        body: UpdateAccountHolderRequest | UpdateAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateAccountHolderResponse:
        """Updates the ``accountHolderDetails`` and ``processingTier`` of an account holder, and adds bank accounts and
        shareholders.

        When updating ``accountHolderDetails``, parameters that are not included in the request are left unchanged
        except for the following object:

        * ``metadata``: Updating the metadata replaces the entire object. This means that to update an existing
            key-value pair, you must provide the changes, as well as other existing key-value pairs.

        When updating any field in the following objects, you must submit all the fields required for validation:

         * ``address``

        * ``fullPhoneNumber``

        * ``bankAccountDetails.BankAccountDetail``

        * ``businessDetails.shareholders.ShareholderContact``

         For example, to update the ``address.postalCode``, you must also submit the ``address.country``, ``.city``,
            ``.street``, ``.postalCode``, and possibly ``.stateOrProvince`` so that the address can be validated.

        To add a bank account or shareholder, provide the bank account or shareholder details without a
        ``bankAccountUUID`` or a ``shareholderCode``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (
            await self._with_raw_response.post_update_account_holder(body=body, request_options=request_options)
        ).unwrap()

    async def post_update_account_holder_state(
        self,
        *,
        body: UpdateAccountHolderStateRequest | UpdateAccountHolderStateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetAccountHolderStatusResponse:
        """Disables or enables the processing or payout state of an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (
            await self._with_raw_response.post_update_account_holder_state(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountHoldersWithRawResponse:
        return self._with_raw_response


class AccountHoldersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_account_holders_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountHolder, GetAccountHoldersIdErrorBody]:
        """Returns an account holder.

        Args:
            id: The unique identifier of the account holder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/accountHolders/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AccountHolder],
            error_mapper=get_account_holders_id_error_mapper,
            request_options=request_options,
        )

    def get_account_holders_id_balance_accounts(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedBalanceAccountsResponse, GetAccountHoldersIdBalanceAccountsErrorBody]:
        """Returns a paginated list of the balance accounts associated with an account holder. To fetch multiple pages,
        use the query parameters.

        For example, to limit the page to 5 balance accounts and skip the first 10, use
        ``/accountHolders/{id}/balanceAccounts?limit=5&offset=10``.

        Args:
            id: The unique identifier of the account holder.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/accountHolders/{id}/balanceAccounts"),
            path_params=[param[str]("id", id)],
            query_params=[param[int | None]("offset", offset), param[int | None]("limit", limit)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaginatedBalanceAccountsResponse],
            error_mapper=get_account_holders_id_balance_accounts_error_mapper,
            request_options=request_options,
        )

    def get_account_holders_id_tax_form_summary(
        self, id: str, form_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaxFormSummaryResponse, RawError]:
        """Returns a summary of all tax forms for an account holder.

        Args:
            id: The unique identifier of the account holder.
            form_type: The type of tax form you want a summary for. Accepted values are **US1099k** and **US1099nec**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/accountHolders/{id}/taxFormSummary"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("formType", form_type)],
            decoder=json_decoder[TaxFormSummaryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_account_holders_id_tax_forms(
        self,
        id: str,
        form_type: FormTypeOrStr,
        year: int,
        *,
        legal_entity_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetTaxFormResponse1, GetAccountHoldersIdTaxFormsErrorBody]:
        """Generates a tax form for account holders operating in the US. For more information, refer to US tax forms for
        `marketplaces <https://docs.adyen.com/marketplaces/us-tax-forms/>`__ or `platforms
        <https://docs.adyen.com/platforms/us-tax-forms/>`__ .

        Args:
            id: The unique identifier of the account holder.
            form_type: The type of tax form you want to retrieve. Accepted values are **US1099k** and **US1099nec**.
            year: The tax year in **YYYY** format for the tax form you want to retrieve.
            legal_entity_id: The legal entity reference whose tax form you want to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/accountHolders/{id}/taxForms"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[FormTypeOrStr]("formType", form_type),
                param[int]("year", year),
                param[str | None]("legalEntityId", legal_entity_id),
            ],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetTaxFormResponse1],
            error_mapper=get_account_holders_id_tax_forms_error_mapper,
            request_options=request_options,
        )

    def get_account_holders_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRulesResponse, GetAccountHoldersIdTransactionRulesErrorBody]:
        """Returns a list of transaction rules associated with an account holder.

        Args:
            id: The unique identifier of the account holder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/accountHolders/{id}/transactionRules"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionRulesResponse],
            error_mapper=get_account_holders_id_transaction_rules_error_mapper,
            request_options=request_options,
        )

    def patch_account_holders_id(
        self,
        id: str,
        *,
        body: AccountHolderUpdateRequest | AccountHolderUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountHolder, PatchAccountHoldersIdErrorBody]:
        """Updates an account holder. When updating an account holder resource, if a parameter is not provided in the
        request, it is left unchanged.

        Args:
            id: The unique identifier of the account holder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/accountHolders/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountHolderUpdateRequest | AccountHolderUpdateRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AccountHolder],
            error_mapper=patch_account_holders_id_error_mapper,
            request_options=request_options,
        )

    def post_account_holders(
        self,
        *,
        body: AccountHolderInfo | AccountHolderInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountHolder, PostAccountHoldersErrorBody]:
        """Creates an account holder linked to a `legal entity
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/accountHolders"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountHolderInfo | AccountHolderInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AccountHolder],
            error_mapper=post_account_holders_error_mapper,
            request_options=request_options,
        )

    def post_close_account_holder(
        self,
        *,
        body: CloseAccountHolderRequest | CloseAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CloseAccountHolderResponse, PostCloseAccountHolderErrorBody]:
        """Changes the `status of an account holder
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses>`__ to
        **Closed**. This state is final. If an account holder is closed, you can't process transactions, pay out funds,
        or reopen it. If payments are made to an account of an account holder with a **Closed**
        https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status,
        the payments are sent to your liable account.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/closeAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CloseAccountHolderRequest | CloseAccountHolderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CloseAccountHolderResponse],
            error_mapper=post_close_account_holder_error_mapper,
            request_options=request_options,
        )

    def post_close_stores(
        self,
        *,
        body: CloseStoresRequest | CloseStoresRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostCloseStoresErrorBody]:
        """Closes stores associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/closeStores"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CloseStoresRequest | CloseStoresRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_close_stores_error_mapper,
            request_options=request_options,
        )

    def post_create_account_holder(
        self,
        *,
        body: CreateAccountHolderRequest | CreateAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateAccountHolderResponse, PostCreateAccountHolderErrorBody]:
        """Creates an account holder that `represents the sub-merchant's entity
        <https://docs.adyen.com/classic-platforms/account-structure#your-platform>`__ in your platform. The details that
        you need to provide in the request depend on the sub-merchant's legal entity type. For more information, refer
        to `Account holder and accounts
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#legal-entity-types>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/createAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAccountHolderRequest | CreateAccountHolderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateAccountHolderResponse],
            error_mapper=post_create_account_holder_error_mapper,
            request_options=request_options,
        )

    def post_get_account_holder(
        self,
        *,
        body: GetAccountHolderRequest | GetAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetAccountHolderResponse, PostGetAccountHolderErrorBody]:
        """Returns the details of an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/getAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetAccountHolderRequest | GetAccountHolderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetAccountHolderResponse],
            error_mapper=post_get_account_holder_error_mapper,
            request_options=request_options,
        )

    def post_get_tax_form(
        self,
        *,
        body: GetTaxFormRequest | GetTaxFormRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetTaxFormResponse, PostGetTaxFormErrorBody]:
        """Generates a tax form for account holders operating in the US. For more information, refer to `Providing tax
        forms <https://docs.adyen.com/classic-platforms/tax-forms>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/getTaxForm"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetTaxFormRequest | GetTaxFormRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetTaxFormResponse],
            error_mapper=post_get_tax_form_error_mapper,
            request_options=request_options,
        )

    def post_suspend_account_holder(
        self,
        *,
        body: SuspendAccountHolderRequest | SuspendAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SuspendAccountHolderResponse, PostSuspendAccountHolderErrorBody]:
        """Changes the `status of an account holder
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses>`__ to
        **Suspended**.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/suspendAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SuspendAccountHolderRequest | SuspendAccountHolderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SuspendAccountHolderResponse],
            error_mapper=post_suspend_account_holder_error_mapper,
            request_options=request_options,
        )

    def post_un_suspend_account_holder(
        self,
        *,
        body: UnSuspendAccountHolderRequest | UnSuspendAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UnSuspendAccountHolderResponse, PostUnSuspendAccountHolderErrorBody]:
        """Changes the `status of an account holder
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses>`__ from
        **Suspended** to **Inactive**. Account holders can have a **Suspended**
        https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status
        if you suspend them through the https://docs.adyen.com/api-explorer/#/Account/v5/post/suspendAccountHolder
        endpoint or if a verification deadline expires.

        You can only unsuspend account holders if they do not have verification checks with a **FAILED**
        https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/unSuspendAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UnSuspendAccountHolderRequest | UnSuspendAccountHolderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UnSuspendAccountHolderResponse],
            error_mapper=post_un_suspend_account_holder_error_mapper,
            request_options=request_options,
        )

    def post_update_account_holder(
        self,
        *,
        body: UpdateAccountHolderRequest | UpdateAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateAccountHolderResponse, PostUpdateAccountHolderErrorBody]:
        """Updates the ``accountHolderDetails`` and ``processingTier`` of an account holder, and adds bank accounts and
        shareholders.

        When updating ``accountHolderDetails``, parameters that are not included in the request are left unchanged
        except for the following object:

        * ``metadata``: Updating the metadata replaces the entire object. This means that to update an existing
            key-value pair, you must provide the changes, as well as other existing key-value pairs.

        When updating any field in the following objects, you must submit all the fields required for validation:

         * ``address``

        * ``fullPhoneNumber``

        * ``bankAccountDetails.BankAccountDetail``

        * ``businessDetails.shareholders.ShareholderContact``

         For example, to update the ``address.postalCode``, you must also submit the ``address.country``, ``.city``,
            ``.street``, ``.postalCode``, and possibly ``.stateOrProvince`` so that the address can be validated.

        To add a bank account or shareholder, provide the bank account or shareholder details without a
        ``bankAccountUUID`` or a ``shareholderCode``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/updateAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateAccountHolderRequest | UpdateAccountHolderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UpdateAccountHolderResponse],
            error_mapper=post_update_account_holder_error_mapper,
            request_options=request_options,
        )

    def post_update_account_holder_state(
        self,
        *,
        body: UpdateAccountHolderStateRequest | UpdateAccountHolderStateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetAccountHolderStatusResponse, PostUpdateAccountHolderStateErrorBody]:
        """Disables or enables the processing or payout state of an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/updateAccountHolderState"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateAccountHolderStateRequest | UpdateAccountHolderStateRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetAccountHolderStatusResponse],
            error_mapper=post_update_account_holder_state_error_mapper,
            request_options=request_options,
        )


class AsyncAccountHoldersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_account_holders_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountHolder, GetAccountHoldersIdErrorBody]:
        """Returns an account holder.

        Args:
            id: The unique identifier of the account holder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/accountHolders/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AccountHolder],
            error_mapper=get_account_holders_id_error_mapper,
            request_options=request_options,
        )

    async def get_account_holders_id_balance_accounts(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedBalanceAccountsResponse, GetAccountHoldersIdBalanceAccountsErrorBody]:
        """Returns a paginated list of the balance accounts associated with an account holder. To fetch multiple pages,
        use the query parameters.

        For example, to limit the page to 5 balance accounts and skip the first 10, use
        ``/accountHolders/{id}/balanceAccounts?limit=5&offset=10``.

        Args:
            id: The unique identifier of the account holder.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/accountHolders/{id}/balanceAccounts"),
            path_params=[param[str]("id", id)],
            query_params=[param[int | None]("offset", offset), param[int | None]("limit", limit)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaginatedBalanceAccountsResponse],
            error_mapper=get_account_holders_id_balance_accounts_error_mapper,
            request_options=request_options,
        )

    async def get_account_holders_id_tax_form_summary(
        self, id: str, form_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaxFormSummaryResponse, RawError]:
        """Returns a summary of all tax forms for an account holder.

        Args:
            id: The unique identifier of the account holder.
            form_type: The type of tax form you want a summary for. Accepted values are **US1099k** and **US1099nec**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/accountHolders/{id}/taxFormSummary"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("formType", form_type)],
            decoder=json_decoder[TaxFormSummaryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_account_holders_id_tax_forms(
        self,
        id: str,
        form_type: FormTypeOrStr,
        year: int,
        *,
        legal_entity_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetTaxFormResponse1, GetAccountHoldersIdTaxFormsErrorBody]:
        """Generates a tax form for account holders operating in the US. For more information, refer to US tax forms for
        `marketplaces <https://docs.adyen.com/marketplaces/us-tax-forms/>`__ or `platforms
        <https://docs.adyen.com/platforms/us-tax-forms/>`__ .

        Args:
            id: The unique identifier of the account holder.
            form_type: The type of tax form you want to retrieve. Accepted values are **US1099k** and **US1099nec**.
            year: The tax year in **YYYY** format for the tax form you want to retrieve.
            legal_entity_id: The legal entity reference whose tax form you want to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/accountHolders/{id}/taxForms"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[FormTypeOrStr]("formType", form_type),
                param[int]("year", year),
                param[str | None]("legalEntityId", legal_entity_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetTaxFormResponse1],
            error_mapper=get_account_holders_id_tax_forms_error_mapper,
            request_options=request_options,
        )

    async def get_account_holders_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRulesResponse, GetAccountHoldersIdTransactionRulesErrorBody]:
        """Returns a list of transaction rules associated with an account holder.

        Args:
            id: The unique identifier of the account holder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/accountHolders/{id}/transactionRules"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionRulesResponse],
            error_mapper=get_account_holders_id_transaction_rules_error_mapper,
            request_options=request_options,
        )

    async def patch_account_holders_id(
        self,
        id: str,
        *,
        body: AccountHolderUpdateRequest | AccountHolderUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountHolder, PatchAccountHoldersIdErrorBody]:
        """Updates an account holder. When updating an account holder resource, if a parameter is not provided in the
        request, it is left unchanged.

        Args:
            id: The unique identifier of the account holder.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/accountHolders/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountHolderUpdateRequest | AccountHolderUpdateRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AccountHolder],
            error_mapper=patch_account_holders_id_error_mapper,
            request_options=request_options,
        )

    async def post_account_holders(
        self,
        *,
        body: AccountHolderInfo | AccountHolderInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountHolder, PostAccountHoldersErrorBody]:
        """Creates an account holder linked to a `legal entity
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/accountHolders"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountHolderInfo | AccountHolderInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AccountHolder],
            error_mapper=post_account_holders_error_mapper,
            request_options=request_options,
        )

    async def post_close_account_holder(
        self,
        *,
        body: CloseAccountHolderRequest | CloseAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CloseAccountHolderResponse, PostCloseAccountHolderErrorBody]:
        """Changes the `status of an account holder
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses>`__ to
        **Closed**. This state is final. If an account holder is closed, you can't process transactions, pay out funds,
        or reopen it. If payments are made to an account of an account holder with a **Closed**
        https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status,
        the payments are sent to your liable account.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/closeAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CloseAccountHolderRequest | CloseAccountHolderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CloseAccountHolderResponse],
            error_mapper=post_close_account_holder_error_mapper,
            request_options=request_options,
        )

    async def post_close_stores(
        self,
        *,
        body: CloseStoresRequest | CloseStoresRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostCloseStoresErrorBody]:
        """Closes stores associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/closeStores"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CloseStoresRequest | CloseStoresRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_close_stores_error_mapper,
            request_options=request_options,
        )

    async def post_create_account_holder(
        self,
        *,
        body: CreateAccountHolderRequest | CreateAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateAccountHolderResponse, PostCreateAccountHolderErrorBody]:
        """Creates an account holder that `represents the sub-merchant's entity
        <https://docs.adyen.com/classic-platforms/account-structure#your-platform>`__ in your platform. The details that
        you need to provide in the request depend on the sub-merchant's legal entity type. For more information, refer
        to `Account holder and accounts
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#legal-entity-types>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/createAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAccountHolderRequest | CreateAccountHolderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateAccountHolderResponse],
            error_mapper=post_create_account_holder_error_mapper,
            request_options=request_options,
        )

    async def post_get_account_holder(
        self,
        *,
        body: GetAccountHolderRequest | GetAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetAccountHolderResponse, PostGetAccountHolderErrorBody]:
        """Returns the details of an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/getAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetAccountHolderRequest | GetAccountHolderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetAccountHolderResponse],
            error_mapper=post_get_account_holder_error_mapper,
            request_options=request_options,
        )

    async def post_get_tax_form(
        self,
        *,
        body: GetTaxFormRequest | GetTaxFormRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetTaxFormResponse, PostGetTaxFormErrorBody]:
        """Generates a tax form for account holders operating in the US. For more information, refer to `Providing tax
        forms <https://docs.adyen.com/classic-platforms/tax-forms>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/getTaxForm"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetTaxFormRequest | GetTaxFormRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetTaxFormResponse],
            error_mapper=post_get_tax_form_error_mapper,
            request_options=request_options,
        )

    async def post_suspend_account_holder(
        self,
        *,
        body: SuspendAccountHolderRequest | SuspendAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SuspendAccountHolderResponse, PostSuspendAccountHolderErrorBody]:
        """Changes the `status of an account holder
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses>`__ to
        **Suspended**.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/suspendAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SuspendAccountHolderRequest | SuspendAccountHolderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SuspendAccountHolderResponse],
            error_mapper=post_suspend_account_holder_error_mapper,
            request_options=request_options,
        )

    async def post_un_suspend_account_holder(
        self,
        *,
        body: UnSuspendAccountHolderRequest | UnSuspendAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UnSuspendAccountHolderResponse, PostUnSuspendAccountHolderErrorBody]:
        """Changes the `status of an account holder
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses>`__ from
        **Suspended** to **Inactive**. Account holders can have a **Suspended**
        https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status
        if you suspend them through the https://docs.adyen.com/api-explorer/#/Account/v5/post/suspendAccountHolder
        endpoint or if a verification deadline expires.

        You can only unsuspend account holders if they do not have verification checks with a **FAILED**
        https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/unSuspendAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UnSuspendAccountHolderRequest | UnSuspendAccountHolderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UnSuspendAccountHolderResponse],
            error_mapper=post_un_suspend_account_holder_error_mapper,
            request_options=request_options,
        )

    async def post_update_account_holder(
        self,
        *,
        body: UpdateAccountHolderRequest | UpdateAccountHolderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateAccountHolderResponse, PostUpdateAccountHolderErrorBody]:
        """Updates the ``accountHolderDetails`` and ``processingTier`` of an account holder, and adds bank accounts and
        shareholders.

        When updating ``accountHolderDetails``, parameters that are not included in the request are left unchanged
        except for the following object:

        * ``metadata``: Updating the metadata replaces the entire object. This means that to update an existing
            key-value pair, you must provide the changes, as well as other existing key-value pairs.

        When updating any field in the following objects, you must submit all the fields required for validation:

         * ``address``

        * ``fullPhoneNumber``

        * ``bankAccountDetails.BankAccountDetail``

        * ``businessDetails.shareholders.ShareholderContact``

         For example, to update the ``address.postalCode``, you must also submit the ``address.country``, ``.city``,
            ``.street``, ``.postalCode``, and possibly ``.stateOrProvince`` so that the address can be validated.

        To add a bank account or shareholder, provide the bank account or shareholder details without a
        ``bankAccountUUID`` or a ``shareholderCode``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/updateAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateAccountHolderRequest | UpdateAccountHolderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UpdateAccountHolderResponse],
            error_mapper=post_update_account_holder_error_mapper,
            request_options=request_options,
        )

    async def post_update_account_holder_state(
        self,
        *,
        body: UpdateAccountHolderStateRequest | UpdateAccountHolderStateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetAccountHolderStatusResponse, PostUpdateAccountHolderStateErrorBody]:
        """Disables or enables the processing or payout state of an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/updateAccountHolderState"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateAccountHolderStateRequest | UpdateAccountHolderStateRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetAccountHolderStatusResponse],
            error_mapper=post_update_account_holder_state_error_mapper,
            request_options=request_options,
        )
