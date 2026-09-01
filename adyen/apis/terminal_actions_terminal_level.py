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
    json_body,
    json_decoder,
    param,
)
from ..errors.post_terminals_schedule_actions_error import (
    PostTerminalsScheduleActionsErrorBody,
    post_terminals_schedule_actions_error_mapper,
)
from ..models.schedule_terminal_actions_request import (
    ScheduleTerminalActionsRequest,
    ScheduleTerminalActionsRequestDict,
)
from ..models.schedule_terminal_actions_response import ScheduleTerminalActionsResponse
from ..server.server import Server


class TerminalActionsTerminalLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TerminalActionsTerminalLevelWithRawResponse(client, server, auth)

    def post_terminals_schedule_actions(
        self,
        *,
        body: ScheduleTerminalActionsRequest | ScheduleTerminalActionsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduleTerminalActionsResponse:
        """Schedules a `terminal action
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__ by specifying the
        action and the terminals that the action must be applied to.

        The following restrictions apply:
        * You can schedule only one action at a time. For example, to install a new app version and remove an old app
            version, you have to make two API requests.
        * The maximum number of terminals in a request is **100**. For example, to apply an action to 250 terminals, you
            have to divide the terminals over three API requests.
        * If there is an error with one or more terminal IDs in the request, the action is scheduled for none of the
            terminals. You need to fix the error and try again.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_terminals_schedule_actions(
            body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TerminalActionsTerminalLevelWithRawResponse:
        return self._with_raw_response


class AsyncTerminalActionsTerminalLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTerminalActionsTerminalLevelWithRawResponse(client, server, auth)

    async def post_terminals_schedule_actions(
        self,
        *,
        body: ScheduleTerminalActionsRequest | ScheduleTerminalActionsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduleTerminalActionsResponse:
        """Schedules a `terminal action
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__ by specifying the
        action and the terminals that the action must be applied to.

        The following restrictions apply:
        * You can schedule only one action at a time. For example, to install a new app version and remove an old app
            version, you have to make two API requests.
        * The maximum number of terminals in a request is **100**. For example, to apply an action to 250 terminals, you
            have to divide the terminals over three API requests.
        * If there is an error with one or more terminal IDs in the request, the action is scheduled for none of the
            terminals. You need to fix the error and try again.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_terminals_schedule_actions(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTerminalActionsTerminalLevelWithRawResponse:
        return self._with_raw_response


class TerminalActionsTerminalLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_terminals_schedule_actions(
        self,
        *,
        body: ScheduleTerminalActionsRequest | ScheduleTerminalActionsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduleTerminalActionsResponse, PostTerminalsScheduleActionsErrorBody]:
        """Schedules a `terminal action
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__ by specifying the
        action and the terminals that the action must be applied to.

        The following restrictions apply:
        * You can schedule only one action at a time. For example, to install a new app version and remove an old app
            version, you have to make two API requests.
        * The maximum number of terminals in a request is **100**. For example, to apply an action to 250 terminals, you
            have to divide the terminals over three API requests.
        * If there is an error with one or more terminal IDs in the request, the action is scheduled for none of the
            terminals. You need to fix the error and try again.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/terminals/scheduleActions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduleTerminalActionsRequest | ScheduleTerminalActionsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ScheduleTerminalActionsResponse],
            error_mapper=post_terminals_schedule_actions_error_mapper,
            request_options=request_options,
        )


class AsyncTerminalActionsTerminalLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_terminals_schedule_actions(
        self,
        *,
        body: ScheduleTerminalActionsRequest | ScheduleTerminalActionsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduleTerminalActionsResponse, PostTerminalsScheduleActionsErrorBody]:
        """Schedules a `terminal action
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__ by specifying the
        action and the terminals that the action must be applied to.

        The following restrictions apply:
        * You can schedule only one action at a time. For example, to install a new app version and remove an old app
            version, you have to make two API requests.
        * The maximum number of terminals in a request is **100**. For example, to apply an action to 250 terminals, you
            have to divide the terminals over three API requests.
        * If there is an error with one or more terminal IDs in the request, the action is scheduled for none of the
            terminals. You need to fix the error and try again.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/terminals/scheduleActions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduleTerminalActionsRequest | ScheduleTerminalActionsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ScheduleTerminalActionsResponse],
            error_mapper=post_terminals_schedule_actions_error_mapper,
            request_options=request_options,
        )
