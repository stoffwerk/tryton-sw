from trytond.model import fields
from trytond.pool import PoolMeta

class ProductSupplier(metaclass=PoolMeta):
    __name__ = 'purchase.product_supplier'
    url = fields.Char("Url", translate=False)