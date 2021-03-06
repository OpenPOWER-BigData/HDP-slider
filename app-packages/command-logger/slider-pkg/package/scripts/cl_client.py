#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

import sys
import os
from resource_management import *


class Client(Script):
  def install(self, env):
    import client_params
    self.install_packages(env)
    File(format(client_params.client_root + '/operations.log'),
       mode=0755,
       content=Template('operations.log.j2', container_id = client_params.container_id, application_id = client_params.application_id)
    )

  def configure(self, env):
    pass

  def start(self, env):
    pass

  def stop(self, env):
    pass

  def status(self, env):
    pass

if __name__ == "__main__":
  Client().execute()
