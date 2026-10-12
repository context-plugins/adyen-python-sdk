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
from ..errors.get_mandates_error import GetMandatesErrorBody, get_mandates_error_mapper
from ..errors.get_mandates_mandate_id_error import GetMandatesMandateIdErrorBody, get_mandates_mandate_id_error_mapper
from ..errors.patch_mandates_mandate_id_error import (
    PatchMandatesMandateIdErrorBody,
    patch_mandates_mandate_id_error_mapper,
)
from ..errors.post_mandates_mandate_id_cancel_error import (
    PostMandatesMandateIdCancelErrorBody,
    post_mandates_mandate_id_cancel_error_mapper,
)
from ..models.list_mandates_response import ListMandatesResponse
from ..models.mandate1 import Mandate1
from ..models.mandate_update import MandateUpdate, MandateUpdateDict
from ..server.server import Server


class DirectDebitMandates:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = DirectDebitMandatesWithRawResponse(client, server)

    def get_mandates(
        self,
        *,
        balance_account_id: str | None = None,
        payment_instrument_id: str | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMandatesResponse:
        """Returns a list of all `direct debit mandates
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__ created for a business account.

        Args:
            balance_account_id: The unique identifier of the balance account linked to the payment instrument.
            payment_instrument_id: The unique identifier of the payment instrument linked to the mandate.
            cursor: The pagination cursor returned in a previous GET ``/mandates`` request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.get_mandates(
                balance_account_id=balance_account_id,
                payment_instrument_id=payment_instrument_id,
                cursor=cursor,
                request_options=request_options,
            ),
        )

    def get_mandates_mandate_id(
        self, mandate_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Mandate1:
        """Returns the details of the specified `direct debit mandate
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__.

        Args:
            mandate_id: The unique identifier of the mandate.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. The mandate was not found. Unprocessable Entity - a request validation error. Internal Server
                Error - the server could not process the request. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return unwrap(self._with_raw_response.get_mandates_mandate_id(mandate_id, request_options=request_options))

    def patch_mandates_mandate_id(
        self,
        mandate_id: str,
        body: MandateUpdate | MandateUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Amend the specified `direct debit mandate
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__.

        Args:
            mandate_id: The unique identifier of the mandate.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted - The request has been accepted

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. The mandate was not found Unprocessable Entity - a request validation error. Internal Server
                Error - the server could not process the request. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return unwrap(
            self._with_raw_response.patch_mandates_mandate_id(mandate_id, body, request_options=request_options)
        )

    def post_mandates_mandate_id_cancel(
        self, mandate_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Cancel a specified `direct debit mandate
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__.

        Args:
            mandate_id: The unique identifier of the mandate.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted - The request has been accepted

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. The mandate was not found. Unprocessable Entity - a request validation error. Internal Server
                Error - the server could not process the request. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return unwrap(
            self._with_raw_response.post_mandates_mandate_id_cancel(mandate_id, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> DirectDebitMandatesWithRawResponse:
        return self._with_raw_response


class AsyncDirectDebitMandates:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncDirectDebitMandatesWithRawResponse(client, server)

    async def get_mandates(
        self,
        *,
        balance_account_id: str | None = None,
        payment_instrument_id: str | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMandatesResponse:
        """Returns a list of all `direct debit mandates
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__ created for a business account.

        Args:
            balance_account_id: The unique identifier of the balance account linked to the payment instrument.
            payment_instrument_id: The unique identifier of the payment instrument linked to the mandate.
            cursor: The pagination cursor returned in a previous GET ``/mandates`` request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.get_mandates(
                balance_account_id=balance_account_id,
                payment_instrument_id=payment_instrument_id,
                cursor=cursor,
                request_options=request_options,
            ),
        )

    async def get_mandates_mandate_id(
        self, mandate_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Mandate1:
        """Returns the details of the specified `direct debit mandate
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__.

        Args:
            mandate_id: The unique identifier of the mandate.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. The mandate was not found. Unprocessable Entity - a request validation error. Internal Server
                Error - the server could not process the request. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_mandates_mandate_id(mandate_id, request_options=request_options)
        )

    async def patch_mandates_mandate_id(
        self,
        mandate_id: str,
        body: MandateUpdate | MandateUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Amend the specified `direct debit mandate
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__.

        Args:
            mandate_id: The unique identifier of the mandate.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted - The request has been accepted

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. The mandate was not found Unprocessable Entity - a request validation error. Internal Server
                Error - the server could not process the request. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return unwrap(
            await self._with_raw_response.patch_mandates_mandate_id(mandate_id, body, request_options=request_options)
        )

    async def post_mandates_mandate_id_cancel(
        self, mandate_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Cancel a specified `direct debit mandate
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__.

        Args:
            mandate_id: The unique identifier of the mandate.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted - The request has been accepted

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. The mandate was not found. Unprocessable Entity - a request validation error. Internal Server
                Error - the server could not process the request. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return unwrap(
            await self._with_raw_response.post_mandates_mandate_id_cancel(mandate_id, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncDirectDebitMandatesWithRawResponse:
        return self._with_raw_response


class DirectDebitMandatesWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_mandates(
        self,
        *,
        balance_account_id: str | None = None,
        payment_instrument_id: str | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMandatesResponse, GetMandatesErrorBody]:
        """Returns a list of all `direct debit mandates
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__ created for a business account.

        Args:
            balance_account_id: The unique identifier of the balance account linked to the payment instrument.
            payment_instrument_id: The unique identifier of the payment instrument linked to the mandate.
            cursor: The pagination cursor returned in a previous GET ``/mandates`` request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/mandates"),
            query_params=[
                param[str | None]("balanceAccountId", balance_account_id),
                param[str | None]("paymentInstrumentId", payment_instrument_id),
                param[str | None]("cursor", cursor),
            ],
            decoder=json_decoder[ListMandatesResponse],
            error_mapper=get_mandates_error_mapper,
            request_options=request_options,
        )

    def get_mandates_mandate_id(
        self, mandate_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Mandate1, GetMandatesMandateIdErrorBody]:
        """Returns the details of the specified `direct debit mandate
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__.

        Args:
            mandate_id: The unique identifier of the mandate.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/mandates/{mandateId}"),
            path_params=[param[str]("mandateId", mandate_id)],
            decoder=json_decoder[Mandate1],
            error_mapper=get_mandates_mandate_id_error_mapper,
            request_options=request_options,
        )

    def patch_mandates_mandate_id(
        self,
        mandate_id: str,
        body: MandateUpdate | MandateUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PatchMandatesMandateIdErrorBody]:
        """Amend the specified `direct debit mandate
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__.

        Args:
            mandate_id: The unique identifier of the mandate.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/mandates/{mandateId}"),
            path_params=[param[str]("mandateId", mandate_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MandateUpdate | MandateUpdateDict](body),
            decoder=empty_response,
            error_mapper=patch_mandates_mandate_id_error_mapper,
            request_options=request_options,
        )

    def post_mandates_mandate_id_cancel(
        self, mandate_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, PostMandatesMandateIdCancelErrorBody]:
        """Cancel a specified `direct debit mandate
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__.

        Args:
            mandate_id: The unique identifier of the mandate.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/mandates/{mandateId}/cancel"),
            path_params=[param[str]("mandateId", mandate_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=post_mandates_mandate_id_cancel_error_mapper,
            request_options=request_options,
        )


class AsyncDirectDebitMandatesWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_mandates(
        self,
        *,
        balance_account_id: str | None = None,
        payment_instrument_id: str | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMandatesResponse, GetMandatesErrorBody]:
        """Returns a list of all `direct debit mandates
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__ created for a business account.

        Args:
            balance_account_id: The unique identifier of the balance account linked to the payment instrument.
            payment_instrument_id: The unique identifier of the payment instrument linked to the mandate.
            cursor: The pagination cursor returned in a previous GET ``/mandates`` request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/mandates"),
            query_params=[
                param[str | None]("balanceAccountId", balance_account_id),
                param[str | None]("paymentInstrumentId", payment_instrument_id),
                param[str | None]("cursor", cursor),
            ],
            decoder=async_json_decoder[ListMandatesResponse],
            error_mapper=get_mandates_error_mapper,
            request_options=request_options,
        )

    async def get_mandates_mandate_id(
        self, mandate_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Mandate1, GetMandatesMandateIdErrorBody]:
        """Returns the details of the specified `direct debit mandate
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__.

        Args:
            mandate_id: The unique identifier of the mandate.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/mandates/{mandateId}"),
            path_params=[param[str]("mandateId", mandate_id)],
            decoder=async_json_decoder[Mandate1],
            error_mapper=get_mandates_mandate_id_error_mapper,
            request_options=request_options,
        )

    async def patch_mandates_mandate_id(
        self,
        mandate_id: str,
        body: MandateUpdate | MandateUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PatchMandatesMandateIdErrorBody]:
        """Amend the specified `direct debit mandate
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__.

        Args:
            mandate_id: The unique identifier of the mandate.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/mandates/{mandateId}"),
            path_params=[param[str]("mandateId", mandate_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MandateUpdate | MandateUpdateDict](body),
            decoder=async_empty_response,
            error_mapper=patch_mandates_mandate_id_error_mapper,
            request_options=request_options,
        )

    async def post_mandates_mandate_id_cancel(
        self, mandate_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, PostMandatesMandateIdCancelErrorBody]:
        """Cancel a specified `direct debit mandate
        <https://docs.adyen.com/business-accounts/accept-direct-debits-uk>`__.

        Args:
            mandate_id: The unique identifier of the mandate.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/mandates/{mandateId}/cancel"),
            path_params=[param[str]("mandateId", mandate_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=async_empty_response,
            error_mapper=post_mandates_mandate_id_cancel_error_mapper,
            request_options=request_options,
        )
