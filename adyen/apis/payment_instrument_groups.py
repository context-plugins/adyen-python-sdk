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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.get_payment_instrument_groups_id_error import (
    GetPaymentInstrumentGroupsIdErrorBody,
    get_payment_instrument_groups_id_error_mapper,
)
from ..errors.get_payment_instrument_groups_id_transaction_rules_error import (
    GetPaymentInstrumentGroupsIdTransactionRulesErrorBody,
    get_payment_instrument_groups_id_transaction_rules_error_mapper,
)
from ..errors.post_payment_instrument_groups_error import (
    PostPaymentInstrumentGroupsErrorBody,
    post_payment_instrument_groups_error_mapper,
)
from ..models.payment_instrument_group import PaymentInstrumentGroup
from ..models.payment_instrument_group_info import PaymentInstrumentGroupInfo, PaymentInstrumentGroupInfoDict
from ..models.transaction_rules_response import TransactionRulesResponse
from ..server.server import Server


class PaymentInstrumentGroups:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PaymentInstrumentGroupsWithRawResponse(client, server, auth)

    def get_payment_instrument_groups_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentInstrumentGroup:
        """Returns the details of a payment instrument group.

        Args:
            id_: The unique identifier of the payment instrument group.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(self._with_raw_response.get_payment_instrument_groups_id(id_, request_options=request_options))

    def get_payment_instrument_groups_id_transaction_rules(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRulesResponse:
        """Returns a list of all the transaction rules associated with a payment instrument group.

        Args:
            id_: The unique identifier of the payment instrument group.
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
            self._with_raw_response.get_payment_instrument_groups_id_transaction_rules(
                id_, request_options=request_options
            ),
        )

    def post_payment_instrument_groups(
        self,
        *,
        body: PaymentInstrumentGroupInfo | PaymentInstrumentGroupInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInstrumentGroup:
        """Creates a payment instrument group to associate and group payment instrument resources together. You can
        apply a transaction rule to a payment instrument group.

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
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_payment_instrument_groups(body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> PaymentInstrumentGroupsWithRawResponse:
        return self._with_raw_response


class AsyncPaymentInstrumentGroups:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPaymentInstrumentGroupsWithRawResponse(client, server, auth)

    async def get_payment_instrument_groups_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentInstrumentGroup:
        """Returns the details of a payment instrument group.

        Args:
            id_: The unique identifier of the payment instrument group.
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
            await self._with_raw_response.get_payment_instrument_groups_id(id_, request_options=request_options)
        )

    async def get_payment_instrument_groups_id_transaction_rules(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRulesResponse:
        """Returns a list of all the transaction rules associated with a payment instrument group.

        Args:
            id_: The unique identifier of the payment instrument group.
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
            await self._with_raw_response.get_payment_instrument_groups_id_transaction_rules(
                id_, request_options=request_options
            ),
        )

    async def post_payment_instrument_groups(
        self,
        *,
        body: PaymentInstrumentGroupInfo | PaymentInstrumentGroupInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInstrumentGroup:
        """Creates a payment instrument group to associate and group payment instrument resources together. You can
        apply a transaction rule to a payment instrument group.

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
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_payment_instrument_groups(body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncPaymentInstrumentGroupsWithRawResponse:
        return self._with_raw_response


class PaymentInstrumentGroupsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_payment_instrument_groups_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentInstrumentGroup, GetPaymentInstrumentGroupsIdErrorBody]:
        """Returns the details of a payment instrument group.

        Args:
            id_: The unique identifier of the payment instrument group.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstrumentGroups/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentInstrumentGroup],
            error_mapper=get_payment_instrument_groups_id_error_mapper,
            request_options=request_options,
        )

    def get_payment_instrument_groups_id_transaction_rules(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRulesResponse, GetPaymentInstrumentGroupsIdTransactionRulesErrorBody]:
        """Returns a list of all the transaction rules associated with a payment instrument group.

        Args:
            id_: The unique identifier of the payment instrument group.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstrumentGroups/{id}/transactionRules"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionRulesResponse],
            error_mapper=get_payment_instrument_groups_id_transaction_rules_error_mapper,
            request_options=request_options,
        )

    def post_payment_instrument_groups(
        self,
        *,
        body: PaymentInstrumentGroupInfo | PaymentInstrumentGroupInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInstrumentGroup, PostPaymentInstrumentGroupsErrorBody]:
        """Creates a payment instrument group to associate and group payment instrument resources together. You can
        apply a transaction rule to a payment instrument group.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/paymentInstrumentGroups"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInstrumentGroupInfo | PaymentInstrumentGroupInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentInstrumentGroup],
            error_mapper=post_payment_instrument_groups_error_mapper,
            request_options=request_options,
        )


class AsyncPaymentInstrumentGroupsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_payment_instrument_groups_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentInstrumentGroup, GetPaymentInstrumentGroupsIdErrorBody]:
        """Returns the details of a payment instrument group.

        Args:
            id_: The unique identifier of the payment instrument group.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstrumentGroups/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[PaymentInstrumentGroup],
            error_mapper=get_payment_instrument_groups_id_error_mapper,
            request_options=request_options,
        )

    async def get_payment_instrument_groups_id_transaction_rules(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRulesResponse, GetPaymentInstrumentGroupsIdTransactionRulesErrorBody]:
        """Returns a list of all the transaction rules associated with a payment instrument group.

        Args:
            id_: The unique identifier of the payment instrument group.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstrumentGroups/{id}/transactionRules"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TransactionRulesResponse],
            error_mapper=get_payment_instrument_groups_id_transaction_rules_error_mapper,
            request_options=request_options,
        )

    async def post_payment_instrument_groups(
        self,
        *,
        body: PaymentInstrumentGroupInfo | PaymentInstrumentGroupInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInstrumentGroup, PostPaymentInstrumentGroupsErrorBody]:
        """Creates a payment instrument group to associate and group payment instrument resources together. You can
        apply a transaction rule to a payment instrument group.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/paymentInstrumentGroups"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInstrumentGroupInfo | PaymentInstrumentGroupInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[PaymentInstrumentGroup],
            error_mapper=post_payment_instrument_groups_error_mapper,
            request_options=request_options,
        )
