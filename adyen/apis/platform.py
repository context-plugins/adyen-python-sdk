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
from ..errors.get_balance_platforms_id_account_holders_error import (
    GetBalancePlatformsIdAccountHoldersErrorBody,
    get_balance_platforms_id_account_holders_error_mapper,
)
from ..errors.get_balance_platforms_id_error import (
    GetBalancePlatformsIdErrorBody,
    get_balance_platforms_id_error_mapper,
)
from ..errors.get_balance_platforms_id_transaction_rules_error import (
    GetBalancePlatformsIdTransactionRulesErrorBody,
    get_balance_platforms_id_transaction_rules_error_mapper,
)
from ..models.balance_platform import BalancePlatform
from ..models.paginated_account_holders_response import PaginatedAccountHoldersResponse
from ..models.transaction_rules_response import TransactionRulesResponse
from ..server.server import Server


class Platform:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PlatformWithRawResponse(client, server, auth)

    def get_balance_platforms_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BalancePlatform:
        """Returns a balance platform.

        Args:
            id: The unique identifier of the balance platform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_balance_platforms_id(id, request_options=request_options).unwrap()

    def get_balance_platforms_id_account_holders(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedAccountHoldersResponse:
        """Returns a paginated list of all the account holders that belong to the balance platform. To fetch multiple
        pages, use the query parameters.

        For example, to limit the page to 5 account holders and to skip the first 20, use
        ``/balancePlatforms/{id}/accountHolders?limit=5&offset=20``.

        Args:
            id: The unique identifier of the balance platform.
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
        return self._with_raw_response.get_balance_platforms_id_account_holders(
            id, offset=offset, limit=limit, request_options=request_options
        ).unwrap()

    def get_balance_platforms_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRulesResponse:
        """Returns a list of transaction rules associated with a balance platform.

        Args:
            id: The unique identifier of the balance platform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_balance_platforms_id_transaction_rules(
            id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PlatformWithRawResponse:
        return self._with_raw_response


class AsyncPlatform:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPlatformWithRawResponse(client, server, auth)

    async def get_balance_platforms_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BalancePlatform:
        """Returns a balance platform.

        Args:
            id: The unique identifier of the balance platform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (await self._with_raw_response.get_balance_platforms_id(id, request_options=request_options)).unwrap()

    async def get_balance_platforms_id_account_holders(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedAccountHoldersResponse:
        """Returns a paginated list of all the account holders that belong to the balance platform. To fetch multiple
        pages, use the query parameters.

        For example, to limit the page to 5 account holders and to skip the first 20, use
        ``/balancePlatforms/{id}/accountHolders?limit=5&offset=20``.

        Args:
            id: The unique identifier of the balance platform.
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
            await self._with_raw_response.get_balance_platforms_id_account_holders(
                id, offset=offset, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def get_balance_platforms_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRulesResponse:
        """Returns a list of transaction rules associated with a balance platform.

        Args:
            id: The unique identifier of the balance platform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_balance_platforms_id_transaction_rules(
                id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPlatformWithRawResponse:
        return self._with_raw_response


class PlatformWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_balance_platforms_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BalancePlatform, GetBalancePlatformsIdErrorBody]:
        """Returns a balance platform.

        Args:
            id: The unique identifier of the balance platform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BalancePlatform],
            error_mapper=get_balance_platforms_id_error_mapper,
            request_options=request_options,
        )

    def get_balance_platforms_id_account_holders(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedAccountHoldersResponse, GetBalancePlatformsIdAccountHoldersErrorBody]:
        """Returns a paginated list of all the account holders that belong to the balance platform. To fetch multiple
        pages, use the query parameters.

        For example, to limit the page to 5 account holders and to skip the first 20, use
        ``/balancePlatforms/{id}/accountHolders?limit=5&offset=20``.

        Args:
            id: The unique identifier of the balance platform.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{id}/accountHolders"),
            path_params=[param[str]("id", id)],
            query_params=[param[int | None]("offset", offset), param[int | None]("limit", limit)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaginatedAccountHoldersResponse],
            error_mapper=get_balance_platforms_id_account_holders_error_mapper,
            request_options=request_options,
        )

    def get_balance_platforms_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRulesResponse, GetBalancePlatformsIdTransactionRulesErrorBody]:
        """Returns a list of transaction rules associated with a balance platform.

        Args:
            id: The unique identifier of the balance platform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{id}/transactionRules"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionRulesResponse],
            error_mapper=get_balance_platforms_id_transaction_rules_error_mapper,
            request_options=request_options,
        )


class AsyncPlatformWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_balance_platforms_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BalancePlatform, GetBalancePlatformsIdErrorBody]:
        """Returns a balance platform.

        Args:
            id: The unique identifier of the balance platform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BalancePlatform],
            error_mapper=get_balance_platforms_id_error_mapper,
            request_options=request_options,
        )

    async def get_balance_platforms_id_account_holders(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedAccountHoldersResponse, GetBalancePlatformsIdAccountHoldersErrorBody]:
        """Returns a paginated list of all the account holders that belong to the balance platform. To fetch multiple
        pages, use the query parameters.

        For example, to limit the page to 5 account holders and to skip the first 20, use
        ``/balancePlatforms/{id}/accountHolders?limit=5&offset=20``.

        Args:
            id: The unique identifier of the balance platform.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{id}/accountHolders"),
            path_params=[param[str]("id", id)],
            query_params=[param[int | None]("offset", offset), param[int | None]("limit", limit)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaginatedAccountHoldersResponse],
            error_mapper=get_balance_platforms_id_account_holders_error_mapper,
            request_options=request_options,
        )

    async def get_balance_platforms_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRulesResponse, GetBalancePlatformsIdTransactionRulesErrorBody]:
        """Returns a list of transaction rules associated with a balance platform.

        Args:
            id: The unique identifier of the balance platform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{id}/transactionRules"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionRulesResponse],
            error_mapper=get_balance_platforms_id_transaction_rules_error_mapper,
            request_options=request_options,
        )
