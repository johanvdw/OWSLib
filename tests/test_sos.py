import pytest

from unittest import TestCase

from owslib.sos import SensorObservationService

class TestSos(TestCase):
    @pytest.mark.remote
    def test_content(self):
        service = SensorObservationService('http://sensorweb.demo.52north.org/52n-sos-webapp/sos/kvp',       version='2.0.0')
        assert "http://www.52north.org/test/offering/1" in service.contents
