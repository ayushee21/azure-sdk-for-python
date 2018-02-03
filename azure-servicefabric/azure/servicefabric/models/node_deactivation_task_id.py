# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NodeDeactivationTaskId(Model):
    """Identity of the task related to deactivation operation on the node.

    :param id: Value of the task id.
    :type id: str
    :param node_deactivation_task_type: The type of the task that performed
     the node deactivation. Following are the possible values. Possible values
     include: 'Invalid', 'Infrastructure', 'Repair', 'Client'
    :type node_deactivation_task_type: str or
     ~azure.servicefabric.models.NodeDeactivationTaskType
    """

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'node_deactivation_task_type': {'key': 'NodeDeactivationTaskType', 'type': 'str'},
    }

    def __init__(self, id=None, node_deactivation_task_type=None):
        super(NodeDeactivationTaskId, self).__init__()
        self.id = id
        self.node_deactivation_task_type = node_deactivation_task_type
