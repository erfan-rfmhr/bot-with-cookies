from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import sqltypes


class BaseTable(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(sqltypes.INTEGER, primary_key=True)

class BaseUserTable(BaseTable):
    __tablename__ = "user"
    username: Mapped[str] = mapped_column(sqltypes.VARCHAR(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(sqltypes.VARCHAR(255), nullable=False)
    is_admin: Mapped[bool] = mapped_column(sqltypes.BOOLEAN, nullable=False, default=False)

    def __str__(self):
        return f"{self.__class__.__name__}({self.username})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.username}, {self.password})"
