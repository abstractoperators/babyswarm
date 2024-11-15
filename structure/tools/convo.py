from concrete import tools


class ConversateTool(metaclass=tools.MetaTool):
    @staticmethod
    def contribute(idea=None, **kwargs) -> True:
        """
        Contribute something to the previous statement
        """
        return

    @staticmethod
    def abstain() -> True:
        """
        Don't say anything because you don't have anything to add
        """
        return
