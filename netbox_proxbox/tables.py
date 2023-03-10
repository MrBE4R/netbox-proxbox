# tables.py
import django_tables2 as table

from netbox.tables import NetBoxTable
from .models import ProxmoxVM

class ProxmoxVMTable(NetBoxTable):
    """Table for displaying BGP Peering objects."""

    id = table.LinkColumn()
    cluster = table.LinkColumn()
    virtual_machine = table.LinkColumn()
    proxmox_vm_id = table.LinkColumn()

    class Meta(NetBoxTable.Meta):
        model = ProxmoxVM
        fields = (
            "id",
            "virtual_machine",
            "proxmox_vm_id",
            "status",
            "type",
            "node",
            "cluster",
        )

class VMUpdateResult(table.Table):
    """Table for displaying VM/CT update results"""

    name = table.Column()
    changes = table.Column()

    '''
    status = tables.Column()
    custom_fields = tables.Column()
    local_context = tables.Column()
    resources = tables.Column()
    tag = tables.Column()
    result = tables.Column()
    '''

    class Meta(NetBoxTable.Meta):
        fields = ('name', 'changes')
        default_columns = ('name', 'changes')
        #fields = ('name', 'status', 'custom_fields', 'local_context', 'resources', 'tag', 'result')
        #default_columns = ('name', 'status', 'custom_fields', 'local_context', 'resources', 'tag', 'result')