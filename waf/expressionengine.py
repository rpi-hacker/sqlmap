#!/usr/bin/env python

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.core.enums import HTTP_HEADER
from lib.core.settings import WAF_ATTACK_VECTORS

__product__ = "ExpressionEngine (EllisLab)"

def detect(get_page):
    retval = False

    for vector in WAF_ATTACK_VECTORS:
        page, headers, _ = get_page(get=vector)
        retval |= any((page or "").strip() == _ for _ in ("Invalid GET Data", "Invalid URI")) and re.search(r"\bexp_last_", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
        if retval:
            break

    return retval
