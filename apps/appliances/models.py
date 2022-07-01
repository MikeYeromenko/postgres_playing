import uuid

from sqlalchemy import Column, text, ForeignKey, VARCHAR, SMALLINT, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from bases import Base, CreatedUpdatedMixin, UUIDMixin, CreatedAtMixin

__all__ = ["Panels", "Meters", "MeterTypes"]


def _locations_table():
    from ..locations.models import Locations

    return Locations


class Panels(Base, CreatedUpdatedMixin):
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, server_default=text("gen_random_uuid()"), primary_key=True)
    location_id = Column(UUID(as_uuid=True), ForeignKey(_locations_table().id, ondelete="SET NULL"), nullable=True)
    node = Column(VARCHAR(length=64), nullable=False)
    name = Column(VARCHAR(length=128), nullable=False)
    description = Column(VARCHAR(length=256))

    meters = relationship("Meters", back_populates="panel", order_by="Meters.meter_id")
    location = relationship(_locations_table, back_populates="panels")

    def __repr__(self):
        return f"{self.__class__.__name__}(location_id={self.location_id}, node='{self.node}', name='{self.name}')"


class MeterTypes(Base, UUIDMixin):
    name = Column(VARCHAR(length=128), nullable=False, unique=True, index=True)
    number_of_channels = Column(SMALLINT, nullable=False)

    meters = relationship("Meters", back_populates="meter_type")

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', number_of_channels={self.number_of_channels})"


class Meters(Base, UUIDMixin, CreatedAtMixin):
    panel_id = Column(UUID(as_uuid=True), ForeignKey("panels.id", ondelete="CASCADE"), nullable=False)
    meter_type_id = Column(UUID(as_uuid=True), ForeignKey("meter_types.id"))
    meter_id = Column(SMALLINT, nullable=False)

    meter_type = relationship("MeterTypes", back_populates="meters")
    panel = relationship("Panels", back_populates="meters")

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(panel_id={self.panel_id}, meter_type_id={self.meter_type_id}, "
            f"meter_id={self.meter_id})"
        )


class Devices(Base, UUIDMixin, CreatedUpdatedMixin):
    name = Column(VARCHAR(length=128), nullable=False, unique=True, index=True)
    color = Column(VARCHAR(length=30), nullable=False)
    icon = Column(VARCHAR(length=128), nullable=False)

    device_meters = relationship("DeviceMeters", back_populates="device")

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', color='{self.color}', icon='{self.icon}')"


class DeviceMeters(Base, UUIDMixin, CreatedAtMixin):
    __table_args__ = (UniqueConstraint("meter_id", "channel"),)

    device_id = Column(UUID(as_uuid=True), ForeignKey("devices.id", ondelete="CASCADE"), nullable=False)
    meter_id = Column(UUID(as_uuid=True), ForeignKey("meters.id", ondelete="CASCADE"), nullable=False)
    channel = Column(SMALLINT, nullable=False)

    device = relationship("Devices", back_populates="device_meters")
    meter = relationship("Meters", back_populates="device_meters")

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(device_id={self.device_id}, meter_id={self.meter_id}, channel={self.channel})"
        )
