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

from .execution_activity import ExecutionActivity


class HDInsightStreamingActivity(ExecutionActivity):
    """HDInsight streaming activity type.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param user_properties: Activity user properties.
    :type user_properties: list[~azure.mgmt.datafactory.models.UserProperty]
    :param type: Required. Constant filled by server.
    :type type: str
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param policy: Activity policy.
    :type policy: ~azure.mgmt.datafactory.models.ActivityPolicy
    :param storage_linked_services: Storage linked service references.
    :type storage_linked_services:
     list[~azure.mgmt.datafactory.models.LinkedServiceReference]
    :param arguments: User specified arguments to HDInsightActivity.
    :type arguments: list[object]
    :param get_debug_info: Debug info option. Possible values include: 'None',
     'Always', 'Failure'
    :type get_debug_info: str or
     ~azure.mgmt.datafactory.models.HDInsightActivityDebugInfoOption
    :param mapper: Required. Mapper executable name. Type: string (or
     Expression with resultType string).
    :type mapper: object
    :param reducer: Required. Reducer executable name. Type: string (or
     Expression with resultType string).
    :type reducer: object
    :param input: Required. Input blob path. Type: string (or Expression with
     resultType string).
    :type input: object
    :param output: Required. Output blob path. Type: string (or Expression
     with resultType string).
    :type output: object
    :param file_paths: Required. Paths to streaming job files. Can be
     directories.
    :type file_paths: list[object]
    :param file_linked_service: Linked service reference where the files are
     located.
    :type file_linked_service:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param combiner: Combiner executable name. Type: string (or Expression
     with resultType string).
    :type combiner: object
    :param command_environment: Command line environment values.
    :type command_environment: list[object]
    :param defines: Allows user to specify defines for streaming job request.
    :type defines: dict[str, object]
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'mapper': {'required': True},
        'reducer': {'required': True},
        'input': {'required': True},
        'output': {'required': True},
        'file_paths': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '[UserProperty]'},
        'type': {'key': 'type', 'type': 'str'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'policy': {'key': 'policy', 'type': 'ActivityPolicy'},
        'storage_linked_services': {'key': 'typeProperties.storageLinkedServices', 'type': '[LinkedServiceReference]'},
        'arguments': {'key': 'typeProperties.arguments', 'type': '[object]'},
        'get_debug_info': {'key': 'typeProperties.getDebugInfo', 'type': 'str'},
        'mapper': {'key': 'typeProperties.mapper', 'type': 'object'},
        'reducer': {'key': 'typeProperties.reducer', 'type': 'object'},
        'input': {'key': 'typeProperties.input', 'type': 'object'},
        'output': {'key': 'typeProperties.output', 'type': 'object'},
        'file_paths': {'key': 'typeProperties.filePaths', 'type': '[object]'},
        'file_linked_service': {'key': 'typeProperties.fileLinkedService', 'type': 'LinkedServiceReference'},
        'combiner': {'key': 'typeProperties.combiner', 'type': 'object'},
        'command_environment': {'key': 'typeProperties.commandEnvironment', 'type': '[object]'},
        'defines': {'key': 'typeProperties.defines', 'type': '{object}'},
    }

    def __init__(self, **kwargs):
        super(HDInsightStreamingActivity, self).__init__(**kwargs)
        self.storage_linked_services = kwargs.get('storage_linked_services', None)
        self.arguments = kwargs.get('arguments', None)
        self.get_debug_info = kwargs.get('get_debug_info', None)
        self.mapper = kwargs.get('mapper', None)
        self.reducer = kwargs.get('reducer', None)
        self.input = kwargs.get('input', None)
        self.output = kwargs.get('output', None)
        self.file_paths = kwargs.get('file_paths', None)
        self.file_linked_service = kwargs.get('file_linked_service', None)
        self.combiner = kwargs.get('combiner', None)
        self.command_environment = kwargs.get('command_environment', None)
        self.defines = kwargs.get('defines', None)
        self.type = 'HDInsightStreaming'