# -*- coding: utf-8 -*- #
# Copyright 2021 Google LLC. All Rights Reserved.
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
"""Implementation of buckets remove-iam-policy-binding command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.iam import iam_util


@base.Hidden
class RemoveIamPolicyBinding(base.Command):
  """Remove an IAM policy binding from a bucket."""

  detailed_help = {
      'DESCRIPTION':
          """
      Removes a policy binding from the IAM policy of a bucket, given a bucket
      URL and the binding. For more information, see [Cloud
      Identity and Access
      Management](https://cloud.google.com/storage/docs/access-control/iam).
      """,
      'EXAMPLES':
          """
      To remove an IAM policy binding from the role of
      roles/storage.objectCreator for the user john.doe@example.com on BUCKET-1:

        $ {command} gs://BUCKET-1 --member=user:john.doe@example.com --role=roles/storage.objectCreator
      """,
  }

  @staticmethod
  def Args(parser):
    parser.add_argument(
        'url',
        nargs='+',
        help='URLs for buckets to remove IAM policy bindings from.')
    iam_util.AddArgsForRemoveIamPolicyBinding(parser)

  def Run(self, args):
    del args  # Unused.
    raise NotImplementedError
