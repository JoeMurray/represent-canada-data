# coding: utf-8
from datetime import date

import boundaries


def ider(f):
    # http://www.ville.dorval.qc.ca/en/downloads/pdf/Map_Electoral_Districts.pdf
    return {
        'Désiré-Girouard': '1',
        'La Présentation': '2',
        'Fénelon': '3',
        'Pine Beach': '4',
        'Strathmore': '5',
        'Surrey': '6',
    }[f.get('NOM_DISTRI')]


boundaries.register('Dorval districts',
    domain='Dorval, QC',
    last_updated=date(2016, 1, 13),
    name_func=boundaries.attr('NOM_DISTRI'),
    id_func=ider,
    authority='Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2009-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/portail/licence/',
    data_url='http://donnees.ville.montreal.qc.ca/dataset/cbc2aeb1-dc73-487e-9b72-d803db631b15/resource/2b1074a3-2e81-456b-abb8-1ebbb0888562/download/elections-2009-districts-multi-poly.zip',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:2466087'},
    is_valid_func=lambda f: int(f.get('MONTREAL')) == 0 and int(f.get('NUM_ARR')) == 1,
)
