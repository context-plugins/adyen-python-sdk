from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    json_body,
    json_decoder,
    param,
)
from ..errors.get_disputes_error import GetDisputesErrorBody, get_disputes_error_mapper
from ..errors.get_disputes_id_error import GetDisputesIdErrorBody, get_disputes_id_error_mapper
from ..errors.patch_disputes_id_error import PatchDisputesIdErrorBody, patch_disputes_id_error_mapper
from ..errors.post_disputes_error import PostDisputesErrorBody, post_disputes_error_mapper
from ..models.dispute_request import DisputeRequest, DisputeRequestDict
from ..models.dispute_response import DisputeResponse
from ..models.patchable_dispute_request import PatchableDisputeRequest, PatchableDisputeRequestDict
from ..server.server import Server


class RaiseDisputes:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = RaiseDisputesWithRawResponse(client, server)

    def get_disputes(
        self,
        *,
        status: str | None = None,
        payment_instrument: str | None = None,
        created_since: str | None = None,
        created_until: str | None = None,
        offset: str | None = None,
        limit: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[list[DisputeResponse]]:
        r"""Returns a list of raised disputes that match the query parameters.

        This endpoint supports cursor-based pagination. The response returns the first page of results, and returns
        links to the next page when applicable. You can use the links to page through the results. The response also
        returns links to the previous page when applicable.

        Args:
            status: The current status of the dispute. Possible values: **draft**, **submitted**, **closed**, **won**,
                **chargeback**, **secondPresentment**.
            payment_instrument: The unique identifier of the payment instrument.
            created_since: Only include disputes that have been created on or after this point in time. The value must
                be in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601\>`__ format. For example, 2021-05-30T15:07:40Z.
            created_until: Only include disputes that have been created on or before this point in time. The value must
                be in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601\>`__ format. For example,
                **2021-05-30T15:07:40Z**.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum of 500 items. By default, the response returns 100
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_disputes(
            status=status,
            payment_instrument=payment_instrument,
            created_since=created_since,
            created_until=created_until,
            offset=offset,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    def get_disputes_id(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> DisputeResponse:
        """Get a raised dispute by ID.

        Args:
            id: The unique identifier of the raised dispute.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_disputes_id(id, request_options=request_options).unwrap()

    def patch_disputes_id(
        self,
        id: str,
        *,
        body: PatchableDisputeRequest | PatchableDisputeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DisputeResponse:
        """Update information related to a raised dispute, or change a dispute's status from **draft** to **submitted**
        or **closed**.

        **Note:** Changing the status of a dispute to **submitted** or **closed** is a final action. You cannot make
        updates to a **submitted** or **closed** dispute. Make sure to upload all supporting attachments using the
        ``POST /disputes/{id}/attachments`` endpoint before you submit a dispute. When you update a dispute to
        **submitted**, Adyen sends the raised dispute to the card scheme for review and acquirer defense. When you
        update a raised dispute to **closed**, Adyen closes the dispute, and the dispute is no longer eligible for
        review by the card scheme.

        Args:
            id: The unique identifier of the raised dispute.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.patch_disputes_id(id, body=body, request_options=request_options).unwrap()

    def post_disputes(
        self, body: DisputeRequest | DisputeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DisputeResponse:
        """Raise a dispute for an underlying transaction, providing a dispute type and the amount you want to dispute.

        Raising a dispute returns a dispute ID, which you can use to update details about the dispute, provide
        supporting documentation, close the dispute, or submit the dispute for a chargeback. You can also use the
        dispute ID to view the status of the dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.post_disputes(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> RaiseDisputesWithRawResponse:
        return self._with_raw_response


class AsyncRaiseDisputes:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncRaiseDisputesWithRawResponse(client, server)

    async def get_disputes(
        self,
        *,
        status: str | None = None,
        payment_instrument: str | None = None,
        created_since: str | None = None,
        created_until: str | None = None,
        offset: str | None = None,
        limit: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[list[DisputeResponse]]:
        r"""Returns a list of raised disputes that match the query parameters.

        This endpoint supports cursor-based pagination. The response returns the first page of results, and returns
        links to the next page when applicable. You can use the links to page through the results. The response also
        returns links to the previous page when applicable.

        Args:
            status: The current status of the dispute. Possible values: **draft**, **submitted**, **closed**, **won**,
                **chargeback**, **secondPresentment**.
            payment_instrument: The unique identifier of the payment instrument.
            created_since: Only include disputes that have been created on or after this point in time. The value must
                be in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601\>`__ format. For example, 2021-05-30T15:07:40Z.
            created_until: Only include disputes that have been created on or before this point in time. The value must
                be in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601\>`__ format. For example,
                **2021-05-30T15:07:40Z**.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum of 500 items. By default, the response returns 100
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_disputes(
                status=status,
                payment_instrument=payment_instrument,
                created_since=created_since,
                created_until=created_until,
                offset=offset,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    async def get_disputes_id(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> DisputeResponse:
        """Get a raised dispute by ID.

        Args:
            id: The unique identifier of the raised dispute.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (await self._with_raw_response.get_disputes_id(id, request_options=request_options)).unwrap()

    async def patch_disputes_id(
        self,
        id: str,
        *,
        body: PatchableDisputeRequest | PatchableDisputeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DisputeResponse:
        """Update information related to a raised dispute, or change a dispute's status from **draft** to **submitted**
        or **closed**.

        **Note:** Changing the status of a dispute to **submitted** or **closed** is a final action. You cannot make
        updates to a **submitted** or **closed** dispute. Make sure to upload all supporting attachments using the
        ``POST /disputes/{id}/attachments`` endpoint before you submit a dispute. When you update a dispute to
        **submitted**, Adyen sends the raised dispute to the card scheme for review and acquirer defense. When you
        update a raised dispute to **closed**, Adyen closes the dispute, and the dispute is no longer eligible for
        review by the card scheme.

        Args:
            id: The unique identifier of the raised dispute.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.patch_disputes_id(id, body=body, request_options=request_options)
        ).unwrap()

    async def post_disputes(
        self, body: DisputeRequest | DisputeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DisputeResponse:
        """Raise a dispute for an underlying transaction, providing a dispute type and the amount you want to dispute.

        Raising a dispute returns a dispute ID, which you can use to update details about the dispute, provide
        supporting documentation, close the dispute, or submit the dispute for a chargeback. You can also use the
        dispute ID to view the status of the dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Authentication required. Insufficient permissions to process the request. A request validation
                error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (await self._with_raw_response.post_disputes(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncRaiseDisputesWithRawResponse:
        return self._with_raw_response


class RaiseDisputesWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_disputes(
        self,
        *,
        status: str | None = None,
        payment_instrument: str | None = None,
        created_since: str | None = None,
        created_until: str | None = None,
        offset: str | None = None,
        limit: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[list[DisputeResponse]], GetDisputesErrorBody]:
        r"""Returns a list of raised disputes that match the query parameters.

        This endpoint supports cursor-based pagination. The response returns the first page of results, and returns
        links to the next page when applicable. You can use the links to page through the results. The response also
        returns links to the previous page when applicable.

        Args:
            status: The current status of the dispute. Possible values: **draft**, **submitted**, **closed**, **won**,
                **chargeback**, **secondPresentment**.
            payment_instrument: The unique identifier of the payment instrument.
            created_since: Only include disputes that have been created on or after this point in time. The value must
                be in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601\>`__ format. For example, 2021-05-30T15:07:40Z.
            created_until: Only include disputes that have been created on or before this point in time. The value must
                be in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601\>`__ format. For example,
                **2021-05-30T15:07:40Z**.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum of 500 items. By default, the response returns 100
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default23("/disputes"),
            query_params=[
                param[str | None]("status", status),
                param[str | None]("paymentInstrument", payment_instrument),
                param[str | None]("createdSince", created_since),
                param[str | None]("createdUntil", created_until),
                param[str | None]("offset", offset),
                param[str | None]("limit", limit),
            ],
            decoder=json_decoder[list[list[DisputeResponse]]],
            error_mapper=get_disputes_error_mapper,
            request_options=request_options,
        )

    def get_disputes_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisputeResponse, GetDisputesIdErrorBody]:
        """Get a raised dispute by ID.

        Args:
            id: The unique identifier of the raised dispute.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default23("/disputes/{id}"),
            path_params=[param[str]("id", id)],
            decoder=json_decoder[DisputeResponse],
            error_mapper=get_disputes_id_error_mapper,
            request_options=request_options,
        )

    def patch_disputes_id(
        self,
        id: str,
        *,
        body: PatchableDisputeRequest | PatchableDisputeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DisputeResponse, PatchDisputesIdErrorBody]:
        """Update information related to a raised dispute, or change a dispute's status from **draft** to **submitted**
        or **closed**.

        **Note:** Changing the status of a dispute to **submitted** or **closed** is a final action. You cannot make
        updates to a **submitted** or **closed** dispute. Make sure to upload all supporting attachments using the
        ``POST /disputes/{id}/attachments`` endpoint before you submit a dispute. When you update a dispute to
        **submitted**, Adyen sends the raised dispute to the card scheme for review and acquirer defense. When you
        update a raised dispute to **closed**, Adyen closes the dispute, and the dispute is no longer eligible for
        review by the card scheme.

        Args:
            id: The unique identifier of the raised dispute.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default23("/disputes/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PatchableDisputeRequest | PatchableDisputeRequestDict | None](body),
            decoder=json_decoder[DisputeResponse],
            error_mapper=patch_disputes_id_error_mapper,
            request_options=request_options,
        )

    def post_disputes(
        self, body: DisputeRequest | DisputeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisputeResponse, PostDisputesErrorBody]:
        """Raise a dispute for an underlying transaction, providing a dispute type and the amount you want to dispute.

        Raising a dispute returns a dispute ID, which you can use to update details about the dispute, provide
        supporting documentation, close the dispute, or submit the dispute for a chargeback. You can also use the
        dispute ID to view the status of the dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default23("/disputes"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisputeRequest | DisputeRequestDict](body),
            decoder=json_decoder[DisputeResponse],
            error_mapper=post_disputes_error_mapper,
            request_options=request_options,
        )


class AsyncRaiseDisputesWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_disputes(
        self,
        *,
        status: str | None = None,
        payment_instrument: str | None = None,
        created_since: str | None = None,
        created_until: str | None = None,
        offset: str | None = None,
        limit: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[list[DisputeResponse]], GetDisputesErrorBody]:
        r"""Returns a list of raised disputes that match the query parameters.

        This endpoint supports cursor-based pagination. The response returns the first page of results, and returns
        links to the next page when applicable. You can use the links to page through the results. The response also
        returns links to the previous page when applicable.

        Args:
            status: The current status of the dispute. Possible values: **draft**, **submitted**, **closed**, **won**,
                **chargeback**, **secondPresentment**.
            payment_instrument: The unique identifier of the payment instrument.
            created_since: Only include disputes that have been created on or after this point in time. The value must
                be in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601\>`__ format. For example, 2021-05-30T15:07:40Z.
            created_until: Only include disputes that have been created on or before this point in time. The value must
                be in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601\>`__ format. For example,
                **2021-05-30T15:07:40Z**.
            offset: The number of items that you want to skip.
            limit: The number of items returned per page, maximum of 500 items. By default, the response returns 100
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default23("/disputes"),
            query_params=[
                param[str | None]("status", status),
                param[str | None]("paymentInstrument", payment_instrument),
                param[str | None]("createdSince", created_since),
                param[str | None]("createdUntil", created_until),
                param[str | None]("offset", offset),
                param[str | None]("limit", limit),
            ],
            decoder=json_decoder[list[list[DisputeResponse]]],
            error_mapper=get_disputes_error_mapper,
            request_options=request_options,
        )

    async def get_disputes_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisputeResponse, GetDisputesIdErrorBody]:
        """Get a raised dispute by ID.

        Args:
            id: The unique identifier of the raised dispute.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default23("/disputes/{id}"),
            path_params=[param[str]("id", id)],
            decoder=json_decoder[DisputeResponse],
            error_mapper=get_disputes_id_error_mapper,
            request_options=request_options,
        )

    async def patch_disputes_id(
        self,
        id: str,
        *,
        body: PatchableDisputeRequest | PatchableDisputeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DisputeResponse, PatchDisputesIdErrorBody]:
        """Update information related to a raised dispute, or change a dispute's status from **draft** to **submitted**
        or **closed**.

        **Note:** Changing the status of a dispute to **submitted** or **closed** is a final action. You cannot make
        updates to a **submitted** or **closed** dispute. Make sure to upload all supporting attachments using the
        ``POST /disputes/{id}/attachments`` endpoint before you submit a dispute. When you update a dispute to
        **submitted**, Adyen sends the raised dispute to the card scheme for review and acquirer defense. When you
        update a raised dispute to **closed**, Adyen closes the dispute, and the dispute is no longer eligible for
        review by the card scheme.

        Args:
            id: The unique identifier of the raised dispute.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default23("/disputes/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PatchableDisputeRequest | PatchableDisputeRequestDict | None](body),
            decoder=json_decoder[DisputeResponse],
            error_mapper=patch_disputes_id_error_mapper,
            request_options=request_options,
        )

    async def post_disputes(
        self, body: DisputeRequest | DisputeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisputeResponse, PostDisputesErrorBody]:
        """Raise a dispute for an underlying transaction, providing a dispute type and the amount you want to dispute.

        Raising a dispute returns a dispute ID, which you can use to update details about the dispute, provide
        supporting documentation, close the dispute, or submit the dispute for a chargeback. You can also use the
        dispute ID to view the status of the dispute.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default23("/disputes"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisputeRequest | DisputeRequestDict](body),
            decoder=json_decoder[DisputeResponse],
            error_mapper=post_disputes_error_mapper,
            request_options=request_options,
        )
