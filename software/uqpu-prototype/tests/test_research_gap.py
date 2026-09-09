import unittest
from uqpu.research_gap import GapStatus, ResearchGap

class ResearchGapTests(unittest.TestCase):
    def test_blocked_research_requires_unlock_path(self):
        g=ResearchGap("RG-X","future device",GapStatus.RESOURCE_BLOCKED,"MODEL_ONLY",("fab unavailable",),"simulate first",("facility available",),("run process simulation",))
        g.validate()

    def test_missing_unlock_path_rejected(self):
        g=ResearchGap("RG-X","future device",GapStatus.TOOL_BLOCKED,"MODEL_ONLY",("tool unavailable",),"model",(),("simulate",))
        with self.assertRaises(ValueError): g.validate()

if __name__=="__main__": unittest.main()
