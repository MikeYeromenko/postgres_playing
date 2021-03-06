"""Initial

Revision ID: f57ae41b3a59
Revises: 
Create Date: 2022-06-27 18:35:06.460130+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f57ae41b3a59'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('name', sa.VARCHAR(length=256), nullable=False),
    sa.Column('area', sa.DECIMAL(), nullable=False),
    sa.Column('tcl', sa.DECIMAL(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_locations'))
    )
    op.create_table('meter_types',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('number_of_channels', sa.SMALLINT(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_meter_types'))
    )
    op.create_index(op.f('ix_meter_types_name'), 'meter_types', ['name'], unique=True)
    op.create_table('panels',
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('location_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('node', sa.VARCHAR(length=64), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('description', sa.VARCHAR(length=256), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], name=op.f('fk_panels_location_id_locations'), ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_panels'))
    )
    op.create_table('events',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('date_time', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('panel_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('meter_number', sa.SMALLINT(), nullable=False),
    sa.Column('frequency', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('voltage', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('power_factor', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_current', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_active_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_reactive_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_active_energy', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_reactive_energy', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_apparent_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.ForeignKeyConstraint(['panel_id'], ['panels.id'], name=op.f('fk_events_panel_id_panels'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_events')),
    sa.UniqueConstraint('date_time', 'panel_id', 'meter_number', name=op.f('uq_events_date_time'))
    )
    op.create_table('events1',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('date_time', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('panel_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('meter_number', sa.SMALLINT(), nullable=False),
    sa.Column('frequency', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('voltage', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('power_factor', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_current', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_active_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_reactive_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_active_energy', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_reactive_energy', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_apparent_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.ForeignKeyConstraint(['panel_id'], ['panels.id'], name=op.f('fk_events1_panel_id_panels'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_events1')),
    sa.UniqueConstraint('date_time', 'panel_id', 'meter_number', name=op.f('uq_events1_date_time'))
    )
    op.create_index(op.f('ix_events1_panel_id'), 'events1', ['panel_id'], unique=False)
    op.create_table('events_btree',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('date_time', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('panel_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('meter_number', sa.SMALLINT(), nullable=False),
    sa.Column('frequency', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('voltage', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('power_factor', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_current', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_active_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_reactive_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_active_energy', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_reactive_energy', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_apparent_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.ForeignKeyConstraint(['panel_id'], ['panels.id'], name=op.f('fk_events_btree_panel_id_panels'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_events_btree')),
    sa.UniqueConstraint('date_time', 'panel_id', 'meter_number', name=op.f('uq_events_btree_date_time'))
    )
    op.create_index(op.f('ix_events_btree_date_time'), 'events_btree', ['date_time'], unique=False)
    op.create_index(op.f('ix_events_btree_meter_number'), 'events_btree', ['meter_number'], unique=False)
    op.create_index(op.f('ix_events_btree_panel_id'), 'events_btree', ['panel_id'], unique=False)
    op.create_table('meters',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('panel_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('meter_type_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('meter_id', sa.SMALLINT(), nullable=False),
    sa.ForeignKeyConstraint(['meter_type_id'], ['meter_types.id'], name=op.f('fk_meters_meter_type_id_meter_types')),
    sa.ForeignKeyConstraint(['panel_id'], ['panels.id'], name=op.f('fk_meters_panel_id_panels'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_meters'))
    )
    op.create_table('cm',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('event_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date_time', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('panel_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('meter_number', sa.SMALLINT(), nullable=False),
    sa.Column('phase', sa.VARCHAR(length=1), nullable=True),
    sa.Column('channel', sa.SMALLINT(), nullable=False),
    sa.Column('current', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('active_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('reactive_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('apparent_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('frequency', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('active_energy', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('reactive_energy', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('power_factor', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('current_harmonics', sa.DECIMAL(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name=op.f('fk_cm_event_id_events'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['panel_id'], ['panels.id'], name=op.f('fk_cm_panel_id_panels'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cm')),
    sa.UniqueConstraint('event_id', 'channel', 'phase', name=op.f('uq_cm_event_id'))
    )
    op.create_index(op.f('ix_cm_date_time'), 'cm', ['date_time'], unique=False)
    op.create_index(op.f('ix_cm_event_id'), 'cm', ['event_id'], unique=False)
    op.create_index(op.f('ix_cm_meter_number'), 'cm', ['meter_number'], unique=False)
    op.create_index(op.f('ix_cm_panel_id'), 'cm', ['panel_id'], unique=False)
    op.create_index('ix_metrics_event_id_channel', 'cm', ['event_id', 'channel', 'phase'], unique=True)
    op.create_table('cm1',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('event_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date_time', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('panel_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('meter_number', sa.SMALLINT(), nullable=False),
    sa.Column('phase', sa.VARCHAR(length=1), nullable=True),
    sa.Column('channel', sa.SMALLINT(), nullable=False),
    sa.Column('current', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('active_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('reactive_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('apparent_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('frequency', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('active_energy', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('reactive_energy', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('power_factor', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('current_harmonics', sa.DECIMAL(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name=op.f('fk_cm1_event_id_events'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['panel_id'], ['panels.id'], name=op.f('fk_cm1_panel_id_panels'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cm1')),
    sa.UniqueConstraint('event_id', 'channel', 'phase', name=op.f('uq_cm1_event_id'))
    )
    op.create_index('ix_cm1_metrics_event_id_channel', 'cm1', ['event_id', 'channel', 'phase'], unique=True)
    op.create_table('cm_btree',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("timezone('utc', now())"), nullable=False),
    sa.Column('event_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date_time', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('panel_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('meter_number', sa.SMALLINT(), nullable=False),
    sa.Column('phase', sa.VARCHAR(length=1), nullable=True),
    sa.Column('channel', sa.SMALLINT(), nullable=False),
    sa.Column('current', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('active_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('reactive_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('apparent_power', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('frequency', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('active_energy', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('reactive_energy', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('power_factor', sa.DECIMAL(), server_default=sa.text('0'), nullable=False),
    sa.Column('current_harmonics', sa.DECIMAL(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events_btree.id'], name=op.f('fk_cm_btree_event_id_events_btree'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['panel_id'], ['panels.id'], name=op.f('fk_cm_btree_panel_id_panels'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cm_btree')),
    sa.UniqueConstraint('event_id', 'channel', 'phase', name=op.f('uq_cm_btree_event_id'))
    )
    op.create_index('ix_btree_metrics_event_id_channel', 'cm_btree', ['event_id', 'channel', 'phase'], unique=True)
    op.create_index(op.f('ix_cm_btree_date_time'), 'cm_btree', ['date_time'], unique=False)
    op.create_index(op.f('ix_cm_btree_event_id'), 'cm_btree', ['event_id'], unique=False)
    op.create_index(op.f('ix_cm_btree_meter_number'), 'cm_btree', ['meter_number'], unique=False)
    op.create_index(op.f('ix_cm_btree_panel_id'), 'cm_btree', ['panel_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cm_btree_panel_id'), table_name='cm_btree')
    op.drop_index(op.f('ix_cm_btree_meter_number'), table_name='cm_btree')
    op.drop_index(op.f('ix_cm_btree_event_id'), table_name='cm_btree')
    op.drop_index(op.f('ix_cm_btree_date_time'), table_name='cm_btree')
    op.drop_index('ix_btree_metrics_event_id_channel', table_name='cm_btree')
    op.drop_table('cm_btree')
    op.drop_index('ix_cm1_metrics_event_id_channel', table_name='cm1')
    op.drop_table('cm1')
    op.drop_index('ix_metrics_event_id_channel', table_name='cm')
    op.drop_index(op.f('ix_cm_panel_id'), table_name='cm')
    op.drop_index(op.f('ix_cm_meter_number'), table_name='cm')
    op.drop_index(op.f('ix_cm_event_id'), table_name='cm')
    op.drop_index(op.f('ix_cm_date_time'), table_name='cm')
    op.drop_table('cm')
    op.drop_table('meters')
    op.drop_index(op.f('ix_events_btree_panel_id'), table_name='events_btree')
    op.drop_index(op.f('ix_events_btree_meter_number'), table_name='events_btree')
    op.drop_index(op.f('ix_events_btree_date_time'), table_name='events_btree')
    op.drop_table('events_btree')
    op.drop_index(op.f('ix_events1_panel_id'), table_name='events1')
    op.drop_table('events1')
    op.drop_index(op.f('ix_events_panel_id'), table_name='events')
    op.drop_table('events')
    op.drop_table('panels')
    op.drop_index(op.f('ix_meter_types_name'), table_name='meter_types')
    op.drop_table('meter_types')
    op.drop_table('locations')
    # ### end Alembic commands ###
