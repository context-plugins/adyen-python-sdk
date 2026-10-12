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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.get_grants_error import GetGrantsErrorBody, get_grants_error_mapper
from ..errors.get_grants_id_error import GetGrantsIdErrorBody, get_grants_id_error_mapper
from ..errors.post_grants_error import PostGrantsErrorBody, post_grants_error_mapper
from ..models.capital_grant import CapitalGrant
from ..models.capital_grant_info import CapitalGrantInfo, CapitalGrantInfoDict
from ..models.capital_grants import CapitalGrants
from ..server.server import Server


class Capital:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CapitalWithRawResponse(client, server, auth)

    def get_grants(
        self, *, counterparty_account_holder_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CapitalGrants:
        """Returns a list of grants with status and outstanding balances.

        Args:
            counterparty_account_holder_id: The counterparty account holder id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.get_grants(
                counterparty_account_holder_id=counterparty_account_holder_id, request_options=request_options
            ),
        )

    def get_grants_id(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> CapitalGrant:
        """Returns the details of a capital account specified in the path.

        Args:
            id_: The unique identifier of the grant.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return unwrap(self._with_raw_response.get_grants_id(id_, request_options=request_options))

    def post_grants(
        self,
        *,
        idempotency_key: str | None = None,
        body: CapitalGrantInfo | CapitalGrantInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CapitalGrant:
        """Requests the payout of the selected grant offer.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_grants(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> CapitalWithRawResponse:
        return self._with_raw_response


class AsyncCapital:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCapitalWithRawResponse(client, server, auth)

    async def get_grants(
        self, *, counterparty_account_holder_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CapitalGrants:
        """Returns a list of grants with status and outstanding balances.

        Args:
            counterparty_account_holder_id: The counterparty account holder id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_grants(
                counterparty_account_holder_id=counterparty_account_holder_id, request_options=request_options
            ),
        )

    async def get_grants_id(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> CapitalGrant:
        """Returns the details of a capital account specified in the path.

        Args:
            id_: The unique identifier of the grant.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return unwrap(await self._with_raw_response.get_grants_id(id_, request_options=request_options))

    async def post_grants(
        self,
        *,
        idempotency_key: str | None = None,
        body: CapitalGrantInfo | CapitalGrantInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CapitalGrant:
        """Requests the payout of the selected grant offer.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the payment was not
                found Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_grants(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncCapitalWithRawResponse:
        return self._with_raw_response


class CapitalWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_grants(
        self, *, counterparty_account_holder_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CapitalGrants, GetGrantsErrorBody]:
        """Returns a list of grants with status and outstanding balances.

        Args:
            counterparty_account_holder_id: The counterparty account holder id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/grants"),
            query_params=[param[str | None]("counterpartyAccountHolderId", counterparty_account_holder_id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CapitalGrants],
            error_mapper=get_grants_error_mapper,
            request_options=request_options,
        )

    def get_grants_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CapitalGrant, GetGrantsIdErrorBody]:
        """Returns the details of a capital account specified in the path.

        Args:
            id_: The unique identifier of the grant.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/grants/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CapitalGrant],
            error_mapper=get_grants_id_error_mapper,
            request_options=request_options,
        )

    def post_grants(
        self,
        *,
        idempotency_key: str | None = None,
        body: CapitalGrantInfo | CapitalGrantInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CapitalGrant, PostGrantsErrorBody]:
        """Requests the payout of the selected grant offer.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/grants"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CapitalGrantInfo | CapitalGrantInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CapitalGrant],
            error_mapper=post_grants_error_mapper,
            request_options=request_options,
        )


class AsyncCapitalWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_grants(
        self, *, counterparty_account_holder_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CapitalGrants, GetGrantsErrorBody]:
        """Returns a list of grants with status and outstanding balances.

        Args:
            counterparty_account_holder_id: The counterparty account holder id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/grants"),
            query_params=[param[str | None]("counterpartyAccountHolderId", counterparty_account_holder_id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CapitalGrants],
            error_mapper=get_grants_error_mapper,
            request_options=request_options,
        )

    async def get_grants_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CapitalGrant, GetGrantsIdErrorBody]:
        """Returns the details of a capital account specified in the path.

        Args:
            id_: The unique identifier of the grant.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/grants/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CapitalGrant],
            error_mapper=get_grants_id_error_mapper,
            request_options=request_options,
        )

    async def post_grants(
        self,
        *,
        idempotency_key: str | None = None,
        body: CapitalGrantInfo | CapitalGrantInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CapitalGrant, PostGrantsErrorBody]:
        """Requests the payout of the selected grant offer.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/grants"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CapitalGrantInfo | CapitalGrantInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CapitalGrant],
            error_mapper=post_grants_error_mapper,
            request_options=request_options,
        )
