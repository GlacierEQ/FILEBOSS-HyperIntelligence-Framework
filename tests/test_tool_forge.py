import unittest
from tools.dynamic_tool_forge import DynamicToolForge

class TestDynamicToolForge(unittest.TestCase):
    def test_initialization(self):
        tool_forge = DynamicToolForge()
        self.assertIsNotNone(tool_forge)
        self.assertIsNotNone(tool_forge.tool_templates)
        self.assertIsNotNone(tool_forge.code_compiler)
        self.assertIsNotNone(tool_forge.dependency_resolver)
        self.assertIsNotNone(tool_forge.quality_analyzer)
        self.assertIsNotNone(tool_forge.deployment_manager)
        self.assertEqual(tool_forge.generated_tools, {})

if __name__ == '__main__':
    unittest.main()
