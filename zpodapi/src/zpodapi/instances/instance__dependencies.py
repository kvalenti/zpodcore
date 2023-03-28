from typing import Annotated

from fastapi import Depends, HTTPException, Path

from zpodapi.lib import dependencies
from zpodcommon import models as M

from .instance__services import InstanceService
from .instance__types import InstanceIdType


def get_instance_record(
    *,
    session: dependencies.GetSession,
    id: Annotated[
        InstanceIdType,
        Path(
            examples={
                "id": {"value": "1"},
                "name": {"value": "name=tanzu-lab"},
            },
        ),
    ],
):
    if instance := InstanceService(session=session).get(value=id):
        return instance
    raise HTTPException(status_code=404, detail="Instance not found")


GetInstanceRecordDepends = Depends(get_instance_record)
GetInstanceRecord = Annotated[M.Instance, GetInstanceRecordDepends]
