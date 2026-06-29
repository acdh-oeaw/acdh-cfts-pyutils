import unittest

from acdh_cfts_pyutils import CFTS_SCHEMA

CFTS_SCHEMA_FIELD_NAMES = [
    "id",
    "rec_id",
    "resolver",
    "project",
    "title",
    "full_text",
    "date",
    "year",
    "persons",
    "places",
    "orgs",
    "works",
    "keywords",
]


class TestCfts(unittest.TestCase):
    """Tests for `acdh_cfts_pyutils` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001(self):
        self.assertIsInstance(CFTS_SCHEMA, dict)

    def test_002(self):
        self.assertEqual(len(CFTS_SCHEMA.keys()), 3)

    def test_003(self):
        self.assertEqual(len(CFTS_SCHEMA["fields"]), len(CFTS_SCHEMA_FIELD_NAMES))
