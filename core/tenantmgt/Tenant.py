# Copyright 2016 Team - LMP, University Of Peradeniya
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Tenant is an isolated entity in the same server instance.
Has separate db ids..

"""


class Tenant:
    def __init__(self, id="", name="", userName="", password="", email=""):
        self.name = name
        self.id = id
        self.userName = userName
        self.password = password
        self.email = email
