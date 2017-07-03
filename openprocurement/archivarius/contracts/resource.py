# -*- coding: utf-8 -*-
import os
from iso8601 import parse_date
from datetime import timedelta

STATUS = ['terminated']
SANDBOX_MODE = os.environ.get('SANDBOX_MODE', False)
TIMEDELTA = timedelta(days=20) if SANDBOX_MODE else timedelta(days=100)


def contract_filter(item, time):
    return item.value['status'] in STATUS and parse_date(item.key) < (time - TIMEDELTA)
