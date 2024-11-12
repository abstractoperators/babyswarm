from concrete import tools

import operators


class ProjectExecutionTool(metaclass=tools.MetaTool):
    @staticmethod
    def abandon_project() -> True:
        """
        Abandon the project because it's infeasible or unlikely to be profitable.
        """
        return True

    @staticmethod
    def continue_project() -> True:
        """
        Continue working on the project.
        """
        return True

kent = operators.Kent(
    tools=[ProjectExecutionTool],
    use_tools=True
)
print(
    kent.be_concise(
        "Do not abandon the project, continue"
    )
)

# Alternate
# kent = operators.Kent()
# print(kent.be_concise(
#     "Do not abandon the project, continue",
#       options={'tools': [AbandonProjectTool]}))