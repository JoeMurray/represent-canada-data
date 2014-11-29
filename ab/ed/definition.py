from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Alberta electoral districts',
    domain='Alberta',
    last_updated=date(2011, 11, 25),
    name_func=boundaries.clean_attr('EDNAME'),
    id_func=boundaries.attr('EDNUMBER'),
    authority='Her Majesty the Queen in Right of Alberta',
    source_url='http://www.altalis.com/products/base/alberta_boundary_data.html',
    licence_url='http://www.altalis.com/pdf/AltaLIS%20Web%20Use%20Agreement.pdf',
    data_url='http://www.altalis.com/Samples/Provincial%20Electoral%20Divisions.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '48'},
)
