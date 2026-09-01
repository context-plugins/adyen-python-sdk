from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    json_decoder,
    param,
)
from ..errors.get_cardorders_error import GetCardordersErrorBody, get_cardorders_error_mapper
from ..errors.get_cardorders_id_items_error import GetCardordersIdItemsErrorBody, get_cardorders_id_items_error_mapper
from ..models.paginated_get_card_order_item_response import PaginatedGetCardOrderItemResponse
from ..models.paginated_get_card_order_response import PaginatedGetCardOrderResponse
from ..server.server import Server


class CardOrders:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CardOrdersWithRawResponse(client, server, auth)

    def get_cardorders(
        self,
        *,
        id: str | None = None,
        card_manufacturing_profile_id: str | None = None,
        status: str | None = None,
        tx_variant_code: str | None = None,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        locked_since: RFC3339DateTime | None = None,
        locked_until: RFC3339DateTime | None = None,
        service_center: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedGetCardOrderResponse:
        """Returns a paginated list of card orders.

        Args:
            id: The unique identifier of the card order.
            card_manufacturing_profile_id: The unique identifier of the card manufacturer profile.
            status: The status of the card order.
            tx_variant_code: The unique code of the card manufacturer profile. Possible values: **mcmaestro**, **mc**,
                **visa**, **mcdebit**.
            created_since: Only include card orders that have been created on or after this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            created_until: Only include card orders that have been created on or before this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            locked_since: Only include card orders that have been locked on or after this point in time. The value must
                be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            locked_until: Only include card orders that have been locked on or before this point in time. The value must
                be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            service_center: The service center at which the card is issued. The value is case-sensitive.
            offset: Specifies the position of an element in a list of card orders. The response includes a list of card
                orders that starts at the specified offset. **Default:** 0, which means that the response contains all
                the elements in the list of card orders.
            limit: The number of card orders returned per page. **Default:** 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return self._with_raw_response.get_cardorders(
            id=id,
            card_manufacturing_profile_id=card_manufacturing_profile_id,
            status=status,
            tx_variant_code=tx_variant_code,
            created_since=created_since,
            created_until=created_until,
            locked_since=locked_since,
            locked_until=locked_until,
            service_center=service_center,
            offset=offset,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    def get_cardorders_id_items(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedGetCardOrderItemResponse:
        """Returns the item list of a specific card order.

        Args:
            id: The unique identifier of the card order.
            offset: Specifies the position of an element in a list of card orders. The response includes a list of card
                order items that starts at the specified offset. **Default:** 0, which means that the response contains
                all the elements in the list of card order items.
            limit: The number of card order items returned per page. **Default:** 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return self._with_raw_response.get_cardorders_id_items(
            id, offset=offset, limit=limit, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> CardOrdersWithRawResponse:
        return self._with_raw_response


class AsyncCardOrders:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCardOrdersWithRawResponse(client, server, auth)

    async def get_cardorders(
        self,
        *,
        id: str | None = None,
        card_manufacturing_profile_id: str | None = None,
        status: str | None = None,
        tx_variant_code: str | None = None,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        locked_since: RFC3339DateTime | None = None,
        locked_until: RFC3339DateTime | None = None,
        service_center: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedGetCardOrderResponse:
        """Returns a paginated list of card orders.

        Args:
            id: The unique identifier of the card order.
            card_manufacturing_profile_id: The unique identifier of the card manufacturer profile.
            status: The status of the card order.
            tx_variant_code: The unique code of the card manufacturer profile. Possible values: **mcmaestro**, **mc**,
                **visa**, **mcdebit**.
            created_since: Only include card orders that have been created on or after this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            created_until: Only include card orders that have been created on or before this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            locked_since: Only include card orders that have been locked on or after this point in time. The value must
                be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            locked_until: Only include card orders that have been locked on or before this point in time. The value must
                be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            service_center: The service center at which the card is issued. The value is case-sensitive.
            offset: Specifies the position of an element in a list of card orders. The response includes a list of card
                orders that starts at the specified offset. **Default:** 0, which means that the response contains all
                the elements in the list of card orders.
            limit: The number of card orders returned per page. **Default:** 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_cardorders(
                id=id,
                card_manufacturing_profile_id=card_manufacturing_profile_id,
                status=status,
                tx_variant_code=tx_variant_code,
                created_since=created_since,
                created_until=created_until,
                locked_since=locked_since,
                locked_until=locked_until,
                service_center=service_center,
                offset=offset,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    async def get_cardorders_id_items(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedGetCardOrderItemResponse:
        """Returns the item list of a specific card order.

        Args:
            id: The unique identifier of the card order.
            offset: Specifies the position of an element in a list of card orders. The response includes a list of card
                order items that starts at the specified offset. **Default:** 0, which means that the response contains
                all the elements in the list of card order items.
            limit: The number of card order items returned per page. **Default:** 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_cardorders_id_items(
                id, offset=offset, limit=limit, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCardOrdersWithRawResponse:
        return self._with_raw_response


class CardOrdersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_cardorders(
        self,
        *,
        id: str | None = None,
        card_manufacturing_profile_id: str | None = None,
        status: str | None = None,
        tx_variant_code: str | None = None,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        locked_since: RFC3339DateTime | None = None,
        locked_until: RFC3339DateTime | None = None,
        service_center: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedGetCardOrderResponse, GetCardordersErrorBody]:
        """Returns a paginated list of card orders.

        Args:
            id: The unique identifier of the card order.
            card_manufacturing_profile_id: The unique identifier of the card manufacturer profile.
            status: The status of the card order.
            tx_variant_code: The unique code of the card manufacturer profile. Possible values: **mcmaestro**, **mc**,
                **visa**, **mcdebit**.
            created_since: Only include card orders that have been created on or after this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            created_until: Only include card orders that have been created on or before this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            locked_since: Only include card orders that have been locked on or after this point in time. The value must
                be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            locked_until: Only include card orders that have been locked on or before this point in time. The value must
                be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            service_center: The service center at which the card is issued. The value is case-sensitive.
            offset: Specifies the position of an element in a list of card orders. The response includes a list of card
                orders that starts at the specified offset. **Default:** 0, which means that the response contains all
                the elements in the list of card orders.
            limit: The number of card orders returned per page. **Default:** 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/cardorders"),
            query_params=[
                param[str | None]("id", id),
                param[str | None]("cardManufacturingProfileId", card_manufacturing_profile_id),
                param[str | None]("status", status),
                param[str | None]("txVariantCode", tx_variant_code),
                param[RFC3339DateTime | None]("createdSince", created_since),
                param[RFC3339DateTime | None]("createdUntil", created_until),
                param[RFC3339DateTime | None]("lockedSince", locked_since),
                param[RFC3339DateTime | None]("lockedUntil", locked_until),
                param[str | None]("serviceCenter", service_center),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaginatedGetCardOrderResponse],
            error_mapper=get_cardorders_error_mapper,
            request_options=request_options,
        )

    def get_cardorders_id_items(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedGetCardOrderItemResponse, GetCardordersIdItemsErrorBody]:
        """Returns the item list of a specific card order.

        Args:
            id: The unique identifier of the card order.
            offset: Specifies the position of an element in a list of card orders. The response includes a list of card
                order items that starts at the specified offset. **Default:** 0, which means that the response contains
                all the elements in the list of card order items.
            limit: The number of card order items returned per page. **Default:** 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/cardorders/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[param[int | None]("offset", offset), param[int | None]("limit", limit)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaginatedGetCardOrderItemResponse],
            error_mapper=get_cardorders_id_items_error_mapper,
            request_options=request_options,
        )


class AsyncCardOrdersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_cardorders(
        self,
        *,
        id: str | None = None,
        card_manufacturing_profile_id: str | None = None,
        status: str | None = None,
        tx_variant_code: str | None = None,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        locked_since: RFC3339DateTime | None = None,
        locked_until: RFC3339DateTime | None = None,
        service_center: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedGetCardOrderResponse, GetCardordersErrorBody]:
        """Returns a paginated list of card orders.

        Args:
            id: The unique identifier of the card order.
            card_manufacturing_profile_id: The unique identifier of the card manufacturer profile.
            status: The status of the card order.
            tx_variant_code: The unique code of the card manufacturer profile. Possible values: **mcmaestro**, **mc**,
                **visa**, **mcdebit**.
            created_since: Only include card orders that have been created on or after this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            created_until: Only include card orders that have been created on or before this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            locked_since: Only include card orders that have been locked on or after this point in time. The value must
                be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            locked_until: Only include card orders that have been locked on or before this point in time. The value must
                be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            service_center: The service center at which the card is issued. The value is case-sensitive.
            offset: Specifies the position of an element in a list of card orders. The response includes a list of card
                orders that starts at the specified offset. **Default:** 0, which means that the response contains all
                the elements in the list of card orders.
            limit: The number of card orders returned per page. **Default:** 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/cardorders"),
            query_params=[
                param[str | None]("id", id),
                param[str | None]("cardManufacturingProfileId", card_manufacturing_profile_id),
                param[str | None]("status", status),
                param[str | None]("txVariantCode", tx_variant_code),
                param[RFC3339DateTime | None]("createdSince", created_since),
                param[RFC3339DateTime | None]("createdUntil", created_until),
                param[RFC3339DateTime | None]("lockedSince", locked_since),
                param[RFC3339DateTime | None]("lockedUntil", locked_until),
                param[str | None]("serviceCenter", service_center),
                param[int | None]("offset", offset),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaginatedGetCardOrderResponse],
            error_mapper=get_cardorders_error_mapper,
            request_options=request_options,
        )

    async def get_cardorders_id_items(
        self,
        id: str,
        *,
        offset: int | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedGetCardOrderItemResponse, GetCardordersIdItemsErrorBody]:
        """Returns the item list of a specific card order.

        Args:
            id: The unique identifier of the card order.
            offset: Specifies the position of an element in a list of card orders. The response includes a list of card
                order items that starts at the specified offset. **Default:** 0, which means that the response contains
                all the elements in the list of card order items.
            limit: The number of card order items returned per page. **Default:** 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/cardorders/{id}/items"),
            path_params=[param[str]("id", id)],
            query_params=[param[int | None]("offset", offset), param[int | None]("limit", limit)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaginatedGetCardOrderItemResponse],
            error_mapper=get_cardorders_id_items_error_mapper,
            request_options=request_options,
        )
