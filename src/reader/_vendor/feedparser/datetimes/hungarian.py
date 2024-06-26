# Copyright 2010-2021 Kurt McKee <contactme@kurtmckee.org>
# Copyright 2002-2008 Mark Pilgrim
# All rights reserved.
#
# This file is a part of feedparser.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import re

from reader._vendor.feedparser.datetimes.w3dtf import _parse_date_w3dtf

branch_coverage = { 
    "parse_date_hungarian_1": False, 
    "parse_date_hungarian_2": False, 
    "parse_date_hungarian_3": False, 
    "parse_date_hungarian_4": False,
    "parse_date_hungarian_5": False,
    "parse_date_hungarian_6": False
} 

# Unicode strings for Hungarian date strings
_hungarian_months = {
    'janu\u00e1r':   '01',  # e1 in iso-8859-2
    'febru\u00e1ri': '02',  # e1 in iso-8859-2
    'm\u00e1rcius':  '03',  # e1 in iso-8859-2
    '\u00e1prilis':  '04',  # e1 in iso-8859-2
    'm\u00e1ujus':   '05',  # e1 in iso-8859-2
    'j\u00fanius':   '06',  # fa in iso-8859-2
    'j\u00falius':   '07',  # fa in iso-8859-2
    'augusztus':     '08',
    'szeptember':    '09',
    'okt\u00f3ber':  '10',  # f3 in iso-8859-2
    'november':      '11',
    'december':      '12',
}

_hungarian_date_format_re = re.compile(r'(\d{4})-([^-]+)-(\d{,2})T(\d{,2}):(\d{2})([+-](\d{,2}:\d{2}))')


def _parse_date_hungarian(date_string):
    """Parse a string according to a Hungarian 8-bit date format."""
    m = _hungarian_date_format_re.match(date_string)
    if not m or m.group(2) not in _hungarian_months:
        branch_coverage["parse_date_hungarian_1"] = True 
        branch_coverage_print_hungarian()
        return None
    else:
        branch_coverage["parse_date_hungarian_2"] = True 
    month = _hungarian_months[m.group(2)]
    day = m.group(3)
    if len(day) == 1:
        branch_coverage["parse_date_hungarian_3"] = True 
        day = '0' + day
    else:
        branch_coverage["parse_date_hungarian_4"] = True 
    hour = m.group(4)
    if len(hour) == 1:
        branch_coverage["parse_date_hungarian_5"] = True 
        hour = '0' + hour
    else:
        branch_coverage["parse_date_hungarian_6"] = True 
    w3dtfdate = '%(year)s-%(month)s-%(day)sT%(hour)s:%(minute)s%(zonediff)s' % \
                {
                    'year': m.group(1),
                    'month': month,
                    'day': day,
                    'hour': hour,
                    'minute': m.group(5),
                    'zonediff': m.group(6),
                }
    branch_coverage_print_hungarian()
    return _parse_date_w3dtf(w3dtfdate)

def branch_coverage_print_hungarian(): 
    hitItems = 0
    with open("CoverageHun.txt", "a") as coverageFile:
        for branch, hit in branch_coverage.items(): 
            if hit:
                hitItems = hitItems + 1
                coverageFile.write(branch + " was hit\n")
            else:
                coverageFile.write(branch + " was not hit\n")
        coverageFile.write("Branch coverage percentage: " + str((hitItems/6) * 100) + "%\n\n")