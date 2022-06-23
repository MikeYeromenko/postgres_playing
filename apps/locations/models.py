from sqlalchemy import Column, VARCHAR, DECIMAL
from sqlalchemy.orm import relationship

from bases import Base, UUIDMixin, CreatedUpdatedMixin

__all__ = ["Locations"]


def _panels_table():
    from ..appliances.models import Panels

    return Panels


class Locations(Base, UUIDMixin, CreatedUpdatedMixin):
    name = Column(VARCHAR(length=256), nullable=False)
    area = Column(DECIMAL, nullable=False)
    tcl = Column(DECIMAL, nullable=True)

    panels = relationship(_panels_table, back_populates="location")

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self.id}, name={self.name}, area={self.area}, "
            f"tcl={self.tcl})"
        )
