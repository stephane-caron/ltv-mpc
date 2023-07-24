# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

### Added

- Base class for exceptions raised by this library
- Documentation checks using ``ruff``
- Exception: ``ProblemDefinitionError``
- MPCProblem: setter for the initial state
- MPCProblem: target state trajectory for stage state cost
- Plan: ``first_input`` getter
- Plan: ``is_empty`` property

### Changed

- Always add state-input inequalities (even when unfeasible)
- Don't assume a ``Problem`` is fully defined in constructor
- Initial and goal states are now keyword arguments of ``MPCProblem``
- Rename ``Problem`` to ``MPCProblem``
- Rename ``Solution`` to ``Plan``
- Rename ``stacked_inputs`` to just ``inputs`` in plans
- Rename ``stacked_states`` to just ``states`` in plans
- Rename ``build_qp`` to ``build_mpc_qp``
- Solver keyword argument to ``solve_mpc`` is now mandatory
- Use problem class from ``qpsolvers`` internally
- Warn rather than raise an exception when initial state is unfeasible

## [1.0.0] - 2022/08/12

### Added

- New ``mpc_interface`` alternative in the README

### Changed

- ``solve_qp`` now takes a mandatory ``solver`` keyword argument

### Fixed

- Unit tests for the new ``solver`` keyword argument

## [0.7.0] - 2022/04/03

### Added

- ``sparse`` keyword argument to use with sparse QP solvers
- Usage and examples documentation sections

### Changed

- Only export ``Problem``, ``Solution`` and ``solve_mpc`` module-wide

### Fixed

- Edge case where inputs don't affect the first inequality constraints

## [0.6.0] - 2022/03/30

### Added

- Initial import from [pymanoid](https://github.com/stephane-caron/pymanoid/blob/5158d8902df6265604cec5d790e96f0035575c7a/pymanoid/mpc.py)'s ``mpc.py``.
- Humanoid step example
- Triple integrator example

### Changed

- Extend to time-varying state and input transition matrices
