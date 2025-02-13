"""first migrations

Revision ID: a3bd5a59ba36
Revises: 8a7dbe430409
Create Date: 2024-07-07 16:32:08.476268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3bd5a59ba36'
down_revision = '8a7dbe430409'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('jury_examinateur_id_fkey', 'jury', type_='foreignkey')
    op.drop_constraint('jury_rapporteur_id_fkey', 'jury', type_='foreignkey')
    op.drop_constraint('jury_president_id_fkey', 'jury', type_='foreignkey')
    op.create_foreign_key(None, 'jury', 'enseignant', ['president_id'], ['id'], source_schema='public', ondelete='CASCADE')
    op.create_foreign_key(None, 'jury', 'enseignant', ['rapporteur_id'], ['id'], source_schema='public', ondelete='CASCADE')
    op.create_foreign_key(None, 'jury', 'enseignant', ['examinateur_id'], ['id'], source_schema='public', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'jury', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'jury', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'jury', schema='public', type_='foreignkey')
    op.create_foreign_key('jury_president_id_fkey', 'jury', 'enseignant', ['president_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('jury_rapporteur_id_fkey', 'jury', 'enseignant', ['rapporteur_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('jury_examinateur_id_fkey', 'jury', 'enseignant', ['examinateur_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
