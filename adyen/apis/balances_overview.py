from __future__ import annotations

from ..core import ApiResult, AsyncRawClient, BaseRawResponse, RawClient, RequestOptionsOrDict, json_decoder, param
from ..errors.get_balance_overview_companies_company_account_code_balances_error import (
    GetBalanceOverviewCompaniesCompanyAccountCodeBalancesErrorBody,
    get_balance_overview_companies_company_account_code_balances_error_mapper,
)
from ..errors.get_balance_overview_merchants_merchant_account_code_balances_error import (
    GetBalanceOverviewMerchantsMerchantAccountCodeBalancesErrorBody,
    get_balance_overview_merchants_merchant_account_code_balances_error_mapper,
)
from ..models.company_balances import CompanyBalances
from ..models.merchant_balance import MerchantBalance
from ..server.server import Server


class BalancesOverview:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = BalancesOverviewWithRawResponse(client, server)

    def get_balance_overview_companies_company_account_code_balances(
        self, company_account_code: str, currency: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CompanyBalances:
        """Returns an array with details about the balances available for all merchant accounts under your company
        account. For each merchant account, the response returns the following:

        * **Available funds**: The funds in the merchant account that have been settled and are available for use.


        * **Pending balance**: The funds in the merchant account that have not been settled yet.


        * **Next payout amount**: The amount that will be settled to your bank account with the next payout.


        * **Reserve**: The available amount to cover refunds, payouts, chargebacks, and other operational expenses that
            cannot be covered by your in-process funds.


        * **Deposit**: The amount withheld by Adyen to cover potential losses and liabilities due to payment processing.

        Args:
            company_account_code: The unique identifier of your company account.
            currency: The currency for which you want a balances overview.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - Authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Content - A request validation error. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return self._with_raw_response.get_balance_overview_companies_company_account_code_balances(
            company_account_code, currency, request_options=request_options
        ).unwrap()

    def get_balance_overview_merchants_merchant_account_code_balances(
        self, merchant_account_code: str, currency: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MerchantBalance:
        """Returns an overview of the different balances available for the merchant account. This includes details about
        the following:

        * **Available funds**: The funds in the merchant account that have been settled and are available for use.


        * **Pending balance**: The funds in the merchant account that have not been settled yet.


        * **Next payout amount**: The amount that will be settled to your bank account with the next payout.


        * **Reserve**: The available amount to cover refunds, payouts, chargebacks, and other operational expenses that
            cannot be covered by your in-process funds.


        * **Deposit**: The amount withheld by Adyen to cover potential losses and liabilities due to payment processing.

        Args:
            merchant_account_code: The unique identifier of your merchant account.
            currency: The currency for which you want a balances overview.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - Authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Content - A request validation error. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return self._with_raw_response.get_balance_overview_merchants_merchant_account_code_balances(
            merchant_account_code, currency, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> BalancesOverviewWithRawResponse:
        return self._with_raw_response


class AsyncBalancesOverview:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncBalancesOverviewWithRawResponse(client, server)

    async def get_balance_overview_companies_company_account_code_balances(
        self, company_account_code: str, currency: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CompanyBalances:
        """Returns an array with details about the balances available for all merchant accounts under your company
        account. For each merchant account, the response returns the following:

        * **Available funds**: The funds in the merchant account that have been settled and are available for use.


        * **Pending balance**: The funds in the merchant account that have not been settled yet.


        * **Next payout amount**: The amount that will be settled to your bank account with the next payout.


        * **Reserve**: The available amount to cover refunds, payouts, chargebacks, and other operational expenses that
            cannot be covered by your in-process funds.


        * **Deposit**: The amount withheld by Adyen to cover potential losses and liabilities due to payment processing.

        Args:
            company_account_code: The unique identifier of your company account.
            currency: The currency for which you want a balances overview.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - Authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Content - A request validation error. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return (
            await self._with_raw_response.get_balance_overview_companies_company_account_code_balances(
                company_account_code, currency, request_options=request_options
            )
        ).unwrap()

    async def get_balance_overview_merchants_merchant_account_code_balances(
        self, merchant_account_code: str, currency: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MerchantBalance:
        """Returns an overview of the different balances available for the merchant account. This includes details about
        the following:

        * **Available funds**: The funds in the merchant account that have been settled and are available for use.


        * **Pending balance**: The funds in the merchant account that have not been settled yet.


        * **Next payout amount**: The amount that will be settled to your bank account with the next payout.


        * **Reserve**: The available amount to cover refunds, payouts, chargebacks, and other operational expenses that
            cannot be covered by your in-process funds.


        * **Deposit**: The amount withheld by Adyen to cover potential losses and liabilities due to payment processing.

        Args:
            merchant_account_code: The unique identifier of your merchant account.
            currency: The currency for which you want a balances overview.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unauthorized - Authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Content - A request validation error. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return (
            await self._with_raw_response.get_balance_overview_merchants_merchant_account_code_balances(
                merchant_account_code, currency, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncBalancesOverviewWithRawResponse:
        return self._with_raw_response


class BalancesOverviewWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_balance_overview_companies_company_account_code_balances(
        self, company_account_code: str, currency: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CompanyBalances, GetBalanceOverviewCompaniesCompanyAccountCodeBalancesErrorBody]:
        """Returns an array with details about the balances available for all merchant accounts under your company
        account. For each merchant account, the response returns the following:

        * **Available funds**: The funds in the merchant account that have been settled and are available for use.


        * **Pending balance**: The funds in the merchant account that have not been settled yet.


        * **Next payout amount**: The amount that will be settled to your bank account with the next payout.


        * **Reserve**: The available amount to cover refunds, payouts, chargebacks, and other operational expenses that
            cannot be covered by your in-process funds.


        * **Deposit**: The amount withheld by Adyen to cover potential losses and liabilities due to payment processing.

        Args:
            company_account_code: The unique identifier of your company account.
            currency: The currency for which you want a balances overview.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/balanceOverview/companies/{companyAccountCode}/balances"),
            path_params=[param[str]("companyAccountCode", company_account_code)],
            query_params=[param[str]("currency", currency)],
            decoder=json_decoder[CompanyBalances],
            error_mapper=get_balance_overview_companies_company_account_code_balances_error_mapper,
            request_options=request_options,
        )

    def get_balance_overview_merchants_merchant_account_code_balances(
        self, merchant_account_code: str, currency: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MerchantBalance, GetBalanceOverviewMerchantsMerchantAccountCodeBalancesErrorBody]:
        """Returns an overview of the different balances available for the merchant account. This includes details about
        the following:

        * **Available funds**: The funds in the merchant account that have been settled and are available for use.


        * **Pending balance**: The funds in the merchant account that have not been settled yet.


        * **Next payout amount**: The amount that will be settled to your bank account with the next payout.


        * **Reserve**: The available amount to cover refunds, payouts, chargebacks, and other operational expenses that
            cannot be covered by your in-process funds.


        * **Deposit**: The amount withheld by Adyen to cover potential losses and liabilities due to payment processing.

        Args:
            merchant_account_code: The unique identifier of your merchant account.
            currency: The currency for which you want a balances overview.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/balanceOverview/merchants/{merchantAccountCode}/balances"),
            path_params=[param[str]("merchantAccountCode", merchant_account_code)],
            query_params=[param[str]("currency", currency)],
            decoder=json_decoder[MerchantBalance],
            error_mapper=get_balance_overview_merchants_merchant_account_code_balances_error_mapper,
            request_options=request_options,
        )


class AsyncBalancesOverviewWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_balance_overview_companies_company_account_code_balances(
        self, company_account_code: str, currency: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CompanyBalances, GetBalanceOverviewCompaniesCompanyAccountCodeBalancesErrorBody]:
        """Returns an array with details about the balances available for all merchant accounts under your company
        account. For each merchant account, the response returns the following:

        * **Available funds**: The funds in the merchant account that have been settled and are available for use.


        * **Pending balance**: The funds in the merchant account that have not been settled yet.


        * **Next payout amount**: The amount that will be settled to your bank account with the next payout.


        * **Reserve**: The available amount to cover refunds, payouts, chargebacks, and other operational expenses that
            cannot be covered by your in-process funds.


        * **Deposit**: The amount withheld by Adyen to cover potential losses and liabilities due to payment processing.

        Args:
            company_account_code: The unique identifier of your company account.
            currency: The currency for which you want a balances overview.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/balanceOverview/companies/{companyAccountCode}/balances"),
            path_params=[param[str]("companyAccountCode", company_account_code)],
            query_params=[param[str]("currency", currency)],
            decoder=json_decoder[CompanyBalances],
            error_mapper=get_balance_overview_companies_company_account_code_balances_error_mapper,
            request_options=request_options,
        )

    async def get_balance_overview_merchants_merchant_account_code_balances(
        self, merchant_account_code: str, currency: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MerchantBalance, GetBalanceOverviewMerchantsMerchantAccountCodeBalancesErrorBody]:
        """Returns an overview of the different balances available for the merchant account. This includes details about
        the following:

        * **Available funds**: The funds in the merchant account that have been settled and are available for use.


        * **Pending balance**: The funds in the merchant account that have not been settled yet.


        * **Next payout amount**: The amount that will be settled to your bank account with the next payout.


        * **Reserve**: The available amount to cover refunds, payouts, chargebacks, and other operational expenses that
            cannot be covered by your in-process funds.


        * **Deposit**: The amount withheld by Adyen to cover potential losses and liabilities due to payment processing.

        Args:
            merchant_account_code: The unique identifier of your merchant account.
            currency: The currency for which you want a balances overview.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/balanceOverview/merchants/{merchantAccountCode}/balances"),
            path_params=[param[str]("merchantAccountCode", merchant_account_code)],
            query_params=[param[str]("currency", currency)],
            decoder=json_decoder[MerchantBalance],
            error_mapper=get_balance_overview_merchants_merchant_account_code_balances_error_mapper,
            request_options=request_options,
        )
