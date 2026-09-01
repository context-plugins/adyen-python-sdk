from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.get_balance_accounts_id_error import GetBalanceAccountsIdErrorBody, get_balance_accounts_id_error_mapper
from ..errors.get_balance_accounts_id_payment_instruments_error import (
    GetBalanceAccountsIdPaymentInstrumentsErrorBody,
    get_balance_accounts_id_payment_instruments_error_mapper,
)
from ..errors.get_balance_accounts_id_transaction_rules_error import (
    GetBalanceAccountsIdTransactionRulesErrorBody,
    get_balance_accounts_id_transaction_rules_error_mapper,
)
from ..errors.patch_balance_accounts_id_error import (
    PatchBalanceAccountsIdErrorBody,
    patch_balance_accounts_id_error_mapper,
)
from ..errors.post_balance_accounts_error import PostBalanceAccountsErrorBody, post_balance_accounts_error_mapper
from ..models.balance_account import BalanceAccount
from ..models.balance_account_info import BalanceAccountInfo, BalanceAccountInfoDict
from ..models.balance_account_update_request import BalanceAccountUpdateRequest, BalanceAccountUpdateRequestDict
from ..models.paginated_payment_instruments_response import PaginatedPaymentInstrumentsResponse
from ..models.transaction_rules_response import TransactionRulesResponse
from ..server.server import Server


