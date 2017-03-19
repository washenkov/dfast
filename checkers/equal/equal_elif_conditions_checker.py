# -*- coding: utf-8 -*-
"""The module represents equal if and elif conditions checker class.

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


class EqualIfConditionsChecker(equal_checker.EqualChecker):
    """The class represents equal if and elif conditions checker.

    Attributes:
        ERROR_MSG (str): A message which describes the problem.

    """

    def __init__(self):
        super(EqualIfConditionsChecker, self).__init__()
        self.ERROR_MSG = "if branches with equal conditions"

    def _get_code_snippet(self, ast_vertex, source_file):
        super(equal_checker.EqualChecker, self).\
            _get_code_snippet(ast_vertex, source_file)

        snippet = ''
        first_line_idx = ast_vertex.lineno - self.SNIPPET_RADIUS - 1

        for else_vertex in ast_vertex.orelse:
            if isinstance(else_vertex, ast.If):
                if self._are_equal_ast_vertices(self, ast_vertex.test, else_vertex.test):
                    last_line_idx = else_vertex.lineno + \
                                    self.SNIPPET_RADIUS - 1

        source_file.seek(0)

        lines = source_file.readlines()

        for i in range(first_line_idx, last_line_idx):
            snippet += lines[i]
        return snippet

    def check(self, ast_vertex, source_file):  # todo: refactor this
        super(EqualIfConditionsChecker, self).check(ast_vertex, source_file)

        if isinstance(ast_vertex, ast.If):
            for else_vertex in ast_vertex.orelse:
                if isinstance(else_vertex, ast.If) and \
                   self._are_equal_ast_vertices(self, ast_vertex.test, else_vertex.test):
                    if ast_vertex.col_offset == else_vertex.col_offset - 5:  # todo: it's a magic number!
                        self.raise_issue(ast_vertex, source_file, self.ERROR_MSG)
                        return True
        return False
