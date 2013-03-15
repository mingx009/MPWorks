import json
from pprint import pprint
import datetime
from pymatgen.core.structure import Structure
from pymatgen.io.vaspio_set import MaterialsProjectVaspInputSet
from pymatgen.matproj.snl import StructureNL

__author__ = 'Anubhav Jain'
__copyright__ = 'Copyright 2013, The Materials Project'
__version__ = '0.1'
__maintainer__ = 'Anubhav Jain'
__email__ = 'ajain@lbl.gov'
__date__ = 'Mar 15, 2013'

import numpy as np

def snl_to_spec(snl):
    spec = {}

    mpvis = MaterialsProjectVaspInputSet()
    structure = snl.structure

    spec['vasp_pmg'] = {}
    spec['vasp_pmg']['incar'] = mpvis.get_incar(structure).to_dict
    spec['vasp_pmg']['poscar'] = mpvis.get_poscar(structure).to_dict
    spec['vasp_pmg']['kpoints'] = mpvis.get_kpoints(structure).to_dict
    spec['vasp_pmg']['potcar'] = mpvis.get_potcar(structure).to_dict
    spec['vaspinputset'] = mpvis.to_dict
    spec['vaspinputset_name'] = mpvis.__class__.__name__
    spec['task_type'] = 'optimize structure (2x)'
    spec['snl'] = snl.to_dict
    spec['snl_id'] = -1
    spec['snl_group'] = -2
    spec['snl_strictgroup'] = -2
    spec['tags'] = ['auto_generation_v1.0']

    return spec





if __name__ == '__main__':
    s = Structure(np.eye(3, 3) * 3, ["Fe", "Mn"], [[0, 0, 0], [0.5, 0.5, 0.5]])
    snl = StructureNL(s, "Anubhav Jain <ajain@lbl.gov>")

    spec = snl_to_spec(snl)
    print json.dumps(spec, default= lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None)
    print '--'
    pprint(spec)
