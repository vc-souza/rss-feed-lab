from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Feed(Base):
    """
    RSS feed characteristics and configuration.
    """

    __tablename__ = "feeds"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(unique=True)
    title: Mapped[str] = mapped_column()
