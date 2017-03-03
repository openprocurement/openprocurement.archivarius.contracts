# -*- coding: utf-8 -*-
from iso8601 import parse_date
from datetime import timedelta

STATUS = ['terminated']
TIMEDELTA = timedelta(days=30)


def contract_filter(item, time):
    return item.doc['status'] in STATUS and parse_date(item.key) < (time - TIMEDELTA)
