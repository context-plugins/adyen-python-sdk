from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.delete_payment_instruments_payment_instrument_id_authorised_card_users_error import (
    DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody,
    delete_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper,
)
from ..errors.get_payment_instruments_payment_instrument_id_authorised_card_users_error import (
    GetPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody,
    get_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper,
)
from ..errors.patch_payment_instruments_payment_instrument_id_authorised_card_users_error import (
    PatchPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody,
    patch_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper,
)
from ..errors.post_payment_instruments_payment_instrument_id_authorised_card_users_error import (
    PostPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody,
    post_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper,
)
from ..models.authorised_card_users import AuthorisedCardUsers, AuthorisedCardUsersDict
from ..server.server import Server


class AuthorizedCardUsers:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = AuthorizedCardUsersWithRawResponse(client, server)

    def delete_payment_instruments_payment_instrument_id_authorised_card_users(
        self, payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes the list of authorized users assigned to a card.

        Args:
            payment_instrument_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: Unauthorized Forbidden ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.delete_payment_instruments_payment_instrument_id_authorised_card_users(
                payment_instrument_id, request_options=request_options
            ),
        )

    def get_payment_instruments_payment_instrument_id_authorised_card_users(
        self, payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AuthorisedCardUsers:
        """Returns the authorized users for a card.

        Args:
            payment_instrument_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: Unauthorized Forbidden Not Found Unprocessable Entity - a request validation error. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.get_payment_instruments_payment_instrument_id_authorised_card_users(
                payment_instrument_id, request_options=request_options
            ),
        )

    def patch_payment_instruments_payment_instrument_id_authorised_card_users(
        self,
        payment_instrument_id: str,
        body: AuthorisedCardUsers | AuthorisedCardUsersDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates the list of authorized users for a card.

        >This request replaces all existing authorized users for the card.

        Args:
            payment_instrument_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: Bad request Unauthorized Forbidden Unprocessable Entity - a request validation error. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.patch_payment_instruments_payment_instrument_id_authorised_card_users(
                payment_instrument_id, body, request_options=request_options
            ),
        )

    def post_payment_instruments_payment_instrument_id_authorised_card_users(
        self,
        payment_instrument_id: str,
        body: AuthorisedCardUsers | AuthorisedCardUsersDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Assigns authorized users to a card. Users must have the **authorisedPaymentInstrumentUser** capability to be
        able to use the card.

        Args:
            payment_instrument_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: Bad request Unauthorized Forbidden Unprocessable Entity - a request validation error. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.post_payment_instruments_payment_instrument_id_authorised_card_users(
                payment_instrument_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AuthorizedCardUsersWithRawResponse:
        return self._with_raw_response


class AsyncAuthorizedCardUsers:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncAuthorizedCardUsersWithRawResponse(client, server)

    async def delete_payment_instruments_payment_instrument_id_authorised_card_users(
        self, payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes the list of authorized users assigned to a card.

        Args:
            payment_instrument_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: Unauthorized Forbidden ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_payment_instruments_payment_instrument_id_authorised_card_users(
                payment_instrument_id, request_options=request_options
            ),
        )

    async def get_payment_instruments_payment_instrument_id_authorised_card_users(
        self, payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AuthorisedCardUsers:
        """Returns the authorized users for a card.

        Args:
            payment_instrument_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: Unauthorized Forbidden Not Found Unprocessable Entity - a request validation error. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.get_payment_instruments_payment_instrument_id_authorised_card_users(
                payment_instrument_id, request_options=request_options
            ),
        )

    async def patch_payment_instruments_payment_instrument_id_authorised_card_users(
        self,
        payment_instrument_id: str,
        body: AuthorisedCardUsers | AuthorisedCardUsersDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates the list of authorized users for a card.

        >This request replaces all existing authorized users for the card.

        Args:
            payment_instrument_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: Bad request Unauthorized Forbidden Unprocessable Entity - a request validation error. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.patch_payment_instruments_payment_instrument_id_authorised_card_users(
                payment_instrument_id, body, request_options=request_options
            ),
        )

    async def post_payment_instruments_payment_instrument_id_authorised_card_users(
        self,
        payment_instrument_id: str,
        body: AuthorisedCardUsers | AuthorisedCardUsersDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Assigns authorized users to a card. Users must have the **authorisedPaymentInstrumentUser** capability to be
        able to use the card.

        Args:
            payment_instrument_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: Bad request Unauthorized Forbidden Unprocessable Entity - a request validation error. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.post_payment_instruments_payment_instrument_id_authorised_card_users(
                payment_instrument_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncAuthorizedCardUsersWithRawResponse:
        return self._with_raw_response


class AuthorizedCardUsersWithRawResponse(BaseRawResponse[RawClient, Server]):
    def delete_payment_instruments_payment_instrument_id_authorised_card_users(
        self, payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]:
        """Deletes the list of authorized users assigned to a card.

        Args:
            payment_instrument_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/paymentInstruments/{paymentInstrumentId}/authorisedCardUsers"),
            path_params=[param[str]("paymentInstrumentId", payment_instrument_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=delete_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper,
            request_options=request_options,
        )

    def get_payment_instruments_payment_instrument_id_authorised_card_users(
        self, payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AuthorisedCardUsers, GetPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]:
        """Returns the authorized users for a card.

        Args:
            payment_instrument_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstruments/{paymentInstrumentId}/authorisedCardUsers"),
            path_params=[param[str]("paymentInstrumentId", payment_instrument_id)],
            decoder=json_decoder[AuthorisedCardUsers],
            error_mapper=get_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper,
            request_options=request_options,
        )

    def patch_payment_instruments_payment_instrument_id_authorised_card_users(
        self,
        payment_instrument_id: str,
        body: AuthorisedCardUsers | AuthorisedCardUsersDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PatchPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]:
        """Updates the list of authorized users for a card.

        >This request replaces all existing authorized users for the card.

        Args:
            payment_instrument_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/paymentInstruments/{paymentInstrumentId}/authorisedCardUsers"),
            path_params=[param[str]("paymentInstrumentId", payment_instrument_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AuthorisedCardUsers | AuthorisedCardUsersDict](body),
            decoder=empty_response,
            error_mapper=patch_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper,
            request_options=request_options,
        )

    def post_payment_instruments_payment_instrument_id_authorised_card_users(
        self,
        payment_instrument_id: str,
        body: AuthorisedCardUsers | AuthorisedCardUsersDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PostPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]:
        """Assigns authorized users to a card. Users must have the **authorisedPaymentInstrumentUser** capability to be
        able to use the card.

        Args:
            payment_instrument_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/paymentInstruments/{paymentInstrumentId}/authorisedCardUsers"),
            path_params=[param[str]("paymentInstrumentId", payment_instrument_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AuthorisedCardUsers | AuthorisedCardUsersDict](body),
            decoder=empty_response,
            error_mapper=post_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper,
            request_options=request_options,
        )


class AsyncAuthorizedCardUsersWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def delete_payment_instruments_payment_instrument_id_authorised_card_users(
        self, payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeletePaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]:
        """Deletes the list of authorized users assigned to a card.

        Args:
            payment_instrument_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/paymentInstruments/{paymentInstrumentId}/authorisedCardUsers"),
            path_params=[param[str]("paymentInstrumentId", payment_instrument_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=async_empty_response,
            error_mapper=delete_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper,
            request_options=request_options,
        )

    async def get_payment_instruments_payment_instrument_id_authorised_card_users(
        self, payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AuthorisedCardUsers, GetPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]:
        """Returns the authorized users for a card.

        Args:
            payment_instrument_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstruments/{paymentInstrumentId}/authorisedCardUsers"),
            path_params=[param[str]("paymentInstrumentId", payment_instrument_id)],
            decoder=async_json_decoder[AuthorisedCardUsers],
            error_mapper=get_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper,
            request_options=request_options,
        )

    async def patch_payment_instruments_payment_instrument_id_authorised_card_users(
        self,
        payment_instrument_id: str,
        body: AuthorisedCardUsers | AuthorisedCardUsersDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PatchPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]:
        """Updates the list of authorized users for a card.

        >This request replaces all existing authorized users for the card.

        Args:
            payment_instrument_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/paymentInstruments/{paymentInstrumentId}/authorisedCardUsers"),
            path_params=[param[str]("paymentInstrumentId", payment_instrument_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AuthorisedCardUsers | AuthorisedCardUsersDict](body),
            decoder=async_empty_response,
            error_mapper=patch_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper,
            request_options=request_options,
        )

    async def post_payment_instruments_payment_instrument_id_authorised_card_users(
        self,
        payment_instrument_id: str,
        body: AuthorisedCardUsers | AuthorisedCardUsersDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PostPaymentInstrumentsPaymentInstrumentIdAuthorisedCardUsersErrorBody]:
        """Assigns authorized users to a card. Users must have the **authorisedPaymentInstrumentUser** capability to be
        able to use the card.

        Args:
            payment_instrument_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/paymentInstruments/{paymentInstrumentId}/authorisedCardUsers"),
            path_params=[param[str]("paymentInstrumentId", payment_instrument_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AuthorisedCardUsers | AuthorisedCardUsersDict](body),
            decoder=async_empty_response,
            error_mapper=post_payment_instruments_payment_instrument_id_authorised_card_users_error_mapper,
            request_options=request_options,
        )
