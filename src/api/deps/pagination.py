from typing import Annotated

from fastapi import Depends, Query
from fastapi import BaseModel

class PaginationParams(BaseModel):
    page: Annotated[int | None, Query(None, ge=1)]
    per_page: Annotated[int | None, Query(None, ge=1, lt=50)]

PaginationDep = Annotated[PaginationParams, Depends()]