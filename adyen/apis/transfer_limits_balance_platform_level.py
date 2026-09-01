from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.delete_balance_platforms_id_transfer_limits_transfer_limit_id_error import (
    DeleteBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody,
    delete_balance_platforms_id_transfer_limits_transfer_limit_id_error_mapper,
)
from ..errors.get_balance_platforms_id_transfer_limits_error import (
    GetBalancePlatformsIdTransferLimitsErrorBody,
    get_balance_platforms_id_transfer_limits_error_mapper,
)
from ..errors.get_balance_platforms_id_transfer_limits_transfer_limit_id_error import (
    GetBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody,
    get_balance_platforms_id_transfer_limits_transfer_limit_id_error_mapper,
)
from ..errors.post_balance_platforms_id_transfer_limits_error import (
    PostBalancePlatformsIdTransferLimitsErrorBody,
    post_balance_platforms_id_transfer_limits_error_mapper,
)
from ..models.create_transfer_limit_request import CreateTransferLimitRequest, CreateTransferLimitRequestDict
from ..models.enums.limit_status import LimitStatusOrStr
from ..models.enums.scope import ScopeOrStr
from ..models.enums.transfer_type import TransferTypeOrStr
from ..models.transfer_limit import TransferLimit
from ..models.transfer_limit_list_response import TransferLimitListResponse
from ..server.server import Server


