from OFS.Folder import Folder
from App.special_dtml import DTMLFile

class Product(Folder):
    """product"""
    meta_type = "product"

    def hello(self):
        """ hi to all """
        return "Have a nice day"

    def redirect(self):
        """ redirects to given link """
        request = self.REQUEST
        request.RESPONSE.redirect("http://www.google.com")
        

new_file = DTMLFile("view",globals())

def add_product(context):
    """Add product"""
    context._setObject('Product', Product())


def initialize(context):
    context.registerClass(Product, constructors=(new_file,add_product,))
 

