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
from ..errors.delete_transaction_rules_transaction_rule_id_error import (
    DeleteTransactionRulesTransactionRuleIdErrorBody,
    delete_transaction_rules_transaction_rule_id_error_mapper,
)
from ..errors.get_transaction_rules_transaction_rule_id_error import (
    GetTransactionRulesTransactionRuleIdErrorBody,
    get_transaction_rules_transaction_rule_id_error_mapper,
)
from ..errors.patch_transaction_rules_transaction_rule_id_error import (
    PatchTransactionRulesTransactionRuleIdErrorBody,
    patch_transaction_rules_transaction_rule_id_error_mapper,
)
from ..errors.post_transaction_rules_error import PostTransactionRulesErrorBody, post_transaction_rules_error_mapper
from ..models.transaction_rule import TransactionRule
from ..models.transaction_rule_info import TransactionRuleInfo, TransactionRuleInfoDict
from ..models.transaction_rule_response import TransactionRuleResponse
from ..server.server import Server


class TransactionRules:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TransactionRulesWithRawResponse(client, server, auth)

    def delete_transaction_rules_transaction_rule_id(
        self, transaction_rule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRule:
        """Deletes a transaction rule.

        Args:
            transaction_rule_id: The unique identifier of the transaction rule.
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
            self._with_raw_response.delete_transaction_rules_transaction_rule_id(
                transaction_rule_id, request_options=request_options
            ),
        )

    def get_transaction_rules_transaction_rule_id(
        self, transaction_rule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRuleResponse:
        """Returns the details of a transaction rule.

        Args:
            transaction_rule_id: The unique identifier of the transaction rule.
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
            self._with_raw_response.get_transaction_rules_transaction_rule_id(
                transaction_rule_id, request_options=request_options
            ),
        )

    def patch_transaction_rules_transaction_rule_id(
        self,
        transaction_rule_id: str,
        *,
        body: TransactionRuleInfo | TransactionRuleInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransactionRule:
        """Updates a transaction rule.

        * To update only the status of a transaction rule, send only the ``status`` parameter. All other parameters not
            provided in the request are left unchanged.

        * When updating any other parameter, you need to send all existing resource parameters. If you omit a parameter
            in the request, that parameter is removed from the resource.

        Args:
            transaction_rule_id: The unique identifier of the transaction rule.
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
            self._with_raw_response.patch_transaction_rules_transaction_rule_id(
                transaction_rule_id, body=body, request_options=request_options
            ),
        )

    def post_transaction_rules(
        self,
        *,
        body: TransactionRuleInfo | TransactionRuleInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransactionRule:
        """Creates a `transaction rule <https://docs.adyen.com/issuing/transaction-rules>`__. When your user makes a
        transaction with their Adyen-issued card, the transaction is allowed or declined based on the conditions and
        outcome defined in the transaction rule. You can apply the transaction rule to several cards, such as all the
        cards in your platform, or to a specific card. For use cases, see `examples
        <https://docs.adyen.com/issuing/transaction-rules/examples>`__.

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
        return unwrap(self._with_raw_response.post_transaction_rules(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> TransactionRulesWithRawResponse:
        return self._with_raw_response


class AsyncTransactionRules:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTransactionRulesWithRawResponse(client, server, auth)

    async def delete_transaction_rules_transaction_rule_id(
        self, transaction_rule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRule:
        """Deletes a transaction rule.

        Args:
            transaction_rule_id: The unique identifier of the transaction rule.
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
            await self._with_raw_response.delete_transaction_rules_transaction_rule_id(
                transaction_rule_id, request_options=request_options
            ),
        )

    async def get_transaction_rules_transaction_rule_id(
        self, transaction_rule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRuleResponse:
        """Returns the details of a transaction rule.

        Args:
            transaction_rule_id: The unique identifier of the transaction rule.
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
            await self._with_raw_response.get_transaction_rules_transaction_rule_id(
                transaction_rule_id, request_options=request_options
            ),
        )

    async def patch_transaction_rules_transaction_rule_id(
        self,
        transaction_rule_id: str,
        *,
        body: TransactionRuleInfo | TransactionRuleInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransactionRule:
        """Updates a transaction rule.

        * To update only the status of a transaction rule, send only the ``status`` parameter. All other parameters not
            provided in the request are left unchanged.

        * When updating any other parameter, you need to send all existing resource parameters. If you omit a parameter
            in the request, that parameter is removed from the resource.

        Args:
            transaction_rule_id: The unique identifier of the transaction rule.
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
            await self._with_raw_response.patch_transaction_rules_transaction_rule_id(
                transaction_rule_id, body=body, request_options=request_options
            ),
        )

    async def post_transaction_rules(
        self,
        *,
        body: TransactionRuleInfo | TransactionRuleInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransactionRule:
        """Creates a `transaction rule <https://docs.adyen.com/issuing/transaction-rules>`__. When your user makes a
        transaction with their Adyen-issued card, the transaction is allowed or declined based on the conditions and
        outcome defined in the transaction rule. You can apply the transaction rule to several cards, such as all the
        cards in your platform, or to a specific card. For use cases, see `examples
        <https://docs.adyen.com/issuing/transaction-rules/examples>`__.

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
        return unwrap(await self._with_raw_response.post_transaction_rules(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncTransactionRulesWithRawResponse:
        return self._with_raw_response


class TransactionRulesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_transaction_rules_transaction_rule_id(
        self, transaction_rule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRule, DeleteTransactionRulesTransactionRuleIdErrorBody]:
        """Deletes a transaction rule.

        Args:
            transaction_rule_id: The unique identifier of the transaction rule.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/transactionRules/{transactionRuleId}"),
            path_params=[param[str]("transactionRuleId", transaction_rule_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionRule],
            error_mapper=delete_transaction_rules_transaction_rule_id_error_mapper,
            request_options=request_options,
        )

    def get_transaction_rules_transaction_rule_id(
        self, transaction_rule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRuleResponse, GetTransactionRulesTransactionRuleIdErrorBody]:
        """Returns the details of a transaction rule.

        Args:
            transaction_rule_id: The unique identifier of the transaction rule.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/transactionRules/{transactionRuleId}"),
            path_params=[param[str]("transactionRuleId", transaction_rule_id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionRuleResponse],
            error_mapper=get_transaction_rules_transaction_rule_id_error_mapper,
            request_options=request_options,
        )

    def patch_transaction_rules_transaction_rule_id(
        self,
        transaction_rule_id: str,
        *,
        body: TransactionRuleInfo | TransactionRuleInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransactionRule, PatchTransactionRulesTransactionRuleIdErrorBody]:
        """Updates a transaction rule.

        * To update only the status of a transaction rule, send only the ``status`` parameter. All other parameters not
            provided in the request are left unchanged.

        * When updating any other parameter, you need to send all existing resource parameters. If you omit a parameter
            in the request, that parameter is removed from the resource.

        Args:
            transaction_rule_id: The unique identifier of the transaction rule.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/transactionRules/{transactionRuleId}"),
            path_params=[param[str]("transactionRuleId", transaction_rule_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransactionRuleInfo | TransactionRuleInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionRule],
            error_mapper=patch_transaction_rules_transaction_rule_id_error_mapper,
            request_options=request_options,
        )

    def post_transaction_rules(
        self,
        *,
        body: TransactionRuleInfo | TransactionRuleInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransactionRule, PostTransactionRulesErrorBody]:
        """Creates a `transaction rule <https://docs.adyen.com/issuing/transaction-rules>`__. When your user makes a
        transaction with their Adyen-issued card, the transaction is allowed or declined based on the conditions and
        outcome defined in the transaction rule. You can apply the transaction rule to several cards, such as all the
        cards in your platform, or to a specific card. For use cases, see `examples
        <https://docs.adyen.com/issuing/transaction-rules/examples>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/transactionRules"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransactionRuleInfo | TransactionRuleInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionRule],
            error_mapper=post_transaction_rules_error_mapper,
            request_options=request_options,
        )


class AsyncTransactionRulesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_transaction_rules_transaction_rule_id(
        self, transaction_rule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRule, DeleteTransactionRulesTransactionRuleIdErrorBody]:
        """Deletes a transaction rule.

        Args:
            transaction_rule_id: The unique identifier of the transaction rule.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/transactionRules/{transactionRuleId}"),
            path_params=[param[str]("transactionRuleId", transaction_rule_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TransactionRule],
            error_mapper=delete_transaction_rules_transaction_rule_id_error_mapper,
            request_options=request_options,
        )

    async def get_transaction_rules_transaction_rule_id(
        self, transaction_rule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRuleResponse, GetTransactionRulesTransactionRuleIdErrorBody]:
        """Returns the details of a transaction rule.

        Args:
            transaction_rule_id: The unique identifier of the transaction rule.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/transactionRules/{transactionRuleId}"),
            path_params=[param[str]("transactionRuleId", transaction_rule_id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TransactionRuleResponse],
            error_mapper=get_transaction_rules_transaction_rule_id_error_mapper,
            request_options=request_options,
        )

    async def patch_transaction_rules_transaction_rule_id(
        self,
        transaction_rule_id: str,
        *,
        body: TransactionRuleInfo | TransactionRuleInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransactionRule, PatchTransactionRulesTransactionRuleIdErrorBody]:
        """Updates a transaction rule.

        * To update only the status of a transaction rule, send only the ``status`` parameter. All other parameters not
            provided in the request are left unchanged.

        * When updating any other parameter, you need to send all existing resource parameters. If you omit a parameter
            in the request, that parameter is removed from the resource.

        Args:
            transaction_rule_id: The unique identifier of the transaction rule.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/transactionRules/{transactionRuleId}"),
            path_params=[param[str]("transactionRuleId", transaction_rule_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransactionRuleInfo | TransactionRuleInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TransactionRule],
            error_mapper=patch_transaction_rules_transaction_rule_id_error_mapper,
            request_options=request_options,
        )

    async def post_transaction_rules(
        self,
        *,
        body: TransactionRuleInfo | TransactionRuleInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransactionRule, PostTransactionRulesErrorBody]:
        """Creates a `transaction rule <https://docs.adyen.com/issuing/transaction-rules>`__. When your user makes a
        transaction with their Adyen-issued card, the transaction is allowed or declined based on the conditions and
        outcome defined in the transaction rule. You can apply the transaction rule to several cards, such as all the
        cards in your platform, or to a specific card. For use cases, see `examples
        <https://docs.adyen.com/issuing/transaction-rules/examples>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/transactionRules"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransactionRuleInfo | TransactionRuleInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TransactionRule],
            error_mapper=post_transaction_rules_error_mapper,
            request_options=request_options,
        )
