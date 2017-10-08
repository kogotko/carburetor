# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.utils.translation import ugettext_lazy as _

import horizon
from django.conf import settings

# class Mygroup(horizon.PanelGroup):
#     slug = "uvr_group"
#     name = _("uvr_group")
#     panels = ('vm_manage','instances',)

class Uvs(horizon.Dashboard):
    name = "Управление вычислительными сетями"
    slug = "uvs"
    panels = (
        'networks',
        'routers',
        'floating_ips',
        'firewalls',
        'vpn'
    )
    default_panel = 'vpn'
    subsystem = getattr(settings, "SYBSYSTEM", "uvr")

horizon.register(Uvs)
