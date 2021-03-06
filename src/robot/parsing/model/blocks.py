#  Copyright 2008-2015 Nokia Networks
#  Copyright 2016-     Robot Framework Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import ast

from robot.utils import normalize_whitespace

from ..lexer import Token


class Block(ast.AST):
    _fields = ()


class File(Block):
    _fields = ('sections',)

    def __init__(self):
        self.sections = []

    @property
    def has_tests(self):
        return any(isinstance(s, TestCaseSection) for s in self.sections)


class Section(Block):
    _fields = ('header', 'body')

    def __init__(self, header=None, body=None):
        self.header = header
        self.body = Body(body)


class SettingSection(Section):
    type = Token.SETTING_HEADER


class VariableSection(Section):
    type = Token.VARIABLE_HEADER


class TestCaseSection(Section):
    type = Token.TESTCASE_HEADER

    @property
    def tasks(self):
        header = normalize_whitespace(self.header.data_tokens[0].value)
        return header.strip('* ').upper() in ('TASKS', 'TASK')


class KeywordSection(Section):
    type = Token.KEYWORD_HEADER


class CommentSection(Section):
    type = Token.COMMENT_HEADER


class Body(Block):
    _fields = ('items',)

    def __init__(self, items=None):
        self.items = items or []

    def add(self, item):
        self.items.append(item)


class TestCase(Block):
    type = Token.NAME
    _fields = ('name_tokens', 'body')

    def __init__(self, name_tokens):
        self.name_tokens = name_tokens
        self.body = Body()

    @property
    def name(self):
        return self.name_tokens.name


class Keyword(Block):
    _fields = ('name_tokens', 'body')

    def __init__(self, name_tokens):
        self.name_tokens = name_tokens
        self.body = Body()

    @property
    def name(self):
        return self.name_tokens.name


class ForLoop(Block):
    _fields = ('type', 'header', 'body', 'end')

    def __init__(self, header):
        self.header = header
        self.body = Body()
        self.end = None

    @property
    def variables(self):
        return self.header.variables

    @property
    def values(self):
        return self.header.values

    @property
    def flavor(self):
        return self.header.flavor

    @property
    def _header(self):
        return self.header._header

    @property
    def _end(self):
        return self.end.value if self.end else None