class BalanceAccounts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BalanceAccountsWithRawResponse(client, server, auth)

    def get_balance_accounts_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BalanceAccount:
        """Returns a balance account and its balances for the default currency and other currencies with a non-zero
        balance.

        Args:
            id: The unique identifier of the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_balance_accounts_id(id, request_options=request_options).unwrap()

    def get_balance_accounts_id_payment_instruments(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedPaymentInstrumentsResponse:
        """Returns a paginated list of the payment instruments associated with a balance account.

        To fetch multiple pages, use the query parameters.For example, to limit the page to 3 payment instruments which
        are in active status and to skip the first 6, use
        ``/balanceAccounts/{id}/paymentInstruments?limit=3&offset=6&status=active``.

        Args:
            id: The unique identifier of the balance account.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            status: The status of the payment instruments that you want to get. By default, the response includes
                payment instruments with any status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_balance_accounts_id_payment_instruments(
            id, offset=offset, limit=limit, status=status, request_options=request_options
        ).unwrap()

    def get_balance_accounts_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRulesResponse:
        """Returns a list of transaction rules associated with a balance account.

        Args:
            id: The unique identifier of the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_balance_accounts_id_transaction_rules(
            id, request_options=request_options
        ).unwrap()

    def patch_balance_accounts_id(
        self,
        id: str,
        *,
        body: BalanceAccountUpdateRequest | BalanceAccountUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceAccount:
        """Updates a balance account.

        Args:
            id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_balance_accounts_id(
            id, body=body, request_options=request_options
        ).unwrap()

    def post_balance_accounts(
        self,
        *,
        body: BalanceAccountInfo | BalanceAccountInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceAccount:
        """Creates a balance account that holds the funds of the associated account holder.

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
        return self._with_raw_response.post_balance_accounts(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> BalanceAccountsWithRawResponse:
        return self._with_raw_response


class AsyncBalanceAccounts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBalanceAccountsWithRawResponse(client, server, auth)

    async def get_balance_accounts_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BalanceAccount:
        """Returns a balance account and its balances for the default currency and other currencies with a non-zero
        balance.

        Args:
            id: The unique identifier of the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (await self._with_raw_response.get_balance_accounts_id(id, request_options=request_options)).unwrap()

    async def get_balance_accounts_id_payment_instruments(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedPaymentInstrumentsResponse:
        """Returns a paginated list of the payment instruments associated with a balance account.

        To fetch multiple pages, use the query parameters.For example, to limit the page to 3 payment instruments which
        are in active status and to skip the first 6, use
        ``/balanceAccounts/{id}/paymentInstruments?limit=3&offset=6&status=active``.

        Args:
            id: The unique identifier of the balance account.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            status: The status of the payment instruments that you want to get. By default, the response includes
                payment instruments with any status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_balance_accounts_id_payment_instruments(
                id, offset=offset, limit=limit, status=status, request_options=request_options
            )
        ).unwrap()

    async def get_balance_accounts_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRulesResponse:
        """Returns a list of transaction rules associated with a balance account.

        Args:
            id: The unique identifier of the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_balance_accounts_id_transaction_rules(id, request_options=request_options)
        ).unwrap()

    async def patch_balance_accounts_id(
        self,
        id: str,
        *,
        body: BalanceAccountUpdateRequest | BalanceAccountUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceAccount:
        """Updates a balance account.

        Args:
            id: The unique identifier of the balance account.
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
            await self._with_raw_response.patch_balance_accounts_id(id, body=body, request_options=request_options)
        ).unwrap()

    async def post_balance_accounts(
        self,
        *,
        body: BalanceAccountInfo | BalanceAccountInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceAccount:
        """Creates a balance account that holds the funds of the associated account holder.

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
        return (
            await self._with_raw_response.post_balance_accounts(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncBalanceAccountsWithRawResponse:
        return self._with_raw_response


class BalanceAccountsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_balance_accounts_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BalanceAccount, GetBalanceAccountsIdErrorBody]:
        """Returns a balance account and its balances for the default currency and other currencies with a non-zero
        balance.

        Args:
            id: The unique identifier of the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BalanceAccount],
            error_mapper=get_balance_accounts_id_error_mapper,
            request_options=request_options,
        )

    def get_balance_accounts_id_payment_instruments(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedPaymentInstrumentsResponse, GetBalanceAccountsIdPaymentInstrumentsErrorBody]:
        """Returns a paginated list of the payment instruments associated with a balance account.

        To fetch multiple pages, use the query parameters.For example, to limit the page to 3 payment instruments which
        are in active status and to skip the first 6, use
        ``/balanceAccounts/{id}/paymentInstruments?limit=3&offset=6&status=active``.

        Args:
            id: The unique identifier of the balance account.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            status: The status of the payment instruments that you want to get. By default, the response includes
                payment instruments with any status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{id}/paymentInstruments"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
                param[str | None]("status", status),
            ],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaginatedPaymentInstrumentsResponse],
            error_mapper=get_balance_accounts_id_payment_instruments_error_mapper,
            request_options=request_options,
        )

    def get_balance_accounts_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRulesResponse, GetBalanceAccountsIdTransactionRulesErrorBody]:
        """Returns a list of transaction rules associated with a balance account.

        Args:
            id: The unique identifier of the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{id}/transactionRules"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionRulesResponse],
            error_mapper=get_balance_accounts_id_transaction_rules_error_mapper,
            request_options=request_options,
        )

    def patch_balance_accounts_id(
        self,
        id: str,
        *,
        body: BalanceAccountUpdateRequest | BalanceAccountUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceAccount, PatchBalanceAccountsIdErrorBody]:
        """Updates a balance account.

        Args:
            id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/balanceAccounts/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceAccountUpdateRequest | BalanceAccountUpdateRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BalanceAccount],
            error_mapper=patch_balance_accounts_id_error_mapper,
            request_options=request_options,
        )

    def post_balance_accounts(
        self,
        *,
        body: BalanceAccountInfo | BalanceAccountInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceAccount, PostBalanceAccountsErrorBody]:
        """Creates a balance account that holds the funds of the associated account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balanceAccounts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceAccountInfo | BalanceAccountInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BalanceAccount],
            error_mapper=post_balance_accounts_error_mapper,
            request_options=request_options,
        )


class AsyncBalanceAccountsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_balance_accounts_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BalanceAccount, GetBalanceAccountsIdErrorBody]:
        """Returns a balance account and its balances for the default currency and other currencies with a non-zero
        balance.

        Args:
            id: The unique identifier of the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BalanceAccount],
            error_mapper=get_balance_accounts_id_error_mapper,
            request_options=request_options,
        )

    async def get_balance_accounts_id_payment_instruments(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        status: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedPaymentInstrumentsResponse, GetBalanceAccountsIdPaymentInstrumentsErrorBody]:
        """Returns a paginated list of the payment instruments associated with a balance account.

        To fetch multiple pages, use the query parameters.For example, to limit the page to 3 payment instruments which
        are in active status and to skip the first 6, use
        ``/balanceAccounts/{id}/paymentInstruments?limit=3&offset=6&status=active``.

        Args:
            id: The unique identifier of the balance account.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            status: The status of the payment instruments that you want to get. By default, the response includes
                payment instruments with any status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{id}/paymentInstruments"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
                param[str | None]("status", status),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaginatedPaymentInstrumentsResponse],
            error_mapper=get_balance_accounts_id_payment_instruments_error_mapper,
            request_options=request_options,
        )

    async def get_balance_accounts_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRulesResponse, GetBalanceAccountsIdTransactionRulesErrorBody]:
        """Returns a list of transaction rules associated with a balance account.

        Args:
            id: The unique identifier of the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{id}/transactionRules"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionRulesResponse],
            error_mapper=get_balance_accounts_id_transaction_rules_error_mapper,
            request_options=request_options,
        )

    async def patch_balance_accounts_id(
        self,
        id: str,
        *,
        body: BalanceAccountUpdateRequest | BalanceAccountUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceAccount, PatchBalanceAccountsIdErrorBody]:
        """Updates a balance account.

        Args:
            id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/balanceAccounts/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceAccountUpdateRequest | BalanceAccountUpdateRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BalanceAccount],
            error_mapper=patch_balance_accounts_id_error_mapper,
            request_options=request_options,
        )

    async def post_balance_accounts(
        self,
        *,
        body: BalanceAccountInfo | BalanceAccountInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceAccount, PostBalanceAccountsErrorBody]:
        """Creates a balance account that holds the funds of the associated account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balanceAccounts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceAccountInfo | BalanceAccountInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BalanceAccount],
            error_mapper=post_balance_accounts_error_mapper,
            request_options=request_options,
        )
