from __future__ import annotations

from typing import Any

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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.get_transfers_error import GetTransfersErrorBody, get_transfers_error_mapper
from ..errors.get_transfers_id_error import GetTransfersIdErrorBody, get_transfers_id_error_mapper
from ..errors.post_transfers_approve_error import PostTransfersApproveErrorBody, post_transfers_approve_error_mapper
from ..errors.post_transfers_cancel_error import PostTransfersCancelErrorBody, post_transfers_cancel_error_mapper
from ..errors.post_transfers_error import PostTransfersErrorBody, post_transfers_error_mapper
from ..errors.post_transfers_transfer_id_returns_error import (
    PostTransfersTransferIdReturnsErrorBody,
    post_transfers_transfer_id_returns_error_mapper,
)
from ..models.approve_transfers_request import ApproveTransfersRequest, ApproveTransfersRequestDict
from ..models.cancel_transfers_request import CancelTransfersRequest, CancelTransfersRequestDict
from ..models.enums.category2 import Category2OrStr
from ..models.enums.sort_order import SortOrderOrStr
from ..models.find_transfers_response import FindTransfersResponse
from ..models.return_transfer_request import ReturnTransferRequest, ReturnTransferRequestDict
from ..models.return_transfer_response import ReturnTransferResponse
from ..models.transfer import Transfer
from ..models.transfer_data import TransferData
from ..models.transfer_info import TransferInfo, TransferInfoDict
from ..server.server import Server


