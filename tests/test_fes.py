from owslib.fes import *
from owslib.etree import etree
from owslib.wfs import WebFeatureService

import pytest
from tests.utils import service_ok

SERVICE_URL = 'https://www.dov.vlaanderen.be/geoserver/wfs'


@pytest.mark.online
@pytest.mark.skipif(not service_ok(SERVICE_URL),
                    reason="WFS service is unreachable")
def test_fes_dov():
    wfs11 = WebFeatureService(url=SERVICE_URL, version='1.1.0')
    filter = PropertyIsLike(propertyname='dov', literal='kb28d81w-B115', wildCard='*')
    filterxml = etree.tostring(filter.toXML()).decode("utf-8")
    print(filterxml)
    response = wfs11.getfeature(typename='g3dv2:g3dv2_bo_0900_de_b', filter=filterxml)
    out = open('/tmp/data.gml', 'wb')
    out.write(bytes(response.read(), 'UTF-8'))
    out.close()

@pytest.mark.online
@pytest.mark.skipif(not service_ok(SERVICE_URL),
                    reason="WFS service is unreachable")
def test_fes_dov_20():
    wfs20 = WebFeatureService(url=SERVICE_URL, version='2.0.0')
    filter = PropertyIsLike(propertyname='g3dv2:dov', literal='kb28d81w-B115', wildCard='*')
    filterxml = etree.tostring(filter.toXML(version='2.0.0')).decode("utf-8")
    print(filterxml)
    response = wfs20.getfeature(typename='g3dv2:g3dv2_bo_0900_de_b', filter=filterxml)
    out = open('/tmp/data20.gml', 'wb')
    out.write(bytes(response.read(), 'UTF-8'))
    out.close()

import logging
logging.basicConfig(level=logging.DEBUG)

test_fes_dov()
test_fes_dov_20()
