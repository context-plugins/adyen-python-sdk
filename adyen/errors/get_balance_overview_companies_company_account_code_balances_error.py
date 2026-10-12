from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetBalanceOverviewCompaniesCompanyAccountCodeBalancesErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetBalanceOverviewCompaniesCompanyAccountCodeBalancesError:
    def map(self, status_code: int, content: bytes) -> GetBalanceOverviewCompaniesCompanyAccountCodeBalancesErrorBody:
        match status_code:
            case 401 | 403 | 422:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


get_balance_overview_companies_company_account_code_balances_error_mapper: Final[
    ErrorMapper[GetBalanceOverviewCompaniesCompanyAccountCodeBalancesErrorBody]
] = _GetBalanceOverviewCompaniesCompanyAccountCodeBalancesError()
