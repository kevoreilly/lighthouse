import collections
from ..coverage_file import CoverageFile

class TraceData(CoverageFile):
    """
    An instruction (or basic block) address trace log parser.
    """

    def __init__(self, filepath):
        self._hitmap = {}
        super(TraceData, self).__init__(filepath)

    #--------------------------------------------------------------------------
    # Public
    #--------------------------------------------------------------------------

    def get_addresses(self, module_name=None):
        return self._hitmap.keys()

    #--------------------------------------------------------------------------
    # Parsing Routines - Top Level
    #--------------------------------------------------------------------------

    def _parse(self):
        """
        Parse absolute address coverage from the given log file.
        """
        hitmap = collections.defaultdict(int)
        with open(self.filepath) as f:
            for line in f:
                address_string = line.split(' ')[0]
                try:
                    address = int(address_string, 16)
                    if address:
                        hitmap[int(address_string, 16)] += 1
                except:
                    pass
        self._hitmap = hitmap
