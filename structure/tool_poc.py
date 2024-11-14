from concrete import tools

import operators


class ProjectExecutionTool(metaclass=tools.MetaTool):
    @staticmethod
    def abandon_project() -> True:
        """
        Abandon the project because it's infeasible or unlikely to be profitable.
        """
        return

    @staticmethod
    def continue_project() -> True:
        """
        Continue working on the project.
        """
        return

kent = operators.Kent(
    tools=[ProjectExecutionTool],
    use_tools=True
)
print(
    kent.be_concise(
        # "This project sucks, let's quit"
        "Do not abandon the project, continue"
    )
)

# Alternate
# kent = operators.Kent()
# print(kent.be_concise(
#     "Do not abandon the project, continue",
#       options={'tools': [AbandonProjectTool]}))