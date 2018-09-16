# -*- coding: utf-8 -*-

from ScoutSuite.providers.gcp.configs.base import GCPBaseConfig

from opinel.utils.console import printError, printException, printInfo


class IAMConfig(GCPBaseConfig):
    targets = (
        ('roles', 'Roles', 'list', {}, False),
    )

    def __init__(self, thread_config):

        self.library_type = 'api_client_library'

        self.roles = {}
        self.roles_count = 0

        super(IAMConfig, self).__init__(thread_config)

    def parse_roles(self, instance, params):
        a = instance
