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


class VaultProperties(Model):
    """Properties of the vault.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provisioning_state: Provisioning State.
    :vartype provisioning_state: str
    :param upgrade_details:
    :type upgrade_details: ~azure.mgmt.recoveryservices.models.UpgradeDetails
    """

    _validation = {
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'upgrade_details': {'key': 'upgradeDetails', 'type': 'UpgradeDetails'},
    }

    def __init__(self, **kwargs):
        super(VaultProperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.upgrade_details = kwargs.get('upgrade_details', None)