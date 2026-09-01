from __future__ import annotations

from typing import Any
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
from ..errors.delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id_error import (
    DeleteBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody,
    delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id_error_mapper,
)
from ..errors.get_balance_accounts_balance_account_id_recurring_top_ups_error import (
    GetBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody,
    get_balance_accounts_balance_account_id_recurring_top_ups_error_mapper,
)
from ..errors.patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id_error import (
    PatchBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody,
    patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id_error_mapper,
)
from ..errors.post_balance_accounts_balance_account_id_recurring_top_ups_error import (
    PostBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody,
    post_balance_accounts_balance_account_id_recurring_top_ups_error_mapper,
)
from ..models.create_recurring_top_up import CreateRecurringTopUp, CreateRecurringTopUpDict
from ..models.patchable_create_recurring_top_up import PatchableCreateRecurringTopUp, PatchableCreateRecurringTopUpDict
from ..models.recurring_top_up import RecurringTopUp
from ..models.recurring_top_ups_result import RecurringTopUpsResult
from ..server.server import Server


class RecurringTopUps:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = RecurringTopUpsWithRawResponse(client, server)

    def delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
        self, balance_account_id: str, top_up_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Delete a recurring top up configuration by ``topUpId``.

        For more information, refer to `Manage recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            top_up_id: The unique identifier of the recurring top-up you want to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - the request has been successfully processed, but there is no additional content.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the recurring top up
                was not found Unprocessable Entity - a request validation error. Internal Server Error - the server
                could not process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
            balance_account_id, top_up_id, request_options=request_options
        ).unwrap()

    def get_balance_accounts_balance_account_id_recurring_top_ups(
        self,
        balance_account_id: str,
        *,
        limit: int | None = 10,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringTopUpsResult:
        """View all recurring top ups configured for a specific ``balanceAccountId``.

        For more information, refer to `Manage recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            limit: The number of items to return per page. Value must be between 1 and 100.
            cursor: The cursor used for pagination. Required if you want to see the next or previous page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the recurring top up was not found Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_balance_accounts_balance_account_id_recurring_top_ups(
            balance_account_id, limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
        self,
        balance_account_id: str,
        top_up_id: str,
        body: PatchableCreateRecurringTopUp | PatchableCreateRecurringTopUpDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringTopUp:
        """Update the configuration of an existing recurring top up.

        For more information, refer to `Manage recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            top_up_id: The unique identifier of the recurring top-up you want to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
            balance_account_id, top_up_id, body, request_options=request_options
        ).unwrap()

    def post_balance_accounts_balance_account_id_recurring_top_ups(
        self,
        balance_account_id: str,
        body: CreateRecurringTopUp | CreateRecurringTopUpDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringTopUp:
        """Create a recurring top up configuration.

        For more information, refer to `Create recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/create-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.post_balance_accounts_balance_account_id_recurring_top_ups(
            balance_account_id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> RecurringTopUpsWithRawResponse:
        return self._with_raw_response


class AsyncRecurringTopUps:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncRecurringTopUpsWithRawResponse(client, server)

    async def delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
        self, balance_account_id: str, top_up_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Delete a recurring top up configuration by ``topUpId``.

        For more information, refer to `Manage recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            top_up_id: The unique identifier of the recurring top-up you want to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - the request has been successfully processed, but there is no additional content.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Not Found - the recurring top up
                was not found Unprocessable Entity - a request validation error. Internal Server Error - the server
                could not process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
                balance_account_id, top_up_id, request_options=request_options
            )
        ).unwrap()

    async def get_balance_accounts_balance_account_id_recurring_top_ups(
        self,
        balance_account_id: str,
        *,
        limit: int | None = 10,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringTopUpsResult:
        """View all recurring top ups configured for a specific ``balanceAccountId``.

        For more information, refer to `Manage recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            limit: The number of items to return per page. Value must be between 1 and 100.
            cursor: The cursor used for pagination. Required if you want to see the next or previous page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the recurring top up was not found Internal Server Error - the server could not
                process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_balance_accounts_balance_account_id_recurring_top_ups(
                balance_account_id, limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
        self,
        balance_account_id: str,
        top_up_id: str,
        body: PatchableCreateRecurringTopUp | PatchableCreateRecurringTopUpDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringTopUp:
        """Update the configuration of an existing recurring top up.

        For more information, refer to `Manage recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            top_up_id: The unique identifier of the recurring top-up you want to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
                balance_account_id, top_up_id, body, request_options=request_options
            )
        ).unwrap()

    async def post_balance_accounts_balance_account_id_recurring_top_ups(
        self,
        balance_account_id: str,
        body: CreateRecurringTopUp | CreateRecurringTopUpDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecurringTopUp:
        """Create a recurring top up configuration.

        For more information, refer to `Create recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/create-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.post_balance_accounts_balance_account_id_recurring_top_ups(
                balance_account_id, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncRecurringTopUpsWithRawResponse:
        return self._with_raw_response


class RecurringTopUpsWithRawResponse(BaseRawResponse[RawClient, Server]):
    def delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
        self, balance_account_id: str, top_up_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, DeleteBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody]:
        """Delete a recurring top up configuration by ``topUpId``.

        For more information, refer to `Manage recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            top_up_id: The unique identifier of the recurring top-up you want to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("topUpId", top_up_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[Any],
            error_mapper=delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id_error_mapper,
            request_options=request_options,
        )

    def get_balance_accounts_balance_account_id_recurring_top_ups(
        self,
        balance_account_id: str,
        *,
        limit: int | None = 10,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringTopUpsResult, GetBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody]:
        """View all recurring top ups configured for a specific ``balanceAccountId``.

        For more information, refer to `Manage recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            limit: The number of items to return per page. Value must be between 1 and 100.
            cursor: The cursor used for pagination. Required if you want to see the next or previous page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/recurringTopUps"),
            path_params=[param[str]("balanceAccountId", balance_account_id)],
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            decoder=json_decoder[RecurringTopUpsResult],
            error_mapper=get_balance_accounts_balance_account_id_recurring_top_ups_error_mapper,
            request_options=request_options,
        )

    def patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
        self,
        balance_account_id: str,
        top_up_id: str,
        body: PatchableCreateRecurringTopUp | PatchableCreateRecurringTopUpDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringTopUp, PatchBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody]:
        """Update the configuration of an existing recurring top up.

        For more information, refer to `Manage recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            top_up_id: The unique identifier of the recurring top-up you want to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("topUpId", top_up_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PatchableCreateRecurringTopUp | PatchableCreateRecurringTopUpDict](body),
            decoder=json_decoder[RecurringTopUp],
            error_mapper=patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id_error_mapper,
            request_options=request_options,
        )

    def post_balance_accounts_balance_account_id_recurring_top_ups(
        self,
        balance_account_id: str,
        body: CreateRecurringTopUp | CreateRecurringTopUpDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringTopUp, PostBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody]:
        """Create a recurring top up configuration.

        For more information, refer to `Create recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/create-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/recurringTopUps"),
            path_params=[param[str]("balanceAccountId", balance_account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateRecurringTopUp | CreateRecurringTopUpDict](body),
            decoder=json_decoder[RecurringTopUp],
            error_mapper=post_balance_accounts_balance_account_id_recurring_top_ups_error_mapper,
            request_options=request_options,
        )


class AsyncRecurringTopUpsWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
        self, balance_account_id: str, top_up_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, DeleteBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody]:
        """Delete a recurring top up configuration by ``topUpId``.

        For more information, refer to `Manage recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            top_up_id: The unique identifier of the recurring top-up you want to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("topUpId", top_up_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[Any],
            error_mapper=delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id_error_mapper,
            request_options=request_options,
        )

    async def get_balance_accounts_balance_account_id_recurring_top_ups(
        self,
        balance_account_id: str,
        *,
        limit: int | None = 10,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringTopUpsResult, GetBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody]:
        """View all recurring top ups configured for a specific ``balanceAccountId``.

        For more information, refer to `Manage recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            limit: The number of items to return per page. Value must be between 1 and 100.
            cursor: The cursor used for pagination. Required if you want to see the next or previous page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/recurringTopUps"),
            path_params=[param[str]("balanceAccountId", balance_account_id)],
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            decoder=json_decoder[RecurringTopUpsResult],
            error_mapper=get_balance_accounts_balance_account_id_recurring_top_ups_error_mapper,
            request_options=request_options,
        )

    async def patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
        self,
        balance_account_id: str,
        top_up_id: str,
        body: PatchableCreateRecurringTopUp | PatchableCreateRecurringTopUpDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringTopUp, PatchBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody]:
        """Update the configuration of an existing recurring top up.

        For more information, refer to `Manage recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            top_up_id: The unique identifier of the recurring top-up you want to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("topUpId", top_up_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PatchableCreateRecurringTopUp | PatchableCreateRecurringTopUpDict](body),
            decoder=json_decoder[RecurringTopUp],
            error_mapper=patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id_error_mapper,
            request_options=request_options,
        )

    async def post_balance_accounts_balance_account_id_recurring_top_ups(
        self,
        balance_account_id: str,
        body: CreateRecurringTopUp | CreateRecurringTopUpDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecurringTopUp, PostBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody]:
        """Create a recurring top up configuration.

        For more information, refer to `Create recurring top-ups
        <https://docs.adyen.com/issuing/add-manage-funds/top-ups/create-recurring-top-ups>`__.

        Args:
            balance_account_id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/recurringTopUps"),
            path_params=[param[str]("balanceAccountId", balance_account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateRecurringTopUp | CreateRecurringTopUpDict](body),
            decoder=json_decoder[RecurringTopUp],
            error_mapper=post_balance_accounts_balance_account_id_recurring_top_ups_error_mapper,
            request_options=request_options,
        )
