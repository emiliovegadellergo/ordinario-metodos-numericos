class ErrorAnalyzer:
    @staticmethod
    def absolute_error(true_value: float, approx_value: float) -> float:
        """Calculate the absolute error between a true value and an approximation.

        Args:
            true_value: The exact or reference value.
            approx_value: The approximated value.

        Returns:
            The absolute error |true_value - approx_value|.
        """
        return abs(true_value - approx_value)

    @staticmethod
    def relative_percentage_error(true_value: float, approx_value: float) -> float:
        """Calculate the relative percentage error between a true value and an approximation.

        Args:
            true_value: The exact or reference value (must not be zero).
            approx_value: The approximated value.

        Returns:
            The relative percentage error (|true_value - approx_value| / |true_value|) * 100.

        Raises:
            ValueError: If true_value is zero.
        """
        if true_value == 0:
            raise ValueError("true_value cannot be zero for relative percentage error.")
        return (abs(true_value - approx_value) / abs(true_value)) * 100
