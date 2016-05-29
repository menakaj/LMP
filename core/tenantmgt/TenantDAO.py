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
from common.Constants import DatabaseCollections

# Tenant is an isolated entity which shares the same server instance.
# Separated by tenant Id


class TenantDAO:
    def __init__(self):
        pass

    def createTenant(self, tenant):
        if DatabaseCollections.tenantCollectionName.find({"tenantId": tenant.id}).count() > 0:
            return "Already available"
        else:
            DatabaseCollections.tenantCollectionName.insert_one(
                    {
                        "tenantId": tenant.email,
                        "tenantName": tenant.name,
                        "tenantUserName": tenant.userName,
                        "password": tenant.password,
                        "email": tenant.email
                    }
            )
            return "Successfully created tenant"

    def updateTenant(self, tenentId, tenant):
        if DatabaseCollections.tenantCollectionName.find({"tenantId": tenentId}).count() > 0:
            DatabaseCollections.tenantCollectionName.update_one(
                    {
                        "tenentId": tenentId
                    },
                    {
                        "tenantName": tenant.name,
                        "tenantUserName": tenant.userName,
                        "password": tenant.password,
                        "email": tenant.email
                    }
            )
            return "Updated successfully."
        else:
            return "No matching found"

    def deleteTenant(self, email):
        DatabaseCollections.tenantCollectionName.remove(
                {
                    "email": email
                }
        )

    def getTenant(self, email):
        return DatabaseCollections.tenantCollectionName.find_one(
                {
                    "email": email
                }
        )
