from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
)
from ..errors.get_grant_accounts_id1_error import GetGrantAccountsId1ErrorBody, get_grant_accounts_id1_error_mapper
from ..errors.get_grant_accounts_id_error import GetGrantAccountsIdErrorBody, get_grant_accounts_id_error_mapper
from ..models.capital_grant_account import CapitalGrantAccount
from ..models.grant_account import GrantAccount
from ..server.server import Server


class GrantAccounts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GrantAccountsWithRawResponse(client, server, auth)

    def get_grant_accounts_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CapitalGrantAccount:
        """Returns the details of the `grant account <https://docs.adyen.com/platforms/capital#grant-account>`__.

        Args:
            id: The unique identifier of the grant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_grant_accounts_id(id, request_options=request_options).unwrap()

    def get_grant_accounts_id1(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> GrantAccount:
        """Returns the details of the specified grant account. This account tracks existing grants in your marketplace
        or platform.

        Args:
            id: The unique identifier of the grant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_grant_accounts_id1(id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> GrantAccountsWithRawResponse:
        return self._with_raw_response


class AsyncGrantAccounts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGrantAccountsWithRawResponse(client, server, auth)

    async def get_grant_accounts_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CapitalGrantAccount:
        """Returns the details of the `grant account <https://docs.adyen.com/platforms/capital#grant-account>`__.

        Args:
            id: The unique identifier of the grant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (await self._with_raw_response.get_grant_accounts_id(id, request_options=request_options)).unwrap()

    async def get_grant_accounts_id1(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GrantAccount:
        """Returns the details of the specified grant account. This account tracks existing grants in your marketplace
        or platform.

        Args:
            id: The unique identifier of the grant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return (await self._with_raw_response.get_grant_accounts_id1(id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncGrantAccountsWithRawResponse:
        return self._with_raw_response


class GrantAccountsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_grant_accounts_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CapitalGrantAccount, GetGrantAccountsIdErrorBody]:
        """Returns the details of the `grant account <https://docs.adyen.com/platforms/capital#grant-account>`__.

        Args:
            id: The unique identifier of the grant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/grantAccounts/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CapitalGrantAccount],
            error_mapper=get_grant_accounts_id_error_mapper,
            request_options=request_options,
        )

    def get_grant_accounts_id1(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GrantAccount, GetGrantAccountsId1ErrorBody]:
        """Returns the details of the specified grant account. This account tracks existing grants in your marketplace
        or platform.

        Args:
            id: The unique identifier of the grant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grantAccounts/{id}"),
            path_params=[param[str]("id", id)],
            decoder=json_decoder[GrantAccount],
            error_mapper=get_grant_accounts_id1_error_mapper,
            request_options=request_options,
        )


class AsyncGrantAccountsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_grant_accounts_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CapitalGrantAccount, GetGrantAccountsIdErrorBody]:
        """Returns the details of the `grant account <https://docs.adyen.com/platforms/capital#grant-account>`__.

        Args:
            id: The unique identifier of the grant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/grantAccounts/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CapitalGrantAccount],
            error_mapper=get_grant_accounts_id_error_mapper,
            request_options=request_options,
        )

    async def get_grant_accounts_id1(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GrantAccount, GetGrantAccountsId1ErrorBody]:
        """Returns the details of the specified grant account. This account tracks existing grants in your marketplace
        or platform.

        Args:
            id: The unique identifier of the grant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grantAccounts/{id}"),
            path_params=[param[str]("id", id)],
            decoder=json_decoder[GrantAccount],
            error_mapper=get_grant_accounts_id1_error_mapper,
            request_options=request_options,
        )
