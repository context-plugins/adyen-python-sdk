from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InstitutionalSector(str, Enum):
    """The institutional sector the organization operates within."""

    NON_FINANCIAL_CORPORATION = "nonFinancialCorporation"
    CENTRAL_BANK = "centralBank"
    CREDIT_INSTITUTIONS = "creditInstitutions"
    DEPOSIT_TAKING_CORPORATIONS = "depositTakingCorporations"
    MONEY_MARKET_FUNDS = "moneyMarketFunds"
    NON_MMF_INVESTMENT_FUNDS = "nonMMFInvestmentFunds"
    FINANCIAL_VEHICLE_CORPORATION = "financialVehicleCorporation"
    OTHER_FINANCIAL_INTERMEDIARIES = "otherFinancialIntermediaries"
    FINANCIAL_AUXILIARIES = "financialAuxiliaries"
    CAPTIVE_FINANCIAL_INSTITUTIONS_AND_MONEY_LENDERS = "captiveFinancialInstitutionsAndMoneyLenders"
    INSURANCE_CORPORATIONS = "insuranceCorporations"
    PENSION_FUNDS = "pensionFunds"
    CENTRAL_GOVERNMENT = "centralGovernment"
    STATE_GOVERNMENT = "stateGovernment"
    LOCAL_GOVERNMENT = "localGovernment"
    SOCIAL_SECURITY_FUNDS = "socialSecurityFunds"
    NON_PROFIT_INSTITUTIONS_SERVING_HOUSEHOLDS = "nonProfitInstitutionsServingHouseholds"

    __str__ = str.__str__


InstitutionalSectorOrStr: TypeAlias = Annotated[InstitutionalSector | str, open_enum_validator(InstitutionalSector)]
