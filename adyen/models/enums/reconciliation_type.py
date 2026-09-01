from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReconciliationType(str, Enum):
    """Possible values:
    * **SaleReconciliation**
    * **AcquirerSynchronisation**
    * **AcquirerReconciliation**
    * **PreviousReconciliation**"""

    SALE_RECONCILIATION = "SaleReconciliation"
    ACQUIRER_SYNCHRONISATION = "AcquirerSynchronisation"
    ACQUIRER_RECONCILIATION = "AcquirerReconciliation"
    PREVIOUS_RECONCILIATION = "PreviousReconciliation"

    __str__ = str.__str__


ReconciliationTypeOrStr: TypeAlias = Annotated[ReconciliationType | str, open_enum_validator(ReconciliationType)]
