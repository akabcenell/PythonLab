# some usefull superclasses for the PythonLab project
import sip
sip.setapi('QVariant', 2)# set to version to so that the gui returns QString objects and not generic QVariants
from parameter import Parameter
from instruments import Instrument
from scripts import Script
from loading import load_probes, load_scripts, load_instruments
from qt_b26_widgets import B26QTreeItem
__all__ = ['Instrument', 'Parameter']


