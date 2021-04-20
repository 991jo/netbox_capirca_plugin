from pathlib import Path

from capirca.lib.naming import Naming, UnexpectedDefinitionTypeError

from .exceptions import BasePathEscapeError


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


def combine_paths_checked(base: Path, extension: Path) -> str:
    """
    Combines the base Path and the extension Path, resolves the paths
    (handling things like `..`) and checks if the result is still within the
    base path.

    Returns the combined path.
    Raises an BasePathEscapeError when the resulting path is no longer inside
    the base path.
    """

    combined = base.joinpath(extension).resolve()
    if base in combined.parents:
        return str(combined)

    raise BasePathEscapeError(f"{combined} is not a child of {base}")

def cisco_acl_cleanup(acl: str) -> str:
    """
    Removes things that dont end up in the configuration file on cisco systems
    e.g. comments ("!"), "no ipv6 access-list ..." lines and empty lines.
    """

    acl = acl.splitlines()
    result = list()
    for line in acl:
        if line.lstrip().startswith("!"):
            continue
        if line.lstrip().startswith("no "):
            continue
        if line.strip() == "":
            continue
        result.append(line)

    return "\n".join(result)
