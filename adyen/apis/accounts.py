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
from ..errors.post_close_account_error import PostCloseAccountErrorBody, post_close_account_error_mapper
from ..errors.post_create_account_error import PostCreateAccountErrorBody, post_create_account_error_mapper
from ..errors.post_update_account_error import PostUpdateAccountErrorBody, post_update_account_error_mapper
from ..models.close_account_request import CloseAccountRequest, CloseAccountRequestDict
from ..models.close_account_response import CloseAccountResponse
from ..models.create_account_request import CreateAccountRequest, CreateAccountRequestDict
from ..models.create_account_response import CreateAccountResponse
from ..models.update_account_request import UpdateAccountRequest, UpdateAccountRequestDict
from ..models.update_account_response import UpdateAccountResponse
from ..server.server import Server


class Accounts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountsWithRawResponse(client, server, auth)

    def post_close_account(
        self,
        *,
        body: CloseAccountRequest | CloseAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CloseAccountResponse:
        """Closes an account. If an account is closed, you cannot process transactions, pay out its funds, or reopen it.
        If payments are made to a closed account, the payments are sent to your liable account.

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
        return self._with_raw_response.post_close_account(body=body, request_options=request_options).unwrap()

    def post_create_account(
        self,
        *,
        body: CreateAccountRequest | CreateAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateAccountResponse:
        """Creates an account under an account holder. An account holder can have `multiple accounts
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#create-additional-accounts>`__.

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
        return self._with_raw_response.post_create_account(body=body, request_options=request_options).unwrap()

    def post_update_account(
        self,
        *,
        body: UpdateAccountRequest | UpdateAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateAccountResponse:
        """Updates the description or payout schedule of an account.

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
        return self._with_raw_response.post_update_account(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AccountsWithRawResponse:
        return self._with_raw_response


class AsyncAccounts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountsWithRawResponse(client, server, auth)

    async def post_close_account(
        self,
        *,
        body: CloseAccountRequest | CloseAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CloseAccountResponse:
        """Closes an account. If an account is closed, you cannot process transactions, pay out its funds, or reopen it.
        If payments are made to a closed account, the payments are sent to your liable account.

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
        return (await self._with_raw_response.post_close_account(body=body, request_options=request_options)).unwrap()

    async def post_create_account(
        self,
        *,
        body: CreateAccountRequest | CreateAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateAccountResponse:
        """Creates an account under an account holder. An account holder can have `multiple accounts
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#create-additional-accounts>`__.

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
        return (await self._with_raw_response.post_create_account(body=body, request_options=request_options)).unwrap()

    async def post_update_account(
        self,
        *,
        body: UpdateAccountRequest | UpdateAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateAccountResponse:
        """Updates the description or payout schedule of an account.

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
        return (await self._with_raw_response.post_update_account(body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountsWithRawResponse:
        return self._with_raw_response


class AccountsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_close_account(
        self,
        *,
        body: CloseAccountRequest | CloseAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CloseAccountResponse, PostCloseAccountErrorBody]:
        """Closes an account. If an account is closed, you cannot process transactions, pay out its funds, or reopen it.
        If payments are made to a closed account, the payments are sent to your liable account.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/closeAccount"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CloseAccountRequest | CloseAccountRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CloseAccountResponse],
            error_mapper=post_close_account_error_mapper,
            request_options=request_options,
        )

    def post_create_account(
        self,
        *,
        body: CreateAccountRequest | CreateAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateAccountResponse, PostCreateAccountErrorBody]:
        """Creates an account under an account holder. An account holder can have `multiple accounts
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#create-additional-accounts>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/createAccount"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAccountRequest | CreateAccountRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateAccountResponse],
            error_mapper=post_create_account_error_mapper,
            request_options=request_options,
        )

    def post_update_account(
        self,
        *,
        body: UpdateAccountRequest | UpdateAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateAccountResponse, PostUpdateAccountErrorBody]:
        """Updates the description or payout schedule of an account.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/updateAccount"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateAccountRequest | UpdateAccountRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UpdateAccountResponse],
            error_mapper=post_update_account_error_mapper,
            request_options=request_options,
        )


class AsyncAccountsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_close_account(
        self,
        *,
        body: CloseAccountRequest | CloseAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CloseAccountResponse, PostCloseAccountErrorBody]:
        """Closes an account. If an account is closed, you cannot process transactions, pay out its funds, or reopen it.
        If payments are made to a closed account, the payments are sent to your liable account.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/closeAccount"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CloseAccountRequest | CloseAccountRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CloseAccountResponse],
            error_mapper=post_close_account_error_mapper,
            request_options=request_options,
        )

    async def post_create_account(
        self,
        *,
        body: CreateAccountRequest | CreateAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateAccountResponse, PostCreateAccountErrorBody]:
        """Creates an account under an account holder. An account holder can have `multiple accounts
        <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#create-additional-accounts>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/createAccount"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAccountRequest | CreateAccountRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CreateAccountResponse],
            error_mapper=post_create_account_error_mapper,
            request_options=request_options,
        )

    async def post_update_account(
        self,
        *,
        body: UpdateAccountRequest | UpdateAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateAccountResponse, PostUpdateAccountErrorBody]:
        """Updates the description or payout schedule of an account.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/updateAccount"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateAccountRequest | UpdateAccountRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UpdateAccountResponse],
            error_mapper=post_update_account_error_mapper,
            request_options=request_options,
        )
