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
                        "tenantId": tenant.id,
                        "tenantName": tenant.name
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
                        "tenantName": tenant.name
                    }
            )
            return "Updated successfully."
        else:
            return "No matching found"

    def deleteTenant(self, tenantId):
        DatabaseCollections.tenantCollectionName.remove(
                {
                    "tenantId": tenantId
                }
        )

    def getTenant(self, tenantId):
        return DatabaseCollections.tenantCollectionName.find_one(
                {
                    "tenantId": tenantId
                }
        )
