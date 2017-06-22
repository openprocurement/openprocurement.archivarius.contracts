# -*- coding: utf-8 -*-
from iso8601 import parse_date
from datetime import timedelta

STATUS = ['terminated']
TIMEDELTA = timedelta(days=100)


def contract_filter(item, time):
    return item.value['status'] in STATUS and parse_date(item.key) < (time - TIMEDELTA)
