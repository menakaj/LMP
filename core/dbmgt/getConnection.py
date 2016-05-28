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
from __init__ import *


def getDatabase():
    # url = "mongodb://LMP:lmp123@ds021182.mlab.com:21182/lmp"
    url = "mongodb://lmp123:lmp123@ds019063.mlab.com:19063/lmp"
    client = MongoClient(url)
    db = client.lmp
    return db