class Transfers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TransfersWithRawResponse(client, server, auth)

    def get_transfers(
        self,
        created_since: RFC3339DateTime,
        created_until: RFC3339DateTime,
        *,
        balance_platform: str | None = None,
        account_holder_id: str | None = None,
        balance_account_id: str | None = None,
        payment_instrument_id: str | None = None,
        reference: str | None = None,
        category: Category2OrStr | None = None,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FindTransfersResponse:
        """Returns all the transfers related to a balance account, account holder, or balance platform.

        When making this request, you must include at least one of the following:
        - ``balanceAccountId``
        - ``accountHolderId``
        - ``balancePlatform``.

        This endpoint supports cursor-based pagination. The response returns the first page of results, and returns
        links to the next and previous pages when applicable. You can use the links to page through the results.

        Args:
            created_since: Only include transfers that have been created on or after this point in time. The value must
                be in ISO 8601 format and not earlier than 6 months before the ``createdUntil`` date. For example,
                **2021-05-30T15:07:40Z**.
            created_until: Only include transfers that have been created on or before this point in time. The value must
                be in ISO 8601 format and not later than 6 months after the ``createdSince`` date. For example,
                **2021-05-30T15:07:40Z**.
            balance_platform: The unique identifier of the `balance platform
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``accountHolderId``.
            account_holder_id: The unique identifier of the `account holder
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/accountHolders/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``balancePlatform``. If you provide a
                ``balanceAccountId``, the ``accountHolderId`` must be related to the ``balanceAccountId``.
            balance_account_id: The unique identifier of the `balance account
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id>`__.
                Required if you don't provide an ``accountHolderId`` or ``balancePlatform``. If you provide an
                ``accountHolderId``, the ``balanceAccountId`` must be related to the ``accountHolderId``.
            payment_instrument_id: The unique identifier of the `payment instrument
                <https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_>`__. To use this
                parameter, you must also provide a ``balanceAccountId``, ``accountHolderId``, or ``balancePlatform``.
                The ``paymentInstrumentId`` must be related to the ``balanceAccountId`` or ``accountHolderId`` that you
                provide.
            reference: The reference you provided in the POST `/transfers
                <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__ request
            category: The category of the transfer. Possible values: - **bank**: A transfer involving a `transfer
                instrument
                <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id>`__ or
                a bank account. - **card**: A transfer involving a third-party card. - **internal**: A transfer between
                `balance accounts
                <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id>`__
                within your platform. - **issuedCard**: A transfer initiated by an Adyen-issued card. -
                **platformPayment**: Funds movements related to payments that are acquired for your users. - **topUp**:
                An incoming transfer initiated by your user to top up their balance account.
            sort_order: Determines the sort order of the returned transfers. The sort order is based on the creation
                date of the transfers. Possible values: - **asc**: Ascending order, from oldest to most recent. -
                **desc**: Descending order, from most recent to oldest. Default value: **asc**.
            cursor: The ``cursor`` returned in the links of the previous response.
            limit: The number of items returned per page, maximum of 100 items. By default, the response returns 10
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``TransferServiceRestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.get_transfers(
                created_since,
                created_until,
                balance_platform=balance_platform,
                account_holder_id=account_holder_id,
                balance_account_id=balance_account_id,
                payment_instrument_id=payment_instrument_id,
                reference=reference,
                category=category,
                sort_order=sort_order,
                cursor=cursor,
                limit=limit,
                request_options=request_options,
            ),
        )

    def get_transfers_id(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> TransferData:
        """Returns the details of a specified transfer.

        Args:
            id_: Unique identifier of the transfer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``TransferServiceRestServiceError | RawError``."""
        return unwrap(self._with_raw_response.get_transfers_id(id_, request_options=request_options))

    def post_transfers(
        self,
        *,
        idempotency_key: str | None = None,
        www_authenticate: str | None = None,
        body: TransferInfo | TransferInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Transfer:
        """>Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the
        latest version.

        Starts a request to transfer funds to:
        - `Balance accounts <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts>`__
        - `Transfer instruments <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments>`__
        - `Third-party bank accounts <https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts>`__
        - `Third-party cards <https://docs.adyen.com/payouts/payout-service/pay-out-to-cards>`__

        Adyen sends the outcome of the transfer request through webhooks.

        To use this endpoint:
        - Your API credential must have the **TransferService Webservice Initiate** `role
            <https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3>`__.
        - The account holder must have the required `capabilities
            <https://docs.adyen.com/platforms/verification-overview/capabilities>`__.

        Reach out to your Adyen contact to set up these permissions.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            www_authenticate: Header for authenticating through SCA
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has been accepted for processing, but has not been completed.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``ServiceError1 | TransferServiceRestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_transfers(
                idempotency_key=idempotency_key,
                www_authenticate=www_authenticate,
                body=body,
                request_options=request_options,
            ),
        )

    def post_transfers_approve(
        self,
        *,
        idempotency_key: str | None = None,
        www_authenticate: str | None = None,
        body: ApproveTransfersRequest | ApproveTransfersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Initiates the approval of a list of transfers that triggered an additional `review
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers#request-review>`__. Adyen sends the outcome
        of the approval request through webhooks.

        To use this endpoint:
        - Your API credential must have the **TransferService Approve** `role
            <https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3>`__.
        - The account holder must have the required `capabilities
            <https://docs.adyen.com/platforms/verification-overview/capabilities>`__.

        Reach out to your Adyen contact to set up these permissions.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            www_authenticate: Header for authenticating through SCA
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``ServiceError1 | TransferServiceRestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_transfers_approve(
                idempotency_key=idempotency_key,
                www_authenticate=www_authenticate,
                body=body,
                request_options=request_options,
            ),
        )

    def post_transfers_cancel(
        self,
        *,
        idempotency_key: str | None = None,
        body: CancelTransfersRequest | CancelTransfersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Initiates the cancellation of a list of transfers that triggered an additional `review
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers#request-review>`__. Adyen sends the outcome
        of the cancel request through webhooks.

        To use this endpoint:
        - Your API credential must have the **TransferService Approve** `role
            <https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3>`__.
        - The account holder must have the required `capabilities
            <https://docs.adyen.com/platforms/verification-overview/capabilities>`__.

        Reach out to your Adyen contact to set up these permissions.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``TransferServiceRestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_transfers_cancel(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    def post_transfers_transfer_id_returns(
        self,
        transfer_id: str,
        *,
        idempotency_key: str | None = None,
        body: ReturnTransferRequest | ReturnTransferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReturnTransferResponse:
        """Initiates the return of previously transferred funds without creating a new ``transferId``.

        Args:
            transfer_id: The unique identifier of the transfer to be returned.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``TransferServiceRestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_transfers_transfer_id_returns(
                transfer_id, idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> TransfersWithRawResponse:
        return self._with_raw_response


class AsyncTransfers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTransfersWithRawResponse(client, server, auth)

    async def get_transfers(
        self,
        created_since: RFC3339DateTime,
        created_until: RFC3339DateTime,
        *,
        balance_platform: str | None = None,
        account_holder_id: str | None = None,
        balance_account_id: str | None = None,
        payment_instrument_id: str | None = None,
        reference: str | None = None,
        category: Category2OrStr | None = None,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FindTransfersResponse:
        """Returns all the transfers related to a balance account, account holder, or balance platform.

        When making this request, you must include at least one of the following:
        - ``balanceAccountId``
        - ``accountHolderId``
        - ``balancePlatform``.

        This endpoint supports cursor-based pagination. The response returns the first page of results, and returns
        links to the next and previous pages when applicable. You can use the links to page through the results.

        Args:
            created_since: Only include transfers that have been created on or after this point in time. The value must
                be in ISO 8601 format and not earlier than 6 months before the ``createdUntil`` date. For example,
                **2021-05-30T15:07:40Z**.
            created_until: Only include transfers that have been created on or before this point in time. The value must
                be in ISO 8601 format and not later than 6 months after the ``createdSince`` date. For example,
                **2021-05-30T15:07:40Z**.
            balance_platform: The unique identifier of the `balance platform
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``accountHolderId``.
            account_holder_id: The unique identifier of the `account holder
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/accountHolders/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``balancePlatform``. If you provide a
                ``balanceAccountId``, the ``accountHolderId`` must be related to the ``balanceAccountId``.
            balance_account_id: The unique identifier of the `balance account
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id>`__.
                Required if you don't provide an ``accountHolderId`` or ``balancePlatform``. If you provide an
                ``accountHolderId``, the ``balanceAccountId`` must be related to the ``accountHolderId``.
            payment_instrument_id: The unique identifier of the `payment instrument
                <https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_>`__. To use this
                parameter, you must also provide a ``balanceAccountId``, ``accountHolderId``, or ``balancePlatform``.
                The ``paymentInstrumentId`` must be related to the ``balanceAccountId`` or ``accountHolderId`` that you
                provide.
            reference: The reference you provided in the POST `/transfers
                <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__ request
            category: The category of the transfer. Possible values: - **bank**: A transfer involving a `transfer
                instrument
                <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id>`__ or
                a bank account. - **card**: A transfer involving a third-party card. - **internal**: A transfer between
                `balance accounts
                <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id>`__
                within your platform. - **issuedCard**: A transfer initiated by an Adyen-issued card. -
                **platformPayment**: Funds movements related to payments that are acquired for your users. - **topUp**:
                An incoming transfer initiated by your user to top up their balance account.
            sort_order: Determines the sort order of the returned transfers. The sort order is based on the creation
                date of the transfers. Possible values: - **asc**: Ascending order, from oldest to most recent. -
                **desc**: Descending order, from most recent to oldest. Default value: **asc**.
            cursor: The ``cursor`` returned in the links of the previous response.
            limit: The number of items returned per page, maximum of 100 items. By default, the response returns 10
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``TransferServiceRestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_transfers(
                created_since,
                created_until,
                balance_platform=balance_platform,
                account_holder_id=account_holder_id,
                balance_account_id=balance_account_id,
                payment_instrument_id=payment_instrument_id,
                reference=reference,
                category=category,
                sort_order=sort_order,
                cursor=cursor,
                limit=limit,
                request_options=request_options,
            ),
        )

    async def get_transfers_id(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> TransferData:
        """Returns the details of a specified transfer.

        Args:
            id_: Unique identifier of the transfer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``TransferServiceRestServiceError | RawError``."""
        return unwrap(await self._with_raw_response.get_transfers_id(id_, request_options=request_options))

    async def post_transfers(
        self,
        *,
        idempotency_key: str | None = None,
        www_authenticate: str | None = None,
        body: TransferInfo | TransferInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Transfer:
        """>Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the
        latest version.

        Starts a request to transfer funds to:
        - `Balance accounts <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts>`__
        - `Transfer instruments <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments>`__
        - `Third-party bank accounts <https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts>`__
        - `Third-party cards <https://docs.adyen.com/payouts/payout-service/pay-out-to-cards>`__

        Adyen sends the outcome of the transfer request through webhooks.

        To use this endpoint:
        - Your API credential must have the **TransferService Webservice Initiate** `role
            <https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3>`__.
        - The account holder must have the required `capabilities
            <https://docs.adyen.com/platforms/verification-overview/capabilities>`__.

        Reach out to your Adyen contact to set up these permissions.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            www_authenticate: Header for authenticating through SCA
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has been accepted for processing, but has not been completed.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``ServiceError1 | TransferServiceRestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_transfers(
                idempotency_key=idempotency_key,
                www_authenticate=www_authenticate,
                body=body,
                request_options=request_options,
            ),
        )

    async def post_transfers_approve(
        self,
        *,
        idempotency_key: str | None = None,
        www_authenticate: str | None = None,
        body: ApproveTransfersRequest | ApproveTransfersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Initiates the approval of a list of transfers that triggered an additional `review
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers#request-review>`__. Adyen sends the outcome
        of the approval request through webhooks.

        To use this endpoint:
        - Your API credential must have the **TransferService Approve** `role
            <https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3>`__.
        - The account holder must have the required `capabilities
            <https://docs.adyen.com/platforms/verification-overview/capabilities>`__.

        Reach out to your Adyen contact to set up these permissions.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            www_authenticate: Header for authenticating through SCA
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``ServiceError1 | TransferServiceRestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_transfers_approve(
                idempotency_key=idempotency_key,
                www_authenticate=www_authenticate,
                body=body,
                request_options=request_options,
            ),
        )

    async def post_transfers_cancel(
        self,
        *,
        idempotency_key: str | None = None,
        body: CancelTransfersRequest | CancelTransfersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Initiates the cancellation of a list of transfers that triggered an additional `review
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers#request-review>`__. Adyen sends the outcome
        of the cancel request through webhooks.

        To use this endpoint:
        - Your API credential must have the **TransferService Approve** `role
            <https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3>`__.
        - The account holder must have the required `capabilities
            <https://docs.adyen.com/platforms/verification-overview/capabilities>`__.

        Reach out to your Adyen contact to set up these permissions.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``TransferServiceRestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_transfers_cancel(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    async def post_transfers_transfer_id_returns(
        self,
        transfer_id: str,
        *,
        idempotency_key: str | None = None,
        body: ReturnTransferRequest | ReturnTransferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReturnTransferResponse:
        """Initiates the return of previously transferred funds without creating a new ``transferId``.

        Args:
            transfer_id: The unique identifier of the transfer to be returned.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``TransferServiceRestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_transfers_transfer_id_returns(
                transfer_id, idempotency_key=idempotency_key, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncTransfersWithRawResponse:
        return self._with_raw_response


class TransfersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_transfers(
        self,
        created_since: RFC3339DateTime,
        created_until: RFC3339DateTime,
        *,
        balance_platform: str | None = None,
        account_holder_id: str | None = None,
        balance_account_id: str | None = None,
        payment_instrument_id: str | None = None,
        reference: str | None = None,
        category: Category2OrStr | None = None,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FindTransfersResponse, GetTransfersErrorBody]:
        """Returns all the transfers related to a balance account, account holder, or balance platform.

        When making this request, you must include at least one of the following:
        - ``balanceAccountId``
        - ``accountHolderId``
        - ``balancePlatform``.

        This endpoint supports cursor-based pagination. The response returns the first page of results, and returns
        links to the next and previous pages when applicable. You can use the links to page through the results.

        Args:
            created_since: Only include transfers that have been created on or after this point in time. The value must
                be in ISO 8601 format and not earlier than 6 months before the ``createdUntil`` date. For example,
                **2021-05-30T15:07:40Z**.
            created_until: Only include transfers that have been created on or before this point in time. The value must
                be in ISO 8601 format and not later than 6 months after the ``createdSince`` date. For example,
                **2021-05-30T15:07:40Z**.
            balance_platform: The unique identifier of the `balance platform
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``accountHolderId``.
            account_holder_id: The unique identifier of the `account holder
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/accountHolders/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``balancePlatform``. If you provide a
                ``balanceAccountId``, the ``accountHolderId`` must be related to the ``balanceAccountId``.
            balance_account_id: The unique identifier of the `balance account
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id>`__.
                Required if you don't provide an ``accountHolderId`` or ``balancePlatform``. If you provide an
                ``accountHolderId``, the ``balanceAccountId`` must be related to the ``accountHolderId``.
            payment_instrument_id: The unique identifier of the `payment instrument
                <https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_>`__. To use this
                parameter, you must also provide a ``balanceAccountId``, ``accountHolderId``, or ``balancePlatform``.
                The ``paymentInstrumentId`` must be related to the ``balanceAccountId`` or ``accountHolderId`` that you
                provide.
            reference: The reference you provided in the POST `/transfers
                <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__ request
            category: The category of the transfer. Possible values: - **bank**: A transfer involving a `transfer
                instrument
                <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id>`__ or
                a bank account. - **card**: A transfer involving a third-party card. - **internal**: A transfer between
                `balance accounts
                <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id>`__
                within your platform. - **issuedCard**: A transfer initiated by an Adyen-issued card. -
                **platformPayment**: Funds movements related to payments that are acquired for your users. - **topUp**:
                An incoming transfer initiated by your user to top up their balance account.
            sort_order: Determines the sort order of the returned transfers. The sort order is based on the creation
                date of the transfers. Possible values: - **asc**: Ascending order, from oldest to most recent. -
                **desc**: Descending order, from most recent to oldest. Default value: **asc**.
            cursor: The ``cursor`` returned in the links of the previous response.
            limit: The number of items returned per page, maximum of 100 items. By default, the response returns 10
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/transfers"),
            query_params=[
                param[RFC3339DateTime]("createdSince", created_since),
                param[RFC3339DateTime]("createdUntil", created_until),
                param[str | None]("balancePlatform", balance_platform),
                param[str | None]("accountHolderId", account_holder_id),
                param[str | None]("balanceAccountId", balance_account_id),
                param[str | None]("paymentInstrumentId", payment_instrument_id),
                param[str | None]("reference", reference),
                param[Category2OrStr | None]("category", category),
                param[SortOrderOrStr | None]("sortOrder", sort_order),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[FindTransfersResponse],
            error_mapper=get_transfers_error_mapper,
            request_options=request_options,
        )

    def get_transfers_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransferData, GetTransfersIdErrorBody]:
        """Returns the details of a specified transfer.

        Args:
            id_: Unique identifier of the transfer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/transfers/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransferData],
            error_mapper=get_transfers_id_error_mapper,
            request_options=request_options,
        )

    def post_transfers(
        self,
        *,
        idempotency_key: str | None = None,
        www_authenticate: str | None = None,
        body: TransferInfo | TransferInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Transfer, PostTransfersErrorBody]:
        """>Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the
        latest version.

        Starts a request to transfer funds to:
        - `Balance accounts <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts>`__
        - `Transfer instruments <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments>`__
        - `Third-party bank accounts <https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts>`__
        - `Third-party cards <https://docs.adyen.com/payouts/payout-service/pay-out-to-cards>`__

        Adyen sends the outcome of the transfer request through webhooks.

        To use this endpoint:
        - Your API credential must have the **TransferService Webservice Initiate** `role
            <https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3>`__.
        - The account holder must have the required `capabilities
            <https://docs.adyen.com/platforms/verification-overview/capabilities>`__.

        Reach out to your Adyen contact to set up these permissions.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            www_authenticate: Header for authenticating through SCA
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/transfers"),
            headers=[
                param[str | None]("Idempotency-Key", idempotency_key),
                param[str | None]("WWW-Authenticate", www_authenticate),
            ],
            body=json_body[TransferInfo | TransferInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Transfer],
            error_mapper=post_transfers_error_mapper,
            request_options=request_options,
        )

    def post_transfers_approve(
        self,
        *,
        idempotency_key: str | None = None,
        www_authenticate: str | None = None,
        body: ApproveTransfersRequest | ApproveTransfersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, PostTransfersApproveErrorBody]:
        """Initiates the approval of a list of transfers that triggered an additional `review
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers#request-review>`__. Adyen sends the outcome
        of the approval request through webhooks.

        To use this endpoint:
        - Your API credential must have the **TransferService Approve** `role
            <https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3>`__.
        - The account holder must have the required `capabilities
            <https://docs.adyen.com/platforms/verification-overview/capabilities>`__.

        Reach out to your Adyen contact to set up these permissions.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            www_authenticate: Header for authenticating through SCA
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/transfers/approve"),
            headers=[
                param[str | None]("Idempotency-Key", idempotency_key),
                param[str | None]("WWW-Authenticate", www_authenticate),
            ],
            body=json_body[ApproveTransfersRequest | ApproveTransfersRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Any],
            error_mapper=post_transfers_approve_error_mapper,
            request_options=request_options,
        )

    def post_transfers_cancel(
        self,
        *,
        idempotency_key: str | None = None,
        body: CancelTransfersRequest | CancelTransfersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, PostTransfersCancelErrorBody]:
        """Initiates the cancellation of a list of transfers that triggered an additional `review
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers#request-review>`__. Adyen sends the outcome
        of the cancel request through webhooks.

        To use this endpoint:
        - Your API credential must have the **TransferService Approve** `role
            <https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3>`__.
        - The account holder must have the required `capabilities
            <https://docs.adyen.com/platforms/verification-overview/capabilities>`__.

        Reach out to your Adyen contact to set up these permissions.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/transfers/cancel"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CancelTransfersRequest | CancelTransfersRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Any],
            error_mapper=post_transfers_cancel_error_mapper,
            request_options=request_options,
        )

    def post_transfers_transfer_id_returns(
        self,
        transfer_id: str,
        *,
        idempotency_key: str | None = None,
        body: ReturnTransferRequest | ReturnTransferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReturnTransferResponse, PostTransfersTransferIdReturnsErrorBody]:
        """Initiates the return of previously transferred funds without creating a new ``transferId``.

        Args:
            transfer_id: The unique identifier of the transfer to be returned.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/transfers/{transferId}/returns"),
            path_params=[param[str]("transferId", transfer_id)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[ReturnTransferRequest | ReturnTransferRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ReturnTransferResponse],
            error_mapper=post_transfers_transfer_id_returns_error_mapper,
            request_options=request_options,
        )


class AsyncTransfersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_transfers(
        self,
        created_since: RFC3339DateTime,
        created_until: RFC3339DateTime,
        *,
        balance_platform: str | None = None,
        account_holder_id: str | None = None,
        balance_account_id: str | None = None,
        payment_instrument_id: str | None = None,
        reference: str | None = None,
        category: Category2OrStr | None = None,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FindTransfersResponse, GetTransfersErrorBody]:
        """Returns all the transfers related to a balance account, account holder, or balance platform.

        When making this request, you must include at least one of the following:
        - ``balanceAccountId``
        - ``accountHolderId``
        - ``balancePlatform``.

        This endpoint supports cursor-based pagination. The response returns the first page of results, and returns
        links to the next and previous pages when applicable. You can use the links to page through the results.

        Args:
            created_since: Only include transfers that have been created on or after this point in time. The value must
                be in ISO 8601 format and not earlier than 6 months before the ``createdUntil`` date. For example,
                **2021-05-30T15:07:40Z**.
            created_until: Only include transfers that have been created on or before this point in time. The value must
                be in ISO 8601 format and not later than 6 months after the ``createdSince`` date. For example,
                **2021-05-30T15:07:40Z**.
            balance_platform: The unique identifier of the `balance platform
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``accountHolderId``.
            account_holder_id: The unique identifier of the `account holder
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/accountHolders/{id}__queryParam_id>`__.
                Required if you don't provide a ``balanceAccountId`` or ``balancePlatform``. If you provide a
                ``balanceAccountId``, the ``accountHolderId`` must be related to the ``balanceAccountId``.
            balance_account_id: The unique identifier of the `balance account
                <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id>`__.
                Required if you don't provide an ``accountHolderId`` or ``balancePlatform``. If you provide an
                ``accountHolderId``, the ``balanceAccountId`` must be related to the ``accountHolderId``.
            payment_instrument_id: The unique identifier of the `payment instrument
                <https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_>`__. To use this
                parameter, you must also provide a ``balanceAccountId``, ``accountHolderId``, or ``balancePlatform``.
                The ``paymentInstrumentId`` must be related to the ``balanceAccountId`` or ``accountHolderId`` that you
                provide.
            reference: The reference you provided in the POST `/transfers
                <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__ request
            category: The category of the transfer. Possible values: - **bank**: A transfer involving a `transfer
                instrument
                <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id>`__ or
                a bank account. - **card**: A transfer involving a third-party card. - **internal**: A transfer between
                `balance accounts
                <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id>`__
                within your platform. - **issuedCard**: A transfer initiated by an Adyen-issued card. -
                **platformPayment**: Funds movements related to payments that are acquired for your users. - **topUp**:
                An incoming transfer initiated by your user to top up their balance account.
            sort_order: Determines the sort order of the returned transfers. The sort order is based on the creation
                date of the transfers. Possible values: - **asc**: Ascending order, from oldest to most recent. -
                **desc**: Descending order, from most recent to oldest. Default value: **asc**.
            cursor: The ``cursor`` returned in the links of the previous response.
            limit: The number of items returned per page, maximum of 100 items. By default, the response returns 10
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/transfers"),
            query_params=[
                param[RFC3339DateTime]("createdSince", created_since),
                param[RFC3339DateTime]("createdUntil", created_until),
                param[str | None]("balancePlatform", balance_platform),
                param[str | None]("accountHolderId", account_holder_id),
                param[str | None]("balanceAccountId", balance_account_id),
                param[str | None]("paymentInstrumentId", payment_instrument_id),
                param[str | None]("reference", reference),
                param[Category2OrStr | None]("category", category),
                param[SortOrderOrStr | None]("sortOrder", sort_order),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[FindTransfersResponse],
            error_mapper=get_transfers_error_mapper,
            request_options=request_options,
        )

    async def get_transfers_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransferData, GetTransfersIdErrorBody]:
        """Returns the details of a specified transfer.

        Args:
            id_: Unique identifier of the transfer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/transfers/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TransferData],
            error_mapper=get_transfers_id_error_mapper,
            request_options=request_options,
        )

    async def post_transfers(
        self,
        *,
        idempotency_key: str | None = None,
        www_authenticate: str | None = None,
        body: TransferInfo | TransferInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Transfer, PostTransfersErrorBody]:
        """>Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the
        latest version.

        Starts a request to transfer funds to:
        - `Balance accounts <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts>`__
        - `Transfer instruments <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments>`__
        - `Third-party bank accounts <https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts>`__
        - `Third-party cards <https://docs.adyen.com/payouts/payout-service/pay-out-to-cards>`__

        Adyen sends the outcome of the transfer request through webhooks.

        To use this endpoint:
        - Your API credential must have the **TransferService Webservice Initiate** `role
            <https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3>`__.
        - The account holder must have the required `capabilities
            <https://docs.adyen.com/platforms/verification-overview/capabilities>`__.

        Reach out to your Adyen contact to set up these permissions.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            www_authenticate: Header for authenticating through SCA
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/transfers"),
            headers=[
                param[str | None]("Idempotency-Key", idempotency_key),
                param[str | None]("WWW-Authenticate", www_authenticate),
            ],
            body=json_body[TransferInfo | TransferInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Transfer],
            error_mapper=post_transfers_error_mapper,
            request_options=request_options,
        )

    async def post_transfers_approve(
        self,
        *,
        idempotency_key: str | None = None,
        www_authenticate: str | None = None,
        body: ApproveTransfersRequest | ApproveTransfersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, PostTransfersApproveErrorBody]:
        """Initiates the approval of a list of transfers that triggered an additional `review
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers#request-review>`__. Adyen sends the outcome
        of the approval request through webhooks.

        To use this endpoint:
        - Your API credential must have the **TransferService Approve** `role
            <https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3>`__.
        - The account holder must have the required `capabilities
            <https://docs.adyen.com/platforms/verification-overview/capabilities>`__.

        Reach out to your Adyen contact to set up these permissions.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            www_authenticate: Header for authenticating through SCA
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/transfers/approve"),
            headers=[
                param[str | None]("Idempotency-Key", idempotency_key),
                param[str | None]("WWW-Authenticate", www_authenticate),
            ],
            body=json_body[ApproveTransfersRequest | ApproveTransfersRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Any],
            error_mapper=post_transfers_approve_error_mapper,
            request_options=request_options,
        )

    async def post_transfers_cancel(
        self,
        *,
        idempotency_key: str | None = None,
        body: CancelTransfersRequest | CancelTransfersRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, PostTransfersCancelErrorBody]:
        """Initiates the cancellation of a list of transfers that triggered an additional `review
        <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers#request-review>`__. Adyen sends the outcome
        of the cancel request through webhooks.

        To use this endpoint:
        - Your API credential must have the **TransferService Approve** `role
            <https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3>`__.
        - The account holder must have the required `capabilities
            <https://docs.adyen.com/platforms/verification-overview/capabilities>`__.

        Reach out to your Adyen contact to set up these permissions.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/transfers/cancel"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CancelTransfersRequest | CancelTransfersRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Any],
            error_mapper=post_transfers_cancel_error_mapper,
            request_options=request_options,
        )

    async def post_transfers_transfer_id_returns(
        self,
        transfer_id: str,
        *,
        idempotency_key: str | None = None,
        body: ReturnTransferRequest | ReturnTransferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReturnTransferResponse, PostTransfersTransferIdReturnsErrorBody]:
        """Initiates the return of previously transferred funds without creating a new ``transferId``.

        Args:
            transfer_id: The unique identifier of the transfer to be returned.
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default14("/transfers/{transferId}/returns"),
            path_params=[param[str]("transferId", transfer_id)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[ReturnTransferRequest | ReturnTransferRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[ReturnTransferResponse],
            error_mapper=post_transfers_transfer_id_returns_error_mapper,
            request_options=request_options,
        )
