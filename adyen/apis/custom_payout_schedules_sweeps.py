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
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.delete_balance_accounts_balance_account_id_sweeps_sweep_id_error import (
    DeleteBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody,
    delete_balance_accounts_balance_account_id_sweeps_sweep_id_error_mapper,
)
from ..errors.get_balance_accounts_balance_account_id_sweeps_error import (
    GetBalanceAccountsBalanceAccountIdSweepsErrorBody,
    get_balance_accounts_balance_account_id_sweeps_error_mapper,
)
from ..errors.get_balance_accounts_balance_account_id_sweeps_sweep_id_error import (
    GetBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody,
    get_balance_accounts_balance_account_id_sweeps_sweep_id_error_mapper,
)
from ..errors.patch_balance_accounts_balance_account_id_sweeps_sweep_id_error import (
    PatchBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody,
    patch_balance_accounts_balance_account_id_sweeps_sweep_id_error_mapper,
)
from ..errors.post_balance_accounts_balance_account_id_sweeps_error import (
    PostBalanceAccountsBalanceAccountIdSweepsErrorBody,
    post_balance_accounts_balance_account_id_sweeps_error_mapper,
)
from ..models.balance_sweep_configurations_response import BalanceSweepConfigurationsResponse
from ..models.create_sweep_configuration_v2 import CreateSweepConfigurationV2, CreateSweepConfigurationV2Dict
from ..models.sweep_configuration_v2 import SweepConfigurationV2
from ..models.update_sweep_configuration_v2 import UpdateSweepConfigurationV2, UpdateSweepConfigurationV2Dict
from ..server.server import Server


