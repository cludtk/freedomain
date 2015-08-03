__author__ = 'cvl'

class Domain_model():

    def __init__(self, json_dict):
        self.free_domains = json_dict['free_domains']
        self.paid_domains = json_dict['paid_domains']