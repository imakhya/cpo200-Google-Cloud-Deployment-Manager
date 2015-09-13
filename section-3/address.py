# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Creates a Compute Engine address resource.
"""

import yaml


def GenerateEmbeddableYaml(yaml_string):
    # This function takes a string in YAML format and produces
    # an equivalent YAML representation that can be
    # inserted into another YAML document.
    yaml_object = yaml.load(yaml_string)
    dumped_yaml = yaml.dump(yaml_object, default_flow_style=True)
    return dumped_yaml


def GenerateConfig(context):
    return """
resources:
  - type: compute.v1.address
    name: %(name)s
    properties:
      region: %(compute-region)s
""" % {"name": context.env["name"],
       "compute-region": context.properties["compute-region"]}

