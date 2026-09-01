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
from ..errors.delete_balance_accounts_balance_account_id_payout_schedules_id_error import (
    DeleteBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody,
    delete_balance_accounts_balance_account_id_payout_schedules_id_error_mapper,
)
from ..errors.get_balance_accounts_balance_account_id_payout_schedules_error import (
    GetBalanceAccountsBalanceAccountIdPayoutSchedulesErrorBody,
    get_balance_accounts_balance_account_id_payout_schedules_error_mapper,
)
from ..errors.get_balance_accounts_balance_account_id_payout_schedules_id_error import (
    GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody,
    get_balance_accounts_balance_account_id_payout_schedules_id_error_mapper,
)
from ..errors.get_balance_accounts_balance_account_id_payout_schedules_id_executions_error import (
    GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdExecutionsErrorBody,
    get_balance_accounts_balance_account_id_payout_schedules_id_executions_error_mapper,
)
from ..errors.get_balance_platforms_balance_platform_id_payout_schedules_error import (
    GetBalancePlatformsBalancePlatformIdPayoutSchedulesErrorBody,
    get_balance_platforms_balance_platform_id_payout_schedules_error_mapper,
)
from ..errors.get_balance_platforms_balance_platform_id_payout_schedules_id_error import (
    GetBalancePlatformsBalancePlatformIdPayoutSchedulesIdErrorBody,
    get_balance_platforms_balance_platform_id_payout_schedules_id_error_mapper,
)
from ..errors.patch_balance_accounts_balance_account_id_payout_schedules_id_error import (
    PatchBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody,
    patch_balance_accounts_balance_account_id_payout_schedules_id_error_mapper,
)
from ..errors.post_balance_accounts_balance_account_id_payout_schedules_error import (
    PostBalanceAccountsBalanceAccountIdPayoutSchedulesErrorBody,
    post_balance_accounts_balance_account_id_payout_schedules_error_mapper,
)
from ..models.balance_account_configuration import BalanceAccountConfiguration
from ..models.balance_account_configuration_request import (
    BalanceAccountConfigurationRequest,
    BalanceAccountConfigurationRequestDict,
)
from ..models.balance_account_configuration_update import (
    BalanceAccountConfigurationUpdate,
    BalanceAccountConfigurationUpdateDict,
)
from ..models.balance_account_configurations import BalanceAccountConfigurations
from ..models.balance_platform_configuration import BalancePlatformConfiguration
from ..models.balance_platform_configurations import BalancePlatformConfigurations
from ..models.enums.execution_result import ExecutionResultOrStr
from ..models.payout_schedule_executions import PayoutScheduleExecutions
from ..server.server import Server


