"""
DXProgram Handler
+++++++++++++++++

Programs are data objects which store an executable and specifications
for input, output, and execution.  They can be run by calling the :func:`DXProgram.run` method.

"""

from dxpy.bindings import *

#############
# DXProgram #
#############

class DXProgram(DXDataObject):
    '''
    Remote program object handler

    .. automethod:: _new
    '''

    _class = "program"

    _describe = staticmethod(dxpy.api.programDescribe)
    _add_types = staticmethod(dxpy.api.programAddTypes)
    _remove_types = staticmethod(dxpy.api.programRemoveTypes)
    _get_details = staticmethod(dxpy.api.programGetDetails)
    _set_details = staticmethod(dxpy.api.programSetDetails)
    _set_visibility = staticmethod(dxpy.api.programSetVisibility)
    _rename = staticmethod(dxpy.api.programRename)
    _set_properties = staticmethod(dxpy.api.programSetProperties)
    _add_tags = staticmethod(dxpy.api.programAddTags)
    _remove_tags = staticmethod(dxpy.api.programRemoveTags)
    _close = staticmethod(dxpy.api.programClose)
    _list_projects = staticmethod(dxpy.api.programListProjects)

    def _new(self, dx_hash, **kwargs):
        '''
        :param dx_hash: Standard hash populated in :func:`dxpy.bindings.DXDataObject.new()`
        :type dx_hash: dict
        :param run: run specification
        :type run: dict
        :param inputs: input specification (optional)
        :type inputs: dict
        :param outputs: output specification (optional)
        :type outputs: dict
        :param access: access specification (optional)
        :type access: dict
        :param dxapi: API version string
        :type dxapi: string
        :param description: description string (optional)
        :type description: string
        :param subtitle: subtitle string (optional)
        :type subtitle: string

        It is highly recommended that :mod:`dxpy.program_builder` is
        used for program creation.

        Creates a program with the given parameters (see API
        documentation for the correct syntax).  The program is not run
        until :meth:`run()` is called.

        '''
        for field in 'run', 'dxapi':
            dx_hash[field] = kwargs[field]
            del kwargs[field]
        for field in 'inputs', 'outputs', 'access', 'description', 'subtitle':
            if field in kwargs:
                dx_hash[field] = kwargs[field]
                del kwargs[field]

        resp = dxpy.api.programNew(dx_hash, **kwargs)
        self.set_ids(resp["id"], dx_hash["project"])

    def get(self, **kwargs):
        """
        Returns the contents of the program.
        """
        return dxpy.api.programGet(self._dxid, **kwargs)

    def run(self, program_input, project=None, folder="/", **kwargs):
        '''
        :param program_input: Hash of the program's input arguments
        :type program_input: dict
        :param project: Project ID of the project context
        :type project: string
        :param folder: Folder in which program's outputs will be placed in *project*
        :type folder: string
        :returns: Object handler of the created job now running the program
        :rtype: :class:`dxpy.bindings.DXJob`

        Creates a new job to execute the function "main" of this program
        with the given input *program_input*.

        '''
        if project is None and "DX_JOB_ID" not in os.environ:
            project = self._proj

        return DXJob(dxpy.api.programRun(self._dxid, {"input": program_input,
                                                      "project": project,
                                                      "folder": folder},
                                         **kwargs)["id"])
