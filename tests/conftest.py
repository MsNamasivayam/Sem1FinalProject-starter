"""
Shared fixtures for all test files in this folder.
pytest finds this file automatically, so test files
never need to import from it.
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from database import Base

pass