class CustomPayoutSchedulesSweeps:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CustomPayoutSchedulesSweepsWithRawResponse(client, server, auth)

    def delete_balance_accounts_balance_account_id_sweeps_sweep_id(
        self, balance_account_id: str, sweep_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a sweep for a balance account.

        Args:
            balance_account_id: The unique identifier of the balance account.
            sweep_id: The unique identifier of the sweep.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.delete_balance_accounts_balance_account_id_sweeps_sweep_id(
                balance_account_id, sweep_id, request_options=request_options
            ),
        )

    def get_balance_accounts_balance_account_id_sweeps(
        self,
        balance_account_id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceSweepConfigurationsResponse:
        """Returns a list of the sweeps configured for a balance account.

        To fetch multiple pages, use the query parameters. For example, to limit the page to 5 sweeps and to skip the
        first 10, use ``/balanceAccounts/{balanceAccountId}/sweeps?limit=5&offset=10``.

        Args:
            balance_account_id: The unique identifier of the balance account.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.get_balance_accounts_balance_account_id_sweeps(
                balance_account_id, offset=offset, limit=limit, request_options=request_options
            ),
        )

    def get_balance_accounts_balance_account_id_sweeps_sweep_id(
        self, balance_account_id: str, sweep_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SweepConfigurationV2:
        """Returns a sweep.

        Args:
            balance_account_id: The unique identifier of the balance account.
            sweep_id: The unique identifier of the sweep.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.get_balance_accounts_balance_account_id_sweeps_sweep_id(
                balance_account_id, sweep_id, request_options=request_options
            ),
        )

    def patch_balance_accounts_balance_account_id_sweeps_sweep_id(
        self,
        balance_account_id: str,
        sweep_id: str,
        *,
        body: UpdateSweepConfigurationV2 | UpdateSweepConfigurationV2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SweepConfigurationV2:
        """Updates a sweep. When updating a sweep resource, note that if a request parameter is not provided, the
        parameter is left unchanged.

        Args:
            balance_account_id: The unique identifier of the balance account.
            sweep_id: The unique identifier of the sweep.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.patch_balance_accounts_balance_account_id_sweeps_sweep_id(
                balance_account_id, sweep_id, body=body, request_options=request_options
            ),
        )

    def post_balance_accounts_balance_account_id_sweeps(
        self,
        balance_account_id: str,
        *,
        body: CreateSweepConfigurationV2 | CreateSweepConfigurationV2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SweepConfigurationV2:
        """Creates a sweep that results in moving funds from or to a balance account.

        A sweep pulls in or pushes out funds based on a defined schedule, amount, currency, and a source or a
        destination.

        Args:
            balance_account_id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_balance_accounts_balance_account_id_sweeps(
                balance_account_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> CustomPayoutSchedulesSweepsWithRawResponse:
        return self._with_raw_response


class AsyncCustomPayoutSchedulesSweeps:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCustomPayoutSchedulesSweepsWithRawResponse(client, server, auth)

    async def delete_balance_accounts_balance_account_id_sweeps_sweep_id(
        self, balance_account_id: str, sweep_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a sweep for a balance account.

        Args:
            balance_account_id: The unique identifier of the balance account.
            sweep_id: The unique identifier of the sweep.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_balance_accounts_balance_account_id_sweeps_sweep_id(
                balance_account_id, sweep_id, request_options=request_options
            ),
        )

    async def get_balance_accounts_balance_account_id_sweeps(
        self,
        balance_account_id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceSweepConfigurationsResponse:
        """Returns a list of the sweeps configured for a balance account.

        To fetch multiple pages, use the query parameters. For example, to limit the page to 5 sweeps and to skip the
        first 10, use ``/balanceAccounts/{balanceAccountId}/sweeps?limit=5&offset=10``.

        Args:
            balance_account_id: The unique identifier of the balance account.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_balance_accounts_balance_account_id_sweeps(
                balance_account_id, offset=offset, limit=limit, request_options=request_options
            ),
        )

    async def get_balance_accounts_balance_account_id_sweeps_sweep_id(
        self, balance_account_id: str, sweep_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SweepConfigurationV2:
        """Returns a sweep.

        Args:
            balance_account_id: The unique identifier of the balance account.
            sweep_id: The unique identifier of the sweep.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_balance_accounts_balance_account_id_sweeps_sweep_id(
                balance_account_id, sweep_id, request_options=request_options
            ),
        )

    async def patch_balance_accounts_balance_account_id_sweeps_sweep_id(
        self,
        balance_account_id: str,
        sweep_id: str,
        *,
        body: UpdateSweepConfigurationV2 | UpdateSweepConfigurationV2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SweepConfigurationV2:
        """Updates a sweep. When updating a sweep resource, note that if a request parameter is not provided, the
        parameter is left unchanged.

        Args:
            balance_account_id: The unique identifier of the balance account.
            sweep_id: The unique identifier of the sweep.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.patch_balance_accounts_balance_account_id_sweeps_sweep_id(
                balance_account_id, sweep_id, body=body, request_options=request_options
            ),
        )

    async def post_balance_accounts_balance_account_id_sweeps(
        self,
        balance_account_id: str,
        *,
        body: CreateSweepConfigurationV2 | CreateSweepConfigurationV2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SweepConfigurationV2:
        """Creates a sweep that results in moving funds from or to a balance account.

        A sweep pulls in or pushes out funds based on a defined schedule, amount, currency, and a source or a
        destination.

        Args:
            balance_account_id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_balance_accounts_balance_account_id_sweeps(
                balance_account_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncCustomPayoutSchedulesSweepsWithRawResponse:
        return self._with_raw_response


class CustomPayoutSchedulesSweepsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_balance_accounts_balance_account_id_sweeps_sweep_id(
        self, balance_account_id: str, sweep_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody]:
        """Deletes a sweep for a balance account.

        Args:
            balance_account_id: The unique identifier of the balance account.
            sweep_id: The unique identifier of the sweep.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/sweeps/{sweepId}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("sweepId", sweep_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_balance_accounts_balance_account_id_sweeps_sweep_id_error_mapper,
            request_options=request_options,
        )

    def get_balance_accounts_balance_account_id_sweeps(
        self,
        balance_account_id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceSweepConfigurationsResponse, GetBalanceAccountsBalanceAccountIdSweepsErrorBody]:
        """Returns a list of the sweeps configured for a balance account.

        To fetch multiple pages, use the query parameters. For example, to limit the page to 5 sweeps and to skip the
        first 10, use ``/balanceAccounts/{balanceAccountId}/sweeps?limit=5&offset=10``.

        Args:
            balance_account_id: The unique identifier of the balance account.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/sweeps"),
            path_params=[param[str]("balanceAccountId", balance_account_id)],
            query_params=[param[int | None]("offset", offset), param[int | None]("limit", limit)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BalanceSweepConfigurationsResponse],
            error_mapper=get_balance_accounts_balance_account_id_sweeps_error_mapper,
            request_options=request_options,
        )

    def get_balance_accounts_balance_account_id_sweeps_sweep_id(
        self, balance_account_id: str, sweep_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SweepConfigurationV2, GetBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody]:
        """Returns a sweep.

        Args:
            balance_account_id: The unique identifier of the balance account.
            sweep_id: The unique identifier of the sweep.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/sweeps/{sweepId}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("sweepId", sweep_id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SweepConfigurationV2],
            error_mapper=get_balance_accounts_balance_account_id_sweeps_sweep_id_error_mapper,
            request_options=request_options,
        )

    def patch_balance_accounts_balance_account_id_sweeps_sweep_id(
        self,
        balance_account_id: str,
        sweep_id: str,
        *,
        body: UpdateSweepConfigurationV2 | UpdateSweepConfigurationV2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SweepConfigurationV2, PatchBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody]:
        """Updates a sweep. When updating a sweep resource, note that if a request parameter is not provided, the
        parameter is left unchanged.

        Args:
            balance_account_id: The unique identifier of the balance account.
            sweep_id: The unique identifier of the sweep.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/sweeps/{sweepId}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("sweepId", sweep_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSweepConfigurationV2 | UpdateSweepConfigurationV2Dict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SweepConfigurationV2],
            error_mapper=patch_balance_accounts_balance_account_id_sweeps_sweep_id_error_mapper,
            request_options=request_options,
        )

    def post_balance_accounts_balance_account_id_sweeps(
        self,
        balance_account_id: str,
        *,
        body: CreateSweepConfigurationV2 | CreateSweepConfigurationV2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SweepConfigurationV2, PostBalanceAccountsBalanceAccountIdSweepsErrorBody]:
        """Creates a sweep that results in moving funds from or to a balance account.

        A sweep pulls in or pushes out funds based on a defined schedule, amount, currency, and a source or a
        destination.

        Args:
            balance_account_id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/sweeps"),
            path_params=[param[str]("balanceAccountId", balance_account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSweepConfigurationV2 | CreateSweepConfigurationV2Dict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SweepConfigurationV2],
            error_mapper=post_balance_accounts_balance_account_id_sweeps_error_mapper,
            request_options=request_options,
        )


class AsyncCustomPayoutSchedulesSweepsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_balance_accounts_balance_account_id_sweeps_sweep_id(
        self, balance_account_id: str, sweep_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody]:
        """Deletes a sweep for a balance account.

        Args:
            balance_account_id: The unique identifier of the balance account.
            sweep_id: The unique identifier of the sweep.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/sweeps/{sweepId}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("sweepId", sweep_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_empty_response,
            error_mapper=delete_balance_accounts_balance_account_id_sweeps_sweep_id_error_mapper,
            request_options=request_options,
        )

    async def get_balance_accounts_balance_account_id_sweeps(
        self,
        balance_account_id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceSweepConfigurationsResponse, GetBalanceAccountsBalanceAccountIdSweepsErrorBody]:
        """Returns a list of the sweeps configured for a balance account.

        To fetch multiple pages, use the query parameters. For example, to limit the page to 5 sweeps and to skip the
        first 10, use ``/balanceAccounts/{balanceAccountId}/sweeps?limit=5&offset=10``.

        Args:
            balance_account_id: The unique identifier of the balance account.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items
                per page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/sweeps"),
            path_params=[param[str]("balanceAccountId", balance_account_id)],
            query_params=[param[int | None]("offset", offset), param[int | None]("limit", limit)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[BalanceSweepConfigurationsResponse],
            error_mapper=get_balance_accounts_balance_account_id_sweeps_error_mapper,
            request_options=request_options,
        )

    async def get_balance_accounts_balance_account_id_sweeps_sweep_id(
        self, balance_account_id: str, sweep_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SweepConfigurationV2, GetBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody]:
        """Returns a sweep.

        Args:
            balance_account_id: The unique identifier of the balance account.
            sweep_id: The unique identifier of the sweep.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/sweeps/{sweepId}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("sweepId", sweep_id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[SweepConfigurationV2],
            error_mapper=get_balance_accounts_balance_account_id_sweeps_sweep_id_error_mapper,
            request_options=request_options,
        )

    async def patch_balance_accounts_balance_account_id_sweeps_sweep_id(
        self,
        balance_account_id: str,
        sweep_id: str,
        *,
        body: UpdateSweepConfigurationV2 | UpdateSweepConfigurationV2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SweepConfigurationV2, PatchBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody]:
        """Updates a sweep. When updating a sweep resource, note that if a request parameter is not provided, the
        parameter is left unchanged.

        Args:
            balance_account_id: The unique identifier of the balance account.
            sweep_id: The unique identifier of the sweep.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/sweeps/{sweepId}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("sweepId", sweep_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSweepConfigurationV2 | UpdateSweepConfigurationV2Dict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[SweepConfigurationV2],
            error_mapper=patch_balance_accounts_balance_account_id_sweeps_sweep_id_error_mapper,
            request_options=request_options,
        )

    async def post_balance_accounts_balance_account_id_sweeps(
        self,
        balance_account_id: str,
        *,
        body: CreateSweepConfigurationV2 | CreateSweepConfigurationV2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SweepConfigurationV2, PostBalanceAccountsBalanceAccountIdSweepsErrorBody]:
        """Creates a sweep that results in moving funds from or to a balance account.

        A sweep pulls in or pushes out funds based on a defined schedule, amount, currency, and a source or a
        destination.

        Args:
            balance_account_id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/sweeps"),
            path_params=[param[str]("balanceAccountId", balance_account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSweepConfigurationV2 | CreateSweepConfigurationV2Dict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[SweepConfigurationV2],
            error_mapper=post_balance_accounts_balance_account_id_sweeps_error_mapper,
            request_options=request_options,
        )
