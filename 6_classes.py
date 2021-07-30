

class AClass(object):
    pass

#! Bclass is inehrited from Aclass
class BClass(AClass):
    pass    

class CClass(object):
    pass

#! Tis is multiple inheritance
class DClass(AClass, CClass):
    pass