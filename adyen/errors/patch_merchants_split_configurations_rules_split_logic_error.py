from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PatchMerchantsSplitConfigurationsRulesSplitLogicErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PatchMerchantsSplitConfigurationsRulesSplitLogicError:
    def map(self, response: HttpResponse) -> PatchMerchantsSplitConfigurationsRulesSplitLogicErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


patch_merchants_split_configurations_rules_split_logic_error_mapper: Final[
    ErrorMapper[PatchMerchantsSplitConfigurationsRulesSplitLogicErrorBody]
] = _PatchMerchantsSplitConfigurationsRulesSplitLogicError()
