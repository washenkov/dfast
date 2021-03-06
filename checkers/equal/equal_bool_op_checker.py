# -*- coding: utf-8 -*-
"""The module represents equal boolean operation checker class.
Equal boolean operations are: "or" and "and".

Copyright (C) 2016-2017 Arthur Vaschenkov

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import ast

import checkers.equal.abstract.equal_checker as equal_checker
from checkers.abstract import checker


class EqualBoolOpChecker(equal_checker.EqualChecker):
    """The class represents equal boolean operation checker.

    Attributes:
        ERROR_MSG (str): A message which describes the problem.

    """

    def __init__(self):
        super(EqualBoolOpChecker, self).__init__()
        self.ERROR_MSG = "boolean operation with equal arguments"

    def check(self, ast_vertex, source_file):  # todo: refactor this
        super(EqualBoolOpChecker, self).check(ast_vertex, source_file)

        if isinstance(ast_vertex, ast.BoolOp):
            last_idx = len(ast_vertex.values) - 1

            for arg1_idx in range(last_idx):
                for arg2_idx in range(arg1_idx + 1, last_idx + 1):
                    arg1 = ast_vertex.values[arg1_idx]
                    arg2 = ast_vertex.values[arg2_idx]

                    if self._are_equal_ast_vertices(self, arg1, arg2):
                        self.raise_issue(ast_vertex, source_file, self.ERROR_MSG)
                        return True
        return False
