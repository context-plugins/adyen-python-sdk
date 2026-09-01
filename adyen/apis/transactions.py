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
from ..errors.get_transactions_error import GetTransactionsErrorBody, get_transactions_error_mapper
from ..errors.get_transactions_id_error import GetTransactionsIdErrorBody, get_transactions_id_error_mapper
from ..models.enums.sort_order import SortOrderOrStr
from ..models.transaction import Transaction
from ..models.transaction_search_response import TransactionSearchResponse
from ..server.server import Server


class Transactions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TransactionsWithRawResponse(client, server, auth)

    def get_transactions(
        self,
        created_since: RFC3339DateTime,
        created_until: RFC3339DateTime,
        *,
        balance_platform: str | None = None,
        payment_instrument_id: str | None = None,
        account_holder_id: str | None = None,
        balance_account_id: str | None = None,
        cursor: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransactionSearchResponse:
        """>Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the
        latest version.

        Returns all the transactions related to a balance account, account holder, or balance platform.

        When making this request, you must include at least one of the following:
        - ``balanceAccountId``
        - ``accountHolderId``
        - ``balancePlatform``.

        This endpoint supports cursor-based pagination. The response returns the first page of results, and returns
        links to the next and previous pages when applicable. You can use the links to page through the results.

        Args:
            created_since: Only include transactions that have been created on or after this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            created_until: Only include transactions that have been created on or before this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            balance_platform: The unique identifier of the `balance platform
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``accountHolderId``.
            payment_instrument_id: The unique identifier of the `payment instrument
                <https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_>`__. To use this
                parameter, you must also provide a ``balanceAccountId``, ``accountHolderId``, or ``balancePlatform``.
                The ``paymentInstrumentId`` must be related to the ``balanceAccountId`` or ``accountHolderId`` that you
                provide.
            account_holder_id: The unique identifier of the `account holder
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/accountHolders/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``balancePlatform``. If you provide a
                ``balanceAccountId``, the ``accountHolderId`` must be related to the ``balanceAccountId``.
            balance_account_id: The unique identifier of the `balance account
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id>`__.
                Required if you don't provide an ``accountHolderId`` or ``balancePlatform``. If you provide an
                ``accountHolderId``, the ``balanceAccountId`` must be related to the ``accountHolderId``.
            cursor: The ``cursor`` returned in the links of the previous response.
            sort_order: Determines the sort order of the returned transactions. The sort order is based on the creation
                date of the transaction. Possible values: - **asc**: Ascending order, from oldest to most recent. -
                **desc**: Descending order, from most recent to oldest. Default value: **asc**.
            limit: The number of items returned per page, maximum of 100 items. By default, the response returns 10
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return self._with_raw_response.get_transactions(
            created_since,
            created_until,
            balance_platform=balance_platform,
            payment_instrument_id=payment_instrument_id,
            account_holder_id=account_holder_id,
            balance_account_id=balance_account_id,
            cursor=cursor,
            sort_order=sort_order,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    def get_transactions_id(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> Transaction:
        """>Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the
        latest version.

        Returns a transaction.

        Args:
            id: The unique identifier of the transaction.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return self._with_raw_response.get_transactions_id(id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> TransactionsWithRawResponse:
        return self._with_raw_response


class AsyncTransactions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTransactionsWithRawResponse(client, server, auth)

    async def get_transactions(
        self,
        created_since: RFC3339DateTime,
        created_until: RFC3339DateTime,
        *,
        balance_platform: str | None = None,
        payment_instrument_id: str | None = None,
        account_holder_id: str | None = None,
        balance_account_id: str | None = None,
        cursor: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransactionSearchResponse:
        """>Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the
        latest version.

        Returns all the transactions related to a balance account, account holder, or balance platform.

        When making this request, you must include at least one of the following:
        - ``balanceAccountId``
        - ``accountHolderId``
        - ``balancePlatform``.

        This endpoint supports cursor-based pagination. The response returns the first page of results, and returns
        links to the next and previous pages when applicable. You can use the links to page through the results.

        Args:
            created_since: Only include transactions that have been created on or after this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            created_until: Only include transactions that have been created on or before this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            balance_platform: The unique identifier of the `balance platform
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``accountHolderId``.
            payment_instrument_id: The unique identifier of the `payment instrument
                <https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_>`__. To use this
                parameter, you must also provide a ``balanceAccountId``, ``accountHolderId``, or ``balancePlatform``.
                The ``paymentInstrumentId`` must be related to the ``balanceAccountId`` or ``accountHolderId`` that you
                provide.
            account_holder_id: The unique identifier of the `account holder
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/accountHolders/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``balancePlatform``. If you provide a
                ``balanceAccountId``, the ``accountHolderId`` must be related to the ``balanceAccountId``.
            balance_account_id: The unique identifier of the `balance account
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id>`__.
                Required if you don't provide an ``accountHolderId`` or ``balancePlatform``. If you provide an
                ``accountHolderId``, the ``balanceAccountId`` must be related to the ``accountHolderId``.
            cursor: The ``cursor`` returned in the links of the previous response.
            sort_order: Determines the sort order of the returned transactions. The sort order is based on the creation
                date of the transaction. Possible values: - **asc**: Ascending order, from oldest to most recent. -
                **desc**: Descending order, from most recent to oldest. Default value: **asc**.
            limit: The number of items returned per page, maximum of 100 items. By default, the response returns 10
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_transactions(
                created_since,
                created_until,
                balance_platform=balance_platform,
                payment_instrument_id=payment_instrument_id,
                account_holder_id=account_holder_id,
                balance_account_id=balance_account_id,
                cursor=cursor,
                sort_order=sort_order,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    async def get_transactions_id(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> Transaction:
        """>Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the
        latest version.

        Returns a transaction.

        Args:
            id: The unique identifier of the transaction.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return (await self._with_raw_response.get_transactions_id(id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncTransactionsWithRawResponse:
        return self._with_raw_response


class TransactionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_transactions(
        self,
        created_since: RFC3339DateTime,
        created_until: RFC3339DateTime,
        *,
        balance_platform: str | None = None,
        payment_instrument_id: str | None = None,
        account_holder_id: str | None = None,
        balance_account_id: str | None = None,
        cursor: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransactionSearchResponse, GetTransactionsErrorBody]:
        """>Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the
        latest version.

        Returns all the transactions related to a balance account, account holder, or balance platform.

        When making this request, you must include at least one of the following:
        - ``balanceAccountId``
        - ``accountHolderId``
        - ``balancePlatform``.

        This endpoint supports cursor-based pagination. The response returns the first page of results, and returns
        links to the next and previous pages when applicable. You can use the links to page through the results.

        Args:
            created_since: Only include transactions that have been created on or after this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            created_until: Only include transactions that have been created on or before this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            balance_platform: The unique identifier of the `balance platform
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``accountHolderId``.
            payment_instrument_id: The unique identifier of the `payment instrument
                <https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_>`__. To use this
                parameter, you must also provide a ``balanceAccountId``, ``accountHolderId``, or ``balancePlatform``.
                The ``paymentInstrumentId`` must be related to the ``balanceAccountId`` or ``accountHolderId`` that you
                provide.
            account_holder_id: The unique identifier of the `account holder
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/accountHolders/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``balancePlatform``. If you provide a
                ``balanceAccountId``, the ``accountHolderId`` must be related to the ``balanceAccountId``.
            balance_account_id: The unique identifier of the `balance account
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id>`__.
                Required if you don't provide an ``accountHolderId`` or ``balancePlatform``. If you provide an
                ``accountHolderId``, the ``balanceAccountId`` must be related to the ``accountHolderId``.
            cursor: The ``cursor`` returned in the links of the previous response.
            sort_order: Determines the sort order of the returned transactions. The sort order is based on the creation
                date of the transaction. Possible values: - **asc**: Ascending order, from oldest to most recent. -
                **desc**: Descending order, from most recent to oldest. Default value: **asc**.
            limit: The number of items returned per page, maximum of 100 items. By default, the response returns 10
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/transactions"),
            query_params=[
                param[RFC3339DateTime]("createdSince", created_since),
                param[RFC3339DateTime]("createdUntil", created_until),
                param[str | None]("balancePlatform", balance_platform),
                param[str | None]("paymentInstrumentId", payment_instrument_id),
                param[str | None]("accountHolderId", account_holder_id),
                param[str | None]("balanceAccountId", balance_account_id),
                param[str | None]("cursor", cursor),
                param[SortOrderOrStr | None]("sortOrder", sort_order),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionSearchResponse],
            error_mapper=get_transactions_error_mapper,
            request_options=request_options,
        )

    def get_transactions_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Transaction, GetTransactionsIdErrorBody]:
        """>Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the
        latest version.

        Returns a transaction.

        Args:
            id: The unique identifier of the transaction.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/transactions/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Transaction],
            error_mapper=get_transactions_id_error_mapper,
            request_options=request_options,
        )


class AsyncTransactionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_transactions(
        self,
        created_since: RFC3339DateTime,
        created_until: RFC3339DateTime,
        *,
        balance_platform: str | None = None,
        payment_instrument_id: str | None = None,
        account_holder_id: str | None = None,
        balance_account_id: str | None = None,
        cursor: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransactionSearchResponse, GetTransactionsErrorBody]:
        """>Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the
        latest version.

        Returns all the transactions related to a balance account, account holder, or balance platform.

        When making this request, you must include at least one of the following:
        - ``balanceAccountId``
        - ``accountHolderId``
        - ``balancePlatform``.

        This endpoint supports cursor-based pagination. The response returns the first page of results, and returns
        links to the next and previous pages when applicable. You can use the links to page through the results.

        Args:
            created_since: Only include transactions that have been created on or after this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            created_until: Only include transactions that have been created on or before this point in time. The value
                must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**.
            balance_platform: The unique identifier of the `balance platform
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``accountHolderId``.
            payment_instrument_id: The unique identifier of the `payment instrument
                <https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_>`__. To use this
                parameter, you must also provide a ``balanceAccountId``, ``accountHolderId``, or ``balancePlatform``.
                The ``paymentInstrumentId`` must be related to the ``balanceAccountId`` or ``accountHolderId`` that you
                provide.
            account_holder_id: The unique identifier of the `account holder
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/accountHolders/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``balancePlatform``. If you provide a
                ``balanceAccountId``, the ``accountHolderId`` must be related to the ``balanceAccountId``.
            balance_account_id: The unique identifier of the `balance account
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id>`__.
                Required if you don't provide an ``accountHolderId`` or ``balancePlatform``. If you provide an
                ``accountHolderId``, the ``balanceAccountId`` must be related to the ``accountHolderId``.
            cursor: The ``cursor`` returned in the links of the previous response.
            sort_order: Determines the sort order of the returned transactions. The sort order is based on the creation
                date of the transaction. Possible values: - **asc**: Ascending order, from oldest to most recent. -
                **desc**: Descending order, from most recent to oldest. Default value: **asc**.
            limit: The number of items returned per page, maximum of 100 items. By default, the response returns 10
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/transactions"),
            query_params=[
                param[RFC3339DateTime]("createdSince", created_since),
                param[RFC3339DateTime]("createdUntil", created_until),
                param[str | None]("balancePlatform", balance_platform),
                param[str | None]("paymentInstrumentId", payment_instrument_id),
                param[str | None]("accountHolderId", account_holder_id),
                param[str | None]("balanceAccountId", balance_account_id),
                param[str | None]("cursor", cursor),
                param[SortOrderOrStr | None]("sortOrder", sort_order),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionSearchResponse],
            error_mapper=get_transactions_error_mapper,
            request_options=request_options,
        )

    async def get_transactions_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Transaction, GetTransactionsIdErrorBody]:
        """>Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the
        latest version.

        Returns a transaction.

        Args:
            id: The unique identifier of the transaction.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/transactions/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Transaction],
            error_mapper=get_transactions_id_error_mapper,
            request_options=request_options,
        )
