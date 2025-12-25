from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta

class ProductSupplier(ModelSQL, metaclass=PoolMeta):
    __name__ = 'purchase.product_supplier'
    
    url = fields.Char("URL")