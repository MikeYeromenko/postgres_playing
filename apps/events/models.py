from sqlalchemy import UniqueConstraint, Column, TIMESTAMP, ForeignKey, SMALLINT, DECIMAL, text, VARCHAR, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from bases import Base, UUIDMixin, CreatedAtMixin

__all__ = ["EventsBtree", "CmBtree"]


def _panels_table():
    from ..appliances.models import Panels

    return Panels


class EventsBtree(Base, UUIDMixin, CreatedAtMixin):
    __table_args__ = (UniqueConstraint("date_time", "panel_id", "meter_number"),)

    date_time = Column(TIMESTAMP(timezone=True), nullable=False, index=True)  # Date & Time
    panel_id = Column(
        UUID(as_uuid=True), ForeignKey(_panels_table().id, ondelete="CASCADE"), nullable=False, index=True
    )  # PanelID
    meter_number = Column(SMALLINT, nullable=False, index=True)  # MeterID
    frequency = Column(DECIMAL, server_default=text("0"), nullable=False)  # F => AVG
    voltage = Column(DECIMAL, server_default=text("0"), nullable=False)  # V => AVG
    power_factor = Column(DECIMAL, server_default=text("0"), nullable=False)  # TPF => AVG
    total_current = Column(DECIMAL, server_default=text("0"), nullable=False)  # TI => SUM
    total_active_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # TP => SUM
    total_reactive_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # TQ => SUM
    total_active_energy = Column(DECIMAL, server_default=text("0"), nullable=False)  # TAE => SUM
    total_reactive_energy = Column(DECIMAL, server_default=text("0"), nullable=False)  # TRE => SUM
    total_apparent_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # TS => SUM

    channel_metrics = relationship("CmBtree", back_populates="event", cascade="all, delete-orphan")
    panel = relationship(_panels_table, sync_backref=False)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(date_time={self.date_time}, panel_id={self.panel_id}, "
            f"meter_id={self.meter_number})"
        )


class CmBtree(Base, UUIDMixin, CreatedAtMixin):
    __table_args__ = (
        UniqueConstraint("event_id", "channel", "phase"),
        Index("ix_btree_metrics_event_id_channel", "event_id", "channel", "phase", unique=True),
    )

    event_id = Column(UUID(as_uuid=True), ForeignKey("events_btree.id", ondelete="CASCADE"), nullable=False, index=True)
    date_time = Column(TIMESTAMP(timezone=True), nullable=False, index=True)
    panel_id = Column(UUID(as_uuid=True), ForeignKey("panels.id", ondelete="CASCADE"), nullable=False, index=True)
    meter_number = Column(SMALLINT, nullable=False, index=True)
    phase = Column(VARCHAR(length=1))  # A, B, C or NULL
    channel = Column(SMALLINT, nullable=False)
    current = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}I
    active_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}P
    reactive_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}Q
    apparent_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}S
    frequency = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}F
    active_energy = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}AE
    reactive_energy = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}RE
    power_factor = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}PF
    current_harmonics = Column(DECIMAL)  # C{}ITHD

    event = relationship("EventsBtree", back_populates="channel_metrics")
    panel = relationship(_panels_table, sync_backref=False)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(date_time={self.date_time}, event_id={self.event_id}, channel={self.channel})"
        )


class Events(Base, UUIDMixin, CreatedAtMixin):
    __table_args__ = (UniqueConstraint("date_time", "panel_id", "meter_number"),)

    date_time = Column(TIMESTAMP(timezone=True), nullable=False)  # Date & Time
    panel_id = Column(
        UUID(as_uuid=True), ForeignKey(_panels_table().id, ondelete="CASCADE"), nullable=False)  # PanelID
    meter_number = Column(SMALLINT, nullable=False)  # MeterID
    frequency = Column(DECIMAL, server_default=text("0"), nullable=False)  # F => AVG
    voltage = Column(DECIMAL, server_default=text("0"), nullable=False)  # V => AVG
    power_factor = Column(DECIMAL, server_default=text("0"), nullable=False)  # TPF => AVG
    total_current = Column(DECIMAL, server_default=text("0"), nullable=False)  # TI => SUM
    total_active_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # TP => SUM
    total_reactive_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # TQ => SUM
    total_active_energy = Column(DECIMAL, server_default=text("0"), nullable=False)  # TAE => SUM
    total_reactive_energy = Column(DECIMAL, server_default=text("0"), nullable=False)  # TRE => SUM
    total_apparent_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # TS => SUM

    channel_metrics = relationship("Cm", back_populates="event", cascade="all, delete-orphan")
    panel = relationship(_panels_table, sync_backref=False)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(date_time={self.date_time}, panel_id={self.panel_id}, "
            f"meter_id={self.meter_number})"
        )


