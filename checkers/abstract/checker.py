# -*- coding: utf-8 -*-
"""The module represents abstract checker class and it's components.

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
from abc import ABCMeta, abstractmethod


class IssueLocation(object):
    """The class presents information about detected issue location.

    Attributes:
        source_file (file): A source_file containing the issue.
        ast_vertex (ast.AST): ast vertex from the file.

    """

    def __init__(self, ast_vertex, source_file):
        """IssueLocation constructor.

            Args:
                source_file (file): A source_file to file containing the issue.
                ast_vertex (ast.AST): Line number in the file.

            Raises:
                TypeError: If arg "source_file" is not an instance of "file".
                TypeError: If arg "ast_vertex" is not an instance of "ast.AST".

        """

        if isinstance(source_file, file):
            self.source_file = source_file
        else:
            raise TypeError('Error: arg \"source_file\" is not an instance of \
                    \"file\"!')
        if isinstance(ast_vertex, ast.AST):
            self.ast_vertex = ast_vertex
        else:
            raise TypeError('Error: arg \"ast_vertex\" is not an instance of \
                    \"ast.AST\"!')


class Issue(object):
    """The class presents information about detected issue.

    Attributes:
        issue_loc (IssueLocation): Location info.
        explanation (str): Text explanation for the issue.
        code_snippet (str): Code snippet of the issue.

    """

    def __init__(self, issue_loc, explanation, code_snippet):
        """Issue constructor.

            Args:
                issue_loc (IssueLocation): Location info.
                explanation (str): Text explanation for the issue.
                code_snippet (str): Code snippet of the issue.

            Raises:
                TypeError: If arg "issue_loc" is not an instance of
                "IssueLocation".
                TypeError: If arg "explanation" is not an instance of "str".
                TypeError: If arg "code_snippet" is not an instance of "str".

        """

        if isinstance(issue_loc, IssueLocation):
            self.issue_loc = issue_loc
        else:
            raise TypeError('Error: arg \"issue_loc\" is not an instance of \
                    \"IssueLocation\"!')
        if isinstance(explanation, str):
            self.explanation = explanation
        else:
            raise TypeError('Error: arg \"explanation\" is not an instance of \
                    \"str\"!')
        if isinstance(code_snippet, str):
            self.code_snippet = code_snippet
        else:
            raise TypeError('Error: arg \"code_snippet\" is not an instance \
                            of \"str\"!')

    @property
    def description(self):
        """Issue text description."""
        description = self.issue_loc.source_file.name + ':' + \
                      str(self.issue_loc.ast_vertex.lineno) + ':' + \
                      str(self.issue_loc.ast_vertex.col_offset) + ': ' + \
                      'error: ' + self.explanation + '\n' + \
                      self.code_snippet

        return description


class Statistics(object):
    """The class presents a report of checker's work.

    Attributes:
        raised_issues (List of Issues): A list of raised issues.

    """

    def __init__(self):
        self.raised_issues = []

    def add_issue(self, issue):
        """Adds an issue to the statistics.

        Args:
            issue (Issue): an issue to add.

        Returns:
            None.

        Raises:
            TypeError: If arg "issue" is not an instance of "Issue".

        """

        if isinstance(issue, Issue):
            self.raised_issues.append(issue)
        else:
            raise TypeError('Error: arg \"issue\" is not an instance \
                            of \"Issue\"!')


class Checker(object):
    """The class presents an abstract checker.

    Attributes:
        statistics (Statistics): A statistics of using of the checker.

    """

    def __init__(self):
        """Checker constructor. It initialises a statistics of the checker."""
        self.statistics = Statistics()

    __metaclass__ = ABCMeta

    @abstractmethod
    def _get_code_snippet(self, ast_vertex, source_file):
        """Returns a code snippet for given ast vertex.

        Args:
            ast_vertex (ast.AST): Given ast vertex.
            source_file (file): The file which contains the ast vertex.

        Returns:
            Code snippet as a string.

        Raises:
            TypeError: If arg "ast_vertex" is not an instance of "ast.AST".
            TypeError: If arg "source_file" is not an instance of "file".
            ValueError: If "source_file" is closed.

        """
        if not isinstance(ast_vertex, ast.AST):
            raise TypeError('Error: arg \"ast_vertex\" is not an instance \
                            of \"ast.AST\"!')
        if not isinstance(source_file, file):
            raise TypeError('Error: arg \"source_file\" is not an instance \
                            of \"file\"!')

    @abstractmethod
    def check(self, ast_vertex, source_file):
        """Checks the "ast_vertex" and add a new issue to the statistics,
        if a problem is found.

        Args:
            ast_vertex (ast.AST): A vertex of AST to check.
            source_file (file): The file which contains the "ast_vertex".

        Returns:
            True if an issue was detected by the checker, False otherwise.

        Raises:
            TypeError: If arg "ast_vertex" is not an instance of "ast.AST".
            TypeError: If arg "source_file" is not an instance of "file".
            ValueError: If "source_file" is closed.

        """

        if not isinstance(ast_vertex, ast.AST):
            raise TypeError('Error: arg \"ast_vertex\" is not an instance \
                            of \"ast.AST\"!')
        if not isinstance(source_file, file):
            raise TypeError('Error: arg \"source_file\" is not an instance \
                            of \"file\"!')
