from OFS.Folder import Folder

def add_school(context):
 """add school"""
    context._setObject('school',school())
class school (Folder):
  """set school"""
     meta_type='school'

def initialize(context):
    context.registerClass(school,constructors=(add_school,))

