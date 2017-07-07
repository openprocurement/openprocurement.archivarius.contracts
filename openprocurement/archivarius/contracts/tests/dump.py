# -*- coding: utf-8 -*-
import unittest
from openprocurement.archivarius.contracts.tests.base import BaseContractArchivariusWebTest


class ContractArchivariusResourceTest(BaseContractArchivariusWebTest):

    def test_dump_tender_invalid(self):
        response = self.app.get('/contracts/some_id/dump', status=404)
        self.assertEqual(response.status, '404 Not Found')
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json['status'], 'error')
        self.assertEqual(response.json['errors'], [
            {u'description': u'Not Found', u'location': u'url', u'name': u'contract_id'}
        ])

        response = self.app.get('/contracts/{}/dump'.format(self.contract_id), status=403)
        self.assertEqual(response.status, '403 Forbidden')
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json['status'], 'error')
        self.assertEqual(response.json['errors'], [
            {u'description': u'Forbidden', u'location': u'url', u'name': u'permission'}
        ])

    def test_dump_tender(self):
        self.app.authorization = ('Basic', ('archivarius', ''))
        response = self.app.get('/contracts/{}/dump'.format(self.contract_id))
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.content_type, 'application/json')
        self.assertIn('data', response.json)

    def test_delete_tender_invalid(self):
        response = self.app.delete('/contracts/some_id/dump', status=404)
        self.assertEqual(response.status, '404 Not Found')
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json['status'], 'error')
        self.assertEqual(response.json['errors'], [
            {u'description': u'Not Found', u'location': u'url', u'name': u'contract_id'}
        ])

        response = self.app.delete('/contracts/{}/dump'.format(self.contract_id), status=403)
        self.assertEqual(response.status, '403 Forbidden')
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json['status'], 'error')
        self.assertEqual(response.json['errors'], [
            {u'description': u'Forbidden', u'location': u'url', u'name': u'permission'}
        ])

    def test_delete_tender(self):
        self.app.authorization = ('Basic', ('archivarius', ''))
        response = self.app.delete('/contracts/{}/dump'.format(self.contract_id))
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.content_type, 'application/json')
        self.assertIn('data', response.json)

        response = self.app.get('/contracts/{}/dump'.format(self.contract_id), status=410)
        self.assertEqual(response.status, '410 Gone')
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json['status'], 'error')
        self.assertEqual(response.json['errors'], [
            {u'description': u'Archived', u'location': u'url', u'name': u'contract_id'}
        ])


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ContractArchivariusResourceTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
