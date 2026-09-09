import unittest
from uqpu.fab_route import FabRoute,DeviceRequirement,feasible,select_lowest_model_cost

class FabRouteTests(unittest.TestCase):
    def test_rejects_route_that_cannot_meet_feature(self):
        r=FabRoute("mature",500,1,10,.95,20)
        self.assertFalse(feasible(r,DeviceRequirement(100,20,.9)))
    def test_selects_economic_feasible_route_not_smallest_node(self):
        mature=FabRoute("duv-route",50,2,20,.95,20)
        advanced=FabRoute("advanced-route",10,20,30,.80,10)
        req=DeviceRequirement(60,40,.75)
        self.assertEqual(select_lowest_model_cost([advanced,mature],req).name,"duv-route")
    def test_no_feasible_route(self):
        r=FabRoute("x",100,1,20,.8,10)
        self.assertIsNone(select_lowest_model_cost([r],DeviceRequirement(10,10,.99)))

if __name__=="__main__": unittest.main()
