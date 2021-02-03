from django.contrib import admin
from django.contrib.admin import AdminSite

def has_superuser_permission(request):
    return request.user.is_active and request.user.is_superuser

# Only superuser can access root admin site (default)
admin.site.has_permission = has_superuser_permission

class MOTIAdminSite(AdminSite):
    """MOTI admin page definition"""
    site_header = "HR Admin"

moti_admin_site = MOTIAdminSite(name='moti_admin')