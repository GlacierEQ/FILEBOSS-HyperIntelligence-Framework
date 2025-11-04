import unittest
from orchestrators.hyper_intelligent_orchestrator import HyperIntelligentOrchestrator

import os

class TestHyperIntelligentOrchestrator(unittest.TestCase):
    def test_initialization(self):
        os.environ["API_TOKEN"] = "dummy_token"
        orchestrator = HyperIntelligentOrchestrator(os.environ.get("API_TOKEN"))
        self.assertIsNotNone(orchestrator)
        self.assertIsNotNone(orchestrator.github_connector)
        self.assertIsNotNone(orchestrator.notion_orchestrator)
        self.assertIsNotNone(orchestrator.ai_constellation)
        self.assertIsNotNone(orchestrator.deployment_engine)
        self.assertIsNotNone(orchestrator.scaffold_generator)
        self.assertIsNotNone(orchestrator.provenance_tracker)
        self.assertIsNotNone(orchestrator.intelligence_monitor)

if __name__ == '__main__':
    unittest.main()
