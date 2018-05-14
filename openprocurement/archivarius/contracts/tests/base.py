# -*- coding: utf-8 -*-
import os
import webtest
from openprocurement.api.tests.base import PrefixedRequestClass
try:
    from openprocurement.contracting.api.tests.base import BaseContractWebTest
except ImportError:
    from openprocurement.contracting.core.tests.base import BaseContractWebTest

class BaseContractArchivariusWebTest(BaseContractWebTest):

    def setUp(self):
        self.app = webtest.TestApp(
            "config:tests.ini", relative_to=os.path.dirname(__file__))
        self.app.RequestClass = PrefixedRequestClass
        self.app.authorization = self.initial_auth
        self.couchdb_server = self.app.app.registry.couchdb_server
        self.db = self.app.app.registry.db
        if self.docservice:
            self.setUpDS()
        self.create_contract()
