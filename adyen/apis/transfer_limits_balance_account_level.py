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
from ..errors.delete_balance_accounts_id_transfer_limits_transfer_limit_id_error import (
    DeleteBalanceAccountsIdTransferLimitsTransferLimitIdErrorBody,
    delete_balance_accounts_id_transfer_limits_transfer_limit_id_error_mapper,
)
from ..errors.get_balance_accounts_id_transfer_limits_current_error import (
    GetBalanceAccountsIdTransferLimitsCurrentErrorBody,
    get_balance_accounts_id_transfer_limits_current_error_mapper,
)
from ..errors.get_balance_accounts_id_transfer_limits_error import (
    GetBalanceAccountsIdTransferLimitsErrorBody,
    get_balance_accounts_id_transfer_limits_error_mapper,
)
from ..errors.get_balance_accounts_id_transfer_limits_transfer_limit_id_error import (
    GetBalanceAccountsIdTransferLimitsTransferLimitIdErrorBody,
    get_balance_accounts_id_transfer_limits_transfer_limit_id_error_mapper,
)
from ..errors.post_balance_accounts_id_transfer_limits_approve_error import (
    PostBalanceAccountsIdTransferLimitsApproveErrorBody,
    post_balance_accounts_id_transfer_limits_approve_error_mapper,
)
from ..errors.post_balance_accounts_id_transfer_limits_error import (
    PostBalanceAccountsIdTransferLimitsErrorBody,
    post_balance_accounts_id_transfer_limits_error_mapper,
)
from ..models.approve_transfer_limit_request import ApproveTransferLimitRequest, ApproveTransferLimitRequestDict
from ..models.create_transfer_limit_request import CreateTransferLimitRequest, CreateTransferLimitRequestDict
from ..models.enums.limit_status import LimitStatusOrStr
from ..models.enums.scope import ScopeOrStr
from ..models.enums.transfer_type import TransferTypeOrStr
from ..models.transfer_limit import TransferLimit
from ..models.transfer_limit_list_response import TransferLimitListResponse
from ..server.server import Server


