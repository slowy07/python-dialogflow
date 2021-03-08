# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import
import sys
import warnings

from dialogflow_v2 import types
from dialogflow_v2.gapic import agents_client
from dialogflow_v2.gapic import contexts_client
from dialogflow_v2.gapic import entity_types_client
from dialogflow_v2.gapic import enums
from dialogflow_v2.gapic import environments_client
from dialogflow_v2.gapic import intents_client
from dialogflow_v2.gapic import session_entity_types_client
from dialogflow_v2.gapic import sessions_client


if sys.version_info[:2] == (2, 7):
    message = (
        "A future version of this library will drop support for Python 2.7. "
        "More details about Python 2 support for Google Cloud Client Libraries "
        "can be found at https://cloud.google.com/python/docs/python2-sunset/"
    )
    warnings.warn(message, DeprecationWarning)

raise RuntimeError(
    "'dialogflow' has been renamed to 'google-cloud-dialogflow'. "
    "'dialogflow' will no longer be updated. "
    "For help upgrading to google-cloud-dialogflow>=2.0.0, see "
    "https://github.com/googleapis/python-dialogflow/blob/master/UPGRADING.md"
)


class AgentsClient(agents_client.AgentsClient):
    __doc__ = agents_client.AgentsClient.__doc__
    enums = enums


class ContextsClient(contexts_client.ContextsClient):
    __doc__ = contexts_client.ContextsClient.__doc__
    enums = enums


class EntityTypesClient(entity_types_client.EntityTypesClient):
    __doc__ = entity_types_client.EntityTypesClient.__doc__
    enums = enums


class EnvironmentsClient(environments_client.EnvironmentsClient):
    __doc__ = environments_client.EnvironmentsClient.__doc__
    enums = enums


class IntentsClient(intents_client.IntentsClient):
    __doc__ = intents_client.IntentsClient.__doc__
    enums = enums


class SessionEntityTypesClient(session_entity_types_client.SessionEntityTypesClient):
    __doc__ = session_entity_types_client.SessionEntityTypesClient.__doc__
    enums = enums


class SessionsClient(sessions_client.SessionsClient):
    __doc__ = sessions_client.SessionsClient.__doc__
    enums = enums


__all__ = (
    "enums",
    "types",
    "AgentsClient",
    "ContextsClient",
    "EntityTypesClient",
    "EnvironmentsClient",
    "IntentsClient",
    "SessionEntityTypesClient",
    "SessionsClient",
)
