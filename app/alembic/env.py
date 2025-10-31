from logging.config import fileConfig

import os

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Add parent directory to Python path so we can import db.py
import sys
here = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(here, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import python-dotenv to load DATABASE_URL from .env
from dotenv import load_dotenv
load_dotenv()

# Get DATABASE_URL from environment
db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise ValueError("DATABASE_URL must be set in environment or .env file")

# Create new config section with our URL
section = config.get_section(config.config_ini_section)
if not section:
    section = {}
section["sqlalchemy.url"] = db_url

# Override the section in the config
def get_config_section(name, default=None):
    if name == config.config_ini_section:
        return section
    return default

config.get_section = get_config_section

# Import all models so they're registered with Base.metadata
from db import Base
import models.country  # This registers the Country model with Base.metadata

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
