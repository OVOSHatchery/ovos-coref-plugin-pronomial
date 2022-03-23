import pronomial
from ovos_plugin_manager.coreference import CoreferenceSolverEngine


class PronomialCoreferenceSolver(CoreferenceSolverEngine):
    @classmethod
    def solve_corefs(cls, text, lang="en"):
        return pronomial.replace_corefs(text, lang=lang)