class TransferLimitsBalancePlatformLevel:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = TransferLimitsBalancePlatformLevelWithRawResponse(client, server)

    def delete_balance_platforms_id_transfer_limits_transfer_limit_id(
        self, id: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a scheduled or pending transfer limit using its unique ``transferLimitId``. You cannot delete an
        active limit.

        Args:
            id: The unique identifier of the balance platform.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.delete_balance_platforms_id_transfer_limits_transfer_limit_id(
            id, transfer_limit_id, request_options=request_options
        ).unwrap()

    def get_balance_platforms_id_transfer_limits(
        self,
        id: str,
        *,
        scope: ScopeOrStr | None = None,
        transfer_type: TransferTypeOrStr | None = None,
        status: LimitStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferLimitListResponse:
        """Filter and view the transfer limits configured for your balance platform using the balance platform's unique
        ``id`` and the available query parameters.

        Args:
            id: The unique identifier of the balance platform.
            scope: The scope to which the transfer limit applies. Possible values: * **perTransaction**: you set a
                maximum amount for each transfer made from the balance account or balance platform. * **perDay**: you
                set a maximum total amount for all transfers made from the balance account or balance platform in a day.
            transfer_type: The type of transfer to which the limit applies. Possible values: * **instant**: the limit
                applies to transfers with an **instant** priority. * **all**: the limit applies to all transfers,
                regardless of priority.
            status: The status of the transfer limit. Possible values: * **active**: the limit is currently active. *
                **inactive**: the limit is currently inactive. * **pendingSCA**: the limit is pending until your user
                performs SCA. * **scheduled**: the limit is scheduled to become active at a future date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_balance_platforms_id_transfer_limits(
            id, scope=scope, transfer_type=transfer_type, status=status, request_options=request_options
        ).unwrap()

    def get_balance_platforms_id_transfer_limits_transfer_limit_id(
        self, id: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransferLimit:
        """Get the details of a transfer limit using its unique ``transferLimitId``.

        Args:
            id: The unique identifier of the balance platform.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_balance_platforms_id_transfer_limits_transfer_limit_id(
            id, transfer_limit_id, request_options=request_options
        ).unwrap()

    def post_balance_platforms_id_transfer_limits(
        self,
        id: str,
        body: CreateTransferLimitRequest | CreateTransferLimitRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferLimit:
        """Create a transfer limit for your balance platform using the unique ``id`` of your balance platform.

        Args:
            id: The unique identifier of the balance platform.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.post_balance_platforms_id_transfer_limits(
            id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TransferLimitsBalancePlatformLevelWithRawResponse:
        return self._with_raw_response


class AsyncTransferLimitsBalancePlatformLevel:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncTransferLimitsBalancePlatformLevelWithRawResponse(client, server)

    async def delete_balance_platforms_id_transfer_limits_transfer_limit_id(
        self, id: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a scheduled or pending transfer limit using its unique ``transferLimitId``. You cannot delete an
        active limit.

        Args:
            id: The unique identifier of the balance platform.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.delete_balance_platforms_id_transfer_limits_transfer_limit_id(
                id, transfer_limit_id, request_options=request_options
            )
        ).unwrap()

    async def get_balance_platforms_id_transfer_limits(
        self,
        id: str,
        *,
        scope: ScopeOrStr | None = None,
        transfer_type: TransferTypeOrStr | None = None,
        status: LimitStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferLimitListResponse:
        """Filter and view the transfer limits configured for your balance platform using the balance platform's unique
        ``id`` and the available query parameters.

        Args:
            id: The unique identifier of the balance platform.
            scope: The scope to which the transfer limit applies. Possible values: * **perTransaction**: you set a
                maximum amount for each transfer made from the balance account or balance platform. * **perDay**: you
                set a maximum total amount for all transfers made from the balance account or balance platform in a day.
            transfer_type: The type of transfer to which the limit applies. Possible values: * **instant**: the limit
                applies to transfers with an **instant** priority. * **all**: the limit applies to all transfers,
                regardless of priority.
            status: The status of the transfer limit. Possible values: * **active**: the limit is currently active. *
                **inactive**: the limit is currently inactive. * **pendingSCA**: the limit is pending until your user
                performs SCA. * **scheduled**: the limit is scheduled to become active at a future date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_balance_platforms_id_transfer_limits(
                id, scope=scope, transfer_type=transfer_type, status=status, request_options=request_options
            )
        ).unwrap()

    async def get_balance_platforms_id_transfer_limits_transfer_limit_id(
        self, id: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransferLimit:
        """Get the details of a transfer limit using its unique ``transferLimitId``.

        Args:
            id: The unique identifier of the balance platform.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_balance_platforms_id_transfer_limits_transfer_limit_id(
                id, transfer_limit_id, request_options=request_options
            )
        ).unwrap()

    async def post_balance_platforms_id_transfer_limits(
        self,
        id: str,
        body: CreateTransferLimitRequest | CreateTransferLimitRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferLimit:
        """Create a transfer limit for your balance platform using the unique ``id`` of your balance platform.

        Args:
            id: The unique identifier of the balance platform.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.post_balance_platforms_id_transfer_limits(
                id, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTransferLimitsBalancePlatformLevelWithRawResponse:
        return self._with_raw_response


class TransferLimitsBalancePlatformLevelWithRawResponse(BaseRawResponse[RawClient, Server]):
    def delete_balance_platforms_id_transfer_limits_transfer_limit_id(
        self, id: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody]:
        """Delete a scheduled or pending transfer limit using its unique ``transferLimitId``. You cannot delete an
        active limit.

        Args:
            id: The unique identifier of the balance platform.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/balancePlatforms/{id}/transferLimits/{transferLimitId}"),
            path_params=[param[str]("id", id), param[str]("transferLimitId", transfer_limit_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=delete_balance_platforms_id_transfer_limits_transfer_limit_id_error_mapper,
            request_options=request_options,
        )

    def get_balance_platforms_id_transfer_limits(
        self,
        id: str,
        *,
        scope: ScopeOrStr | None = None,
        transfer_type: TransferTypeOrStr | None = None,
        status: LimitStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferLimitListResponse, GetBalancePlatformsIdTransferLimitsErrorBody]:
        """Filter and view the transfer limits configured for your balance platform using the balance platform's unique
        ``id`` and the available query parameters.

        Args:
            id: The unique identifier of the balance platform.
            scope: The scope to which the transfer limit applies. Possible values: * **perTransaction**: you set a
                maximum amount for each transfer made from the balance account or balance platform. * **perDay**: you
                set a maximum total amount for all transfers made from the balance account or balance platform in a day.
            transfer_type: The type of transfer to which the limit applies. Possible values: * **instant**: the limit
                applies to transfers with an **instant** priority. * **all**: the limit applies to all transfers,
                regardless of priority.
            status: The status of the transfer limit. Possible values: * **active**: the limit is currently active. *
                **inactive**: the limit is currently inactive. * **pendingSCA**: the limit is pending until your user
                performs SCA. * **scheduled**: the limit is scheduled to become active at a future date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{id}/transferLimits"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[ScopeOrStr | None]("scope", scope),
                param[TransferTypeOrStr | None]("transferType", transfer_type),
                param[LimitStatusOrStr | None]("status", status),
            ],
            decoder=json_decoder[TransferLimitListResponse],
            error_mapper=get_balance_platforms_id_transfer_limits_error_mapper,
            request_options=request_options,
        )

    def get_balance_platforms_id_transfer_limits_transfer_limit_id(
        self, id: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransferLimit, GetBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody]:
        """Get the details of a transfer limit using its unique ``transferLimitId``.

        Args:
            id: The unique identifier of the balance platform.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{id}/transferLimits/{transferLimitId}"),
            path_params=[param[str]("id", id), param[str]("transferLimitId", transfer_limit_id)],
            decoder=json_decoder[TransferLimit],
            error_mapper=get_balance_platforms_id_transfer_limits_transfer_limit_id_error_mapper,
            request_options=request_options,
        )

    def post_balance_platforms_id_transfer_limits(
        self,
        id: str,
        body: CreateTransferLimitRequest | CreateTransferLimitRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferLimit, PostBalancePlatformsIdTransferLimitsErrorBody]:
        """Create a transfer limit for your balance platform using the unique ``id`` of your balance platform.

        Args:
            id: The unique identifier of the balance platform.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balancePlatforms/{id}/transferLimits"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTransferLimitRequest | CreateTransferLimitRequestDict](body),
            decoder=json_decoder[TransferLimit],
            error_mapper=post_balance_platforms_id_transfer_limits_error_mapper,
            request_options=request_options,
        )


class AsyncTransferLimitsBalancePlatformLevelWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def delete_balance_platforms_id_transfer_limits_transfer_limit_id(
        self, id: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody]:
        """Delete a scheduled or pending transfer limit using its unique ``transferLimitId``. You cannot delete an
        active limit.

        Args:
            id: The unique identifier of the balance platform.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/balancePlatforms/{id}/transferLimits/{transferLimitId}"),
            path_params=[param[str]("id", id), param[str]("transferLimitId", transfer_limit_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=delete_balance_platforms_id_transfer_limits_transfer_limit_id_error_mapper,
            request_options=request_options,
        )

    async def get_balance_platforms_id_transfer_limits(
        self,
        id: str,
        *,
        scope: ScopeOrStr | None = None,
        transfer_type: TransferTypeOrStr | None = None,
        status: LimitStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferLimitListResponse, GetBalancePlatformsIdTransferLimitsErrorBody]:
        """Filter and view the transfer limits configured for your balance platform using the balance platform's unique
        ``id`` and the available query parameters.

        Args:
            id: The unique identifier of the balance platform.
            scope: The scope to which the transfer limit applies. Possible values: * **perTransaction**: you set a
                maximum amount for each transfer made from the balance account or balance platform. * **perDay**: you
                set a maximum total amount for all transfers made from the balance account or balance platform in a day.
            transfer_type: The type of transfer to which the limit applies. Possible values: * **instant**: the limit
                applies to transfers with an **instant** priority. * **all**: the limit applies to all transfers,
                regardless of priority.
            status: The status of the transfer limit. Possible values: * **active**: the limit is currently active. *
                **inactive**: the limit is currently inactive. * **pendingSCA**: the limit is pending until your user
                performs SCA. * **scheduled**: the limit is scheduled to become active at a future date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{id}/transferLimits"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[ScopeOrStr | None]("scope", scope),
                param[TransferTypeOrStr | None]("transferType", transfer_type),
                param[LimitStatusOrStr | None]("status", status),
            ],
            decoder=json_decoder[TransferLimitListResponse],
            error_mapper=get_balance_platforms_id_transfer_limits_error_mapper,
            request_options=request_options,
        )

    async def get_balance_platforms_id_transfer_limits_transfer_limit_id(
        self, id: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransferLimit, GetBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody]:
        """Get the details of a transfer limit using its unique ``transferLimitId``.

        Args:
            id: The unique identifier of the balance platform.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{id}/transferLimits/{transferLimitId}"),
            path_params=[param[str]("id", id), param[str]("transferLimitId", transfer_limit_id)],
            decoder=json_decoder[TransferLimit],
            error_mapper=get_balance_platforms_id_transfer_limits_transfer_limit_id_error_mapper,
            request_options=request_options,
        )

    async def post_balance_platforms_id_transfer_limits(
        self,
        id: str,
        body: CreateTransferLimitRequest | CreateTransferLimitRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferLimit, PostBalancePlatformsIdTransferLimitsErrorBody]:
        """Create a transfer limit for your balance platform using the unique ``id`` of your balance platform.

        Args:
            id: The unique identifier of the balance platform.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balancePlatforms/{id}/transferLimits"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTransferLimitRequest | CreateTransferLimitRequestDict](body),
            decoder=json_decoder[TransferLimit],
            error_mapper=post_balance_platforms_id_transfer_limits_error_mapper,
            request_options=request_options,
        )
