# -*- coding: utf-8 -*-
from openprocurement.contracting.core.utils import contractingresource
from openprocurement.archivarius.core.utils import ArchivariusResource
from openprocurement.archivarius.contracts.utils import factory


@contractingresource(name='Contract Archivarius',
                     path='/contracts/{contract_id}/dump',
                     description="Contract Archivarius View",
                     factory=factory)
class ContractArchivariusResource(ArchivariusResource):

    pass
