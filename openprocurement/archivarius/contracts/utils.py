# -*- coding: utf-8 -*-

from openprocurement.archivarius.core.utils import Root


def factory(request):
    request.validated['contract_src'] = {}
    root = Root(request)
    if not request.matchdict or not request.matchdict.get('contract_id'):
        return root
    request.validated['contract_id'] = request.matchdict['contract_id']
    contract = request.contract
    contract.__parent__ = root
    request.validated['contract'] = request.validated['db_doc'] = contract
    return contract
