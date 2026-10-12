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
from ..errors.delete_transfer_instruments_id_error import (
    DeleteTransferInstrumentsIdErrorBody,
    delete_transfer_instruments_id_error_mapper,
)
from ..errors.get_transfer_instruments_id_error import (
    GetTransferInstrumentsIdErrorBody,
    get_transfer_instruments_id_error_mapper,
)
from ..errors.patch_transfer_instruments_id_error import (
    PatchTransferInstrumentsIdErrorBody,
    patch_transfer_instruments_id_error_mapper,
)
from ..errors.post_transfer_instruments_error import (
    PostTransferInstrumentsErrorBody,
    post_transfer_instruments_error_mapper,
)
from ..models.transfer_instrument import TransferInstrument
from ..models.transfer_instrument_info import TransferInstrumentInfo, TransferInstrumentInfoDict
from ..server.server import Server


class TransferInstruments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TransferInstrumentsWithRawResponse(client, server, auth)

    def delete_transfer_instruments_id(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes a transfer instrument.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the transfer instrument to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.delete_transfer_instruments_id(id_, request_options=request_options))

    def get_transfer_instruments_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransferInstrument:
        """Returns the details of a transfer instrument.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the transfer instrument.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.get_transfer_instruments_id(id_, request_options=request_options))

    def patch_transfer_instruments_id(
        self,
        id_: str,
        *,
        x_requested_verification_code: str | None = None,
        body: TransferInstrumentInfo | TransferInstrumentInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferInstrument:
        """Updates a transfer instrument.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the transfer instrument.
            x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors
                associated with the transfer instrument. Requested verification codes can only be used in your test
                environment.
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
            self._with_raw_response.patch_transfer_instruments_id(
                id_,
                x_requested_verification_code=x_requested_verification_code,
                body=body,
                request_options=request_options,
            ),
        )

    def post_transfer_instruments(
        self,
        *,
        x_requested_verification_code: str | None = None,
        body: TransferInstrumentInfo | TransferInstrumentInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferInstrument:
        """Creates a transfer instrument.

        A transfer instrument is a bank account that a legal entity owns. Adyen performs verification checks on the
        transfer instrument as required by payment industry regulations. We inform you of the verification results
        through webhooks or API responses.

        When the transfer instrument passes the verification checks, you can start sending funds from the balance
        platform to the transfer instrument (such as payouts).

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            x_requested_verification_code: Use a suberror code as your requested verification code. You can include one
                code at a time in your request header. Requested verification codes can only be used in your test
                environment.
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
            self._with_raw_response.post_transfer_instruments(
                x_requested_verification_code=x_requested_verification_code, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> TransferInstrumentsWithRawResponse:
        return self._with_raw_response


class AsyncTransferInstruments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTransferInstrumentsWithRawResponse(client, server, auth)

    async def delete_transfer_instruments_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a transfer instrument.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the transfer instrument to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_transfer_instruments_id(id_, request_options=request_options)
        )

    async def get_transfer_instruments_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransferInstrument:
        """Returns the details of a transfer instrument.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the transfer instrument.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(await self._with_raw_response.get_transfer_instruments_id(id_, request_options=request_options))

    async def patch_transfer_instruments_id(
        self,
        id_: str,
        *,
        x_requested_verification_code: str | None = None,
        body: TransferInstrumentInfo | TransferInstrumentInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferInstrument:
        """Updates a transfer instrument.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the transfer instrument.
            x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors
                associated with the transfer instrument. Requested verification codes can only be used in your test
                environment.
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
            await self._with_raw_response.patch_transfer_instruments_id(
                id_,
                x_requested_verification_code=x_requested_verification_code,
                body=body,
                request_options=request_options,
            ),
        )

    async def post_transfer_instruments(
        self,
        *,
        x_requested_verification_code: str | None = None,
        body: TransferInstrumentInfo | TransferInstrumentInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferInstrument:
        """Creates a transfer instrument.

        A transfer instrument is a bank account that a legal entity owns. Adyen performs verification checks on the
        transfer instrument as required by payment industry regulations. We inform you of the verification results
        through webhooks or API responses.

        When the transfer instrument passes the verification checks, you can start sending funds from the balance
        platform to the transfer instrument (such as payouts).

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            x_requested_verification_code: Use a suberror code as your requested verification code. You can include one
                code at a time in your request header. Requested verification codes can only be used in your test
                environment.
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
            await self._with_raw_response.post_transfer_instruments(
                x_requested_verification_code=x_requested_verification_code, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncTransferInstrumentsWithRawResponse:
        return self._with_raw_response


class TransferInstrumentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_transfer_instruments_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteTransferInstrumentsIdErrorBody]:
        """Deletes a transfer instrument.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the transfer instrument to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default18("/transferInstruments/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_transfer_instruments_id_error_mapper,
            request_options=request_options,
        )

    def get_transfer_instruments_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransferInstrument, GetTransferInstrumentsIdErrorBody]:
        """Returns the details of a transfer instrument.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the transfer instrument.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/transferInstruments/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransferInstrument],
            error_mapper=get_transfer_instruments_id_error_mapper,
            request_options=request_options,
        )

    def patch_transfer_instruments_id(
        self,
        id_: str,
        *,
        x_requested_verification_code: str | None = None,
        body: TransferInstrumentInfo | TransferInstrumentInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferInstrument, PatchTransferInstrumentsIdErrorBody]:
        """Updates a transfer instrument.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the transfer instrument.
            x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors
                associated with the transfer instrument. Requested verification codes can only be used in your test
                environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default18("/transferInstruments/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[
                param[str | None]("x-requested-verification-code", x_requested_verification_code),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TransferInstrumentInfo | TransferInstrumentInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransferInstrument],
            error_mapper=patch_transfer_instruments_id_error_mapper,
            request_options=request_options,
        )

    def post_transfer_instruments(
        self,
        *,
        x_requested_verification_code: str | None = None,
        body: TransferInstrumentInfo | TransferInstrumentInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferInstrument, PostTransferInstrumentsErrorBody]:
        """Creates a transfer instrument.

        A transfer instrument is a bank account that a legal entity owns. Adyen performs verification checks on the
        transfer instrument as required by payment industry regulations. We inform you of the verification results
        through webhooks or API responses.

        When the transfer instrument passes the verification checks, you can start sending funds from the balance
        platform to the transfer instrument (such as payouts).

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            x_requested_verification_code: Use a suberror code as your requested verification code. You can include one
                code at a time in your request header. Requested verification codes can only be used in your test
                environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/transferInstruments"),
            headers=[
                param[str | None]("x-requested-verification-code", x_requested_verification_code),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TransferInstrumentInfo | TransferInstrumentInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransferInstrument],
            error_mapper=post_transfer_instruments_error_mapper,
            request_options=request_options,
        )


class AsyncTransferInstrumentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_transfer_instruments_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteTransferInstrumentsIdErrorBody]:
        """Deletes a transfer instrument.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the transfer instrument to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default18("/transferInstruments/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_empty_response,
            error_mapper=delete_transfer_instruments_id_error_mapper,
            request_options=request_options,
        )

    async def get_transfer_instruments_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransferInstrument, GetTransferInstrumentsIdErrorBody]:
        """Returns the details of a transfer instrument.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the transfer instrument.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/transferInstruments/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TransferInstrument],
            error_mapper=get_transfer_instruments_id_error_mapper,
            request_options=request_options,
        )

    async def patch_transfer_instruments_id(
        self,
        id_: str,
        *,
        x_requested_verification_code: str | None = None,
        body: TransferInstrumentInfo | TransferInstrumentInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferInstrument, PatchTransferInstrumentsIdErrorBody]:
        """Updates a transfer instrument.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the transfer instrument.
            x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors
                associated with the transfer instrument. Requested verification codes can only be used in your test
                environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default18("/transferInstruments/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[
                param[str | None]("x-requested-verification-code", x_requested_verification_code),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TransferInstrumentInfo | TransferInstrumentInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TransferInstrument],
            error_mapper=patch_transfer_instruments_id_error_mapper,
            request_options=request_options,
        )

    async def post_transfer_instruments(
        self,
        *,
        x_requested_verification_code: str | None = None,
        body: TransferInstrumentInfo | TransferInstrumentInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferInstrument, PostTransferInstrumentsErrorBody]:
        """Creates a transfer instrument.

        A transfer instrument is a bank account that a legal entity owns. Adyen performs verification checks on the
        transfer instrument as required by payment industry regulations. We inform you of the verification results
        through webhooks or API responses.

        When the transfer instrument passes the verification checks, you can start sending funds from the balance
        platform to the transfer instrument (such as payouts).

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            x_requested_verification_code: Use a suberror code as your requested verification code. You can include one
                code at a time in your request header. Requested verification codes can only be used in your test
                environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/transferInstruments"),
            headers=[
                param[str | None]("x-requested-verification-code", x_requested_verification_code),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TransferInstrumentInfo | TransferInstrumentInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TransferInstrument],
            error_mapper=post_transfer_instruments_error_mapper,
            request_options=request_options,
        )
