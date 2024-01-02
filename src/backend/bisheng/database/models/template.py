from datetime import datetime
from typing import Dict, Optional
from uuid import UUID

from bisheng.database.models.base import SQLModelSerializable
from sqlalchemy import JSON, Column, DateTime, text
from sqlmodel import Field


class TemplateSkillBase(SQLModelSerializable):
    name: str = Field(index=True)
    description: str = Field(index=False)
    data: Optional[Dict] = Field(default=None, sa_column=Column(JSON))
    order_num: Optional[int] = Field(default=True)
    flow_id: Optional[UUID] = Field(index=False)
    create_time: Optional[datetime] = Field(sa_column=Column(
        DateTime, nullable=False, index=True, server_default=text('CURRENT_TIMESTAMP')))
    update_time: Optional[datetime] = Field(
        sa_column=Column(DateTime,
                         nullable=False,
                         server_default=text('CURRENT_TIMESTAMP'),
                         onupdate=text('CURRENT_TIMESTAMP')))


class Template(TemplateSkillBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class TemplateRead(TemplateSkillBase):
    id: int
    name: str


class TemplateCreate(TemplateSkillBase):
    pass


class TemplateUpdate(SQLModelSerializable):
    name: Optional[str] = None
    description: Optional[str] = None
    data: Optional[Dict] = None
    order_num: Optional[int] = None
