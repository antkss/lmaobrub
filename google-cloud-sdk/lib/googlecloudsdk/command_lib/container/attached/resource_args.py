# -*- coding: utf-8 -*- #
# Copyright 2022 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Shared resource flags for `gcloud container attached` commands."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope.concepts import concepts
from googlecloudsdk.calliope.concepts import deps
from googlecloudsdk.command_lib.util.concepts import concept_parsers
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources


def AttachedClusterAttributeConfig():
  return concepts.ResourceParameterAttributeConfig(
      name='cluster', help_text='cluster of the {resource}.')


def LocationAttributeConfig():
  """Gets Google Cloud location resource attribute."""
  return concepts.ResourceParameterAttributeConfig(
      name='location',
      help_text='Google Cloud location for the {resource}.',
      fallthroughs=[
          deps.PropertyFallthrough(
              properties.VALUES.container_attached.location),
      ])


def GetAttachedClusterResourceSpec():
  return concepts.ResourceSpec(
      'gkemulticloud.projects.locations.attachedClusters',
      resource_name='cluster',
      attachedClustersId=AttachedClusterAttributeConfig(),
      locationsId=LocationAttributeConfig(),
      projectsId=concepts.DEFAULT_PROJECT_ATTRIBUTE_CONFIG)


def GetLocationResourceSpec():
  return concepts.ResourceSpec(
      'gkemulticloud.projects.locations',
      resource_name='location',
      locationsId=LocationAttributeConfig(),
      projectsId=concepts.DEFAULT_PROJECT_ATTRIBUTE_CONFIG)


def AddAttachedClusterResourceArg(parser, verb, positional=True):
  """Adds a resource argument for an Attached cluster.

  Args:
    parser: The argparse parser to add the resource arg to.
    verb: str, the verb to describe the resource, such as 'to update'.
    positional: bool, whether the argument is positional or not.
  """
  name = 'cluster' if positional else '--cluster'
  concept_parsers.ConceptParser.ForResource(
      name,
      GetAttachedClusterResourceSpec(),
      'cluster {}.'.format(verb),
      required=True).AddToParser(parser)


def AddLocationResourceArg(parser, verb):
  """Adds a resource argument for Google Cloud location.

  Args:
    parser: The argparse parser to add the resource arg to.
    verb: str, the verb to describe the resource, such as 'to update'.
  """
  concept_parsers.ConceptParser.ForResource(
      '--location',
      GetLocationResourceSpec(),
      'Google Cloud location {}.'.format(verb),
      required=True).AddToParser(parser)


def ParseAttachedClusterResourceArg(args):
  return resources.REGISTRY.ParseRelativeName(
      args.CONCEPTS.cluster.Parse().RelativeName(),
      collection='gkemulticloud.projects.locations.attachedClusters')