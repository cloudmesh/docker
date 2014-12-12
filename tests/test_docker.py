""" run with

nosetests -v --nocapture

"""
from __future__ import print_function
from cloudmesh_common.util import HEADING
from cloudmesh_common.logger import LOGGER, LOGGING_ON, LOGGING_OFF

log = LOGGER(__file__)


class Test:

    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_01_sample(self):
        HEADING()
        a = 1
        b = 2
        assert (a + b == 3)
