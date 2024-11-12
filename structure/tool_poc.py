from concrete import tools

import operators


class AbandonProjectTool(metaclass=tools.MetaTool):
    @staticmethod
    def abandon_project() -> True:
        return True

    @staticmethod
    def continue_project() -> True:
        return True

kent = operators.Kent(
    tools=[AbandonProjectTool]
)
print(kent.be_concise(
    "Do not abandon the project, continue"))

# Alternate
# kent = operators.Kent()
# print(kent.be_concise(
#     "Do not abandon the project, continue",
#       options={'tools': [AbandonProjectTool]}))