class TransferLimitsBalanceAccountLevel:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = TransferLimitsBalanceAccountLevelWithRawResponse(client, server)

    def delete_balance_accounts_id_transfer_limits_transfer_limit_id(
        self, id_: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a scheduled or pending transfer limit using its unique ``transferLimitId``. You cannot delete an
        active limit.

        Args:
            id_: The unique identifier of the balance account.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.delete_balance_accounts_id_transfer_limits_transfer_limit_id(
                id_, transfer_limit_id, request_options=request_options
            ),
        )

    def get_balance_accounts_id_transfer_limits(
        self,
        id_: str,
        *,
        scope: ScopeOrStr | None = None,
        transfer_type: TransferTypeOrStr | None = None,
        status: LimitStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferLimitListResponse:
        """Filter and view the transfer limits configured for a balance account using the balance account's unique
        ``id`` and the available query parameters.

        Args:
            id_: The unique identifier of the balance account.
            scope: The scope to which the transfer limit applies. Possible values: * **perTransaction**: you set a
                maximum amount for each transfer made from the balance account or balance platform. * **perDay**: you
                set a maximum total amount for all transfers made from the balance account or balance platform in a day.
            transfer_type: The type of transfer to which the limit applies. Possible values: * **instant**: the limit
                applies to transfers with an **instant** priority. * **all**: the limit applies to all transfers,
                regardless of priority.
            status: The status of the transfer limit. Possible values: * **active**: the limit is currently active. *
                **inactive**: the limit is currently inactive. * **pendingSCA**: the limit is pending until your user
                performs SCA. * **scheduled**: the limit is scheduled to become active at a future date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.get_balance_accounts_id_transfer_limits(
                id_, scope=scope, transfer_type=transfer_type, status=status, request_options=request_options
            ),
        )

    def get_balance_accounts_id_transfer_limits_current(
        self,
        id_: str,
        *,
        scope: ScopeOrStr | None = None,
        transfer_type: TransferTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferLimitListResponse:
        """Get all transfer limits that currently apply to a balance account using the unique ``id`` of the balance
        account.

        Args:
            id_: The unique identifier of the balance account.
            scope: The scope to which the transfer limit applies. Possible values: * **perTransaction**: you set a
                maximum amount for each transfer made from the balance account or balance platform. * **perDay**: you
                set a maximum total amount for all transfers made from the balance account or balance platform in a day.
            transfer_type: The type of transfer to which the limit applies. Possible values: * **instant**: the limit
                applies to transfers with an **instant** priority. * **all**: the limit applies to all transfers,
                regardless of priority.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.get_balance_accounts_id_transfer_limits_current(
                id_, scope=scope, transfer_type=transfer_type, request_options=request_options
            ),
        )

    def get_balance_accounts_id_transfer_limits_transfer_limit_id(
        self, id_: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransferLimit:
        """Get the details of a transfer limit using its unique ``transferLimitId``.

        Args:
            id_: The unique identifier of the balance account.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.get_balance_accounts_id_transfer_limits_transfer_limit_id(
                id_, transfer_limit_id, request_options=request_options
            ),
        )

    def post_balance_accounts_id_transfer_limits(
        self,
        id_: str,
        body: CreateTransferLimitRequest | CreateTransferLimitRequestDict,
        *,
        www_authenticate: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferLimit:
        """Create a transfer limit for your balance account using the unique ``id`` of your balance account.

        Args:
            id_: The unique identifier of the balance account.
            body: The request body.
            www_authenticate: Header for authenticating through SCA
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The input is invalid, or no registered device for SCA was found. Unauthorized -
                Authentication required via Strong Customer Authentication (SCA). The client must resolve the provided
                challenge. Unprocessable Content - A request validation error. ``error`` is ``DefaultErrorResponseEntity
                | RawError``."""
        return unwrap(
            self._with_raw_response.post_balance_accounts_id_transfer_limits(
                id_, body, www_authenticate=www_authenticate, request_options=request_options
            ),
        )

    def post_balance_accounts_id_transfer_limits_approve(
        self,
        id_: str,
        body: ApproveTransferLimitRequest | ApproveTransferLimitRequestDict,
        *,
        www_authenticate: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Approve transfer limits that are pending SCA authentication.

        Args:
            id_: The unique identifier of the balance account.
            body: The request body.
            www_authenticate: Header for authenticating using SCA.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - The request has succeeded.

        Raises:
            ApiError: Unauthorized - Authentication required via Strong Customer Authentication (SCA). The client must
                resolve the provided challenge. Not found - One of the transfer limits could not be found. Unprocessable
                Content - A request validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.post_balance_accounts_id_transfer_limits_approve(
                id_, body, www_authenticate=www_authenticate, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> TransferLimitsBalanceAccountLevelWithRawResponse:
        return self._with_raw_response


class AsyncTransferLimitsBalanceAccountLevel:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncTransferLimitsBalanceAccountLevelWithRawResponse(client, server)

    async def delete_balance_accounts_id_transfer_limits_transfer_limit_id(
        self, id_: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a scheduled or pending transfer limit using its unique ``transferLimitId``. You cannot delete an
        active limit.

        Args:
            id_: The unique identifier of the balance account.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_balance_accounts_id_transfer_limits_transfer_limit_id(
                id_, transfer_limit_id, request_options=request_options
            ),
        )

    async def get_balance_accounts_id_transfer_limits(
        self,
        id_: str,
        *,
        scope: ScopeOrStr | None = None,
        transfer_type: TransferTypeOrStr | None = None,
        status: LimitStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferLimitListResponse:
        """Filter and view the transfer limits configured for a balance account using the balance account's unique
        ``id`` and the available query parameters.

        Args:
            id_: The unique identifier of the balance account.
            scope: The scope to which the transfer limit applies. Possible values: * **perTransaction**: you set a
                maximum amount for each transfer made from the balance account or balance platform. * **perDay**: you
                set a maximum total amount for all transfers made from the balance account or balance platform in a day.
            transfer_type: The type of transfer to which the limit applies. Possible values: * **instant**: the limit
                applies to transfers with an **instant** priority. * **all**: the limit applies to all transfers,
                regardless of priority.
            status: The status of the transfer limit. Possible values: * **active**: the limit is currently active. *
                **inactive**: the limit is currently inactive. * **pendingSCA**: the limit is pending until your user
                performs SCA. * **scheduled**: the limit is scheduled to become active at a future date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.get_balance_accounts_id_transfer_limits(
                id_, scope=scope, transfer_type=transfer_type, status=status, request_options=request_options
            ),
        )

    async def get_balance_accounts_id_transfer_limits_current(
        self,
        id_: str,
        *,
        scope: ScopeOrStr | None = None,
        transfer_type: TransferTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferLimitListResponse:
        """Get all transfer limits that currently apply to a balance account using the unique ``id`` of the balance
        account.

        Args:
            id_: The unique identifier of the balance account.
            scope: The scope to which the transfer limit applies. Possible values: * **perTransaction**: you set a
                maximum amount for each transfer made from the balance account or balance platform. * **perDay**: you
                set a maximum total amount for all transfers made from the balance account or balance platform in a day.
            transfer_type: The type of transfer to which the limit applies. Possible values: * **instant**: the limit
                applies to transfers with an **instant** priority. * **all**: the limit applies to all transfers,
                regardless of priority.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.get_balance_accounts_id_transfer_limits_current(
                id_, scope=scope, transfer_type=transfer_type, request_options=request_options
            ),
        )

    async def get_balance_accounts_id_transfer_limits_transfer_limit_id(
        self, id_: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransferLimit:
        """Get the details of a transfer limit using its unique ``transferLimitId``.

        Args:
            id_: The unique identifier of the balance account.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not found - One of the transfer limits could not be found. Unprocessable Content - A request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.get_balance_accounts_id_transfer_limits_transfer_limit_id(
                id_, transfer_limit_id, request_options=request_options
            ),
        )

    async def post_balance_accounts_id_transfer_limits(
        self,
        id_: str,
        body: CreateTransferLimitRequest | CreateTransferLimitRequestDict,
        *,
        www_authenticate: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferLimit:
        """Create a transfer limit for your balance account using the unique ``id`` of your balance account.

        Args:
            id_: The unique identifier of the balance account.
            body: The request body.
            www_authenticate: Header for authenticating through SCA
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The input is invalid, or no registered device for SCA was found. Unauthorized -
                Authentication required via Strong Customer Authentication (SCA). The client must resolve the provided
                challenge. Unprocessable Content - A request validation error. ``error`` is ``DefaultErrorResponseEntity
                | RawError``."""
        return unwrap(
            await self._with_raw_response.post_balance_accounts_id_transfer_limits(
                id_, body, www_authenticate=www_authenticate, request_options=request_options
            ),
        )

    async def post_balance_accounts_id_transfer_limits_approve(
        self,
        id_: str,
        body: ApproveTransferLimitRequest | ApproveTransferLimitRequestDict,
        *,
        www_authenticate: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Approve transfer limits that are pending SCA authentication.

        Args:
            id_: The unique identifier of the balance account.
            body: The request body.
            www_authenticate: Header for authenticating using SCA.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - The request has succeeded.

        Raises:
            ApiError: Unauthorized - Authentication required via Strong Customer Authentication (SCA). The client must
                resolve the provided challenge. Not found - One of the transfer limits could not be found. Unprocessable
                Content - A request validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.post_balance_accounts_id_transfer_limits_approve(
                id_, body, www_authenticate=www_authenticate, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncTransferLimitsBalanceAccountLevelWithRawResponse:
        return self._with_raw_response


class TransferLimitsBalanceAccountLevelWithRawResponse(BaseRawResponse[RawClient, Server]):
    def delete_balance_accounts_id_transfer_limits_transfer_limit_id(
        self, id_: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteBalanceAccountsIdTransferLimitsTransferLimitIdErrorBody]:
        """Delete a scheduled or pending transfer limit using its unique ``transferLimitId``. You cannot delete an
        active limit.

        Args:
            id_: The unique identifier of the balance account.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/balanceAccounts/{id}/transferLimits/{transferLimitId}"),
            path_params=[param[str]("id", id_), param[str]("transferLimitId", transfer_limit_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=delete_balance_accounts_id_transfer_limits_transfer_limit_id_error_mapper,
            request_options=request_options,
        )

    def get_balance_accounts_id_transfer_limits(
        self,
        id_: str,
        *,
        scope: ScopeOrStr | None = None,
        transfer_type: TransferTypeOrStr | None = None,
        status: LimitStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferLimitListResponse, GetBalanceAccountsIdTransferLimitsErrorBody]:
        """Filter and view the transfer limits configured for a balance account using the balance account's unique
        ``id`` and the available query parameters.

        Args:
            id_: The unique identifier of the balance account.
            scope: The scope to which the transfer limit applies. Possible values: * **perTransaction**: you set a
                maximum amount for each transfer made from the balance account or balance platform. * **perDay**: you
                set a maximum total amount for all transfers made from the balance account or balance platform in a day.
            transfer_type: The type of transfer to which the limit applies. Possible values: * **instant**: the limit
                applies to transfers with an **instant** priority. * **all**: the limit applies to all transfers,
                regardless of priority.
            status: The status of the transfer limit. Possible values: * **active**: the limit is currently active. *
                **inactive**: the limit is currently inactive. * **pendingSCA**: the limit is pending until your user
                performs SCA. * **scheduled**: the limit is scheduled to become active at a future date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{id}/transferLimits"),
            path_params=[param[str]("id", id_)],
            query_params=[
                param[ScopeOrStr | None]("scope", scope),
                param[TransferTypeOrStr | None]("transferType", transfer_type),
                param[LimitStatusOrStr | None]("status", status),
            ],
            decoder=json_decoder[TransferLimitListResponse],
            error_mapper=get_balance_accounts_id_transfer_limits_error_mapper,
            request_options=request_options,
        )

    def get_balance_accounts_id_transfer_limits_current(
        self,
        id_: str,
        *,
        scope: ScopeOrStr | None = None,
        transfer_type: TransferTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferLimitListResponse, GetBalanceAccountsIdTransferLimitsCurrentErrorBody]:
        """Get all transfer limits that currently apply to a balance account using the unique ``id`` of the balance
        account.

        Args:
            id_: The unique identifier of the balance account.
            scope: The scope to which the transfer limit applies. Possible values: * **perTransaction**: you set a
                maximum amount for each transfer made from the balance account or balance platform. * **perDay**: you
                set a maximum total amount for all transfers made from the balance account or balance platform in a day.
            transfer_type: The type of transfer to which the limit applies. Possible values: * **instant**: the limit
                applies to transfers with an **instant** priority. * **all**: the limit applies to all transfers,
                regardless of priority.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{id}/transferLimits/current"),
            path_params=[param[str]("id", id_)],
            query_params=[
                param[ScopeOrStr | None]("scope", scope), param[TransferTypeOrStr | None]("transferType", transfer_type)
            ],
            decoder=json_decoder[TransferLimitListResponse],
            error_mapper=get_balance_accounts_id_transfer_limits_current_error_mapper,
            request_options=request_options,
        )

    def get_balance_accounts_id_transfer_limits_transfer_limit_id(
        self, id_: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransferLimit, GetBalanceAccountsIdTransferLimitsTransferLimitIdErrorBody]:
        """Get the details of a transfer limit using its unique ``transferLimitId``.

        Args:
            id_: The unique identifier of the balance account.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{id}/transferLimits/{transferLimitId}"),
            path_params=[param[str]("id", id_), param[str]("transferLimitId", transfer_limit_id)],
            decoder=json_decoder[TransferLimit],
            error_mapper=get_balance_accounts_id_transfer_limits_transfer_limit_id_error_mapper,
            request_options=request_options,
        )

    def post_balance_accounts_id_transfer_limits(
        self,
        id_: str,
        body: CreateTransferLimitRequest | CreateTransferLimitRequestDict,
        *,
        www_authenticate: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferLimit, PostBalanceAccountsIdTransferLimitsErrorBody]:
        """Create a transfer limit for your balance account using the unique ``id`` of your balance account.

        Args:
            id_: The unique identifier of the balance account.
            body: The request body.
            www_authenticate: Header for authenticating through SCA
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balanceAccounts/{id}/transferLimits"),
            path_params=[param[str]("id", id_)],
            headers=[param[str | None]("WWW-Authenticate", www_authenticate), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTransferLimitRequest | CreateTransferLimitRequestDict](body),
            decoder=json_decoder[TransferLimit],
            error_mapper=post_balance_accounts_id_transfer_limits_error_mapper,
            request_options=request_options,
        )

    def post_balance_accounts_id_transfer_limits_approve(
        self,
        id_: str,
        body: ApproveTransferLimitRequest | ApproveTransferLimitRequestDict,
        *,
        www_authenticate: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PostBalanceAccountsIdTransferLimitsApproveErrorBody]:
        """Approve transfer limits that are pending SCA authentication.

        Args:
            id_: The unique identifier of the balance account.
            body: The request body.
            www_authenticate: Header for authenticating using SCA.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balanceAccounts/{id}/transferLimits/approve"),
            path_params=[param[str]("id", id_)],
            headers=[param[str | None]("WWW-Authenticate", www_authenticate), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ApproveTransferLimitRequest | ApproveTransferLimitRequestDict](body),
            decoder=empty_response,
            error_mapper=post_balance_accounts_id_transfer_limits_approve_error_mapper,
            request_options=request_options,
        )


