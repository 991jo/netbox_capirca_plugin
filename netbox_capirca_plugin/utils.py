from capirca.lib.naming import Naming

class NamingWrapper(Naming):

    def add_definitions(self, definitions: str, def_type: str):
        """
        Adds definitions to the Naming Instance.

        Args:
            definitions: a str with the usual definitions format
            def_type: a str, either "networks" or "services"

        Returns:
            None
        """

        if def_type not in ["networks", "services"]:
            raise UnexpectedDefinitionTypeError(f"Received an unexpected definition type: { def_type }")

        data = definitions.splitlines()

        if def_type == "networks":
            self.ParseNetworkList(data)

        elif def_type == "services":
            self.ParseServiceList(data)

        self._CheckUnseen(def_type)
