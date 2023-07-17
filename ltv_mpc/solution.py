#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Process solutions to a model predictive control problem."""

import numpy as np

from .problem import Problem


class Solution:
    r"""State and input trajectories that optimize an MPC problem.

    See also the :class:`ltv_mpc.problem.Problem` class.

    Attributes:
        stacked_inputs: Stacked vector of inputs :math:`u_k` for
            :math:`k \in \{0, \ldots, N - 1\}`.
    """

    stacked_inputs: np.ndarray

    def __init__(self, problem: Problem, stacked_inputs: np.ndarray):
        """Test."""
        self.problem = problem
        self.stacked_inputs = stacked_inputs
        self.__stacked_states = None

    @property
    def first_input(self) -> np.ndarray:
        """Get the first control input of the solution.

        In model predictive control, this is the part of the solution we are
        mainly interested in.
        """
        return self.stacked_inputs[0]

    @property
    def stacked_states(self):
        r"""Stacked vector of states.

        This is the vector :math:`X` structured as:

        .. math::

            X = \begin{bmatrix} x_0 \\ x_1 \\ \vdots \\ x_N \end{bmatrix}

        with :math:`N` the number of timesteps.

        Note:
            The time complexity of calling this property is :math:`O(N)` the
            first time, then :math:`O(1)` as the result is memoized.
        """
        if self.__stacked_states is not None:
            return self.__stacked_states
        X = np.zeros((self.problem.nb_timesteps + 1, self.problem.state_dim))
        X[0] = self.problem.initial_state
        for k in range(self.problem.nb_timesteps):
            A = self.problem.get_transition_state_matrix(k)
            B = self.problem.get_transition_input_matrix(k)
            X[k + 1] = A.dot(X[k]) + B.dot(self.stacked_inputs[k])
        self.__stacked_states = X
        return X
