from __future__ import annotations

import numpy as np

from fdsn import (
    critical_fractional_order,
    fractional_stability_margin,
    is_integer_order_stable,
    is_purely_fractionally_stabilized,
)


def main() -> None:
    # Complex-conjugate pair with positive real part: unstable for alpha=1,
    # but stable for sufficiently small fractional order.
    A = np.array([[0.10, -1.00], [1.00, 0.10]])
    alpha = 0.8

    vals = np.linalg.eigvals(A)
    print("A =\n", A)
    print("eigenvalues:", vals)
    print("critical alpha:", critical_fractional_order(A))
    print("margin at alpha=", alpha, ":", fractional_stability_margin(A, alpha))
    print("integer-order stable:", is_integer_order_stable(A))
    print("purely fractional stabilization:", is_purely_fractionally_stabilized(A, alpha))


if __name__ == "__main__":
    main()
