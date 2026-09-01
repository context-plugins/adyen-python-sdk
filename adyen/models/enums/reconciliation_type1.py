from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReconciliationType1(str, Enum):
    """Type of Reconciliation requested by the Sale to the POI. Possible values:
    * **AcquirerReconciliation**
    * **AcquirerSynchronisation**
    * **PreviousReconciliation**
    * **SaleReconciliation**"""

    SALE_RECONCILIATION = "SaleReconciliation"
    ACQUIRER_SYNCHRONISATION = "AcquirerSynchronisation"
    ACQUIRER_RECONCILIATION = "AcquirerReconciliation"
    PREVIOUS_RECONCILIATION = "PreviousReconciliation"

    __str__ = str.__str__


ReconciliationType1OrStr: TypeAlias = Annotated[ReconciliationType1 | str, open_enum_validator(ReconciliationType1)]
