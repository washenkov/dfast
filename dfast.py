# -*- coding: utf-8 -*-
"""The module represents main script to run the tool.

Examples:
        $ python path2ProjectRoot/dfast.py path2ProjectToAnalyse > output.txt

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

Todo:
    * Rewrite the file.

"""

import sys
import os
import ast

import checkers.equal.equal_bool_op_checker as equal_bool_op_checker
import checkers.equal.equal_comp_checker as equal_comp_checker


def walk(checker_list, source_file):
    ast_root = ast.parse(source_file.read())
    for ast_vertex in ast.walk(ast_root):
        for checker in checker_list:
            checker.check(ast_vertex, source_file)


def show_issues(checkers):
    for checker in checkers:
        for issue in checker.statistics.raised_issues:
            description = issue.description

            print description


def check_path(source_path_p):
    for file_name in os.listdir(source_path_p):
        if os.path.isfile(source_path_p + '/' + file_name) and \
                file_name.lower().endswith('.py'):
            source_file = open(source_path_p + '/' + file_name, 'r')

            checkers = [
                equal_bool_op_checker.EqualBoolOpChecker(),
                equal_comp_checker.EqualComparisonChecker()
            ]

            try:
                walk(checkers, source_file)
            except SyntaxError:
                print 'Parsing failed!'
            except StandardError:
                print 'Parsing failed!'
            source_file.close()
            show_issues(checkers)
        elif os.path.isdir(source_path_p + '/' + file_name):
            check_path(source_path_p + "/" + file_name)

source_path = sys.argv[1]

check_path(source_path)
