# -*- coding: utf-8 -*-
"""The module represents equal comparison checker class.
Comparison operations are: "==", "!=" or "<>", "<", "<=", ">", ">=",
"is", "is not", "in", "not in".

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
import checkers.abstract.checker as checker


class EqualComparisonChecker(equal_checker.EqualChecker):
    """The class represents equal comparison operation checker.

    Attributes:
        ERROR_MSG (str): A message which describes the problem.

    """

    def __init__(self):
        super(EqualComparisonChecker, self).__init__()
        self.ERROR_MSG = "comparison of equal arguments"

    def check(self, ast_vertex, source_file):  # todo: refactor this
        super(EqualComparisonChecker, self).check(ast_vertex, source_file)

        if isinstance(ast_vertex, ast.Compare):
            arg1 = ast_vertex.left
            for arg2 in ast_vertex.comparators:
                if self._are_equal_ast_vertices(self, arg1, arg2):
                    self.raise_issue(ast_vertex, source_file, self.ERROR_MSG)
                    return True
                arg1 = arg2
        return False
