import math
from utils import ErrorAnalyzer


class MaclaurinSolver:
    """Aproxima sin(x) usando la serie de Maclaurin con parada temprana por error."""

    MAX_TERMS = 10
    STOP_ERROR = 5.0  # porcentaje

    def solve(self, x: float = math.pi / 3, verbose: bool = True) -> float:
        true_value = math.sin(x)
        accumulated = 0.0

        for n in range(self.MAX_TERMS):
            term = ((-1) ** n * x ** (2 * n + 1)) / math.factorial(2 * n + 1)
            accumulated += term
            error = ErrorAnalyzer.relative_percentage_error(true_value, accumulated)

            if verbose:
                print(f"  n={n}  |  término = {term:.10f}  |  acumulado = {accumulated:.10f}  |  error = {error:.6f}%")

            if error < self.STOP_ERROR:
                if verbose:
                    print(f"  -> Parada temprana: error {error:.6f}% < {self.STOP_ERROR}%\n")
                break

        return accumulated
