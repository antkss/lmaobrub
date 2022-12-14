"""Generated client library for cloudbuild version v1alpha2."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudbuild.v1alpha2 import cloudbuild_v1alpha2_messages as messages


class CloudbuildV1alpha2(base_api.BaseApiClient):
  """Generated client library for service cloudbuild version v1alpha2."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://cloudbuild.googleapis.com/'
  MTLS_BASE_URL = 'https://cloudbuild.mtls.googleapis.com/'

  _PACKAGE = 'cloudbuild'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha2'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CloudbuildV1alpha2'
  _URL_VERSION = 'v1alpha2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudbuild handle."""
    url = url or self.BASE_URL
    super(CloudbuildV1alpha2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects_workerPools = self.ProjectsWorkerPoolsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(CloudbuildV1alpha2.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (CloudbuildProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='cloudbuild.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='CloudbuildProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (CloudbuildProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='cloudbuild.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}',
        request_field='',
        request_type_name='CloudbuildProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(CloudbuildV1alpha2.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsWorkerPoolsService(base_api.BaseApiService):
    """Service class for the projects_workerPools resource."""

    _NAME = 'projects_workerPools'

    def __init__(self, client):
      super(CloudbuildV1alpha2.ProjectsWorkerPoolsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a `WorkerPool` to run the builds, and returns the new worker pool.

      Args:
        request: (CloudbuildProjectsWorkerPoolsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (WorkerPool) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/workerPools',
        http_method='POST',
        method_id='cloudbuild.projects.workerPools.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['workerPoolId'],
        relative_path='v1alpha2/{+parent}/workerPools',
        request_field='workerPool',
        request_type_name='CloudbuildProjectsWorkerPoolsCreateRequest',
        response_type_name='WorkerPool',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a `WorkerPool`.

      Args:
        request: (CloudbuildProjectsWorkerPoolsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/workerPools/{workerPoolsId}',
        http_method='DELETE',
        method_id='cloudbuild.projects.workerPools.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}',
        request_field='',
        request_type_name='CloudbuildProjectsWorkerPoolsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Returns details of a `WorkerPool`.

      Args:
        request: (CloudbuildProjectsWorkerPoolsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (WorkerPool) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/workerPools/{workerPoolsId}',
        http_method='GET',
        method_id='cloudbuild.projects.workerPools.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}',
        request_field='',
        request_type_name='CloudbuildProjectsWorkerPoolsGetRequest',
        response_type_name='WorkerPool',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists `WorkerPool`s by project.

      Args:
        request: (CloudbuildProjectsWorkerPoolsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListWorkerPoolsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/workerPools',
        http_method='GET',
        method_id='cloudbuild.projects.workerPools.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha2/{+parent}/workerPools',
        request_field='',
        request_type_name='CloudbuildProjectsWorkerPoolsListRequest',
        response_type_name='ListWorkerPoolsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a `WorkerPool`.

      Args:
        request: (CloudbuildProjectsWorkerPoolsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (WorkerPool) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/workerPools/{workerPoolsId}',
        http_method='PATCH',
        method_id='cloudbuild.projects.workerPools.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha2/{+name}',
        request_field='workerPool',
        request_type_name='CloudbuildProjectsWorkerPoolsPatchRequest',
        response_type_name='WorkerPool',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(CloudbuildV1alpha2.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
