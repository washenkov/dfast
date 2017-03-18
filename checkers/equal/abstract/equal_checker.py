# -*- coding: utf-8 -*-
"""The module represents an abstract equal checker class.

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

from abc import abstractmethod

import checkers.abstract.checker

import ast


class EqualChecker(checkers.abstract.checker.Checker):
    """The class presents a report of checker's work.

    Attributes:
        SNIPPET_RADIUS (int): A radius of code snippets for issues raised by
        the checker.

    """

    def __init__(self):
        super(EqualChecker, self).__init__()
        self.SNIPPET_RADIUS = 2

    def _get_code_snippet(self, ast_vertex, source_file):
        """Return a snippet of code related to the found issue.

            Args:
                ast_vertex (ast.AST): A vertex of AST for hash generation.
                source_file (file): A source file which contains the vertex.

            Returns:
                Code snippet as a string.

            Raises:
                TypeError: If arg "ast_vertex" is not an instance of "ast.AST".
                TypeError: If arg "source_file" is not an instance of "file".
                ValueError: If "source_file" is closed.

        """

        super(EqualChecker, self)._get_code_snippet(ast_vertex, source_file)

        snippet = ''
        first_line_idx = ast_vertex.lineno - self.SNIPPET_RADIUS - 1
        last_line_idx = ast_vertex.lineno + self.SNIPPET_RADIUS - 1

        source_file.seek(0)

        lines = source_file.readlines()

        for i in range(first_line_idx, last_line_idx):
            snippet += lines[i]
        return snippet

    @staticmethod
    def __get_ast_vertex_hash(self, ast_vertex):  # TODO: Bullshit!!!
        """Return a hash of the ast vertex as a string.

            Args:
                ast_vertex (ast.AST): A vertex of AST for hash generation.

            Returns:
                Hash of the node as a string.

        """

        return ast.dump(ast_vertex)

    @staticmethod
    def _are_equal(self, ast_vertex1, ast_vertex2):
        """Return True if the vertexes are equal, False otherwise.

        Args:
            ast_vertex1 (ast.AST): The first vertex of AST to compare.
            ast_vertex2 (ast.AST): The second vertex of AST to compare.

        Returns:
            True if the vertexes are equal, False otherwise.

        Raises:
            TypeError: If arg "ast_vertex1" or "ast_vertex2" is not an instance
            of "ast.AST".

        """

        if not isinstance(ast_vertex1, ast.AST):
            raise TypeError('Error: arg \"ast_vertex1\" is not an instance \
                            of \"ast.AST\"!')
        if not isinstance(ast_vertex2, ast.AST):
            raise TypeError('Error: arg \"ast_vertex2\" is not an instance \
                            of \"ast.AST\"!')

        if self.__get_ast_vertex_hash(self, ast_vertex1) == \
                self.__get_ast_vertex_hash(self, ast_vertex2):
            return True
        else:
            return False

    @abstractmethod
    def check(self, ast_vertex, source_file):
        super(EqualChecker, self).check(ast_vertex, source_file)