class AsyncTransferLimitsBalanceAccountLevelWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def delete_balance_accounts_id_transfer_limits_transfer_limit_id(
        self, id_: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteBalanceAccountsIdTransferLimitsTransferLimitIdErrorBody]:
        """Delete a scheduled or pending transfer limit using its unique ``transferLimitId``. You cannot delete an
        active limit.

        Args:
            id_: The unique identifier of the balance account.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/balanceAccounts/{id}/transferLimits/{transferLimitId}"),
            path_params=[param[str]("id", id_), param[str]("transferLimitId", transfer_limit_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=async_empty_response,
            error_mapper=delete_balance_accounts_id_transfer_limits_transfer_limit_id_error_mapper,
            request_options=request_options,
        )

    async def get_balance_accounts_id_transfer_limits(
        self,
        id_: str,
        *,
        scope: ScopeOrStr | None = None,
        transfer_type: TransferTypeOrStr | None = None,
        status: LimitStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferLimitListResponse, GetBalanceAccountsIdTransferLimitsErrorBody]:
        """Filter and view the transfer limits configured for a balance account using the balance account's unique
        ``id`` and the available query parameters.

        Args:
            id_: The unique identifier of the balance account.
            scope: The scope to which the transfer limit applies. Possible values: * **perTransaction**: you set a
                maximum amount for each transfer made from the balance account or balance platform. * **perDay**: you
                set a maximum total amount for all transfers made from the balance account or balance platform in a day.
            transfer_type: The type of transfer to which the limit applies. Possible values: * **instant**: the limit
                applies to transfers with an **instant** priority. * **all**: the limit applies to all transfers,
                regardless of priority.
            status: The status of the transfer limit. Possible values: * **active**: the limit is currently active. *
                **inactive**: the limit is currently inactive. * **pendingSCA**: the limit is pending until your user
                performs SCA. * **scheduled**: the limit is scheduled to become active at a future date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{id}/transferLimits"),
            path_params=[param[str]("id", id_)],
            query_params=[
                param[ScopeOrStr | None]("scope", scope),
                param[TransferTypeOrStr | None]("transferType", transfer_type),
                param[LimitStatusOrStr | None]("status", status),
            ],
            decoder=async_json_decoder[TransferLimitListResponse],
            error_mapper=get_balance_accounts_id_transfer_limits_error_mapper,
            request_options=request_options,
        )

    async def get_balance_accounts_id_transfer_limits_current(
        self,
        id_: str,
        *,
        scope: ScopeOrStr | None = None,
        transfer_type: TransferTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferLimitListResponse, GetBalanceAccountsIdTransferLimitsCurrentErrorBody]:
        """Get all transfer limits that currently apply to a balance account using the unique ``id`` of the balance
        account.

        Args:
            id_: The unique identifier of the balance account.
            scope: The scope to which the transfer limit applies. Possible values: * **perTransaction**: you set a
                maximum amount for each transfer made from the balance account or balance platform. * **perDay**: you
                set a maximum total amount for all transfers made from the balance account or balance platform in a day.
            transfer_type: The type of transfer to which the limit applies. Possible values: * **instant**: the limit
                applies to transfers with an **instant** priority. * **all**: the limit applies to all transfers,
                regardless of priority.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{id}/transferLimits/current"),
            path_params=[param[str]("id", id_)],
            query_params=[
                param[ScopeOrStr | None]("scope", scope), param[TransferTypeOrStr | None]("transferType", transfer_type)
            ],
            decoder=async_json_decoder[TransferLimitListResponse],
            error_mapper=get_balance_accounts_id_transfer_limits_current_error_mapper,
            request_options=request_options,
        )

    async def get_balance_accounts_id_transfer_limits_transfer_limit_id(
        self, id_: str, transfer_limit_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransferLimit, GetBalanceAccountsIdTransferLimitsTransferLimitIdErrorBody]:
        """Get the details of a transfer limit using its unique ``transferLimitId``.

        Args:
            id_: The unique identifier of the balance account.
            transfer_limit_id: The unique identifier of the transfer limit.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{id}/transferLimits/{transferLimitId}"),
            path_params=[param[str]("id", id_), param[str]("transferLimitId", transfer_limit_id)],
            decoder=async_json_decoder[TransferLimit],
            error_mapper=get_balance_accounts_id_transfer_limits_transfer_limit_id_error_mapper,
            request_options=request_options,
        )

    async def post_balance_accounts_id_transfer_limits(
        self,
        id_: str,
        body: CreateTransferLimitRequest | CreateTransferLimitRequestDict,
        *,
        www_authenticate: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferLimit, PostBalanceAccountsIdTransferLimitsErrorBody]:
        """Create a transfer limit for your balance account using the unique ``id`` of your balance account.

        Args:
            id_: The unique identifier of the balance account.
            body: The request body.
            www_authenticate: Header for authenticating through SCA
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balanceAccounts/{id}/transferLimits"),
            path_params=[param[str]("id", id_)],
            headers=[param[str | None]("WWW-Authenticate", www_authenticate), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTransferLimitRequest | CreateTransferLimitRequestDict](body),
            decoder=async_json_decoder[TransferLimit],
            error_mapper=post_balance_accounts_id_transfer_limits_error_mapper,
            request_options=request_options,
        )

    async def post_balance_accounts_id_transfer_limits_approve(
        self,
        id_: str,
        body: ApproveTransferLimitRequest | ApproveTransferLimitRequestDict,
        *,
        www_authenticate: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PostBalanceAccountsIdTransferLimitsApproveErrorBody]:
        """Approve transfer limits that are pending SCA authentication.

        Args:
            id_: The unique identifier of the balance account.
            body: The request body.
            www_authenticate: Header for authenticating using SCA.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balanceAccounts/{id}/transferLimits/approve"),
            path_params=[param[str]("id", id_)],
            headers=[param[str | None]("WWW-Authenticate", www_authenticate), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ApproveTransferLimitRequest | ApproveTransferLimitRequestDict](body),
            decoder=async_empty_response,
            error_mapper=post_balance_accounts_id_transfer_limits_approve_error_mapper,
            request_options=request_options,
        )
