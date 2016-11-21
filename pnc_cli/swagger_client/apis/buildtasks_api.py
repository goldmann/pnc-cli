# coding: utf-8

"""
BuildtasksApi.py
Copyright 2015 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class BuildtasksApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def build(self, build_execution_configuration_id, **kwargs):
        """
        Cancel the build execution defined with given executionConfigurationId.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.build(build_execution_configuration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int build_execution_configuration_id: Build Execution Configuration ID. See org.jboss.pnc.spi.executor.BuildExecutionConfiguration. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'build_execution_configuration_id' is set
        if build_execution_configuration_id is None:
            raise ValueError("Missing the required parameter `build_execution_configuration_id` when calling `build`")

        all_params = ['build_execution_configuration_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method build" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/build-tasks/cancel-build/{buildExecutionConfigurationId}'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        if 'build_execution_configuration_id' in params:
            path_params['buildExecutionConfigurationId'] = params['build_execution_configuration_id']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def build_1(self, build_execution_configuration, **kwargs):
        """
        Triggers the build execution for a given configuration.


        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.build_1(build_execution_configuration, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str build_execution_configuration: Build Execution Configuration. See org.jboss.pnc.spi.executor.BuildExecutionConfiguration. (required)
        :param str username_triggered: Username who triggered the build. If empty current user is used.
        :param str callback_url: Optional Callback URL
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'build_execution_configuration' is set
        if build_execution_configuration is None:
            raise ValueError("Missing the required parameter `build_execution_configuration` when calling `build_1`")

        all_params = ['build_execution_configuration', 'username_triggered', 'callback_url']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method build_1" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/build-tasks/execute-build'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}
        if 'build_execution_configuration' in params:
            form_params['buildExecutionConfiguration'] = params['build_execution_configuration']
        if 'username_triggered' in params:
            form_params['usernameTriggered'] = params['username_triggered']
        if 'callback_url' in params:
            form_params['callbackUrl'] = params['callback_url']

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def build_task_completed(self, task_id, build_result, **kwargs):
        """
        Notifies the completion of externally managed build task process.


        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.build_task_completed(task_id, build_result, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int task_id: Build task id (required)
        :param str build_result: Build result (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'task_id' is set
        if task_id is None:
            raise ValueError("Missing the required parameter `task_id` when calling `build_task_completed`")
        # verify the required parameter 'build_result' is set
        if build_result is None:
            raise ValueError("Missing the required parameter `build_result` when calling `build_task_completed`")

        all_params = ['task_id', 'build_result']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method build_task_completed" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/build-tasks/{taskId}/completed'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        if 'task_id' in params:
            path_params['taskId'] = params['task_id']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}
        if 'build_result' in params:
            form_params['buildResult'] = params['build_result']

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