class ManagedPayoutSchedules:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = ManagedPayoutSchedulesWithRawResponse(client, server)

    def delete_balance_accounts_balance_account_id_payout_schedules_id(
        self, balance_account_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a payout schedule applied to a balance account.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule applied to the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.delete_balance_accounts_balance_account_id_payout_schedules_id(
            balance_account_id, id, request_options=request_options
        ).unwrap()

    def get_balance_accounts_balance_account_id_payout_schedules(
        self,
        balance_account_id: str,
        *,
        currency: str | None = None,
        cursor: str | None = None,
        limit: int | None = 10,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceAccountConfigurations:
        """Returns a list of all managed payout schedules that are configured on a balance account. You can use query
        parameters to filter the elements that are returned in the list.

        Args:
            balance_account_id: The unique identifier of the balance account.
            currency: The three-character `ISO currency code
                <https://docs.adyen.com/development-resources/currency-codes>`__ of the currency used in the payout
                schedule.
            cursor: The ``cursor`` returned in the links of the previous response.
            limit: The number of items returned per page, maximum of 100 items. By default, the response returns 10
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_balance_accounts_balance_account_id_payout_schedules(
            balance_account_id, currency=currency, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def get_balance_accounts_balance_account_id_payout_schedules_id(
        self, balance_account_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BalanceAccountConfiguration:
        """Returns the specified payout schedule.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule for the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_balance_accounts_balance_account_id_payout_schedules_id(
            balance_account_id, id, request_options=request_options
        ).unwrap()

    def get_balance_accounts_balance_account_id_payout_schedules_id_executions(
        self,
        balance_account_id: str,
        id: str,
        offset: int,
        *,
        results: list[ExecutionResultOrStr] | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayoutScheduleExecutions:
        """View information about the executions of a managed payout schedule on the specified balance account. An
        execution is an attempt to make a payout according to the payout schedule.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule on the balance account.
            offset: The page number to be returned. Default: **1**
            results: Contains a list of payout statuses. If included, the response returns only executed payouts that
                currently have one of the specified statuses. Possible statuses: - **succeeded**: The payout was sent
                successfully. - **failed**: The payout was not sent due to an error. - **skipped**: The payout was not
                triggered as expected.
            limit: The number of items returned per page. Default: **10**
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_balance_accounts_balance_account_id_payout_schedules_id_executions(
            balance_account_id, id, offset, results=results, limit=limit, request_options=request_options
        ).unwrap()

    def get_balance_platforms_balance_platform_id_payout_schedules(
        self,
        balance_platform_id: str,
        *,
        country_code: str | None = None,
        currency: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalancePlatformConfigurations:
        """Returns a list of all the payout schedules that are configured for your balance platform. You can use query
        parameters to filter the elements that are returned in the list.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            country_code: The two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__
                country code of the country to which the payout configuration applies.
            currency: The three-character `ISO currency code
                <https://docs.adyen.com/development-resources/currency-codes>`__ of the currency used in the payout
                configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_balance_platforms_balance_platform_id_payout_schedules(
            balance_platform_id, country_code=country_code, currency=currency, request_options=request_options
        ).unwrap()

    def get_balance_platforms_balance_platform_id_payout_schedules_id(
        self, balance_platform_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BalancePlatformConfiguration:
        """Returns the specified managed payout schedule configured on your balance platform.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            id: The unique identifier of the payout configuration for your balance platform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_balance_platforms_balance_platform_id_payout_schedules_id(
            balance_platform_id, id, request_options=request_options
        ).unwrap()

    def patch_balance_accounts_balance_account_id_payout_schedules_id(
        self,
        balance_account_id: str,
        id: str,
        body: BalanceAccountConfigurationUpdate | BalanceAccountConfigurationUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceAccountConfiguration:
        """Update a managed payout schedule applied to a balance account. If an optional parameter is not included in
        the request, it remains unchanged.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule applied to the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.patch_balance_accounts_balance_account_id_payout_schedules_id(
            balance_account_id, id, body, request_options=request_options
        ).unwrap()

    def post_balance_accounts_balance_account_id_payout_schedules(
        self,
        balance_account_id: str,
        body: BalanceAccountConfigurationRequest | BalanceAccountConfigurationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceAccountConfiguration:
        """Apply a managed payout schedule to a balance account. This payout schedule is based on an existing payout
        schedule in your balance platform.

        Args:
            balance_account_id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.post_balance_accounts_balance_account_id_payout_schedules(
            balance_account_id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ManagedPayoutSchedulesWithRawResponse:
        return self._with_raw_response


class AsyncManagedPayoutSchedules:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncManagedPayoutSchedulesWithRawResponse(client, server)

    async def delete_balance_accounts_balance_account_id_payout_schedules_id(
        self, balance_account_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a payout schedule applied to a balance account.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule applied to the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.delete_balance_accounts_balance_account_id_payout_schedules_id(
                balance_account_id, id, request_options=request_options
            )
        ).unwrap()

    async def get_balance_accounts_balance_account_id_payout_schedules(
        self,
        balance_account_id: str,
        *,
        currency: str | None = None,
        cursor: str | None = None,
        limit: int | None = 10,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceAccountConfigurations:
        """Returns a list of all managed payout schedules that are configured on a balance account. You can use query
        parameters to filter the elements that are returned in the list.

        Args:
            balance_account_id: The unique identifier of the balance account.
            currency: The three-character `ISO currency code
                <https://docs.adyen.com/development-resources/currency-codes>`__ of the currency used in the payout
                schedule.
            cursor: The ``cursor`` returned in the links of the previous response.
            limit: The number of items returned per page, maximum of 100 items. By default, the response returns 10
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_balance_accounts_balance_account_id_payout_schedules(
                balance_account_id, currency=currency, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def get_balance_accounts_balance_account_id_payout_schedules_id(
        self, balance_account_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BalanceAccountConfiguration:
        """Returns the specified payout schedule.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule for the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_balance_accounts_balance_account_id_payout_schedules_id(
                balance_account_id, id, request_options=request_options
            )
        ).unwrap()

    async def get_balance_accounts_balance_account_id_payout_schedules_id_executions(
        self,
        balance_account_id: str,
        id: str,
        offset: int,
        *,
        results: list[ExecutionResultOrStr] | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayoutScheduleExecutions:
        """View information about the executions of a managed payout schedule on the specified balance account. An
        execution is an attempt to make a payout according to the payout schedule.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule on the balance account.
            offset: The page number to be returned. Default: **1**
            results: Contains a list of payout statuses. If included, the response returns only executed payouts that
                currently have one of the specified statuses. Possible statuses: - **succeeded**: The payout was sent
                successfully. - **failed**: The payout was not sent due to an error. - **skipped**: The payout was not
                triggered as expected.
            limit: The number of items returned per page. Default: **10**
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_balance_accounts_balance_account_id_payout_schedules_id_executions(
                balance_account_id, id, offset, results=results, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def get_balance_platforms_balance_platform_id_payout_schedules(
        self,
        balance_platform_id: str,
        *,
        country_code: str | None = None,
        currency: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalancePlatformConfigurations:
        """Returns a list of all the payout schedules that are configured for your balance platform. You can use query
        parameters to filter the elements that are returned in the list.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            country_code: The two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__
                country code of the country to which the payout configuration applies.
            currency: The three-character `ISO currency code
                <https://docs.adyen.com/development-resources/currency-codes>`__ of the currency used in the payout
                configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_balance_platforms_balance_platform_id_payout_schedules(
                balance_platform_id, country_code=country_code, currency=currency, request_options=request_options
            )
        ).unwrap()

    async def get_balance_platforms_balance_platform_id_payout_schedules_id(
        self, balance_platform_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BalancePlatformConfiguration:
        """Returns the specified managed payout schedule configured on your balance platform.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            id: The unique identifier of the payout configuration for your balance platform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_balance_platforms_balance_platform_id_payout_schedules_id(
                balance_platform_id, id, request_options=request_options
            )
        ).unwrap()

    async def patch_balance_accounts_balance_account_id_payout_schedules_id(
        self,
        balance_account_id: str,
        id: str,
        body: BalanceAccountConfigurationUpdate | BalanceAccountConfigurationUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceAccountConfiguration:
        """Update a managed payout schedule applied to a balance account. If an optional parameter is not included in
        the request, it remains unchanged.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule applied to the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.patch_balance_accounts_balance_account_id_payout_schedules_id(
                balance_account_id, id, body, request_options=request_options
            )
        ).unwrap()

    async def post_balance_accounts_balance_account_id_payout_schedules(
        self,
        balance_account_id: str,
        body: BalanceAccountConfigurationRequest | BalanceAccountConfigurationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalanceAccountConfiguration:
        """Apply a managed payout schedule to a balance account. This payout schedule is based on an existing payout
        schedule in your balance platform.

        Args:
            balance_account_id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Not Found - the resource was not found Unprocessable Entity - a request validation error.
                Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.post_balance_accounts_balance_account_id_payout_schedules(
                balance_account_id, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncManagedPayoutSchedulesWithRawResponse:
        return self._with_raw_response


class ManagedPayoutSchedulesWithRawResponse(BaseRawResponse[RawClient, Server]):
    def delete_balance_accounts_balance_account_id_payout_schedules_id(
        self, balance_account_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody]:
        """Delete a payout schedule applied to a balance account.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule applied to the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/payoutSchedules/{id}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=delete_balance_accounts_balance_account_id_payout_schedules_id_error_mapper,
            request_options=request_options,
        )

    def get_balance_accounts_balance_account_id_payout_schedules(
        self,
        balance_account_id: str,
        *,
        currency: str | None = None,
        cursor: str | None = None,
        limit: int | None = 10,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceAccountConfigurations, GetBalanceAccountsBalanceAccountIdPayoutSchedulesErrorBody]:
        """Returns a list of all managed payout schedules that are configured on a balance account. You can use query
        parameters to filter the elements that are returned in the list.

        Args:
            balance_account_id: The unique identifier of the balance account.
            currency: The three-character `ISO currency code
                <https://docs.adyen.com/development-resources/currency-codes>`__ of the currency used in the payout
                schedule.
            cursor: The ``cursor`` returned in the links of the previous response.
            limit: The number of items returned per page, maximum of 100 items. By default, the response returns 10
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/payoutSchedules"),
            path_params=[param[str]("balanceAccountId", balance_account_id)],
            query_params=[
                param[str | None]("currency", currency),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            decoder=json_decoder[BalanceAccountConfigurations],
            error_mapper=get_balance_accounts_balance_account_id_payout_schedules_error_mapper,
            request_options=request_options,
        )

    def get_balance_accounts_balance_account_id_payout_schedules_id(
        self, balance_account_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BalanceAccountConfiguration, GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody]:
        """Returns the specified payout schedule.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule for the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/payoutSchedules/{id}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("id", id)],
            decoder=json_decoder[BalanceAccountConfiguration],
            error_mapper=get_balance_accounts_balance_account_id_payout_schedules_id_error_mapper,
            request_options=request_options,
        )

    def get_balance_accounts_balance_account_id_payout_schedules_id_executions(
        self,
        balance_account_id: str,
        id: str,
        offset: int,
        *,
        results: list[ExecutionResultOrStr] | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayoutScheduleExecutions, GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdExecutionsErrorBody]:
        """View information about the executions of a managed payout schedule on the specified balance account. An
        execution is an attempt to make a payout according to the payout schedule.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule on the balance account.
            offset: The page number to be returned. Default: **1**
            results: Contains a list of payout statuses. If included, the response returns only executed payouts that
                currently have one of the specified statuses. Possible statuses: - **succeeded**: The payout was sent
                successfully. - **failed**: The payout was not sent due to an error. - **skipped**: The payout was not
                triggered as expected.
            limit: The number of items returned per page. Default: **10**
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/payoutSchedules/{id}/executions"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("id", id)],
            query_params=[
                param[int]("offset", offset),
                param[list[ExecutionResultOrStr] | None]("results", results),
                param[int | None]("limit", limit),
            ],
            decoder=json_decoder[PayoutScheduleExecutions],
            error_mapper=get_balance_accounts_balance_account_id_payout_schedules_id_executions_error_mapper,
            request_options=request_options,
        )

    def get_balance_platforms_balance_platform_id_payout_schedules(
        self,
        balance_platform_id: str,
        *,
        country_code: str | None = None,
        currency: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalancePlatformConfigurations, GetBalancePlatformsBalancePlatformIdPayoutSchedulesErrorBody]:
        """Returns a list of all the payout schedules that are configured for your balance platform. You can use query
        parameters to filter the elements that are returned in the list.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            country_code: The two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__
                country code of the country to which the payout configuration applies.
            currency: The three-character `ISO currency code
                <https://docs.adyen.com/development-resources/currency-codes>`__ of the currency used in the payout
                configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{balancePlatformId}/payoutSchedules"),
            path_params=[param[str]("balancePlatformId", balance_platform_id)],
            query_params=[param[str | None]("countryCode", country_code), param[str | None]("currency", currency)],
            decoder=json_decoder[BalancePlatformConfigurations],
            error_mapper=get_balance_platforms_balance_platform_id_payout_schedules_error_mapper,
            request_options=request_options,
        )

    def get_balance_platforms_balance_platform_id_payout_schedules_id(
        self, balance_platform_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BalancePlatformConfiguration, GetBalancePlatformsBalancePlatformIdPayoutSchedulesIdErrorBody]:
        """Returns the specified managed payout schedule configured on your balance platform.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            id: The unique identifier of the payout configuration for your balance platform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{balancePlatformId}/payoutSchedules/{id}"),
            path_params=[param[str]("balancePlatformId", balance_platform_id), param[str]("id", id)],
            decoder=json_decoder[BalancePlatformConfiguration],
            error_mapper=get_balance_platforms_balance_platform_id_payout_schedules_id_error_mapper,
            request_options=request_options,
        )

    def patch_balance_accounts_balance_account_id_payout_schedules_id(
        self,
        balance_account_id: str,
        id: str,
        body: BalanceAccountConfigurationUpdate | BalanceAccountConfigurationUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceAccountConfiguration, PatchBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody]:
        """Update a managed payout schedule applied to a balance account. If an optional parameter is not included in
        the request, it remains unchanged.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule applied to the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/payoutSchedules/{id}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceAccountConfigurationUpdate | BalanceAccountConfigurationUpdateDict](body),
            decoder=json_decoder[BalanceAccountConfiguration],
            error_mapper=patch_balance_accounts_balance_account_id_payout_schedules_id_error_mapper,
            request_options=request_options,
        )

    def post_balance_accounts_balance_account_id_payout_schedules(
        self,
        balance_account_id: str,
        body: BalanceAccountConfigurationRequest | BalanceAccountConfigurationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceAccountConfiguration, PostBalanceAccountsBalanceAccountIdPayoutSchedulesErrorBody]:
        """Apply a managed payout schedule to a balance account. This payout schedule is based on an existing payout
        schedule in your balance platform.

        Args:
            balance_account_id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/payoutSchedules"),
            path_params=[param[str]("balanceAccountId", balance_account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceAccountConfigurationRequest | BalanceAccountConfigurationRequestDict](body),
            decoder=json_decoder[BalanceAccountConfiguration],
            error_mapper=post_balance_accounts_balance_account_id_payout_schedules_error_mapper,
            request_options=request_options,
        )


class AsyncManagedPayoutSchedulesWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def delete_balance_accounts_balance_account_id_payout_schedules_id(
        self, balance_account_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody]:
        """Delete a payout schedule applied to a balance account.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule applied to the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/payoutSchedules/{id}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=delete_balance_accounts_balance_account_id_payout_schedules_id_error_mapper,
            request_options=request_options,
        )

    async def get_balance_accounts_balance_account_id_payout_schedules(
        self,
        balance_account_id: str,
        *,
        currency: str | None = None,
        cursor: str | None = None,
        limit: int | None = 10,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceAccountConfigurations, GetBalanceAccountsBalanceAccountIdPayoutSchedulesErrorBody]:
        """Returns a list of all managed payout schedules that are configured on a balance account. You can use query
        parameters to filter the elements that are returned in the list.

        Args:
            balance_account_id: The unique identifier of the balance account.
            currency: The three-character `ISO currency code
                <https://docs.adyen.com/development-resources/currency-codes>`__ of the currency used in the payout
                schedule.
            cursor: The ``cursor`` returned in the links of the previous response.
            limit: The number of items returned per page, maximum of 100 items. By default, the response returns 10
                items per page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/payoutSchedules"),
            path_params=[param[str]("balanceAccountId", balance_account_id)],
            query_params=[
                param[str | None]("currency", currency),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            decoder=json_decoder[BalanceAccountConfigurations],
            error_mapper=get_balance_accounts_balance_account_id_payout_schedules_error_mapper,
            request_options=request_options,
        )

    async def get_balance_accounts_balance_account_id_payout_schedules_id(
        self, balance_account_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BalanceAccountConfiguration, GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody]:
        """Returns the specified payout schedule.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule for the balance account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/payoutSchedules/{id}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("id", id)],
            decoder=json_decoder[BalanceAccountConfiguration],
            error_mapper=get_balance_accounts_balance_account_id_payout_schedules_id_error_mapper,
            request_options=request_options,
        )

    async def get_balance_accounts_balance_account_id_payout_schedules_id_executions(
        self,
        balance_account_id: str,
        id: str,
        offset: int,
        *,
        results: list[ExecutionResultOrStr] | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayoutScheduleExecutions, GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdExecutionsErrorBody]:
        """View information about the executions of a managed payout schedule on the specified balance account. An
        execution is an attempt to make a payout according to the payout schedule.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule on the balance account.
            offset: The page number to be returned. Default: **1**
            results: Contains a list of payout statuses. If included, the response returns only executed payouts that
                currently have one of the specified statuses. Possible statuses: - **succeeded**: The payout was sent
                successfully. - **failed**: The payout was not sent due to an error. - **skipped**: The payout was not
                triggered as expected.
            limit: The number of items returned per page. Default: **10**
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/payoutSchedules/{id}/executions"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("id", id)],
            query_params=[
                param[int]("offset", offset),
                param[list[ExecutionResultOrStr] | None]("results", results),
                param[int | None]("limit", limit),
            ],
            decoder=json_decoder[PayoutScheduleExecutions],
            error_mapper=get_balance_accounts_balance_account_id_payout_schedules_id_executions_error_mapper,
            request_options=request_options,
        )

    async def get_balance_platforms_balance_platform_id_payout_schedules(
        self,
        balance_platform_id: str,
        *,
        country_code: str | None = None,
        currency: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalancePlatformConfigurations, GetBalancePlatformsBalancePlatformIdPayoutSchedulesErrorBody]:
        """Returns a list of all the payout schedules that are configured for your balance platform. You can use query
        parameters to filter the elements that are returned in the list.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            country_code: The two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__
                country code of the country to which the payout configuration applies.
            currency: The three-character `ISO currency code
                <https://docs.adyen.com/development-resources/currency-codes>`__ of the currency used in the payout
                configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{balancePlatformId}/payoutSchedules"),
            path_params=[param[str]("balancePlatformId", balance_platform_id)],
            query_params=[param[str | None]("countryCode", country_code), param[str | None]("currency", currency)],
            decoder=json_decoder[BalancePlatformConfigurations],
            error_mapper=get_balance_platforms_balance_platform_id_payout_schedules_error_mapper,
            request_options=request_options,
        )

    async def get_balance_platforms_balance_platform_id_payout_schedules_id(
        self, balance_platform_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BalancePlatformConfiguration, GetBalancePlatformsBalancePlatformIdPayoutSchedulesIdErrorBody]:
        """Returns the specified managed payout schedule configured on your balance platform.

        Args:
            balance_platform_id: The unique identifier of the balance platform.
            id: The unique identifier of the payout configuration for your balance platform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/balancePlatforms/{balancePlatformId}/payoutSchedules/{id}"),
            path_params=[param[str]("balancePlatformId", balance_platform_id), param[str]("id", id)],
            decoder=json_decoder[BalancePlatformConfiguration],
            error_mapper=get_balance_platforms_balance_platform_id_payout_schedules_id_error_mapper,
            request_options=request_options,
        )

    async def patch_balance_accounts_balance_account_id_payout_schedules_id(
        self,
        balance_account_id: str,
        id: str,
        body: BalanceAccountConfigurationUpdate | BalanceAccountConfigurationUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceAccountConfiguration, PatchBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody]:
        """Update a managed payout schedule applied to a balance account. If an optional parameter is not included in
        the request, it remains unchanged.

        Args:
            balance_account_id: The unique identifier of the balance account.
            id: The unique identifier of the payout schedule applied to the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/payoutSchedules/{id}"),
            path_params=[param[str]("balanceAccountId", balance_account_id), param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceAccountConfigurationUpdate | BalanceAccountConfigurationUpdateDict](body),
            decoder=json_decoder[BalanceAccountConfiguration],
            error_mapper=patch_balance_accounts_balance_account_id_payout_schedules_id_error_mapper,
            request_options=request_options,
        )

    async def post_balance_accounts_balance_account_id_payout_schedules(
        self,
        balance_account_id: str,
        body: BalanceAccountConfigurationRequest | BalanceAccountConfigurationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalanceAccountConfiguration, PostBalanceAccountsBalanceAccountIdPayoutSchedulesErrorBody]:
        """Apply a managed payout schedule to a balance account. This payout schedule is based on an existing payout
        schedule in your balance platform.

        Args:
            balance_account_id: The unique identifier of the balance account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/balanceAccounts/{balanceAccountId}/payoutSchedules"),
            path_params=[param[str]("balanceAccountId", balance_account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BalanceAccountConfigurationRequest | BalanceAccountConfigurationRequestDict](body),
            decoder=json_decoder[BalanceAccountConfiguration],
            error_mapper=post_balance_accounts_balance_account_id_payout_schedules_error_mapper,
            request_options=request_options,
        )
