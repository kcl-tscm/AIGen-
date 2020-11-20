import jinja2
from jinja2 import Environment, FileSystemLoader, Template
import os

###############################################
# Library to create automatically inputs for  #
# first principle calculations in DFTB+       #
###############################################

class dftb_geom:

  def __init__(self, name='mol.gen'):
      self.name = name

  def geom(self):
    """ Creating the header of the DFTB input file
    where the geometry name must be specified. The 
    user must provide the name of the file and is
    expected to be transformed to the .gen format 
    """ 
    dftb_geom = """Geometry = GenFormat {
    <<< "{{ title }}"
    }
    """
    return Environment().from_string(dftb_geom).render(title=self.name)

class dftb_driver_sd:

  def __init__(self, relax_method='SteepestDescent', atoms_rel='1:-1', thres_force='1E-8', num_steps='200', step_size='100.0',
               output_prefix='geo_gen',append_geom="No"):
        self.relax_method = relax_method
        self.atoms_rel = atoms_rel
        self.thres_force = thres_force
        self.num_steps = num_steps
        self.step_size = step_size
        self.output_prefix = output_prefix
        self.append_geom = append_geom
        
       
  def sd(self):
    """ Block of the input file in which the user decides
        the relaxation method, atoms to be relaxed, threshold of force 
        and number of steps. For more detailed options refer to 
        the dftb manual. 
    """
    dftb_driver= """Driver = {{ relax_method }} {
    MovedAtoms = {{ atoms_rel }}
    MaxForceComponent = {{ thres_force }}
    MaxSteps = {{ num_steps }}
    StepSize = {{ step_size }}
    OutputPrefix = "{{ output_prefix }}"
    AppendGeometries = {{ append_geom }}
    }
    """
    return Environment().from_string(dftb_driver).render(relax_method=self.relax_method,
                                                         atoms_rel=self.atoms_rel,thres_force=self.thres_force,num_steps=self.num_steps,
                                                         step_size=self.step_size, output_prefix=self.output_prefix,append_geom=self.append_geom)


class dftb_driver_cg:

  def __init__(self, relax_method='ConjugateGradient', atoms_rel='1:-1', thres_force='1E-8', num_steps='200', step_size='100.0',
               output_prefix='geo_gen',append_geom="No"):
        self.relax_method = relax_method
        self.atoms_rel = atoms_rel
        self.thres_force = thres_force
        self.num_steps = num_steps
        self.step_size = step_size
        self.output_prefix = output_prefix
        self.append_geom = append_geom
        
       
  def cg(self):
    """ Block of the input file in which the user decides
        the relaxation method, atoms to be relaxed, threshold of force 
        and number of steps. For more detailed options refer to 
        the dftb manual. 
    """
    dftb_driver= """Driver = {{ relax_method }} {
    MovedAtoms = {{ atoms_rel }}
    MaxForceComponent = {{ thres_force }}
    MaxSteps = {{ num_steps }}
    StepSize = {{ step_size }}
    OutputPrefix = "{{ output_prefix }}"
    AppendGeometries = {{ append_geom }}
    }
    """
    return Environment().from_string(dftb_driver).render(relax_method=self.relax_method,
                                                         atoms_rel=self.atoms_rel,thres_force=self.thres_force,num_steps=self.num_steps,
                                                         step_size=self.step_size, output_prefix=self.output_prefix,append_geom=self.append_geom)