class Cm(Base, UUIDMixin, CreatedAtMixin):
    __table_args__ = (
        UniqueConstraint("event_id", "channel", "phase"),
        Index("ix_metrics_event_id_channel", "event_id", "channel", "phase", unique=True),
    )

    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id", ondelete="CASCADE"), nullable=False, index=True)
    date_time = Column(TIMESTAMP(timezone=True), nullable=False, index=True)
    panel_id = Column(UUID(as_uuid=True), ForeignKey("panels.id", ondelete="CASCADE"), nullable=False, index=True)
    meter_number = Column(SMALLINT, nullable=False, index=True)
    phase = Column(VARCHAR(length=1))  # A, B, C or NULL
    channel = Column(SMALLINT, nullable=False)
    current = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}I
    active_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}P
    reactive_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}Q
    apparent_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}S
    frequency = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}F
    active_energy = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}AE
    reactive_energy = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}RE
    power_factor = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}PF
    current_harmonics = Column(DECIMAL)  # C{}ITHD

    event = relationship("Events", back_populates="channel_metrics")
    panel = relationship(_panels_table, sync_backref=False)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(date_time={self.date_time}, event_id={self.event_id}, channel={self.channel})"
        )


class Events1(Base, UUIDMixin, CreatedAtMixin):
    __table_args__ = (UniqueConstraint("date_time", "panel_id", "meter_number"),)

    date_time = Column(TIMESTAMP(timezone=True), nullable=False)  # Date & Time
    panel_id = Column(
        UUID(as_uuid=True), ForeignKey(_panels_table().id, ondelete="CASCADE"), nullable=False, index=True
    )  # PanelID
    meter_number = Column(SMALLINT, nullable=False)  # MeterID
    frequency = Column(DECIMAL, server_default=text("0"), nullable=False)  # F => AVG
    voltage = Column(DECIMAL, server_default=text("0"), nullable=False)  # V => AVG
    power_factor = Column(DECIMAL, server_default=text("0"), nullable=False)  # TPF => AVG
    total_current = Column(DECIMAL, server_default=text("0"), nullable=False)  # TI => SUM
    total_active_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # TP => SUM
    total_reactive_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # TQ => SUM
    total_active_energy = Column(DECIMAL, server_default=text("0"), nullable=False)  # TAE => SUM
    total_reactive_energy = Column(DECIMAL, server_default=text("0"), nullable=False)  # TRE => SUM
    total_apparent_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # TS => SUM

    channel_metrics = relationship("Cm1", back_populates="event", cascade="all, delete-orphan")
    panel = relationship(_panels_table, sync_backref=False)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(date_time={self.date_time}, panel_id={self.panel_id}, "
            f"meter_id={self.meter_number})"
        )


class Cm1(Base, UUIDMixin, CreatedAtMixin):
    __table_args__ = (
        UniqueConstraint("event_id", "channel", "phase"),
        Index("ix_cm1_metrics_event_id_channel", "event_id", "channel", "phase", unique=True),
    )

    event_id = Column(UUID(as_uuid=True), ForeignKey("events1.id", ondelete="CASCADE"), nullable=False)
    date_time = Column(TIMESTAMP(timezone=True), nullable=False)
    panel_id = Column(UUID(as_uuid=True), ForeignKey("panels.id", ondelete="CASCADE"), nullable=False)
    meter_number = Column(SMALLINT, nullable=False)
    phase = Column(VARCHAR(length=1))  # A, B, C or NULL
    channel = Column(SMALLINT, nullable=False)
    current = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}I
    active_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}P
    reactive_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}Q
    apparent_power = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}S
    frequency = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}F
    active_energy = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}AE
    reactive_energy = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}RE
    power_factor = Column(DECIMAL, server_default=text("0"), nullable=False)  # C{}PF
    current_harmonics = Column(DECIMAL)  # C{}ITHD

    event = relationship("Events1", back_populates="channel_metrics")
    panel = relationship(_panels_table, sync_backref=False)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(date_time={self.date_time}, event_id={self.event_id}, channel={self.channel})"
        )
