#!/home/demori/PycharmProjects/mini-manager/miniManager/venv/bin/python
# -*- coding: utf-8 -*-
# Copyright (C) 2011, 2012, Wolfgang Scherer, <Wolfgang.Scherer at gmx.de>
#
# This file is part of AdHoc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>,
# or write to Wolfgang Scherer, <Wolfgang.Scherer at gmx.de>

# @:adhoc_uncomment:@
# @:adhoc_template:@ doc/index.rst
# AdHoc Standalone Python Script Generator
# ########################################
#
# The *AdHoc* compiler can be used as a program (see `Script Usage`_)
# as well as a module (see :class:`adhoc.AdHoc`).
#
# Since the *AdHoc* compiler itself is installed as a compiled *AdHoc*
# script, it serves as its own usage example.
#
# After installation of the *adhoc.py* script, the full source can be
# obtained in directory ``__adhoc__``, by executing::
#
#     adhoc.py --explode
#
# .. @@contents@@
#
# @:adhoc_template:@ doc/index.rst # off
# @:adhoc_uncomment:@

"""\
.. _Script Usage:

adhoc.py - Python ad hoc compiler.

======  ====================
usage:  adhoc.py [OPTIONS] [file ...]
or      import adhoc
======  ====================

Options
=======

  ===================== ==================================================
  -c, --compile         compile file(s) or standard input into output file
                        (default: standard output).
  -d, --decompile       decompile file(s) or standard input into
                        output directory (default ``__adhoc__``).
  -o, --output OUT      output file for --compile/output directory for
                        --decompile.

  -q, --quiet           suppress warnings
  -v, --verbose         verbose test output
  --debug[=NUM]         show debug information

  -h, --help            display this help message
  --documentation       display module documentation.

  --template list       show available templates.
  --eide[=COMM]         Emacs IDE template list (implies --template list).
  --template[=NAME]     extract named template to standard
                        output. Default NAME is ``-``.
  --extract[=DIR]       extract adhoc files to directory DIR (default: ``.``)
  --explode[=DIR]       explode script with adhoc in directory DIR
                        (default ``__adhoc__``)
  --implode             implode script with adhoc
  --install             install adhoc.py script

  -t, --test            run doc tests
  ===================== ==================================================

*adhoc.py* is compatible with Python 2.4+ and Python 3. (For Python
<2.6 the packages *stringformat* and *argparse* are needed and
included.)

.. _END_OF_HELP:

.. |=NUM| replace:: ``[=NUM]``

Script Examples
===============

Templates
---------

Sections marked by |adhoc_template| can be retrieved as templates on
standard output.

Additionally, all other files compiled into an adhoc file with one of

================ ======================
|adhoc|          ==> |adhoc_import|
|adhoc_verbatim| ==> |adhoc_template_v|
|adhoc_include|  ==> |adhoc_unpack|
================ ======================

are accessible as templates.

``python adhoc.py --template list`` provides a list of templates:

>>> ign = main('adhoc.py --template list'.split())
================================================= ================================ ================
                     Command                                  Template                   Type
================================================= ================================ ================
adhoc.py --template adhoc_test                    # !adhoc_test                    adhoc_import
adhoc.py --template adhoc_test.sub                # !adhoc_test.sub                adhoc_import
adhoc.py --template argparse_local                # !argparse_local                adhoc_import
adhoc.py --template namespace_dict                # !namespace_dict                adhoc_import
adhoc.py --template stringformat_local            # !stringformat_local            adhoc_import
adhoc.py --template use_case_000_                 # !use_case_000_                 adhoc_import
adhoc.py --template use_case_001_templates_       # !use_case_001_templates_       adhoc_import
adhoc.py --template use_case_002_include_         # !use_case_002_include_         adhoc_import
adhoc.py --template use_case_003_import_          # !use_case_003_import_          adhoc_import
adhoc.py --template use_case_005_nested_          # !use_case_005_nested_          adhoc_import
adhoc.py --template docutils.conf                 # docutils.conf                  adhoc_template_v
adhoc.py --template                               # -                              adhoc_template
adhoc.py --template README.txt                    # README.txt                     adhoc_template
adhoc.py --template adhoc_init                    # -adhoc_init                    adhoc_template
adhoc.py --template catch-stdout                  # -catch-stdout                  adhoc_template
adhoc.py --template col-param-closure             # -col-param-closure             adhoc_template
adhoc.py --template doc/USE_CASES.txt             # doc/USE_CASES.txt              adhoc_template
adhoc.py --template doc/index.rst                 # doc/index.rst                  adhoc_template
adhoc.py --template max-width-class               # -max-width-class               adhoc_template
adhoc.py --template rst-to-ascii                  # -rst-to-ascii                  adhoc_template
adhoc.py --template test                          # -test                          adhoc_template
adhoc.py --template MANIFEST.in                   # !MANIFEST.in                   adhoc_unpack
adhoc.py --template Makefile                      # !Makefile                      adhoc_unpack
adhoc.py --template README.css                    # !README.css                    adhoc_unpack
adhoc.py --template doc/Makefile                  # !doc/Makefile                  adhoc_unpack
adhoc.py --template doc/_static/adhoc-logo-32.ico # !doc/_static/adhoc-logo-32.ico adhoc_unpack
adhoc.py --template doc/adhoc-logo.svg            # !doc/adhoc-logo.svg            adhoc_unpack
adhoc.py --template doc/conf.py                   # !doc/conf.py                   adhoc_unpack
adhoc.py --template doc/make.bat                  # !doc/make.bat                  adhoc_unpack
adhoc.py --template doc/z-massage-index.sh        # !doc/z-massage-index.sh        adhoc_unpack
adhoc.py --template setup.py                      # !setup.py                      adhoc_unpack
================================================= ================================ ================

``python adhoc.py --template`` prints the standard template ``-``
(closing delimiter replaced by ellipsis):

>>> ign = main('./adhoc.py --template'.split()) #doctest: +ELLIPSIS
# @:adhoc_disable... allow modification of exploded sources in original place
sys.path.append('__adhoc__')
# @:adhoc_disable...
<BLANKLINE>
# @:adhoc_run_time... The run-time class goes here
# @:adhoc_run_time_engine... settings enabled at run-time
# @:adhoc_enable...
# RtAdHoc.flat = False
# @:adhoc_enable...
# @:adhoc_run_time_engine...
<BLANKLINE>
#import adhoc                                               # @:adhoc...

``python adhoc.py --template test`` prints the template named ``-test``.
the leading ``-`` signifies disposition to standard output:

>>> ign = main('./adhoc.py --template test'.split())
Test template.

Extract
-------

The default destination for extracting files is the current working
directory.

Files extracted consist of

- packed files generated by |adhoc_include|
- templates generated by |adhoc_verbatim|
- templates with a file destination other than standard output

``python adhoc.py --extract __adhoc_extract__`` unpacks the following files into
directory ``__adhoc_extract__``:

>>> import shutil
>>> ign = main('./adhoc.py --extract __adhoc_extract__'.split())
>>> file_list = []
>>> for dir, subdirs, files in os.walk('__adhoc_extract__'):
...     file_list.extend([os.path.join(dir, file_) for file_ in files])
>>> for file_ in sorted(file_list):
...     printf(file_)
__adhoc_extract__/MANIFEST.in
__adhoc_extract__/Makefile
__adhoc_extract__/README.css
__adhoc_extract__/README.txt
__adhoc_extract__/doc/Makefile
__adhoc_extract__/doc/USE_CASES.txt
__adhoc_extract__/doc/_static/adhoc-logo-32.ico
__adhoc_extract__/doc/adhoc-logo.svg
__adhoc_extract__/doc/conf.py
__adhoc_extract__/doc/index.rst
__adhoc_extract__/doc/make.bat
__adhoc_extract__/doc/z-massage-index.sh
__adhoc_extract__/docutils.conf
__adhoc_extract__/setup.py
__adhoc_extract__/use_case_000_.py
__adhoc_extract__/use_case_001_templates_.py
__adhoc_extract__/use_case_002_include_.py
__adhoc_extract__/use_case_003_import_.py
__adhoc_extract__/use_case_005_nested_.py
>>> shutil.rmtree('__adhoc_extract__')

Export
------

The default destination for exporting files is the
subdirectory ``__adhoc__``.

Files exported consist of

- imported modules generated by |adhoc|
- all files covered in section `Extract`_

``python adhoc.py --explode __adhoc_explode__`` unpacks the following files into
directory ``__adhoc_explode__``:

>>> import shutil
>>> ign = main('./adhoc.py --explode __adhoc_explode__'.split())
>>> file_list = []
>>> for dir, subdirs, files in os.walk('__adhoc_explode__'):
...     file_list.extend([os.path.join(dir, file_) for file_ in files])
>>> for file_ in sorted(file_list):
...     printf(file_)
__adhoc_explode__/MANIFEST.in
__adhoc_explode__/Makefile
__adhoc_explode__/README.css
__adhoc_explode__/README.txt
__adhoc_explode__/adhoc.py
__adhoc_explode__/adhoc_test/__init__.py
__adhoc_explode__/adhoc_test/sub/__init__.py
__adhoc_explode__/argparse_local.py
__adhoc_explode__/doc/Makefile
__adhoc_explode__/doc/USE_CASES.txt
__adhoc_explode__/doc/_static/adhoc-logo-32.ico
__adhoc_explode__/doc/adhoc-logo.svg
__adhoc_explode__/doc/conf.py
__adhoc_explode__/doc/index.rst
__adhoc_explode__/doc/make.bat
__adhoc_explode__/doc/z-massage-index.sh
__adhoc_explode__/docutils.conf
__adhoc_explode__/namespace_dict.py
__adhoc_explode__/rt_adhoc.py
__adhoc_explode__/setup.py
__adhoc_explode__/stringformat_local.py
__adhoc_explode__/use_case_000_.py
__adhoc_explode__/use_case_001_templates_.py
__adhoc_explode__/use_case_002_include_.py
__adhoc_explode__/use_case_003_import_.py
__adhoc_explode__/use_case_005_nested_.py
>>> shutil.rmtree('__adhoc_explode__')

File Permissions
================

- File mode is restored.
- File ownership is not restored.
- File modification times are restored.

  Since only naive datetimes are recorded, this only works correctly
  within the same timezone.

.. @:adhoc_index_only:@

AdHoc Module
============

.. @:adhoc_index_only:@
"""

# @:adhoc_uncomment:@
# @:adhoc_template:@ doc/index.rst
#
# Purpose
# =======
#
# *AdHoc* provides python scripts with
#
# - template facilities
# - default file generation
# - standalone module inclusion
#
# @:adhoc_index_only:@
# See also `Use Cases`_.
#
# @:adhoc_index_only:@
# *AdHoc* has been designed to provide an implode/explode cycle:
#
# ========  =======  =========  =======  =========
# source_0                               xsource_0
# source_1  implode             explode  xsource_1
# ...       ------>  script.py  ------>  ...
# source_n                               xsource_n
# ========  =======  =========  =======  =========
#
# where ``xsource_i === source_i``. I.e., ``diff source_i xsource_i``
# does not produce any output.
#
# Quickstart
# ==========
#
# module.py:
#
#     | # -\*- coding: utf-8 -\*-
#     | mvar = 'value'
#
# script.py:
#
#     | # -\*- coding: utf-8 -\*-
#     | # |adhoc_run_time|
#     | import module # |adhoc|
#     | print('mvar: ' + module.mvar)
#
# Compilation::
#
#     adhoc.py --compile script.py >/tmp/script-compiled.py
#
# Execution outside source directory::
#
#     cd /tmp && python script-compiled.py
#
# shows::
#
#     mvar: value
#
# Decompilation::
#
#     cd /tmp && \
#     mkdir -p __adhoc__ && \
#     adhoc.py --decompile <script-compiled.py >__adhoc__/script.py
#
# .. |@:| replace:: ``@:``
# .. |:@| replace:: ``:@``
# .. |adhoc_run_time| replace:: |@:|\ ``adhoc_run_time``\ |:@|
# .. |adhoc| replace:: |@:|\ ``adhoc``\ |:@|
#
# Description
# ===========
#
# The *AdHoc* compiler/decompiler parses text for tagged lines and
# processes them as instructions.
#
# The minimal parsed entity is a tagged line, which is any line
# containing a recognized *AdHoc* tag.
#
# All *AdHoc* tags are enclosed in delimiters (default: |@:| and |:@|). E.g:
#
#   |@:|\ adhoc\ |:@|
#
# Delimiters come in several flavors, namely line and section
# delimiters and a set of macro delimiters. By default, line and
# section delimiters are the same, but they can be defined separately.
#
# `Flags`_ are tagged lines, which denote a single option or
# command. E.g.:
#
#   | import module     # |@:|\ adhoc\ |:@|
#   | # |@:|\ adhoc_self\ |:@| my_module_name
#
# `Sections`_ are tagged line pairs, which delimit a block of
# text. The first tagged line opens the section, the second tagged
# line closes the section. E.g.:
#
#   | # |@:|\ adhoc_enable\ |:@|
#   | # disabled_command()
#   | # |@:|\ adhoc_enable\ |:@|
#
# `Macros`_ have their own delimiters (default: |@m| and |m>|). E.g.:
#
#   | # |@m|\ MACRO_NAME\ |m>|
#
# The implementation is realized as class :class:`adhoc.AdHoc` which
# is mainly used as a namespace. The run-time part of
# :class:`adhoc.AdHoc` -- which handles module import and file export
# -- is included verbatim as class :class:`RtAdHoc` in the generated
# output.
#
# Flags
# -----
#
# :|adhoc_run_time|:
#     The place where the *AdHoc* run-time code is added.  This flag must
#     be present in files, which use the |adhoc| import feature.  It
#     is not needed for the enable/disable features.
#
#     This flag is ignored, if double commented. E.g.:
#
#       | # # |adhoc_run_time|
#
# :|adhoc| [force] [flat | full]:
#     Mark import line for run-time compilation.
#
#     If ``force`` is specified, the module is imported, even if it
#     was imported before.
#
#     If ``flat`` is specified, the module is not recursively
#     exported.
#
#     If ``full`` is specified, the module is recursively
#     exported. (This parameter takes priority over ``flat``).
#
#     If neither ``flat`` nor ``full`` are specified,
#     :attr:`adhoc.AdHoc.flat` determines the export scope.
#
#     This flag is ignored, if the line is commented out. E.g.:
#
#       | # import module  # |adhoc|
#
# .. _adhoc_include:
#
# :|adhoc_include| file_spec, ...:
#     Include files for unpacking. ``file_spec`` is one of
#
#     :file:
#       ``file`` is used for both input and output.
#
#     :file ``from`` default-file:
#       ``file`` is used for input and output. if ``file`` does not
#       exist, ``default-file`` is used for input.
#
#     :source-file ``as`` output-file:
#       ``source-file`` is used for input. ``output-file`` is used for
#       output. If ``source-file`` does not exist, ``output-file`` is
#       used for input also.
#
#     This flag is ignored, if double commented. E.g.:
#
#       | # # |adhoc_include| file
#
# :|adhoc_verbatim| [flags] file_spec, ...:
#     Include files for verbatim extraction. See adhoc_include_ for
#     ``file_spec``.
#
#     The files are included as |adhoc_template_v| sections. *file* is used
#     as *export_file* mark. If *file* is ``--``, the template disposition
#     becomes standard output.
#
#     Optional flags can be any combination of ``[+|-]NUM`` for
#     indentation and ``#`` for commenting. E.g.:
#
#       | # |adhoc_verbatim| +4# my_file from /dev/null
#
#     *my_file* (or ``/dev/null``) is read, commented and indented 4
#     spaces.
#
#     If the |adhoc_verbatim| tag is already indented, the specified
#     indentation is subtracted.
#
#     This flag is ignored, if double commented. E.g.:
#
#       | # # |adhoc_verbatim| file
#
# :|adhoc_self| name ...:
#     Mark name(s) as currently compiling.  This is useful, if
#     ``__init__.py`` imports other module parts. E.g:
#
#       | import pyjsmo             # |@:|\ adhoc\ |:@|
#
#     where ``pyjsmo/__init__.py`` contains:
#
#       | # |@:|\ adhoc_self\ |:@| pyjsmo
#       | from pyjsmo.base import * # |@:|\ adhoc\ |:@|
#
# :|adhoc_compiled|:
#     If present, no compilation is done on this file. This flag is
#     added by the compiler to the run-time version.
#
# Sections
# --------
#
# :|adhoc_enable|:
#     Leading comment char and exactly one space are removed from lines
#     in these sections.
#
# :|adhoc_disable|:
#     A comment char and exactly one space are added to non-blank
#     lines in these sections.
#
# :|adhoc_template| -mark | export_file:
#     If mark starts with ``-``, the output disposition is standard output
#     and the template is ignored, when exporting.
#
#     Otherwise, the template is written to output_file during export.
#
#     All template parts with the same mark/export_file are concatenated
#     to a single string.
#
# :|adhoc_template_v| export_file:
#     Variation of |adhoc_template|. Automatically generated by |adhoc_verbatim|.
#
# :|adhoc_uncomment|:
#     Treated like |adhoc_enable| before template output.
#
# :|adhoc_indent| [+|-]NUM:
#     Add or remove indentation before template output.
#
# :|adhoc_import|:
#     Imported files are marked as such by the compiler. There is no
#     effect during compilation.
#
# :|adhoc_unpack|:
#     Included files are marked as such by the compiler. There is no
#     effect during compilation.
#
# :|adhoc_remove|:
#     Added sections are marked as such by the compiler. Removal is
#     done when exporting.
#
#     Before compilation, existing |adhoc_remove| tags are renamed to
#     |adhoc_remove_|.
#
#     After automatically added |adhoc_remove| sections have been
#     removed during export, remaining |adhoc_remove_| tags are
#     renamed to |adhoc_remove| again.
#
#     .. note:: Think twice, before removing material from original
#        sources at compile time. It will violate the condition
#        ``xsource_i === source_i``.
#
# :|adhoc_run_time_engine|:
#     The run-time class :class:`RtAdHoc` is enclosed in this special
#     template section.
#
#     It is exported as ``rt_adhoc.py`` during export.
#
# Macros
# ------
#
# Macros are defined programmatically::
#
#     AdHoc.macros[MACRO_NAME] = EXPANSION_STRING
#
# A macro is invoked by enclosing a MACRO_NAME in
# :attr:`adhoc.AdHoc.macro_call_delimiters`. (Default: |@m|, |m>|).
#
# :|MACRO_NAME|:
#     Macro call.
#
# Internal
# --------
#
# :|adhoc_run_time_class|:
#     Marks the beginning of the run-time class.  This is only
#     recognized in the *AdHoc* programm/module.
#
# :|adhoc_run_time_section|:
#     All sections are concatenated and used as run-time code.  This is
#     only recognized in the *AdHoc* programm/module.
#
# In order to preserve the ``xsource_i === source_i`` bijective
# condition, macros are expanded/collapsed with special macro
# definition sections. (See :attr:`adhoc.AdHoc.macro_xdef_delimiters`;
# Default: |<m|, |m@|).
#
# :|adhoc_macro_call|:
#     Macro call section.
#
# :|adhoc_macro_expansion|:
#     Macro expansion section.
#
# @:adhoc_template:@ doc/index.rst # off
# @:adhoc_uncomment:@

# @:adhoc_uncomment:@
# @:adhoc_template:@ doc/index.rst
# @:adhoc_index_only:@
#
# .. include:: USE_CASES.txt
# @:adhoc_index_only:@
#
# AdHoc Script
# ============
# @:adhoc_index_only:@
#
# .. automodule:: adhoc
#     :members:
#     :show-inheritance:
#
# .. _namespace_dict:
#
# NameSpace/NameSpaceDict
# =======================
#
# .. automodule:: namespace_dict
#     :members:
#     :show-inheritance:
#
# @:adhoc_index_only:@
# @:adhoc_template:@ doc/index.rst # off
# @:adhoc_uncomment:@

# @:adhoc_uncomment:@
# @:adhoc_template:@ doc/index.rst
#
# .. |adhoc_self| replace:: |@:|\ ``adhoc_self``\ |:@|
# .. |adhoc_include| replace:: |@:|\ ``adhoc_include``\ |:@|
# .. |adhoc_verbatim| replace:: |@:|\ ``adhoc_verbatim``\ |:@|
# .. |adhoc_compiled| replace:: |@:|\ ``adhoc_compiled``\ |:@|
# .. |adhoc_enable| replace:: |@:|\ ``adhoc_enable``\ |:@|
# .. |adhoc_disable| replace:: |@:|\ ``adhoc_disable``\ |:@|
# .. |adhoc_template| replace:: |@:|\ ``adhoc_template``\ |:@|
# .. |adhoc_template_v| replace:: |@:|\ ``adhoc_template_v``\ |:@|
# .. |adhoc_uncomment| replace:: |@:|\ ``adhoc_uncomment``\ |:@|
# .. |adhoc_indent| replace:: |@:|\ ``adhoc_indent``\ |:@|
# .. |adhoc_import| replace:: |@:|\ ``adhoc_import``\ |:@|
# .. |adhoc_unpack| replace:: |@:|\ ``adhoc_unpack``\ |:@|
# .. |adhoc_remove| replace:: |@:|\ ``adhoc_remove``\ |:@|
# .. |adhoc_remove_| replace:: |@:|\ ``adhoc_remove_``\ |:@|
# .. |adhoc_run_time_class| replace:: |@:|\ ``adhoc_run_time_class``\ |:@|
# .. |adhoc_run_time_section| replace:: |@:|\ ``adhoc_run_time_section``\ |:@|
# .. |adhoc_run_time_engine| replace:: |@:|\ ``adhoc_run_time_engine``\ |:@|
# .. |@m| replace:: ``@|:``
# .. |m>| replace:: ``:|>``
# .. |<m| replace:: ``<|:``
# .. |m@| replace:: ``:|@``
# .. |MACRO_NAME| replace:: |@m|\ ``MACRO_NAME``\ |m>|
# .. |adhoc_macro_call| replace:: |<m|\ ``adhoc_macro_call``\ |m@|
# .. |adhoc_macro_expansion| replace:: |<m|\ ``adhoc_macro_expansion``\ |m@|
#
# @:adhoc_template:@ doc/index.rst # off
# @:adhoc_uncomment:@

# --------------------------------------------------
# |||:sec:||| COMPATIBILITY
# --------------------------------------------------

import sys
# (progn (forward-line 1) (snip-insert-mode "py.b.printf" t) (insert "\n"))
# adapted from http://www.daniweb.com/software-development/python/code/217214
try:
    printf = eval("print") # python 3.0 case
except SyntaxError:
    printf_dict = dict()
    try:
        exec("from __future__ import print_function\nprintf=print", printf_dict)
        printf = printf_dict["printf"] # 2.6 case
    except SyntaxError:
        def printf(*args, **kwd): # 2.4, 2.5, define our own Print function
            fout = kwd.get("file", sys.stdout)
            w = fout.write
            if args:
                w(str(args[0]))
            sep = kwd.get("sep", " ")
            for a in args[1:]:
                w(sep)
                w(str(a))
            w(kwd.get("end", "\n"))
    del printf_dict

# (progn (forward-line 1) (snip-insert-mode "py.f.isstring" t) (insert "\n"))
# hide from 2to3
exec('''
def isstring(obj):
    return isinstance(obj, basestring)
''')
try:
    isstring("")
except NameError:
    def isstring(obj):
        return isinstance(obj, str) or isinstance(obj, bytes)

# (progn (forward-line 1) (snip-insert-mode "py.b.dict_items" t) (insert "\n"))
try:
    getattr(dict(), 'iteritems')
    ditems  = lambda d: getattr(d, 'iteritems')()
    dkeys   = lambda d: getattr(d, 'iterkeys')()
    dvalues = lambda d: getattr(d, 'itervalues')()
except AttributeError:
    ditems  = lambda d: getattr(d, 'items')()
    dkeys   = lambda d: getattr(d, 'keys')()
    dvalues = lambda d: getattr(d, 'values')()

import os
import re

# --------------------------------------------------
# |||:sec:||| CONFIGURATION
# --------------------------------------------------

dbg_comm = ((('dbg_comm' in globals()) and (globals()['dbg_comm'])) or ('# '))
dbg_twid = ((('dbg_twid' in globals()) and (globals()['dbg_twid'])) or (9))
dbg_fwid = ((('dbg_fwid' in globals()) and (globals()['dbg_fwid'])) or (23))

# (progn (forward-line 1) (snip-insert-mode "py.b.dbg.setup" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.b.strings" t) (insert "\n"))
def _uc(string):                                           # ||:fnc:||
    return unicode(string, 'utf-8')
try:
    _uc("")
except NameError:
    _uc = lambda x: x

uc_type = type(_uc(""))

def uc(value):                                             # ||:fnc:||
    if isstring(value) and not isinstance(value, uc_type):
        return _uc(value)
    return value

def _utf8str(string):                                      # ||:fnc:||
    if isinstance(string, uc_type):
        return string.encode('utf-8')
    return string

def utf8str(value):                                        # ||:fnc:||
    if isstring(value):
        return _utf8str(value)
    return value

def _nativestr(string):                                    # ||:fnc:||
    # for python3, unicode strings have type str
    if isinstance(string, str):
        return string
    # for python2, encode unicode strings to utf-8 strings
    if isinstance(string, uc_type):
        return string.encode('utf-8')
    try:
        return str(string.decode('utf-8'))
    except UnicodeDecodeError:
        return string

def nativestr(value):                                      # ||:fnc:||
    if isstring(value):
        return _nativestr(value)
    return value

# (progn (forward-line 1) (snip-insert-mode "py.f.strclean" t) (insert "\n"))
def strclean(value):
    '''Make a copy of any structure with all strings converted to
    native strings.

    :func:`strclean` is good for :meth:`__str__` methods.

    It is needed for doctest output that should be compatible with
    both python2 and python3.

    The output structure is not necessarily an exact copy of the input
    structure, since objects providing iterator or item interfaces are
    only copied through those!
    '''
    if isstring(value):
        return _nativestr(value)
    if hasattr(value, 'items'):
        try:
            out = type(value)()
        except:
            (t, e, tb) = sys.exc_info() # |:debug:|
            printf(''.join(traceback.format_tb(tb)), file=sys.stderr)
            printe('OOPS: ' + t.__name__ + ': ' + str(e) + ' [' + str(value.__class__.__name__) + '] [' + str(value) + ']')
        for k, v in value.items():
            out[strclean(k)] = strclean(v)
        return out
    if hasattr(value, '__iter__') or hasattr(value, 'iter'):
        if isinstance(value, tuple):
            out = []
        else:
            out = type(value)()
        for e in value:
            out.append(strclean(e))
        if isinstance(value, tuple):
            out = type(value)(out)
        return out
    return value

# (progn (forward-line 1) (snip-insert-mode "py.f.issequence" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.b.logging" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.b.ordereddict" t) (insert "\n"))

# (progn (forward-line 1) (snip-insert-mode "py.main.pyramid.activate" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.main.project.libdir" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.main.sql.alchemy" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.main.sql.ws" t) (insert "\n"))

# The standard template should be something useful

# @:adhoc_uncomment:@
# @:adhoc_template:@ -
# # @:adhoc_disable:@ allow modification of exploded sources in original place
# sys.path.append('__adhoc__')
# # @:adhoc_disable:@
# @:adhoc_template:@
# @:adhoc_uncomment:@

# @:adhoc_run_time:@
# @:adhoc_remove:@
# @:adhoc_run_time_engine:@
# -*- coding: utf-8 -*-
# @:adhoc_compiled:@ 2022-01-26 16:21:40.151261
import sys
import os
import re

# @:adhoc_uncomment:@
# @:adhoc_template:@ -catch-stdout
try:
    from cStringIO import StringIO as _AdHocBytesIO, StringIO as _AdHocStringIO
except ImportError:
    try:
        from StringIO import StringIO as _AdHocBytesIO, StringIO as _AdHocStringIO
    except ImportError:
        from io import BytesIO as _AdHocBytesIO, StringIO as _AdHocStringIO

# @:adhoc_template:@
# @:adhoc_uncomment:@
class RtAdHoc(object):                                     # |||:cls:|||
    line_delimiters = ('@:', ':@')
    section_delimiters = ('@:', ':@')

    template_process_hooks = {}
    extra_templates = []

    export_dir = '__adhoc__'
    extract_dir = '.'
    flat = True
    forced = False

    frozen = False

    quiet = False
    verbose = False
    debug = False

    include_path = []
    export_need_init = {}
    export_have_init = {}
    extract_warn = False

    def _adhoc_string_util():
        def isstring(obj):
            return isinstance(obj, basestring)
        try:
            isstring("")
        except NameError:
            def isstring(obj):
                return isinstance(obj, str) or isinstance(obj, bytes)
        def _uc(string):
            return unicode(string, 'utf-8')
        try:
            _uc("")
        except NameError:
            _uc = lambda x: x
        uc_type = type(_uc(""))
        def uc(value):
            if isstring(value) and not isinstance(value, uc_type):
                return _uc(value)
            return value
        return staticmethod(isstring), uc_type, staticmethod(uc)

    isstring, uc_type, uc = _adhoc_string_util()

    @staticmethod
    def adhoc_tag(symbol_or_re, delimiters, is_re=False):    # |:fnc:|
        ldlm = delimiters[0]
        rdlm = delimiters[1]
        if is_re:
            ldlm = re.escape(ldlm)
            rdlm = re.escape(rdlm)
        return ''.join((ldlm, symbol_or_re, rdlm))

    @classmethod
    def tag_split(cls, string, tag, is_re=False):            # |:fnc:|
        if not is_re:
            tag = re.escape(tag)
        ro = re.compile(''.join(('^[^\n]*(', tag, ')[^\n]*$')), re.M)
        result = []
        last_end = 0
        string = cls.decode_source(string)
        for mo in re.finditer(ro, string):
            start = mo.start(0)
            end = mo.end(0)
            result.append((False, string[last_end:start]))
            result.append((True, string[start:end+1]))
            last_end = end+1
        result.append((False, string[last_end:]))
        return result

    @classmethod
    def adhoc_parse_line(cls, tagged_line, symbol_or_re=None, # |:clm:|
                         delimiters=None, is_re=False, strip_comment=None):
        if delimiters is None:
            delimiters = cls.line_delimiters
        if symbol_or_re is None:
            dlm = delimiters[1]
            if dlm:
                symbol_or_re = ''.join(('[^', dlm[0], ']+'))
            else:
                symbol_or_re = ''.join(('[^\\s]+'))
            is_re = True
        if not is_re:
            symbol_or_re = re.escape(symbol_or_re)
        tag_rx = cls.adhoc_tag(''.join(('(', symbol_or_re, ')')), delimiters, is_re=True)
        mo = re.search(tag_rx, tagged_line)
        if mo:
            ptag = mo.group(1)
        else:
            ptag = ''
        strip_rx = ''.join(('^.*', tag_rx, '\\s*'))
        tag_arg = re.sub(strip_rx, '', tagged_line).strip()
        if strip_comment:
            tag_arg = re.sub('\\s*#.*', '', tag_arg)
        return (ptag, tag_arg)

    @classmethod
    def set_delimiters(cls, line_delimiters=None, section_delimiters=None): # |:clm:|
        delimiter_state = (cls.line_delimiters, cls.section_delimiters)
        if line_delimiters is None:
            line_delimiters = delimiter_state[0]
            if section_delimiters is None:
                section_delimiters = delimiter_state[1]
        elif section_delimiters is None:
            section_delimiters = line_delimiters
        cls.line_delimiters, cls.section_delimiters = (
            line_delimiters, section_delimiters)
        return delimiter_state

    @classmethod
    def reset_delimiters(cls, delimiter_state):              # |:clm:|
        cls.line_delimiters, cls.section_delimiters = delimiter_state

    @classmethod
    def inc_delimiters(cls):                                 # |:clm:|

        inc_first = lambda dlm: (((not dlm) and ('')) or (dlm[0] + dlm))
        inc_last = lambda dlm: (((not dlm) and ('')) or (dlm + dlm[-1]))
        outer_delimiters = [(inc_first(dlm[0]), inc_last(dlm[1]))
                            for dlm in (cls.line_delimiters,
                                        cls.section_delimiters)]
        return cls.set_delimiters(*outer_delimiters)

    @classmethod
    def line_tag(cls, symbol_or_re, is_re=False):            # |:clm:|
        return cls.adhoc_tag(symbol_or_re, cls.line_delimiters, is_re)

    @classmethod
    def section_tag(cls, symbol_or_re, is_re=False):         # |:clm:|
        return cls.adhoc_tag(symbol_or_re, cls.section_delimiters, is_re)

    @classmethod
    def tag_lines(cls, string, tag, is_re=False):            # |:clm:|
        result = []
        for section in cls.tag_split(string, tag, is_re):
            if section[0]:
                result.append(section[1])
        return result

    @classmethod
    def tag_partition(cls, string, tag, is_re=False, headline=False): # |:clm:|
        in_section = False
        body_parts = []
        sections = []
        tagged_line = ''
        for section in cls.tag_split(string, tag, is_re):
            if section[0]:
                in_section = not in_section
                tagged_line = section[1]
                continue
            if in_section:
                if headline:
                    sections.append((tagged_line, section[1]))
                else:
                    sections.append(section[1])
            else:
                body_parts.append(section[1])
        return body_parts, sections

    @classmethod
    def tag_sections(cls, string, tag, is_re=False, headline=False): # |:clm:|
        body_parts, sections = cls.tag_partition(string, tag, is_re, headline)
        return sections

    @classmethod
    def line_tag_parse(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        return cls.adhoc_parse_line(tagged_line, symbol_or_re, cls.line_delimiters,
                                    is_re, strip_comment=strip_comment)

    @classmethod
    def line_tag_strip(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        return cls.line_tag_parse(tagged_line, symbol_or_re, is_re, strip_comment)[1]

    @classmethod
    def section_tag_parse(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        return cls.adhoc_parse_line(tagged_line, symbol_or_re, cls.section_delimiters,
                                    is_re, strip_comment=strip_comment)

    @classmethod
    def section_tag_strip(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        return cls.section_tag_parse(tagged_line, symbol_or_re, is_re, strip_comment)[1]

    @classmethod
    def transform_lines(cls, transform, string,              # |:clm:|
                        symbol_or_re, is_re=False, delimiters=None):
        if delimiters is None:
            delimiters = cls.line_delimiters
        result = []
        in_section = False
        for section in cls.tag_split(
            string, cls.adhoc_tag(symbol_or_re, delimiters, is_re), is_re):
            blob = section[1]
            if section[0]:
                in_section = not in_section
                blob = transform(blob)
            result.append(blob)
        string = ''.join(result)
        return string

    @classmethod
    def transform_sections(cls, transform, string,           # |:clm:|
                           symbol_or_re, is_re=False):
        result = []
        in_section = False
        headline = ''
        for section in cls.tag_split(
            string, cls.section_tag(symbol_or_re, is_re), is_re):
            blob = section[1]
            if section[0]:
                in_section = not in_section
                if in_section:
                    headline = blob
                    continue
            elif in_section:
                blob, headline = transform(blob, headline)
                result.append(headline)
            result.append(blob)
        string = ''.join(result)
        return string

    @classmethod
    def line_tag_rename(cls, string, symbol_or_re, renamed, is_re=False, delimiters=None): # |:clm:|
        if is_re:
            transform = lambda blob: re.sub(symbol_or_re, renamed, blob)
        else:
            transform = lambda blob: blob.replace(symbol_or_re, renamed)
        return cls.transform_lines(transform, string, symbol_or_re, is_re, delimiters)

    @classmethod
    def line_tag_remove(cls, string, symbol_or_re, is_re=False, delimiters=None): # |:clm:|
        transform = lambda blob: ''
        return cls.transform_lines(transform, string, symbol_or_re, is_re, delimiters)

    @classmethod
    def section_tag_rename(cls, string, symbol_or_re, renamed, is_re=False): # |:clm:|
        if is_re:
            transform = lambda blob: re.sub(symbol_or_re, renamed, blob)
        else:
            transform = lambda blob: blob.replace(symbol_or_re, renamed)
        return cls.transform_lines(transform, string, symbol_or_re, is_re, cls.section_delimiters)

    @classmethod
    def section_tag_remove(cls, string, symbol_or_re, is_re=False): # |:clm:|
        transform = lambda blob: ''
        return cls.transform_lines(transform, string, symbol_or_re, is_re, cls.section_delimiters)

    @classmethod
    def indent_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        result = []
        in_section = False
        indent = 0
        for section in cls.tag_split(
            string, cls.section_tag(symbol_or_re, is_re), is_re):
            blob = section[1]
            if section[0]:
                in_section = not in_section
                if in_section:
                    tag_arg = cls.section_tag_strip(blob)
                    if tag_arg:
                        indent = int(tag_arg)
                    else:
                        indent = -4
            else:
                if in_section and indent:
                    if indent < 0:
                        rx = re.compile(''.join(('^', ' ' * (-indent))), re.M)
                        blob = rx.sub('', blob)
                    elif indent > 0:
                        rx = re.compile('^', re.M)
                        blob = rx.sub(' ' * indent, blob)
                    indent = 0
            result.append(blob)
        string = ''.join(result)
        return string

    @classmethod
    def enable_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        enable_ro = re.compile('^([ \t\r]*)(# ?)', re.M)
        enable_sub = '\\1'
        transform = lambda blob, hl: (enable_ro.sub(enable_sub, blob), hl)
        return cls.transform_sections(transform, string, symbol_or_re, is_re)

    adhoc_rx_tab_check = re.compile('^([ ]*\t)', re.M)
    adhoc_rx_disable_simple = re.compile('^', re.M)
    adhoc_rx_min_indent_check = re.compile('^([ ]*)([^ \t\r\n]|$)', re.M)

    @classmethod
    def disable_transform(cls, section, headline=None):      # |:clm:|
        if not section:
            return (section, headline)

        if cls.adhoc_rx_tab_check.search(section):
            # tabs are evil
            if cls.verbose:
                list(map(sys.stderr.write,
                         ('# dt: evil tabs: ', repr(section), '\n')))
            return (
                cls.adhoc_rx_disable_simple.sub(
                    '# ', section.rstrip()) + '\n',
                headline)

        min_indent = ''
        for mo in cls.adhoc_rx_min_indent_check.finditer(section):
            indent = mo.group(1)
            if indent:
                if (not min_indent or len(min_indent) > len(indent)):
                    min_indent = indent
            elif mo.group(2):
                min_indent = ''
                break
        adhoc_rx_min_indent = re.compile(
            ''.join(('^(', min_indent, '|)([^\n]*)$')), re.M)

        if section.endswith('\n'):
            section = section[:-1]
        dsection = []
        for mo in adhoc_rx_min_indent.finditer(section):
            indent = mo.group(1)
            rest = mo.group(2)
            if not indent and not rest:
                #leave blank lines blank
                dsection.append('\n')
            else:
                dsection.extend((indent, '# ', rest, '\n'))
        return (''.join(dsection), headline)

    @classmethod
    def disable_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        return cls.transform_sections(
            cls.disable_transform, string, symbol_or_re, is_re)

    @classmethod
    def remove_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        ah_retained, ah_removed = cls.tag_partition(
            string, cls.section_tag(symbol_or_re, is_re), is_re)
        return ''.join(ah_retained)

    @staticmethod
    def check_coding(source):                                # |:fnc:|
        if source:
            eol_seen = 0
            for c in source:
                if isinstance(c, int):
                    lt_ = lambda a, b: a < b
                    chr_ = lambda a: chr(a)
                else:
                    lt_ = lambda a, b: True
                    chr_ = lambda a: a
                break
            check = []
            for c in source:
                if lt_(c, 127):
                    check.append(chr_(c))
                if c == '\n':
                    eol_seen += 1
                    if eol_seen == 2:
                        break
            check = ''.join(check)
            mo = re.search('-[*]-.*coding:\\s*([^;\\s]+).*-[*]-', check)
        else:
            mo = None
        if mo:
            coding = mo.group(1)
        else:
            coding = 'utf-8'
        return coding

    @classmethod
    def decode_source(cls, source):                          # |:clm:|
        if not source:
            return cls.uc('')
        if not isinstance(source, cls.uc_type) and hasattr(source, 'decode'):
            source = source.decode(cls.check_coding(source))
        return source

    @classmethod
    def encode_source(cls, source):                          # |:clm:|
        if not source:
            return ''.encode('utf-8')
        if isinstance(source, cls.uc_type) and hasattr(source, 'encode'):
            source = source.encode(cls.check_coding(source))
        return source

    @classmethod
    def read_source(cls, file_, decode=True):                # |:clm:|
        source = None
        if not file_ or file_ == '-':
            # Python3 has a buffer attribute for binary input.
            if hasattr(sys.stdin, 'buffer'):
                source = sys.stdin.buffer.read()
            else:
                source = sys.stdin.read()
        else:
            try:
                sf = open(file_, 'rb')
                source = sf.read()
                sf.close()
            except IOError:
                for module in sys.modules.values():
                    if (module
                        and hasattr(module, '__file__')
                        and module.__file__ == file_):
                        if (hasattr(module, '__adhoc__')
                            and hasattr(module.__adhoc__, 'source')):
                            source = module.__adhoc__.source
                            break
        if source is None:
            raise IOError('source not found for `' + str(file_) + '`')
        if decode:
            return cls.decode_source(source)
        return source

    @classmethod
    def write_source(cls, file_, source, mtime=None, mode=None): # |:clm:|
        esource = cls.encode_source(source)
        if not file_ or file_ == '-':
            if hasattr(sys.stdout, 'buffer'):
                sys.stdout.buffer.write(esource)
            else:
                try:
                    sys.stdout.write(esource)
                except TypeError:
                    sys.stdout.write(source)
        else:
            sf = open(file_, 'wb')
            sf.write(esource)
            sf.close()
            if mode is not None:
                os.chmod(file_, mode)
            if mtime is not None:
                import datetime
                if cls.isstring(mtime):
                    try:
                        date, ms = mtime.split('.')
                    except ValueError:
                        date = mtime
                        ms = 0
                    mtime = cls.strptime(date, '%Y-%m-%dT%H:%M:%S')
                    mtime += datetime.timedelta(microseconds=int(ms))
                if isinstance(mtime, datetime.datetime):
                    ts = int(mtime.strftime("%s"))
                else:
                    ts = mtime
                os.utime(file_, (ts, ts))

    @classmethod
    def check_xfile(cls, file_, xdir=None):                  # |:clm:|
        if xdir is None:
            xdir = cls.extract_dir
        if not file_:
            file_ = '-'
        if file_ == '-':
            return file_
        file_ = os.path.expanduser(file_)
        if os.path.isabs(file_):
            xfile = file_
        else:
            xfile = os.path.join(xdir, file_)
        xfile = os.path.abspath(xfile)
        if os.path.exists(xfile):
            # do not overwrite files
            if (cls.extract_warn or (cls.verbose)) and not cls.quiet:
                list(map(sys.stderr.write, (
                    "# xf: ", cls.__name__, ": warning file `", file_,
                    "` exists. skipping ...\n")))
            return None
        xdir = os.path.dirname(xfile)
        if not os.path.exists(xdir):
            os.makedirs(xdir)
        return xfile

    @classmethod
    def pack_file(cls, source, zipped=True):                 # |:clm:|
        import base64, gzip
        if zipped:
            sio = _AdHocBytesIO()
            gzf = gzip.GzipFile('', 'wb', 9, sio)
            gzf.write(cls.encode_source(source))
            gzf.close()
            source = sio.getvalue()
            sio.close()
        else:
            source = cls.encode_source(source)
        source = base64.b64encode(source)
        source = source.decode('ascii')
        return source

    @classmethod
    def unpack_file(cls, source64, zipped=True, decode=True): # |:clm:|
        import base64, gzip
        source = source64.encode('ascii')
        source = base64.b64decode(source)
        if zipped:
            sio = _AdHocBytesIO(source)
            gzf = gzip.GzipFile('', 'rb', 9, sio)
            source = gzf.read()
            gzf.close()
            sio.close()
        if decode:
            source = cls.decode_source(source)
        return source

    @classmethod
    def unpack_(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                mode=None, zipped=True, flat=None, source64=None):
        xfile = cls.check_xfile(file_, cls.extract_dir)
        if xfile is None:
            return
        if cls.verbose:
            list(map(sys.stderr.write,
                     ("# xf: ", cls.__name__, ": unpacking `", file_, "`\n")))
        source = cls.unpack_file(source64, zipped=zipped, decode=False)
        cls.write_source(xfile, source, mtime, mode)

    @classmethod
    def strptime(cls, date_string, format_):                 # |:clm:|
        import datetime
        if hasattr(datetime.datetime, 'strptime'):
            strptime_ = datetime.datetime.strptime
        else:
            import time
            strptime_ = lambda date_string, format_: (
                datetime.datetime(*(time.strptime(date_string, format_)[0:6])))
        return strptime_(date_string, format_)

    @classmethod
    def import_(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                mode=None, zipped=True, flat=None, source64=None):
        import datetime
        import time

        module = cls.module_setup(mod_name)

        if mtime is None:
            mtime = datetime.datetime.fromtimestamp(0)
        else:
            # mtime=2011-11-23T18:04:26[.218506], zipped=True, flat=None, source64=
            try:
                date, ms = mtime.split('.')
            except ValueError:
                date = mtime
                ms = 0
            mtime = cls.strptime(date, '%Y-%m-%dT%H:%M:%S')
            mtime += datetime.timedelta(microseconds=int(ms))

        source = cls.unpack_file(source64, zipped=zipped, decode=False)

        mod_parts = mod_name.split('.')
        mod_child = mod_parts[-1]
        parent = '.'.join(mod_parts[:-1])
        old_mtime = module.__adhoc__.mtime
        module = cls.module_setup(mod_name, file_, mtime, source, mode)
        if len(parent) > 0:
            setattr(sys.modules[parent], mod_child, module)

        if module.__adhoc__.mtime != old_mtime:
            source = cls.encode_source(module.__adhoc__.source)
            exec(source, module.__dict__)

    @classmethod
    def module_setup(cls, module=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                     source=None, mode=None):
        m = 'ms: '
        class Attr:                                          # |:cls:|
            pass

        import types, datetime, os
        if not isinstance(module, types.ModuleType):
            mod_name = module
            if mod_name is None:
                mod_name = __name__
            try:
                if mod_name not in sys.modules:
                    __import__(mod_name)
                module = sys.modules[mod_name]
            except (ImportError, KeyError):
                import imp
                module = imp.new_module(mod_name)
                sys.modules[mod_name] = module
        else:
            mod_name = module.__name__

        if mtime is None:
            if (file_ is not None
                or source is not None):
                # the info is marked as outdated
                mtime = datetime.datetime.fromtimestamp(1)
            else:
                # the info is marked as very outdated
                mtime = datetime.datetime.fromtimestamp(0)

        if not hasattr(module, '__adhoc__'):
            adhoc = Attr()
            setattr(module, '__adhoc__', adhoc)
            setattr(adhoc, '__module__', module)

            mtime_set = None
            mode_set = mode
            if hasattr(module, '__file__'):
                module_file = module.__file__
                if module_file.endswith('.pyc'):
                    module_file = module_file[:-1]
                if os.access(module_file, os.R_OK):
                    stat = os.stat(module_file)
                    mtime_set = datetime.datetime.fromtimestamp(
                        stat.st_mtime)
                    mode_set = stat.st_mode
            if mtime_set is None:
                # the info is marked as very outdated
                mtime_set = datetime.datetime.fromtimestamp(0)
            adhoc.mtime = mtime_set
            adhoc.mode = mode_set
        else:
            adhoc = module.__adhoc__

        if (mtime > adhoc.mtime
            or not hasattr(module, '__file__')):
            if file_ is not None:
                setattr(module, '__file__', file_)
                if os.access(file_, os.R_OK):             # |:api_fi:|
                    stat = os.stat(file_)
                    adhoc.mtime = datetime.datetime.fromtimestamp(
                        stat.st_mtime)
                    adhoc.mode = stat.st_mode
                    if adhoc.mtime > mtime:
                        # the file on disk is newer than the adhoc'ed source
                        try:
                            delattr(adhoc, 'source')
                        except AttributeError:
                            pass
                        source = None

        if (mtime > adhoc.mtime
            or not hasattr(adhoc, 'source')):
            if source is not None:
                adhoc.source = source
                adhoc.mtime = mtime
                adhoc.mode = mode

        if not hasattr(adhoc, 'source'):
            try:
                file_ = module.__file__
                file_, source = cls.std_source_param(file_, source)
                adhoc.source = source
            except (AttributeError, IOError):
                pass

        return module

    @classmethod
    def std_source_param(cls, file_=None, source=None): # |:clm:||:api_fi:|
        if file_ is None:
            file_ = __file__
        if file_.endswith('.pyc'):
            file_ = file_[:-1]
        if source is None:
            source = cls.read_source(file_)
        return (file_, source)

    @classmethod
    def export_source(cls, string, no_remove=False, no_disable=False): # |:clm:|
        string = cls.collapse_macros(string)
        if not no_remove:
            string = cls.remove_sections(string, 'adhoc_remove')
        string = cls.remove_sections(string, 'adhoc_import')
        string = cls.remove_sections(string, 'adhoc_unpack')
        string = cls.remove_sections(string, 'adhoc_template_v')
        if not no_disable:
            string = cls.enable_sections(string, 'adhoc_disable')
            string = cls.disable_sections(string, 'adhoc_enable')
        if not no_remove:
            string = cls.section_tag_rename(string, 'adhoc_remove_', 'adhoc_remove')
        return string

    @classmethod
    def unpack(cls, file_=None, source=None):                # |:clm:|
        file_, source = cls.std_source_param(file_, source)
        source_sections, unpack_sections = cls.tag_partition(
            source, cls.section_tag('adhoc_unpack'))
        sv_extract_warn = cls.extract_warn
        cls.extract_warn = True
        unpack_call = ''.join((cls.__name__, '.unpack_'))
        for unpack_section in unpack_sections:
            unpack_section = re.sub('^\\s+', '', unpack_section)
            unpack_section = re.sub(
                '^[^(]*(?s)', unpack_call, unpack_section)
            try:
                #RtAdHoc = cls # unpack_call takes care of this
                exec(unpack_section.lstrip(), globals(), locals())
            except IndentationError:
                sys.stderr.write("!!! IndentationError !!!\n")
        cls.extract_warn = sv_extract_warn

    @classmethod
    def extract(cls, file_=None, source=None):               # |:clm:|
        cls.unpack(file_, source)
        cls.extract_templates(file_, source, export=True)

    @classmethod
    def export__(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                 mode=None, zipped=True, flat=None, source64=None):
        source = cls.unpack_file(source64, zipped=zipped, decode=False)
        if file_ is None:
            return
        file_base = os.path.basename(file_)
        if file_base.startswith('__init__.py'):
            is_init = True
        else:
            is_init = False

        parts = mod_name.split('.')
        base = parts.pop()
        if parts:
            module_dir = os.path.join(*parts)
            cls.export_need_init[module_dir] = True
        else:
            module_dir = ''
        if is_init:
            module_dir = os.path.join(module_dir, base)
            cls.export_have_init[module_dir] = True
        module_file = os.path.join(module_dir, file_base)

        cls.export_(source, module_file, mtime, mode, flat)

    @classmethod
    def export_(cls, source, file_, mtime, mode, flat=None): # |:clm:|
        cflat = cls.flat
        if flat is None:
            flat = cflat
        cls.flat = flat
        if not flat:
            # extract to export directory
            sv_extract_dir = cls.extract_dir
            cls.extract_dir = cls.export_dir
            cls.extract(file_, source)
            cls.extract_dir = sv_extract_dir

            source_sections, import_sections = cls.tag_partition(
                source, cls.section_tag('adhoc_import'))
            source = cls.export_source(''.join(source_sections))
            export_call = ''.join((cls.__name__, '.export__'))

            xfile = cls.check_xfile(file_, cls.export_dir)
            if xfile is not None:
                cls.write_source(xfile, source, mtime, mode)
                if cls.verbose:
                    list(map(sys.stderr.write,
                             ("# xp: ", cls.__name__, ".export_ for `", file_,
                              "` using `", export_call,"`\n")))

            for import_section in import_sections:
                # this calls RtAdHoc.export__
                import_section = re.sub('^\\s+', '', import_section)
                import_section = re.sub(
                    '^[^(]*(?s)', export_call, import_section)
                try:
                    #RtAdHoc = cls # export_call takes care of this
                    exec(import_section, globals(), locals())
                except IndentationError:
                    sys.stderr.write("!!! IndentationError !!!\n")
        else:
            xfile = cls.check_xfile(file_, cls.export_dir)
            if xfile is not None:
                cls.write_source(xfile, source, mtime, mode)
                if cls.verbose:
                    list(map(sys.stderr.write,
                             ("# xp: ", cls.__name__, ".export_ for `", file_,
                              "` using `", export_call,"`\n")))
        cls.flat = cflat

    @classmethod
    def export(cls, file_=None, source=None):                # |:clm:|
        file_, source = cls.std_source_param(file_, source)
        sv_import = cls.import_
        cls.import_ = cls.export__

        file_ = os.path.basename(file_)
        cls.export_(source, file_, None, None, False)
        sv_extract_dir = cls.extract_dir
        cls.extract_dir = cls.export_dir
        engine_tag = cls.section_tag('adhoc_run_time_engine')
        engine_source = cls.export_source(
            source, no_remove=True, no_disable=True)
        engine_source = cls.get_named_template(
            None, file_, engine_source, tag=engine_tag, ignore_mark=True)
        if engine_source:
            efile = cls.check_xfile('rt_adhoc.py')
            if efile is not None:
                cls.write_source(efile, engine_source)
        cls.extract_dir = sv_extract_dir
        for init_dir in cls.export_need_init:
            if not cls.export_have_init[init_dir]:
                if cls.verbose:
                    list(map(sys.stderr.write,
                             ("# xp: create __init__.py in `", init_dir, "`\n")))
                inf = open(os.path.join(
                    cls.export_dir, init_dir, '__init__.py'), 'w')
                inf.write('')
                inf.close()
        cls.import_ = sv_import

    @classmethod
    def dump__(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
               mode=None, zipped=True, flat=None, source64=None):
        if cls.verbose:
            list(map(sys.stderr.write,
                     ("# xf: ", cls.__name__, ": dumping `", file_, "`\n")))
        source = cls.unpack_file(source64, zipped=zipped, decode=False)
        return source

    @classmethod
    def dump_(cls, dump_section, dump_type=None):            # |:clm:|
        if dump_type is None:
            dump_type = 'adhoc_import'
        if not dump_section:
            return ''
        dump_call = ''.join(('unpacked = ', cls.__name__, '.dump__'))
        dump_section = re.sub('^\\s+', '', dump_section)
        dump_section = re.sub(
            '^[^(]*(?s)', dump_call, dump_section)
        dump_dict = {'unpacked': ''}
        try:
            #RtAdHoc = cls # dump_call takes care of this
            exec(dump_section.lstrip(), globals(), dump_dict)
        except IndentationError:
            sys.stderr.write("!!! IndentationError !!!\n")
        return dump_dict['unpacked']

    @classmethod
    def dump_file(cls, match, file_=None, source=None, tag=None, # |:clm:|
                  is_re=False):
        file_, source = cls.std_source_param(file_, source)
        if tag is None:
            tag = cls.section_tag('(adhoc_import|adhoc_update)', is_re=True)
            is_re = True
        source_sections, dump_sections = cls.tag_partition(
            source, tag, is_re, headline=True)
        dump_call = ''.join((cls.__name__, '.dump_'))
        for dump_section in dump_sections:
            tagged_line = dump_section[0]
            dump_section = dump_section[1]
            tag_arg = cls.section_tag_strip(tagged_line)
            check_match = match
            if tag_arg != match and not match.startswith('-'):
                check_match = ''.join(('-', match))
            if tag_arg != match and not match.startswith('!'):
                check_match = ''.join(('!', match))
            if tag_arg != match:
                continue
            dump_section = re.sub('^\\s+', '', dump_section)
            dump_section = re.sub(
                '^[^(]*(?s)', dump_call, dump_section)
            try:
                #RtAdHoc = cls # dump_call takes care of this
                exec(dump_section.lstrip(), globals(), locals())
            except IndentationError:
                sys.stderr.write("!!! IndentationError !!!\n")

    macro_call_delimiters = ('@|:', ':|>')
    macro_xdef_delimiters = ('<|:', ':|@')
    macros = {}

    @classmethod
    def expand_macros(cls, source, macro_call_dlm=None, macro_xdef_dlm=None): # |:clm:|
        if macro_call_dlm is None:
            macro_call_dlm = cls.macro_call_delimiters
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        import re
        for macro_name, macro_expansion in cls.macros.items():
            macro_tag = cls.adhoc_tag(macro_name, macro_call_dlm, False)
            macro_tag_rx = cls.adhoc_tag(macro_name, macro_call_dlm, True)
            macro_call = ''.join(('# ', macro_tag, '\n'))
            macro_call_rx = ''.join(('^[^\n]*', macro_tag_rx, '[^\n]*\n'))
            mc_tag = ''.join(('# ', cls.adhoc_tag('adhoc_macro_call', macro_xdef_dlm, False), "\n"))
            mx_tag = ''.join(('# ', cls.adhoc_tag('adhoc_macro_expansion', macro_xdef_dlm, False), "\n"))
            xdef = ''.join((
                mc_tag,
                macro_call,
                mc_tag,
                mx_tag,
                macro_expansion,
                mx_tag,
                ))
            rx = re.compile(macro_call_rx, re.M)
            source = rx.sub(xdef, source)
        return source

    @classmethod
    def has_expanded_macros(cls, source, macro_xdef_dlm=None): # |:clm:|
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        mx_tag = cls.adhoc_tag('adhoc_macro_expansion', macro_xdef_dlm, False)
        me_count = len(cls.tag_lines(source, mx_tag))
        return me_count > 0

    @classmethod
    def activate_macros(cls, source, macro_call_dlm=None, macro_xdef_dlm=None): # |:clm:|
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        if not cls.has_expanded_macros(source, macro_xdef_dlm):
            source = cls.expand_macros(source, macro_call_dlm, macro_xdef_dlm)
        sv = cls.set_delimiters (macro_xdef_dlm)
        source = cls.remove_sections(source, 'adhoc_macro_call')
        source = cls.section_tag_remove(source, 'adhoc_macro_expansion')
        cls.reset_delimiters(sv)
        return source

    @classmethod
    def collapse_macros(cls, source, macro_xdef_dlm=None):   # |:clm:|
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        if cls.has_expanded_macros(source, macro_xdef_dlm):
            sv = cls.set_delimiters (macro_xdef_dlm)
            source = cls.section_tag_remove(source, 'adhoc_macro_call')
            source = cls.remove_sections(source, 'adhoc_macro_expansion')
            cls.reset_delimiters(sv)
        return source

    @classmethod
    def std_template_param(cls, file_=None, source=None,     # |:clm:|
                           tag=None, is_re=False, all_=False):
        file_, source = cls.std_source_param(file_, source)
        if tag is None:
            is_re=True
            if all_:
                tag = cls.section_tag('adhoc_(template(_v)?|import|unpack)', is_re=is_re)
            else:
                tag = cls.section_tag('adhoc_template(_v)?', is_re=is_re)
        source = cls.activate_macros(source)
        return (file_, source, tag, is_re)

    @classmethod
    def get_templates(cls, file_=None, source=None,          # |:clm:|
                      tag=None, is_re=False,
                      ignore_mark=False, all_=False):
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_)
        source = cls.enable_sections(source, 'adhoc_uncomment')
        source = cls.indent_sections(source, 'adhoc_indent')
        source_sections, template_sections = cls.tag_partition(
            source, tag, is_re=is_re, headline=True)
        templates = {}
        for template_section in template_sections:
            tagged_line = template_section[0]
            section = template_section[1]
            tag, tag_arg = cls.section_tag_parse(tagged_line)
            if not tag_arg:
                tag_arg = '-'
            if tag_arg in cls.template_process_hooks:
                section = cls.template_process_hooks[tag_arg](cls, section, tag, tag_arg)
            if ignore_mark:
                tag_arg = '-'
            if tag_arg not in templates:
                templates[tag_arg] = [[section], tag]
            else:
                templates[tag_arg][0].append(section)
        if all_:
            result = dict([(m, (''.join(t[0]), t[1])) for m, t in templates.items()])
        else:
            result = dict([(m, ''.join(t[0])) for m, t in templates.items()])
        return result

    @classmethod
    def template_list(cls, file_=None, source=None,          # |:clm:|
                      tag=None, is_re=False, all_=False):
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_)
        templates = cls.get_templates(file_, source, tag, is_re, all_=all_)
        if all_:
            templates.update([(k, ('', v)) for k, v in cls.extra_templates])
            result = list(sorted(
                [(k, v[1]) for k, v in templates.items()],
                key=lambda kt: '||'.join((
                    kt[1],
                    (((not (kt[0].startswith('-') or kt[0].startswith('!')))
                      and (kt[0]))
                     or (kt[0][1:]))))))
        else:
            templates.update(filter(
                lambda tdef: (tdef[1] == 'adhoc_template'
                              or tdef[1] == 'adhoc_template_v'),
                cls.extra_templates))
            result = list(sorted(
                templates.keys(),
                key=lambda kt: '||'.join((
                    (((not (kt.startswith('-') or kt.startswith('!')))
                      and (kt)) or (kt[1:]))))))
        return result

    @classmethod
    def col_param_closure(cls):                              # |:clm:|
        mw = [0, "", ""]
        def set_(col):                                       # |:clo:|
            lc = len(col)
            if mw[0] < lc:
                mw[0] = lc
                mw[1] = " " * lc
                mw[2] = "=" * lc
            return col
        def get_():                                          # |:clo:|
            return mw
        return set_, get_

    tt_ide = False
    tt_comment = ''
    tt_prefix = ''
    tt_suffix = ''

    @classmethod
    def template_table(cls, file_=None, source=None,         # |:clm:|
                       tag=None, is_re=False):
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_=True)
        pfx = cls.tt_prefix
        sfx = cls.tt_suffix
        comm = cls.tt_comment
        if comm:
            comm = ''.join((comm, ' '))
            pfx = ''.join((comm, pfx))
        if cls.tt_ide:
            command = ''.join(('python ', file_))
        else:
            command = os.path.basename(file_)
        # Parse table
        table = []
        tpl_arg_name = (lambda t: (((not (t.startswith('-') or t.startswith('!'))) and (t)) or (t[1:])))
        col_param = [cls.col_param_closure() for i in range(3)]
        table.append((col_param[0][0]('Command'), col_param[1][0]('Template'), col_param[2][0]('Type')))
        table.extend([
            (col_param[0][0](''.join((
                pfx,
                command, ' --template ',
                tpl_arg_name(t[0])
                )).rstrip()),
             col_param[1][0](''.join((
                 '# ', t[0]
                 )).rstrip()),
             col_param[2][0](''.join((
                 t[1], sfx
                 )).rstrip()),)
            for t in cls.template_list(file_, source, tag, is_re, all_=True)])
        if cls.tt_ide:
            itable = []
            headers = table.pop(0)
            this_type = None
            last_type = None
            for cols in reversed(table):
                this_type = cols[2].replace('")', '')
                if last_type is not None:
                    if last_type != this_type:
                        itable.append((''.join((comm, ':ide: +#-+')), '', ''))
                        itable.append((''.join((comm, '. ', last_type, '()')), '', ''))
                        itable.append(('', '', ''))
                itable.append((''.join((comm, ':ide: ', cols[1].replace('#', 'AdHoc:'))), '', ''))
                itable.append(cols)
                itable.append(('', '', ''))
                last_type = this_type
            if last_type is not None:
                itable.append((''.join((comm, ':ide: +#-+')), '', ''))
                itable.append((''.join((comm, '. ', last_type, '()')), '', ''))
            table = [headers]
            table.extend(itable)
        # Setup table output
        mw, padding = (col_param[0][1]()[0], col_param[0][1]()[1])
        mw1, padding1 = (col_param[1][1]()[0], col_param[1][1]()[1])
        mw2, padding2 = (col_param[2][1]()[0], col_param[2][1]()[1])
        sep = ' '.join([cp[1]()[2] for cp in col_param])
        make_row_c = lambda row: ''.join((
            ''.join((padding[:int((mw-len(row[0]))/2)], row[0], padding))[:mw],
            ' ', ''.join((padding1[:int((mw1-len(row[1]))/2)],
                          row[1], padding1))[:mw1],
            ' ', ''.join((padding2[:int((mw2-len(row[2]))/2)],
                          row[2], padding2))[:mw2].rstrip()))
        make_row = lambda row: ''.join((''.join((row[0], padding))[:mw],
                                        ' ', ''.join((row[1], padding))[:mw1],
                                        ' ', row[2])).rstrip()
        # Generate table
        output = []
        output.append(sep)
        output.append(make_row_c(table.pop(0)))
        if table:
            output.append(sep)
            output.extend([make_row(row) for row in table])
        output.append(sep)
        return output

    @classmethod
    def get_named_template(cls, name=None, file_=None, source=None, # |:clm:|
                           tag=None, is_re=False, ignore_mark=False):
        if name is None:
            name = '-'
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_=True)
        templates = cls.get_templates(
            file_, source, tag, is_re=is_re, ignore_mark=ignore_mark, all_=True)
        check_name = name
        if check_name not in templates and not name.startswith('-'):
            check_name = ''.join(('-', name))
        if check_name not in templates and not name.startswith('!'):
            check_name = ''.join(('!', name))
        if check_name in templates:
            template_set = templates[check_name]
        else:
            template_set = ['', 'adhoc_template']
        template = template_set[0]
        template_type = template_set[1]
        if check_name.startswith('!'):
            template = cls.dump_(template, template_type)
        return template

    @classmethod
    def extract_templates(cls, file_=None, source=None,      # |:clm:|
                          tag=None, is_re=False, ignore_mark=False,
                          export=False):
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re)
        templates = cls.get_templates(
            file_, source, tag, is_re=is_re, ignore_mark=ignore_mark)
        sv_extract_warn = cls.extract_warn
        cls.extract_warn = True
        for outf, template in sorted(templates.items()):
            if outf.startswith('-'):
                outf = '-'
            if outf == '-' and export:
                continue
            xfile = cls.check_xfile(outf, cls.extract_dir)
            if xfile is not None:
                cls.write_source(xfile, template)
        cls.extract_warn = sv_extract_warn


    def compileFile(self, file_name, for_=None, zipped=True, forced=None): # |:mth:|
        file_name, source = self.std_source_param(file_name, None)
        return source
# @:adhoc_run_time_engine:@
# @:adhoc_remove:@
# @:adhoc_remove:@
# @:adhoc_run_time_engine:@
# @:adhoc_run_time_engine:@
# @:adhoc_remove:@
# @:adhoc_template:@ -

# @:adhoc_run_time:@ The run-time class goes here
# @:adhoc_run_time_engine:@ settings enabled at run-time
# @:adhoc_enable:@
# RtAdHoc.flat = False
# @:adhoc_template:@
RtAdHoc.flat = False
# @:adhoc_template:@ -
# @:adhoc_enable:@
# @:adhoc_run_time_engine:@

#import adhoc                                               # @:adhoc:@
# @:adhoc_template:@

# (progn (forward-line 1) (snip-insert-mode "py.b.sformat" t) (insert "\n"))
try:
    ('{0}').format(0)
    def sformat (fmtspec, *args, **kwargs):
        return fmtspec.format(*args, **kwargs)
except AttributeError:
    try:
        import stringformat
    except ImportError:
        try:
            # @:adhoc_import:@ !stringformat_local
            RtAdHoc.import_('stringformat_local', file_='stringformat_local.py',
                mtime='2012-09-18T09:26:21', mode=int("100664", 8),
                zipped=True, flat=None, source64=
                'H4sIAESf8WEC/81abW/bRhL+rl+xlSqQtGVGdpO0FSIbQZoABi6NEaeHHhSF'
                'oMWVxJoiVe7Stqr4v9/M7JLcJWXZbVHc+UOkcGdnZ56dd6rHjg6O2CyL4nQx'
                'YoWcH/2ATzrdbvd1dBOmMx4xIXNYZfMsX4VS6q/sYiOXWcpOx+zEf+53Oq9T'
                'Fq/WCV/xVIYyhqVszuSSs/BhPu7F2wv23fHw2EMGBTDMR+xdkuXAg/0az5Ii'
                'DVGUTgdYZ7lkOe90giBMkiBgYzZx3ile4VXCL4m7M2BOnMbSmcKeOVuGApZz'
                'F46GhXWYyxhFc7xRh8FfxOeseuiKARN8rZfwL+eyyFMmfIMGCDo8EXwE670S'
                'BEDgKfxkvqn/g38Jn8sBy+PFUoI6whfrJJZ4xoAdexUlv5vxtWT/DpOCv81z'
                'wMhiUkoJCqL2TlN8dQgxpZMAQXUFAaAS5BxOzrk/y1brOOEu7c4dt+857NG/'
                'HnP6jt7x1XXPXn2z9dyz0XbrHToP7thu6y1no/t779A9++b+4eNgy/19uWML'
                'WyZftlP1cT89/Lqlz4N778A701x6oNA6CWdki2we8yTqeLXWxVVLa1C44uN4'
                'yCHlQoLNthlVbNZ89iB6pXhnk1en4y9T76xUr8fCJF6kyK+knRwdsunZDv17'
                'TABpSdZDEvj8HB2oL4OzUturUHC2zvk8vhuwFZj/KkzYbRzJ5QA8MCtEmEYC'
                'LcAQ77P/OTr0msf2kM0sFmC+Ja1/5n3r7L4XuVlzAhaBCdDwHwTkbOR+nnhf'
                'P/tfv9hHgpISNjKIKI7v0MfEqeV0j73Jl+n04Ovkiz+ZHnh6c4/crGIOVKjS'
                '9Ou3nkuEWjMwnanDQHsWpzcAfMRkGCcgshkbcg5eEwQ3PEe1g6AMDqaXgM2A'
                'Xrbf+PBQhYIOawQDNodjBJMZwil4fsMpEv6SxhBpucKtjBeNY1y0OHBXI2yA'
                'rHAjKeAEYRSjSqH4eDvjgF5028JWrL1miNhDa0EVp5KwitOI39VIkRqxgMeS'
                'L3ju3mCkasfRkgst23z2h9Qn8DYA0uyVsEmWLkDfThV6NTw179kyd9M2Q3rM'
                '+uzkxUuQTkXgn8OVDsCmpN+ZfDGMy1zZD7CA/8K/nU6HjoIVBXQpoxFKxt2u'
                'FgLy3Tkom6fgxHbK5DmkSSQ5l3WuFWRaKhGyS+AUz+OZSsDvIRQc/StMF0W4'
                '4H7JnD5XpjmrSObD99kSU6VrLGhjASNIM8lWBk5hDFGnTkquc659bJal2pmY'
                'MOVxFCsKgAOKbYMqauloBWFjFQ7qIDQwmY3Zyl/kWbEWrhZKBGmx4nk8g7W2'
                'dc2TDJQInIpY2xAQGzsxOrQNrFRayUdEqH9Ntw+I1wldn+R0ccztebQZypbs'
                'lmMsYn2h75Q5nQezq6PR47kDhug2ZHZIPRUxlZk49V01aE0Qx8xJnVr6HvuJ'
                'z8MikRitnMih2i5Gs6JDFuoBnSWqTdalGMDSlkjJtFCa8QTEwbu24pnGUsvY'
                'iGNNPLuXsL2JoOUZrEKq65nHNPSeOX/6pNtYLlmpXreztxrqNoXBE7vVnZBt'
                'm8B/+vDTh1GVoDE/h3kos7wiWYdCYW4VjsDKdfdfsIAaxuCDf65tvs1diCiX'
                'rjOLsrtfwZC8/Uj9CZAtWwHJrEVyNgxFGG4Nz6Mzb2DBhQKTHZZueFhHBvju'
                'GqzJC0BudBQVARSjPbVz+/Z/Sa/T7DYtjYrieT8nB8iufuMzSS0NJG942mX9'
                'h63BkGygdPSDYJbAdQYBfEshjwRB7a2itDq4BedIFSwKGeiuhqbJECVQuQ7D'
                'Wv/QacBF64fwvWRNcbXm8AfPM0SVHk+GU7qxocGFFtCpU6mINIxVmWNweRfC'
                '09bOoa6G3oVCrkN4dLvkaV31gg2Sqjn/vYhzHlmCsldjaFdSN7/x9oQLwscl'
                'jiT/mAKOS1KVgZpWH7Nit4t7a9H2hpjHnH9XCNK1hL6OeZxASaXlVp+T0dHx'
                'VD+bHB2PpmayRfpaAfwfbKu0hGsjq9cZBPbUiHwxfHAdRtjcw1YF8VGJsGFW'
                '8paH11RHGM15rNr3cj/cWxZF5q2UK1AkNXC+YYdjEti2zvzGn3EsbVyd7pHE'
                'q9PEU670b6SRf/iyQR7ltK/YEKVveHULIsQDXRDddQJX7+e/FUJ7HdzSsQlP'
                '2wdNUI2ND2BKIeMUQ8aYUkOrmtgFMDTBmkLppeYURAWYXW2wfsbKofNkeUwF'
                'SuJkN3HtOrp41jUp9ZplkYdNoFA14oDSLhSSYSqDq43kYkzxqS6qdYkctnt6'
                'v6yKMdJfK7YDFiBqdIJlc9f2HcRq4uPHIooXsXQbIcdMcvQ5wciKO7ypRdi+'
                '3fZW3DbdYw8l9YJLsxSm0zpGtq53lTtcyljkejkYCMWXfq4CTB+riUZaNXpC'
                'o95WN1S1hS0F/JrGpd6iNtMmN2yVZLziWhikfohpSUqdi9Gy2PhUlUarCasl'
                'wTRUmY8aG7TaynbvXc7fpFXB6Kf0BEyYkj9rjStdVVfURvqG6G6X8Wxptngr'
                'DmVipKOT6+k28BOE58YKu+LL8AakT+JrjjL51Qpac9lbvzzULE5PT3dIVTjb'
                'cPTi3vHK3eH4+YnSy/d9CAyXUMGwULCSsE1X4KDm+YnTqdpO1RQHIsmkoPGt'
                'o/p/jErB9W2WR4K+qskbfRXVTLceUOCDTt2+BzjtRXviybxuqInMuCNc9dVx'
                'VYlSP1eHw8L2vrGip4C0Yi9ZJwGB9f8Gl4qoOetRy1DTgovypvSmkvz3SsUM'
                'knL+4HSIVgftK909K9qlyVid4O9WqMfeZCuUlkH9RlNGSFZYJmSQHeJ6ZOF3'
                'nn6UoaiGQqtKAwkrIb2BjM3J2hkPwUXaodyoe3IcqhMPNTZwh16nEbYp4vWd'
                'neA4/b7TpNclM32Fys3ep2bbFDPv7+0+B5yaw2nlkSWrA6rF6vjckIDIRhUJ'
                'e/aMnUwNYNdYEBLRMdaRRqkISEACswZMmlS9mlDTPWdkVP5JDIVZmOg3BVbX'
                'Vu/TnJ1vHAtK2FJVEfXOx+oxDjugodIlF8S8hLMky67LN0yPFWHtOVOzHkPo'
                'aiqPnbLjR4W6A1bo8wAOC+eAydNnDGWxl4vw0UlD2WvuUoL1xd72kiILpBtD'
                'tVokai6pbKGAY47m/TlEQPAgV9+1jZV6NhkdT0kJf+I0zft1IbMjqAmvuBUT'
                'KiOoYyw0Cz9n6Y6Cpg3ELEwRNwGRBBx6nmcr8NkUYwvJ/pgVmOW4HntK6BlA'
                'UrgzKF0Vk0roru1oCJYa2bqG+DaNqRe0NcdNvVF6DV5b34gnxo2Az+8p37Qw'
                'Nbm/zjBoTY6nrTOBpi45VYlkw49S7b6CHnuv8LVQa5HZNzraeQtPus3mXTzh'
                'QulSqzvDC7VMwhK8caPtbI8o1Kiv1nITYKkZXxWSt6YYugOAdgLfFKEj1Ncx'
                '2nXzN21k2md8ygve3Iz8n+IfH9JkY7waAyQ2ICU2rvRy6ynuEVcjLQu/ZiQz'
                'Igca1DUlx4lTRfYyQkCqoaXpo0HufSwEXiAKWguh0r99dgOzxxi/RXJWQ7yf'
                'ubM1jg/sXkJfupEl7ffE/p46rWoc7JFljaOZR/dsM2tNX3Cp+2piNGCTqeeH'
                '6zVkS2tq88A44K+ermrgJ59etudQJLl94Ql8QxErkqqa0z2BquUOwnwBEh0c'
                'XN/iN6Oqg96gbCesfgXNTndbVhNzYTQxZeNeTsCAs42JOs0v1lEouRvFM+lS'
                'nxh7ejDrPeY/c5qWlNQoAKexCPIjTTxzkvY2pakxLBT65VzGXl++OT8foHyW'
                'jWKUpk6zHqHWzefYeuVrdBED3O2ZVW64arQuKLG6PHBYWIxT+47paXNQUfbH'
                'CrAJ7p82nYT4ITvi0A5erXEMqgGkuwhB6gldROQiiedNDdd7ZMjztATS+qvh'
                '9R7HSnvj/x4rvUYffY3c/zGgZrtXNnqV2J1Oj5pF8pErjjkMnKAQUG5jjs/S'
                'a74BWiwdroo4keABavhHzwL9LMBXMNWl9KrWE/IkFRxLKddi9OzZIhbShwJp'
                'WVzh71Genfz44mQ4ZO7rfAX38tHXQx/1y7IZMTWfiI3o6BPm8aKAljcr4Gn8'
                'B8euJbjYBAL/E8jmREyx8tWwJVxD7HCA+DyN5fssKhL+PHj53JyRGazw9wJq'
                '9wzf1L18vmOS9TC5EleNmoDqA82WSnEuZV7M4G7M0VX1grGi9pWpCPp5XUXn'
                'Ohnmwvkslc7AFMAb2DR4FFDoIy8+nP/86e1Ht+LuafppCaweSKkpQg6dfBNL'
                'uASAb8GlGpSJBm4NoSfDETbohuRKsgBES/mdfIJo9iZI+TdP3DS10P8JMs1F'
                'nt1tDGJDcgNk18GstPeQaZ1TAQn9IpFy2SwxM2lkzH5hhYaySBYEwB7LYKsq'
                'KiHGfh4aDWf3iMh64xPtbuxUffYJxNc/gFjENzzVUEQZV90IziVZyFAgKEjC'
                'fGPMEKDsoHhZ2XPlPP7FBrEMLrk8N8Nj2kh6PfaR33BoEZA/TkGh/GfVLdQQ'
                'rTEqVs99DBhBGEU5FwJDZ+S1hKr9OVBG6KbCG7DWUwJ4ACf4KEIrIqZighTT'
                'v1QflQVQk4odnepqoh5PflTnhdWvhiJWvSWfs8sBxFsMylDXCtCvwMsQulMD'
                'lqr0V1VTxRIHzTY9TgDjCCoc7CPoZdAVuq8Av9mqjsHB8bGpRBOQ9tgZkfAe'
                'UrUMGZ+WsTYq+nExhDS4dCt1ZDSMN+vH6uUOeIV+2VdN8mugd/jWRA+enWk1'
                '4tXvo3DsjL+TmnHrPZMq8mY4D9VGb/4AWTMzI8HOzKbPQDwguVYvlXRiwlIW'
                'X3jQs3fYwjaR7JTRoCT1qfw9GR4PB+zHAftez+iBokRIo4tZKg4TCO7qRNQS'
                'u1cNv55jvnMLt7sdjrb02u7e31Y/y7gX912vukNnyaFRZVB2JpFjx1faOf7B'
                '+K3X+IWHbWVR7mKs/MGYcSha4oaHOQai7dDHr+aBkWZh0aHa3R2s1GwfrAU0'
                '6f/nqL866ke7mVWUyOpo+OPR8PuujchePP4ROB4E409isQeJvwLEwzD8HRRq'
                'DKyzdgJgS93W3uawW/Umj116K7XXOb7QdZACQuQMQqCYF4mjfjdb/tSHVAiC'
                'VRjj74uVM9fO3fkvH0tTUIUxAAA=')
            # @:adhoc_import:@
            import stringformat_local as stringformat      # @:adhoc:@
        except ImportError:
            printf('error: (adhoc) stringformat missing.'
                   ' Try *easy_install stringformat*.', file=sys.stderr)
            exit(1)
    def sformat (fmtspec, *args, **kwargs):
        return stringformat.FormattableString(fmtspec).format(
            *args, **kwargs)

import base64
import urllib

#import something.non.existent                              # @:adhoc:@
try:
    import namespace_dict
except ImportError:
    # @:adhoc_import:@ !namespace_dict
    RtAdHoc.import_('namespace_dict', file_='namespace_dict.py',
        mtime='2012-10-02T15:18:04', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        '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')
    # @:adhoc_import:@
    import namespace_dict                                  # @:adhoc:@

# copy of ws_prop_dict.dict_dump
def dict_dump(dict_, wid=0, trunc=0, commstr=None, tag=None, out=None): # ||:fnc:||
    '''Dump a dictionary.'''

    if out is None:
        out = sys.stderr
    if commstr is None:
        commstr = ((('dbg_comm' in globals()) and (globals()['dbg_comm'])) or ('# '))

    dbg_twid = ((('dbg_twid' in globals()) and (globals()['dbg_twid'])) or (9))
    if tag is None:
        tag = ':DBG:'

    max_wid = 0
    for key in dict_.keys():
        _wid = len(key)
        if max_wid < _wid:
            max_wid = _wid

    dbg_fwid = ((('dbg_fwid' in globals()) and (globals()['dbg_fwid'])) or (max_wid))
    if dbg_fwid < max_wid:
        dbg_fwid = max_wid

    printf(sformat('{0}{1}', commstr, '-' * 30), file=out)
    indent = (sformat("{0}{3:^{1}} {4:<{2}s}:  ",
            commstr, dbg_twid, dbg_fwid,
            '', ''))

    for key, value in sorted(dict_.items()):
        value = str(value)
        value = value.replace('\n', '\\n')
        value = value.replace('\r', '\\r')
        value = value.replace('\t', '\\t')
        value = value.replace('\f', '\\f')
        if wid == 0:
            wid = 78 - len(indent) - 1
            if wid < 50:
                wid = 50
        start = 0
        limit = len(value)
        value_lines = []
        while start < limit:
            line = value[start:start+wid]
            space_pos = wid - 1
            if len(line) == wid:
                space_pos = line.rfind(' ')
                if space_pos > 0:
                    line = line[:space_pos + 1]
                else:
                    space_pos = wid - 1
            value_lines.append(line)
            start += space_pos + 1
        if trunc > 0:
            value_lines = value_lines[:trunc]
        value_lines[-1] = sformat('{0}[', value_lines[-1])
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}",
                commstr, dbg_twid, dbg_fwid,
                tag, key, value_lines[0]), file=out)
        for line in value_lines[1:]:
            printf(sformat('{0}{1}',indent, line), file=out)

def dump_attr(obj, wid=0, trunc=0, commstr=None,           # ||:fnc:||
              tag=None, out=None):
    if out is None:
        out = sys.stdout
    dict_dump(
        vars(obj), wid=wid, trunc=trunc, commstr=commstr, tag=tag, out=out)

printe = printf

# (progn (forward-line 1) (snip-insert-mode "py.b.posix" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.b.os.system.sh" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.b.prog.path" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.b.line.loop" t) (insert "\n"))

# --------------------------------------------------
# |||:sec:||| CLASSES
# --------------------------------------------------

# (progn (forward-line 1) (snip-insert-mode "py.c.placeholder.template" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.c.key.hash.ordered.dict" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.c.progress" t) (insert "\n"))

# --------------------------------------------------
# |||:sec:||| EXCEPTION
# --------------------------------------------------

class AdHocError(Exception):                               # ||:cls:||
    pass

# --------------------------------------------------
# |||:sec:||| ADHOC
# --------------------------------------------------

# @:adhoc_run_time_section:@ START
import sys
import os
import re

# @:adhoc_uncomment:@
# @:adhoc_template:@ -catch-stdout
try:
    from cStringIO import StringIO as _AdHocBytesIO, StringIO as _AdHocStringIO
except ImportError:
    try:
        from StringIO import StringIO as _AdHocBytesIO, StringIO as _AdHocStringIO
    except ImportError:
        from io import BytesIO as _AdHocBytesIO, StringIO as _AdHocStringIO

# @:adhoc_template:@
# @:adhoc_uncomment:@
# @:adhoc_run_time_section:@ off
if not hasattr(os.path, 'relpath'):
    def relpath(path, start=os.curdir):
        """Return a relative version of a path"""

        if not path:
            raise ValueError("no path specified")

        start_list = os.path.abspath(start).split(os.sep)
        path_list = os.path.abspath(path).split(os.sep)

        # Work out how much of the filepath is shared by start and path.
        i = len(os.path.commonprefix([start_list, path_list]))

        rel_list = [os.pardir] * (len(start_list)-i) + path_list[i:]
        if not rel_list:
            return os.curdir
        return os.path.join(*rel_list)
    os.path.relpath = relpath
    del relpath

AH_CHECK_SOURCE = '''\
not in section
# >:cmd:< arg0 arg1 # comment
# <:tag:> on
in section
# >:cmd:< arg2 arg3 # comment
in section
# <:tag:> off
not in section
# <:tag2:> on
in section
in section
# <:tag2:> off
not in section
'''

# @:adhoc_run_time_section:@ on
# @:adhoc_run_time_class:@
class AdHoc(object):                                     # |||:cls:|||
    # @:adhoc_run_time_section:@ off
    """
    :class:`AdHoc` is mainly used as a namespace, which is partially
    included verbatim as :class:`RtAdHoc` in the generated output.

    It is only instantiated for compiling adhoc output
    (:meth:`compileFile`, :meth:`compile`).

    **Attributes**

    The following class attrbutes determine the operation of AdHoc:

    - :attr:`line_delimiters`
    - :attr:`section_delimiters`
    - :attr:`template_process_hooks`
    - :attr:`extra_templates`
    - :attr:`export_dir`
    - :attr:`extract_dir`
    - :attr:`flat`
    - :attr:`frozen`
    - :attr:`quiet`
    - :attr:`verbose`
    - :attr:`debug`

    Run-time class attributes can be set like this:

    | # |adhoc_run_time|
    | # |adhoc_enable|
    | # RtAdHoc.flat = False
    | # RtAdHoc.frozen = True
    | # |adhoc_enable|

    or like this:

    | # |adhoc_run_time|
    | if 'RtAdHoc' in globals():
    |     RtAdHoc.flat = False
    |     RtAdHoc.frozen = True

    **Low-Level Functions**

    :meth:`adhoc_tag` constructs a delimited tag or tag regular
    expression:

    >>> adhoc_tag = AdHoc.adhoc_tag
    >>> delimiters = ('<:', ':>')

    >>> tag_sym = 'my_tag'
    >>> adhoc_tag(tag_sym, delimiters)
    '<:my_tag:>'

    >>> tag_rx = 'my_[^:]+'
    >>> adhoc_tag(tag_rx, delimiters, is_re=True)
    '\\\\<\\\\:my_[^:]+\\\\:\\\\>'

    :meth:`tag_split` splits a string into tagged line parts and
    untagged parts.

    :meth:`adhoc_parse_line` splits a tagged line into a tag symbol and
    additional arguments:

    >>> adhoc_parse_line = AdHoc.adhoc_parse_line
    >>> tagged_line = 'anything # <:my_tag:>  additonal arguments # end comment'

    >>> adhoc_parse_line(tagged_line, tag_sym, delimiters)
    ('my_tag', 'additonal arguments # end comment')

    >>> adhoc_parse_line(tagged_line, tag_rx, delimiters, is_re=True)
    ('my_tag', 'additonal arguments # end comment')

    >>> adhoc_parse_line(tagged_line, tag_rx, delimiters, is_re=True, strip_comment=True)
    ('my_tag', 'additonal arguments')

    **Low-Level Convenience Functions**

    *Tag Generation*

    :meth:`line_tag`, :meth:`section_tag`

    >>> class ah(AdHoc):
    ...     line_delimiters = ('>:', ':<')
    ...     section_delimiters = ('<:', ':>')

    >>> ah.line_tag('tag-symbol')
    '>:tag-symbol:<'

    >>> ah.line_tag('tag.?rx', True)
    '\\\\>\\\\:tag.?rx\\\\:\\\\<'

    >>> ah.section_tag('tag-symbol')
    '<:tag-symbol:>'

    >>> ah.section_tag('tag.?rx', True)
    '\\\\<\\\\:tag.?rx\\\\:\\\\>'

    *Tagged Line/Section Retrieval*

    :meth:`tag_lines`, :meth:`tag_partition`, :meth:`tag_sections`

    >>> source = AH_CHECK_SOURCE

    >>> line_tag = ah.line_tag('cmd')
    >>> tagged_lines = ah.tag_lines(source, line_tag)
    >>> adhoc_dump_list(tagged_lines, 40)
    #   :DBG:   elt[0]                 : ]'# >:cmd:< arg0 arg1 # comment\\n'[
    #   :DBG:   elt[1]                 : ]'# >:cmd:< arg2 arg3 # comment\\n'[

    >>> is_re = True
    >>> section_tag_rx = ah.section_tag('tag.?', is_re=is_re)
    >>> body, sections = ah.tag_partition(source, section_tag_rx, is_re=is_re)
    >>> adhoc_dump_list(body, 40)
    #   :DBG:   elt[0]                 : ]'not in section\\n# >:cmd:< arg0 arg1 #  ...'[
    #   :DBG:   elt[1]                 : ]'not in section\\n'[
    #   :DBG:   elt[2]                 : ]'not in section\\n'[
    >>> adhoc_dump_list(sections, 40)
    #   :DBG:   elt[0]                 : ]'in section\\n# >:cmd:< arg2 arg3 # comm ...'[
    #   :DBG:   elt[1]                 : ]'in section\\nin section\\n'[

    >>> body, sections = ah.tag_partition(source, section_tag_rx, is_re=is_re, headline=True)
    >>> adhoc_dump_sections(sections, 40)
    #   :DBG:   section[0]             : ]['# <:tag:> on\\n', 'in section\\n# >:cmd:< arg2 arg3 # comm ...'][
    #   :DBG:   section[1]             : ]['# <:tag2:> on\\n', 'in section\\nin section\\n'][

    >>> sections = ah.tag_sections(source, section_tag_rx, is_re=is_re, headline=True)
    >>> adhoc_dump_sections(sections, 40)
    #   :DBG:   section[0]             : ]['# <:tag:> on\\n', 'in section\\n# >:cmd:< arg2 arg3 # comm ...'][
    #   :DBG:   section[1]             : ]['# <:tag2:> on\\n', 'in section\\nin section\\n'][

    *Tagged Line Parsing*

    - :meth:`line_tag_parse`, :meth:`line_tag_strip`
    - :meth:`section_tag_parse`, :meth:`section_tag_strip`

    >>> strclean(ah.line_tag_parse(tagged_lines[0], 'cmd'))
    ('cmd', 'arg0 arg1 # comment')

    >>> strclean(ah.line_tag_strip(tagged_lines[0], 'cmd', strip_comment=True))
    'arg0 arg1'

    >>> strclean(ah.section_tag_parse(sections[1][0], 'tag.?', is_re=True))
    ('tag2', 'on')

    >>> strclean(ah.section_tag_strip(sections[1][0], 'tag.?', is_re=True))
    'on'

    **Tagged Line/Section Transformations**

    - :meth:`transform_lines`, :meth:`transform_sections`
    - :meth:`line_tag_rename`, :meth:`line_tag_remove`
    - :meth:`section_tag_rename`, :meth:`section_tag_remove`
    - :meth:`indent_sections`
    - :meth:`enable_sections`, :meth:`disable_transform`, :meth:`disable_sections`
    - :meth:`remove_sections`

    **IO Functions**

    - :meth:`check_coding`
    - :meth:`decode_source`, :meth:`encode_source`
    - :meth:`read_source`, :meth:`write_source`
    - :meth:`check_xfile`
    - :meth:`pack_file`, :meth:`unpack_file`

    **Run-Time Unpack/Import Interface**

    - :meth:`unpack_`
    - :meth:`import_`, :meth:`module_setup`

    **Export Tools**

    - :meth:`std_source_param`
    - :meth:`export_source`

    **Extract Interface**

    - :meth:`unpack`
    - :meth:`extract`

    **Export Interface**

    - :meth:`export__`, :meth:`export_`, :meth:`export`

    **Dump Interface (Import/Unpack Substitute)**

    - :meth:`dump__`, :meth:`dump_`, :meth:`dump_file`

    **Macro Interface**

    Naive macro expansion would violate the condition
    ``xsource_i === source_i``.

    Here is a simple macro system which preserves the bijectivity
    condition. It is quite useful for conditional templating. (See
    `Use Cases`_ generator scripts).

    *Limitations*

    - Macro expansions are not prefixed with the current indentation
    - Macros cannot be nested

    *Attributes*

    - :attr:`macro_call_delimiters`

      Delimiters for macros, e.g.: ``@|:MACRO_NAME:|>``

    - :attr:`macro_xdef_delimiters`

      Delimiters for macro expansion, e.g.::

          # <|:adhoc_macro_call\x3a|@
          # @|:MACRO_NAME:|>
          # <|:adhoc_macro_call\x3a|@
          # <|:adhoc_macro_expansion\x3a|@
          The macro definition ...
          The macro definition ...
          # <|:adhoc_macro_expansion\x3a|@

    - :attr:`macros`

      Macro definitions.

    *Methods*

    - :meth:`expand_macros`
    - :meth:`has_expanded_macros`
    - :meth:`activate_macros`
    - :meth:`collapse_macros`

    **Template Interface**

    - :meth:`std_template_param`
    - :meth:`get_templates`
    - :meth:`template_list`, :meth:`col_param_closure`, :meth:`template_table`
    - :meth:`get_named_template`
    - :meth:`extract_templates`

    **Template Extraction (uncompiled)**

    - Expand and activate macros for uncompiled source
    - Activate macros on compiled source

    **Compile**

    - Expand macros before compilation

    **Export**

    - Collapse macros on export of compiled source.

    **Compilation Attributes**

    - :attr:`include_path`

    **Compilation Interface**

    - :meth:`setup_tags`
    - :meth:`strquote`
    - :meth:`adhoc_run_time_sections_from_string`
    - :meth:`adhoc_run_time_section_from_file`
    - :meth:`adhoc_get_run_time_section`
    - :meth:`prepare_run_time_section`
    - :meth:`verbatim_`
    - :meth:`include_`
    - :meth:`encode_module_`
    - :meth:`compile_`

    **User API**

    - :meth:`encode_include`
    - :meth:`encode_module`
    - :meth:`compile`
    - :meth:`compileFile`

    .. \\|:here:|
    """
    # @:adhoc_run_time_section:@ on
    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Attributes
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    line_delimiters = ('@:', ':@')
    # @:adhoc_run_time_section:@ off
    '''Tag delimiters for lines.'''
    # @:adhoc_run_time_section:@ on
    section_delimiters = ('@:', ':@')
    # @:adhoc_run_time_section:@ off
    '''Tag delimiters for sections.'''
    # @:adhoc_run_time_section:@ on

    template_process_hooks = {}
    # @:adhoc_run_time_section:@ off
    '''Dictionary of ``template-name, hook-function`` items.

    If the name of a template section matches an item in this
    dictionary, the ``hook-function`` is called::

        section = hook-function(cls, section, tag, template_name)
    '''
    # @:adhoc_run_time_section:@ on
    extra_templates = []
    # @:adhoc_run_time_section:@ off
    '''List of additional templates::

        [(name, type), ...]
    '''
    # @:adhoc_run_time_section:@ on

    export_dir = '__adhoc__'
    # @:adhoc_run_time_section:@ off
    '''Export directory (for :meth:`export`, ``--explode``).'''
    # @:adhoc_run_time_section:@ on
    extract_dir = '.'
    # @:adhoc_run_time_section:@ off
    '''Export directory (for :meth:`extract`, ``--extract``).'''
    # @:adhoc_run_time_section:@ on
    flat = True
    # @:adhoc_run_time_section:@ off
    '''If True, do not export files recursively.'''
    # @:adhoc_run_time_section:@ on
    forced = False
    # @:adhoc_run_time_section:@ off
    '''If True, allow duplicate imports.'''
    # @:adhoc_run_time_section:@ on

    frozen = False
    # @:adhoc_run_time_section:@ off
    '''If True, do not attempt to load modules from external
    sources (\\|:todo:| not implemented).'''
    # @:adhoc_run_time_section:@ on

    quiet = False
    # @:adhoc_run_time_section:@ off
    '''If True, suppress warnings.'''
    # @:adhoc_run_time_section:@ on
    verbose = False
    # @:adhoc_run_time_section:@ off
    '''If True, display messages.'''
    # @:adhoc_run_time_section:@ on
    debug = False
    # @:adhoc_run_time_section:@ off
    '''If True, display debug messages.'''
    # @:adhoc_run_time_section:@ on

    include_path = []
    # @:adhoc_run_time_section:@ off
    '''Search path for include files. Only relevant during compilation.'''
    # @:adhoc_run_time_section:@ on
    export_need_init = {}
    export_have_init = {}
    extract_warn = False

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Low-Level Functions
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    def _adhoc_string_util():
        # @:adhoc_run_time_section:@ off
        '''Define string utilities.

        - static method :meth:`isstring`
        - unicode type :attr:`uc_type`
        - static method :meth:`uc`
        '''
        # @:adhoc_run_time_section:@ on
        def isstring(obj):
            return isinstance(obj, basestring)
        try:
            isstring("")
        except NameError:
            def isstring(obj):
                return isinstance(obj, str) or isinstance(obj, bytes)
        def _uc(string):
            return unicode(string, 'utf-8')
        try:
            _uc("")
        except NameError:
            _uc = lambda x: x
        uc_type = type(_uc(""))
        def uc(value):
            if isstring(value) and not isinstance(value, uc_type):
                return _uc(value)
            return value
        return staticmethod(isstring), uc_type, staticmethod(uc)

    isstring, uc_type, uc = _adhoc_string_util()

    @staticmethod
    def adhoc_tag(symbol_or_re, delimiters, is_re=False):    # |:fnc:|
        # @:adhoc_run_time_section:@ off
        '''Make a tag from symbol_or_re and delimiters.

        :param symbol_or_re: symbol string or regular expresssion.
        :param delimiters: tuple of delimiter strings
          ``(prefix, suffix)``.
        :param is_re: if True, escape the delimiters for regular
          expressions.
        '''
        # @:adhoc_run_time_section:@ on
        ldlm = delimiters[0]
        rdlm = delimiters[1]
        if is_re:
            ldlm = re.escape(ldlm)
            rdlm = re.escape(rdlm)
        return ''.join((ldlm, symbol_or_re, rdlm))

    @classmethod
    def tag_split(cls, string, tag, is_re=False):            # |:fnc:|
        # @:adhoc_run_time_section:@ off
        """Split string with tag line.

        :returns:
          a list of tuples with a flag and a section::

            [(is_tag, section), ... ]

        **Example**

        >>> source = AH_CHECK_SOURCE
        >>> printf(str(source), end='')
        not in section
        # >:cmd:< arg0 arg1 # comment
        # <:tag:> on
        in section
        # >:cmd:< arg2 arg3 # comment
        in section
        # <:tag:> off
        not in section
        # <:tag2:> on
        in section
        in section
        # <:tag2:> off
        not in section

        **Split on literal tag**

        >>> is_re = False
        >>> tag = AdHoc.adhoc_tag('tag', ('<:', ':>'), is_re)
        >>> parts = AdHoc.tag_split(source, tag, is_re)
        >>> adhoc_dump_sections(parts, 40)
        #   :DBG:   section[0]             : ][False, 'not in section\\n# >:cmd:< arg0 arg1 #  ...'][
        #   :DBG:   section[1]             : ][True, '# <:tag:> on\\n'][
        #   :DBG:   section[2]             : ][False, 'in section\\n# >:cmd:< arg2 arg3 # comm ...'][
        #   :DBG:   section[3]             : ][True, '# <:tag:> off\\n'][
        #   :DBG:   section[4]             : ][False, 'not in section\\n# <:tag2:> on\\nin secti ...'][

        **Split on tag regexp**

        >>> is_re = True
        >>> tag = AdHoc.adhoc_tag('tag.?', ('<:', ':>'), is_re)
        >>> parts = AdHoc.tag_split(source, tag, is_re)
        >>> adhoc_dump_sections(parts, 40)
        #   :DBG:   section[0]             : ][False, 'not in section\\n# >:cmd:< arg0 arg1 #  ...'][
        #   :DBG:   section[1]             : ][True, '# <:tag:> on\\n'][
        #   :DBG:   section[2]             : ][False, 'in section\\n# >:cmd:< arg2 arg3 # comm ...'][
        #   :DBG:   section[3]             : ][True, '# <:tag:> off\\n'][
        #   :DBG:   section[4]             : ][False, 'not in section\\n'][
        #   :DBG:   section[5]             : ][True, '# <:tag2:> on\\n'][
        #   :DBG:   section[6]             : ][False, 'in section\\nin section\\n'][
        #   :DBG:   section[7]             : ][True, '# <:tag2:> off\\n'][
        #   :DBG:   section[8]             : ][False, 'not in section\\n'][

        **Assemble section**

        >>> section = []
        >>> in_section = False
        >>> for part in parts:
        ...     if part[0]:
        ...         in_section = not in_section
        ...         continue
        ...     if in_section:
        ...         section.append(part[1])
        >>> section = ''.join(section)
        >>> printf(str(section), end='')
        in section
        # >:cmd:< arg2 arg3 # comment
        in section
        in section
        in section
        """
        # @:adhoc_run_time_section:@ on
        if not is_re:
            tag = re.escape(tag)
        ro = re.compile(''.join(('^[^\n]*(', tag, ')[^\n]*$')), re.M)
        result = []
        last_end = 0
        string = cls.decode_source(string)
        for mo in re.finditer(ro, string):
            start = mo.start(0)
            end = mo.end(0)
            result.append((False, string[last_end:start]))
            result.append((True, string[start:end+1]))
            last_end = end+1
        result.append((False, string[last_end:]))
        return result

    @classmethod
    def adhoc_parse_line(cls, tagged_line, symbol_or_re=None, # |:clm:|
                         delimiters=None, is_re=False, strip_comment=None):
        # @:adhoc_run_time_section:@ off
        """Parse a tagged line into tag-symbol and argument parts.

        :returns: a tuple ``(tag-symbol, tag-arguments)``.

        :param tagged_line: string to be parsed.
        :param symbol_or_re: symbol string or regular expresssion to
          be parsed, default is any sequence of characters except the
          first character of the suffix delimiter.
        :param delimiters: tuple of delimiter strings
          ``(prefix, suffix)``. Default is :attr:`line_delimiters`.
        :param strip_comment: If True, remove trailing ``#`` comment
          from arguments. Default: False.

        >>> tagged_line = ' # @:' 'adhoc_test' ':@   arg1 arg2  # comment'
        >>> AdHoc.adhoc_parse_line(tagged_line)
        ('adhoc_test', 'arg1 arg2  # comment')

        >>> AdHoc.adhoc_parse_line(tagged_line, 'adhoc_.*', is_re=True)
        ('adhoc_test', 'arg1 arg2  # comment')

        >>> AdHoc.adhoc_parse_line(tagged_line, strip_comment=True)
        ('adhoc_test', 'arg1 arg2')

        >>> AdHoc.adhoc_parse_line(tagged_line.replace('@', '<'))
        ('', '# <:adhoc_test:<   arg1 arg2  # comment')

        >>> AdHoc.adhoc_parse_line(tagged_line.replace('@', '|'), delimiters=('|:', ':|'))
        ('adhoc_test', 'arg1 arg2  # comment')
        """
        # @:adhoc_run_time_section:@ on
        if delimiters is None:
            delimiters = cls.line_delimiters
        if symbol_or_re is None:
            dlm = delimiters[1]
            if dlm:
                symbol_or_re = ''.join(('[^', dlm[0], ']+'))
            else:
                symbol_or_re = ''.join(('[^\\s]+'))
            is_re = True
        if not is_re:
            symbol_or_re = re.escape(symbol_or_re)
        tag_rx = cls.adhoc_tag(''.join(('(', symbol_or_re, ')')), delimiters, is_re=True)
        mo = re.search(tag_rx, tagged_line)
        if mo:
            ptag = mo.group(1)
        else:
            ptag = ''
        strip_rx = ''.join(('^.*', tag_rx, '\\s*'))
        tag_arg = re.sub(strip_rx, '', tagged_line).strip()
        if strip_comment:
            tag_arg = re.sub('\\s*#.*', '', tag_arg)
        return (ptag, tag_arg)

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Low-Level Convenience Functions
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def set_delimiters(cls, line_delimiters=None, section_delimiters=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Set line/section delimiters.

        :returns: saved delimiter state suitable for
          :meth:`reset_delimiters`.

        :param line_delimiters: the line delimiters. If None, line
          delimiters are not changed.
        :param section_delimiters: the section delimiters. If None,
          `line_delimiters` is used.

        If both `line_delimiters` and `section_delimiters` are None,
        the delimiter state is returned without any modification to
        the current delimiters.

        >>> AdHoc.set_delimiters()
        (('@:', ':@'), ('@:', ':@'))

        >>> sv = AdHoc.inc_delimiters()
        >>> sv
        (('@:', ':@'), ('@:', ':@'))

        >>> AdHoc.set_delimiters()
        (('@@:', ':@@'), ('@@:', ':@@'))

        >>> AdHoc.reset_delimiters(sv)
        >>> AdHoc.set_delimiters()
        (('@:', ':@'), ('@:', ':@'))

        >>> AdHoc.set_delimiters(('<:', ':>'))
        (('@:', ':@'), ('@:', ':@'))

        >>> AdHoc.set_delimiters()
        (('<:', ':>'), ('<:', ':>'))

        >>> AdHoc.reset_delimiters(sv)
        >>> AdHoc.set_delimiters()
        (('@:', ':@'), ('@:', ':@'))

        '''
        # @:adhoc_run_time_section:@ on
        delimiter_state = (cls.line_delimiters, cls.section_delimiters)
        if line_delimiters is None:
            line_delimiters = delimiter_state[0]
            if section_delimiters is None:
                section_delimiters = delimiter_state[1]
        elif section_delimiters is None:
            section_delimiters = line_delimiters
        cls.line_delimiters, cls.section_delimiters = (
            line_delimiters, section_delimiters)
        return delimiter_state

    @classmethod
    def reset_delimiters(cls, delimiter_state):              # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Reset line/section delimiters from saved state.

        :param delimiter_state: delimiter state as returned by
          :meth:`set_delimiters`.
        '''
        # @:adhoc_run_time_section:@ on
        cls.line_delimiters, cls.section_delimiters = delimiter_state

    @classmethod
    def inc_delimiters(cls):                                 # |:clm:|
    # @:adhoc_run_time_section:@ off
        '''Duplicate outer delimiter characters.

        :returns: saved delimiter state suitable for
          :meth:`reset_delimiters`.

        E.g.::

            "@:", ":@" => "@@:", ":@@"

        See :meth:`set_delimiters` for doctest example.
        '''
        # @:adhoc_run_time_section:@ on

        inc_first = lambda dlm: (((not dlm) and ('')) or (dlm[0] + dlm))
        inc_last = lambda dlm: (((not dlm) and ('')) or (dlm + dlm[-1]))
        outer_delimiters = [(inc_first(dlm[0]), inc_last(dlm[1]))
                            for dlm in (cls.line_delimiters,
                                        cls.section_delimiters)]
        return cls.set_delimiters(*outer_delimiters)

    @classmethod
    def line_tag(cls, symbol_or_re, is_re=False):            # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Make a line tag from symbol or regular expression.

        :returns: unicode string.

        :param symbol_or_re: symbol string or regular expresssion.
        :param is_re: if True, escape the delimiters for regular
          expressions.
        '''
        # @:adhoc_run_time_section:@ on
        return cls.adhoc_tag(symbol_or_re, cls.line_delimiters, is_re)

    @classmethod
    def section_tag(cls, symbol_or_re, is_re=False):         # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Make a section tag from symbol or regular expression.

        :returns: unicode string.

        :param symbol_or_re: symbol string or regular expresssion.
        :param is_re: if True, escape the delimiters for regular
          expressions.
        '''
        # @:adhoc_run_time_section:@ on
        return cls.adhoc_tag(symbol_or_re, cls.section_delimiters, is_re)

    @classmethod
    def tag_lines(cls, string, tag, is_re=False):            # |:clm:|
        # @:adhoc_run_time_section:@ off
        """Get lines matching tag.

        :returns: list of tag lines.

        See :meth:`tag_split`.
        """
        # @:adhoc_run_time_section:@ on
        result = []
        for section in cls.tag_split(string, tag, is_re):
            if section[0]:
                result.append(section[1])
        return result

    @classmethod
    def tag_partition(cls, string, tag, is_re=False, headline=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Split the string into body parts and sections.

        If `headline` is True, the starting tag line is included for
        sections.'''
        # @:adhoc_run_time_section:@ on
        in_section = False
        body_parts = []
        sections = []
        tagged_line = ''
        for section in cls.tag_split(string, tag, is_re):
            if section[0]:
                in_section = not in_section
                tagged_line = section[1]
                continue
            if in_section:
                if headline:
                    sections.append((tagged_line, section[1]))
                else:
                    sections.append(section[1])
            else:
                body_parts.append(section[1])
        return body_parts, sections

    @classmethod
    def tag_sections(cls, string, tag, is_re=False, headline=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Split the string into sections.

        If `headline` is True, the starting tag line is included.

        See :meth:`tag_partition`.
        '''
        # @:adhoc_run_time_section:@ on
        body_parts, sections = cls.tag_partition(string, tag, is_re, headline)
        return sections

    @classmethod
    def line_tag_parse(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        # @:adhoc_run_time_section:@ off
        """Parse a line tag line into tag-symbol and argument parts.

        :returns: a tuple ``(tag-symbol, tag-arguments)``.

        See :meth:`adhoc_parse_line`.
        """
        # @:adhoc_run_time_section:@ on
        return cls.adhoc_parse_line(tagged_line, symbol_or_re, cls.line_delimiters,
                                    is_re, strip_comment=strip_comment)

    @classmethod
    def line_tag_strip(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        # @:adhoc_run_time_section:@ off
        """Remove tag and optionally comment from line tag line.

        :returns: tag arguments.

        See :meth:`adhoc_parse_line`.
        """
        # @:adhoc_run_time_section:@ on
        return cls.line_tag_parse(tagged_line, symbol_or_re, is_re, strip_comment)[1]

    @classmethod
    def section_tag_parse(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        # @:adhoc_run_time_section:@ off
        """Parse a section tag line into tag-symbol and argument parts.

        :returns: a tuple ``(tag-symbol, tag-arguments)``.

        See :meth:`adhoc_parse_line`.
        """
        # @:adhoc_run_time_section:@ on
        return cls.adhoc_parse_line(tagged_line, symbol_or_re, cls.section_delimiters,
                                    is_re, strip_comment=strip_comment)

    @classmethod
    def section_tag_strip(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        # @:adhoc_run_time_section:@ off
        """Remove tag and optionally comment from section tag line.

        :returns: tag arguments.

        See :meth:`adhoc_parse_line`.
        """
        # @:adhoc_run_time_section:@ on
        return cls.section_tag_parse(tagged_line, symbol_or_re, is_re, strip_comment)[1]

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Tagged Line/Section Transformations
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def transform_lines(cls, transform, string,              # |:clm:|
                        symbol_or_re, is_re=False, delimiters=None):
        # @:adhoc_run_time_section:@ off
        """Split string into line tag lines and other sections; call
        transform callback on each tagged line.

        :returns: transformed string.

        :param transform: callback which receives argument ``tagged-line``.
        """
        # @:adhoc_run_time_section:@ on
        if delimiters is None:
            delimiters = cls.line_delimiters
        result = []
        in_section = False
        for section in cls.tag_split(
            string, cls.adhoc_tag(symbol_or_re, delimiters, is_re), is_re):
            blob = section[1]
            if section[0]:
                in_section = not in_section
                blob = transform(blob)
            result.append(blob)
        string = ''.join(result)
        return string

    @classmethod
    def transform_sections(cls, transform, string,           # |:clm:|
                           symbol_or_re, is_re=False):
        # @:adhoc_run_time_section:@ off
        """Split string into sections and call transform callback on each section.

        :returns: transformed string.

        :param transform: callback which receives and returns
          arguments ``section``, ``headline``.
        """
        # @:adhoc_run_time_section:@ on
        result = []
        in_section = False
        headline = ''
        for section in cls.tag_split(
            string, cls.section_tag(symbol_or_re, is_re), is_re):
            blob = section[1]
            if section[0]:
                in_section = not in_section
                if in_section:
                    headline = blob
                    continue
            elif in_section:
                blob, headline = transform(blob, headline)
                result.append(headline)
            result.append(blob)
        string = ''.join(result)
        return string

    @classmethod
    def line_tag_rename(cls, string, symbol_or_re, renamed, is_re=False, delimiters=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Rename tag-symbol.

        Default tag delimiters are :attr:`line_delimiters`.

        >>> tpl = AdHoc.get_named_template("col-param-closure")

        .. >>> printf(str(AdHoc.line_tag_rename(tpl, "adhoc_run_time_section", "should_be_kept")))
        '''
        # @:adhoc_run_time_section:@ on
        if is_re:
            transform = lambda blob: re.sub(symbol_or_re, renamed, blob)
        else:
            transform = lambda blob: blob.replace(symbol_or_re, renamed)
        return cls.transform_lines(transform, string, symbol_or_re, is_re, delimiters)

    @classmethod
    def line_tag_remove(cls, string, symbol_or_re, is_re=False, delimiters=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Remove tagged lines.

        Default tag delimiters are :attr:`line_delimiters`.

        >>> tpl = AdHoc.get_named_template("col-param-closure")

        .. >>> printf(str(AdHoc.line_tag_remove(tpl, "adhoc_run_time_section")))
        '''
        # @:adhoc_run_time_section:@ on
        transform = lambda blob: ''
        return cls.transform_lines(transform, string, symbol_or_re, is_re, delimiters)

    @classmethod
    def section_tag_rename(cls, string, symbol_or_re, renamed, is_re=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Rename tag-symbol of lines tagged with :attr:`section_delimiters`.

        >>> tpl = AdHoc.get_named_template("col-param-closure")
        >>> res = AdHoc.section_tag_rename(tpl, "adhoc_run_time_section", "should_be_kept")
        >>> res = '\\n'.join(res.splitlines()[:4])
        >>> printf(str(res)) #doctest: +ELLIPSIS
            # @:should_be_kept:@ on
            @classmethod
            def col_param_closure(cls):...
                # @:should_be_kept:@ off
        '''
        # @:adhoc_run_time_section:@ on
        if is_re:
            transform = lambda blob: re.sub(symbol_or_re, renamed, blob)
        else:
            transform = lambda blob: blob.replace(symbol_or_re, renamed)
        return cls.transform_lines(transform, string, symbol_or_re, is_re, cls.section_delimiters)

    @classmethod
    def section_tag_remove(cls, string, symbol_or_re, is_re=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Remove lines tagged with :attr:`section_delimiters`.

        >>> tpl = AdHoc.get_named_template("col-param-closure")
        >>> res = AdHoc.section_tag_remove(tpl, "adhoc_run_time_section")
        >>> res = '\\n'.join(res.splitlines()[:4])
        >>> printf(str(res)) #doctest: +ELLIPSIS
            @classmethod
            def col_param_closure(cls):...
                ...Closure for setting up maximum width, padding and separator
                for table columns.
        '''
        # @:adhoc_run_time_section:@ on
        transform = lambda blob: ''
        return cls.transform_lines(transform, string, symbol_or_re, is_re, cls.section_delimiters)

    @classmethod
    def indent_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''
        >>> section = """\\
        ... # prefix
        ...   # @:adhoc_indent_check:@ +4
        ...   #line 1
        ...   #  line 2
        ...   #
        ...   # line 3
        ...   # @:adhoc_indent_check:@
        ...   # suffix\\
        ... """

        >>> printf(AdHoc.indent_sections(section, "adhoc_indent_check"))
        # prefix
          # @:adhoc_indent_check:@ +4
              #line 1
              #  line 2
              #
              # line 3
              # @:adhoc_indent_check:@
          # suffix

        >>> printf(AdHoc.indent_sections(section.replace("+4", "-1"),
        ...        "adhoc_indent_check"))
        # prefix
          # @:adhoc_indent_check:@ -1
         #line 1
         #  line 2
         #
         # line 3
          # @:adhoc_indent_check:@
          # suffix

        '''
        # @:adhoc_run_time_section:@ on
        result = []
        in_section = False
        indent = 0
        for section in cls.tag_split(
            string, cls.section_tag(symbol_or_re, is_re), is_re):
            blob = section[1]
            if section[0]:
                in_section = not in_section
                if in_section:
                    tag_arg = cls.section_tag_strip(blob)
                    if tag_arg:
                        indent = int(tag_arg)
                    else:
                        indent = -4
            else:
                if in_section and indent:
                    if indent < 0:
                        rx = re.compile(''.join(('^', ' ' * (-indent))), re.M)
                        blob = rx.sub('', blob)
                    elif indent > 0:
                        rx = re.compile('^', re.M)
                        blob = rx.sub(' ' * indent, blob)
                    indent = 0
            result.append(blob)
        string = ''.join(result)
        return string

    @classmethod
    def enable_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''
        >>> section = """\\
        ... # prefix
        ...   # @:adhoc_enable_check:@
        ...   #line 1
        ...   #  line 2
        ...   #
        ...   # line 3
        ...   # @:adhoc_enable_check:@
        ...   # suffix\\
        ... """
        >>> printf(AdHoc.enable_sections(section, "adhoc_enable_check"))
        # prefix
          # @:adhoc_enable_check:@
          line 1
           line 2
        <BLANKLINE>
          line 3
          # @:adhoc_enable_check:@
          # suffix
        '''
        # @:adhoc_run_time_section:@ on
        enable_ro = re.compile('^([ \t\r]*)(# ?)', re.M)
        enable_sub = '\\1'
        transform = lambda blob, hl: (enable_ro.sub(enable_sub, blob), hl)
        return cls.transform_sections(transform, string, symbol_or_re, is_re)

    adhoc_rx_tab_check = re.compile('^([ ]*\t)', re.M)
    adhoc_rx_disable_simple = re.compile('^', re.M)
    adhoc_rx_min_indent_check = re.compile('^([ ]*)([^ \t\r\n]|$)', re.M)

    @classmethod
    def disable_transform(cls, section, headline=None):      # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Disable section transform callback.'''
        # @:adhoc_run_time_section:@ on
        if not section:
            return (section, headline)

        if cls.adhoc_rx_tab_check.search(section):
            # tabs are evil
            if cls.verbose:
                list(map(sys.stderr.write,
                         ('# dt: evil tabs: ', repr(section), '\n')))
            return (
                cls.adhoc_rx_disable_simple.sub(
                    '# ', section.rstrip()) + '\n',
                headline)

        min_indent = ''
        for mo in cls.adhoc_rx_min_indent_check.finditer(section):
            indent = mo.group(1)
            if indent:
                if (not min_indent or len(min_indent) > len(indent)):
                    min_indent = indent
            elif mo.group(2):
                min_indent = ''
                break
        adhoc_rx_min_indent = re.compile(
            ''.join(('^(', min_indent, '|)([^\n]*)$')), re.M)

        if section.endswith('\n'):
            section = section[:-1]
        dsection = []
        for mo in adhoc_rx_min_indent.finditer(section):
            indent = mo.group(1)
            rest = mo.group(2)
            if not indent and not rest:
                #leave blank lines blank
                dsection.append('\n')
            else:
                dsection.extend((indent, '# ', rest, '\n'))
        return (''.join(dsection), headline)

    @classmethod
    def disable_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''
        >>> section = """\\
        ... prefix
        ...   @:adhoc_disable_check:@
        ...   line 1
        ...     line 2
        ...
        ...   line 3
        ...   @:adhoc_disable_check:@
        ...   suffix\\
        ... """
        >>> printf(AdHoc.disable_sections(section, "adhoc_disable_check"))
        prefix
          @:adhoc_disable_check:@
          # line 1
          #   line 2
        <BLANKLINE>
          # line 3
          @:adhoc_disable_check:@
          suffix
        '''
        # @:adhoc_run_time_section:@ on
        return cls.transform_sections(
            cls.disable_transform, string, symbol_or_re, is_re)

    @classmethod
    def remove_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Remove sections.'''
        # @:adhoc_run_time_section:@ on
        ah_retained, ah_removed = cls.tag_partition(
            string, cls.section_tag(symbol_or_re, is_re), is_re)
        return ''.join(ah_retained)

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| IO Functions
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @staticmethod
    def check_coding(source):                                # |:fnc:|
        # @:adhoc_run_time_section:@ off
        '''Determine coding for source.

        :returns: coding type for string.

        :param source: source string/unicode.

        If the ``source`` string contains a coding specification
        within the first two lines, the specified coding is used,
        otherwise, ``UTF-8`` is returned.
        '''
        # @:adhoc_run_time_section:@ on
        if source:
            eol_seen = 0
            for c in source:
                if isinstance(c, int):
                    lt_ = lambda a, b: a < b
                    chr_ = lambda a: chr(a)
                else:
                    lt_ = lambda a, b: True
                    chr_ = lambda a: a
                break
            check = []
            for c in source:
                if lt_(c, 127):
                    check.append(chr_(c))
                if c == '\n':
                    eol_seen += 1
                    if eol_seen == 2:
                        break
            check = ''.join(check)
            mo = re.search('-[*]-.*coding:\\s*([^;\\s]+).*-[*]-', check)
        else:
            mo = None
        if mo:
            coding = mo.group(1)
        else:
            coding = 'utf-8'
        return coding

    @classmethod
    def decode_source(cls, source):                          # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Decode source to unicode.

        :param source: source string (may already be unicode).

        If the ``source`` string contains a coding specification
        within the first two lines, the specified coding is used,
        otherwise, ``UTF-8`` is applied.
        '''
        # @:adhoc_run_time_section:@ on
        if not source:
            return cls.uc('')
        if not isinstance(source, cls.uc_type) and hasattr(source, 'decode'):
            source = source.decode(cls.check_coding(source))
        return source

    @classmethod
    def encode_source(cls, source):                          # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Encode source from unicode.

        :param source: source string (may already be encoded).

        If the ``source`` string contains a coding specification
        within the first two lines, the specified coding is used,
        otherwise, ``UTF-8`` is applied.
        '''
        # @:adhoc_run_time_section:@ on
        if not source:
            return ''.encode('utf-8')
        if isinstance(source, cls.uc_type) and hasattr(source, 'encode'):
            source = source.encode(cls.check_coding(source))
        return source

    @classmethod
    def read_source(cls, file_, decode=True):                # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Read source from file.

        :returns: unicode string.

        :param file_: If None, empty or ``-``, sys.stdin is used,
          otherwise the file is read from ``file_`` and decoded with
          :meth:`decode_source`.
        '''
        # @:adhoc_run_time_section:@ on
        source = None
        if not file_ or file_ == '-':
            # Python3 has a buffer attribute for binary input.
            if hasattr(sys.stdin, 'buffer'):
                source = sys.stdin.buffer.read()
            else:
                source = sys.stdin.read()
        else:
            try:
                sf = open(file_, 'rb')
                source = sf.read()
                sf.close()
            except IOError:
                for module in sys.modules.values():
                    if (module
                        and hasattr(module, '__file__')
                        and module.__file__ == file_):
                        if (hasattr(module, '__adhoc__')
                            and hasattr(module.__adhoc__, 'source')):
                            source = module.__adhoc__.source
                            break
        if source is None:
            raise IOError('source not found for `' + str(file_) + '`')
        if decode:
            return cls.decode_source(source)
        return source

    @classmethod
    def write_source(cls, file_, source, mtime=None, mode=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Write source to file.

        :param file_: If None, empty or ``-``, sys.stdout is used,
          otherwise the file is written to ``file_`` after encoding
          with :meth:`encode_source`.
        '''
        # @:adhoc_run_time_section:@ on
        esource = cls.encode_source(source)
        if not file_ or file_ == '-':
            # @:adhoc_run_time_section:@ off
            # For Python2, sys.stdout is effectively binary, so source
            # can be pre-encoded.
            #
            # With Python3 sys.stdout does automatic encoding (which
            # is unwanted).
            # Normal sys.stdout has a buffer member which allows
            # binary output, but not during doctest.
            # @:adhoc_run_time_section:@ on
            if hasattr(sys.stdout, 'buffer'):
                sys.stdout.buffer.write(esource)
            else:
                try:
                    sys.stdout.write(esource)
                except TypeError:
                    sys.stdout.write(source)
        else:
            sf = open(file_, 'wb')
            sf.write(esource)
            sf.close()
            if mode is not None:
                os.chmod(file_, mode)
            if mtime is not None:
                import datetime
                if cls.isstring(mtime):
                    try:
                        date, ms = mtime.split('.')
                    except ValueError:
                        date = mtime
                        ms = 0
                    mtime = cls.strptime(date, '%Y-%m-%dT%H:%M:%S')
                    mtime += datetime.timedelta(microseconds=int(ms))
                if isinstance(mtime, datetime.datetime):
                    # @:adhoc_run_time_section:@ off
                    # import calendar
                    # if mtime.utcoffset() is not None:
                    #     mtime = mtime - mtime.utcoffset()
                    # millis = int(calendar.timegm(mtime.timetuple()) * 1000 +
                    #                mtime.microsecond / 1000)
                    # ts = float(millis) / 1000
                    # @:adhoc_run_time_section:@ on
                    ts = int(mtime.strftime("%s"))
                else:
                    ts = mtime
                os.utime(file_, (ts, ts))

    @classmethod
    def check_xfile(cls, file_, xdir=None):                  # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Prepare extraction of a file.

        :returns: None, if the file already exists. Otherwise, the
          file directory is created and the absolute path name of the
          file is returned.

        :param file_: filename.
        :param xdir: extraction directory. If it is `None`,
          :attr:`extract_dir` is used.

        If ``file_`` is `None`, empty or ``-``, the filename ``-`` is
        returned.

        If ``file_`` starts with a slash ``/``, ``xdir`` is ignored,
        otherwise, ``xdir`` is prepended to ``file_``.
        '''
        # @:adhoc_run_time_section:@ on
        if xdir is None:
            xdir = cls.extract_dir
        if not file_:
            file_ = '-'
        if file_ == '-':
            return file_
        file_ = os.path.expanduser(file_)
        if os.path.isabs(file_):
            xfile = file_
        else:
            xfile = os.path.join(xdir, file_)
        xfile = os.path.abspath(xfile)
        if os.path.exists(xfile):
            # do not overwrite files
            if (cls.extract_warn or (cls.verbose)) and not cls.quiet:
                list(map(sys.stderr.write, (
                    "# xf: ", cls.__name__, ": warning file `", file_,
                    "` exists. skipping ...\n")))
            return None
        xdir = os.path.dirname(xfile)
        if not os.path.exists(xdir):
            os.makedirs(xdir)
        return xfile

    @classmethod
    def pack_file(cls, source, zipped=True):                 # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Optionally gzip a file and base64-encode it.

        :returns: base64-encoded unicode string.

        :param source: string to be packed.
        :param zipped: if True, gzip ``source`` before
          base64-encoding. (Default: True).
        '''
        # @:adhoc_run_time_section:@ on
        import base64, gzip
        if zipped:
            sio = _AdHocBytesIO()
            gzf = gzip.GzipFile('', 'wb', 9, sio)
            gzf.write(cls.encode_source(source))
            gzf.close()
            source = sio.getvalue()
            sio.close()
        else:
            source = cls.encode_source(source)
        source = base64.b64encode(source)
        source = source.decode('ascii')
        return source

    @classmethod
    def unpack_file(cls, source64, zipped=True, decode=True): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Base64-decode a file and optionally ungzip it.

        :returns: unicode string if ``decode`` is True.

        :param source64: base64 encoded unicode string to be unpacked.
        :param zipped: if True, ungzip ``source`` after
          base64-decoding. (Default: True).
        '''
        # @:adhoc_run_time_section:@ on
        import base64, gzip
        # @:adhoc_run_time_section:@ off
        if cls.debug:
            printf(sformat(
                "{0}{3:^{1}} {4:<{2}s}: ]{5:>7d}[ ]{6!s}[ {7}",
                dbg_comm, dbg_twid, dbg_fwid,
                ':DBG:', 'source64', len(source64), source64[:80],
                'b64decode ...'))
        # @:adhoc_run_time_section:@ on
        source = source64.encode('ascii')
        source = base64.b64decode(source)
        if zipped:
            # @:adhoc_run_time_section:@ off
            if cls.debug:
                printf(sformat(
                    "{0}{3:^{1}} {4:<{2}s}: ]{5:>7d}[ ]{6!s}[ {7}",
                    dbg_comm, dbg_twid, dbg_fwid,
                    ':DBG:', 'source (zip)', len(source), repr(source)[:80],
                    'unzipping ...'))
            # @:adhoc_run_time_section:@ on
            sio = _AdHocBytesIO(source)
            gzf = gzip.GzipFile('', 'rb', 9, sio)
            source = gzf.read()
            gzf.close()
            sio.close()
        if decode:
            source = cls.decode_source(source)
        # @:adhoc_run_time_section:@ off
        if cls.debug:
            printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5:>7d}[ ]{6!s}[",
                    dbg_comm, dbg_twid, dbg_fwid,
                    ':DBG:', 'source', len(source), repr(source)[:80]))

        # @:adhoc_run_time_section:@ on
        return source

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Run-Time Unpack/Import Interface
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def unpack_(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                mode=None, zipped=True, flat=None, source64=None):
        # @:adhoc_run_time_section:@ off
        """Unpack adhoc'ed file, if it does not exist."""
        # @:adhoc_run_time_section:@ on
        xfile = cls.check_xfile(file_, cls.extract_dir)
        if xfile is None:
            return
        if cls.verbose:
            list(map(sys.stderr.write,
                     ("# xf: ", cls.__name__, ": unpacking `", file_, "`\n")))
        source = cls.unpack_file(source64, zipped=zipped, decode=False)
        cls.write_source(xfile, source, mtime, mode)

    @classmethod
    def strptime(cls, date_string, format_):                 # |:clm:|
        # @:adhoc_run_time_section:@ off
        """Python 2.4 compatible"""
        # @:adhoc_run_time_section:@ on
        import datetime
        if hasattr(datetime.datetime, 'strptime'):
            strptime_ = datetime.datetime.strptime
        else:
            import time
            strptime_ = lambda date_string, format_: (
                datetime.datetime(*(time.strptime(date_string, format_)[0:6])))
        return strptime_(date_string, format_)

    @classmethod
    def import_(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                mode=None, zipped=True, flat=None, source64=None):
        # @:adhoc_run_time_section:@ off
        """Import adhoc'ed module."""
        # @:adhoc_run_time_section:@ on
        import datetime
        import time

        module = cls.module_setup(mod_name)

        if mtime is None:
            mtime = datetime.datetime.fromtimestamp(0)
        else:
            # mtime=2011-11-23T18:04:26[.218506], zipped=True, flat=None, source64=
            try:
                date, ms = mtime.split('.')
            except ValueError:
                date = mtime
                ms = 0
            mtime = cls.strptime(date, '%Y-%m-%dT%H:%M:%S')
            mtime += datetime.timedelta(microseconds=int(ms))

        source = cls.unpack_file(source64, zipped=zipped, decode=False)

        # @:adhoc_run_time_section:@ off
        # |:todo:| add to parent module
        # @:adhoc_run_time_section:@ on
        mod_parts = mod_name.split('.')
        mod_child = mod_parts[-1]
        parent = '.'.join(mod_parts[:-1])
        # @:adhoc_run_time_section:@ off
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                dbg_comm, dbg_twid, dbg_fwid, ':DBG:', 'parent', parent))

        # @:adhoc_run_time_section:@ on
        old_mtime = module.__adhoc__.mtime
        module = cls.module_setup(mod_name, file_, mtime, source, mode)
        if len(parent) > 0:
            setattr(sys.modules[parent], mod_child, module)

        if module.__adhoc__.mtime != old_mtime:
            # @:adhoc_run_time_section:@ off
            printf(sformat('{0}Executing source', dbg_comm))
            # @:adhoc_run_time_section:@ on
            source = cls.encode_source(module.__adhoc__.source)
            exec(source, module.__dict__)
        # @:adhoc_run_time_section:@ off

        msg = (((mod_name in sys.modules) and ('YES')) or ('NO'))
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                       dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                       mod_name + ' imported', msg))

        module_name = module.__name__
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                       dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                       'module_name', module_name))
        dump_attr(module, wid=80, trunc=5)
        # @:adhoc_run_time_section:@ on

    @classmethod
    def module_setup(cls, module=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                     source=None, mode=None):
        # @:adhoc_run_time_section:@ off
        '''Setup module for `AdHoc`.
        \\|:todo:| various modes are possible:
        - always use newest version (development) (currently implemented)
        - always use adhoc\'ed version (freeze) (not implemented)
        '''
        # @:adhoc_run_time_section:@ on
        m = 'ms: '
        class Attr:                                          # |:cls:|
            pass

        import types, datetime, os
        if not isinstance(module, types.ModuleType):
            mod_name = module
            if mod_name is None:
                mod_name = __name__
            try:
                if mod_name not in sys.modules:
                    # @:adhoc_run_time_section:@ off
                    if cls.verbose:
                        printe(sformat('{0}{1}__import__({2})',
                                       dbg_comm, m, mod_name))
                    # @:adhoc_run_time_section:@ on
                    __import__(mod_name)
                module = sys.modules[mod_name]
            except (ImportError, KeyError):
                # @:adhoc_run_time_section:@ off
                if cls.verbose:
                    printe(sformat('{0}{1}imp.new_module({2})',
                                   dbg_comm, m, mod_name))
                # @:adhoc_run_time_section:@ on
                import imp
                module = imp.new_module(mod_name)
                sys.modules[mod_name] = module
        else:
            mod_name = module.__name__

        if mtime is None:
            if (file_ is not None
                or source is not None):
                # the info is marked as outdated
                mtime = datetime.datetime.fromtimestamp(1)
            else:
                # the info is marked as very outdated
                mtime = datetime.datetime.fromtimestamp(0)

        if not hasattr(module, '__adhoc__'):
            adhoc = Attr()
            setattr(module, '__adhoc__', adhoc)
            setattr(adhoc, '__module__', module)

            mtime_set = None
            mode_set = mode
            if hasattr(module, '__file__'):
                module_file = module.__file__
                if module_file.endswith('.pyc'):
                    module_file = module_file[:-1]
                if os.access(module_file, os.R_OK):
                    stat = os.stat(module_file)
                    mtime_set = datetime.datetime.fromtimestamp(
                        stat.st_mtime)
                    mode_set = stat.st_mode
            if mtime_set is None:
                # the info is marked as very outdated
                mtime_set = datetime.datetime.fromtimestamp(0)
            adhoc.mtime = mtime_set
            adhoc.mode = mode_set
        else:
            adhoc = module.__adhoc__

        if (mtime > adhoc.mtime
            or not hasattr(module, '__file__')):
            if file_ is not None:
                setattr(module, '__file__', file_)
                if os.access(file_, os.R_OK):             # |:api_fi:|
                    stat = os.stat(file_)
                    adhoc.mtime = datetime.datetime.fromtimestamp(
                        stat.st_mtime)
                    adhoc.mode = stat.st_mode
                    if adhoc.mtime > mtime:
                        # the file on disk is newer than the adhoc'ed source
                        try:
                            delattr(adhoc, 'source')
                        except AttributeError:
                            pass
                        source = None

        if (mtime > adhoc.mtime
            or not hasattr(adhoc, 'source')):
            if source is not None:
                adhoc.source = source
                adhoc.mtime = mtime
                adhoc.mode = mode

        if not hasattr(adhoc, 'source'):
            try:
                file_ = module.__file__
                file_, source = cls.std_source_param(file_, source)
                adhoc.source = source
            except (AttributeError, IOError):
                # @:adhoc_run_time_section:@ off
                # if hasattr(module, '__path__'): # |:debug:|
                #     list(map(sys.stderr.write,
                #         ('module path: ', module.__path__, '\n')))
                # else:
                #     sys.stderr.write('no module.__path__\n')
                #     list(map(sys.stderr.write,
                #         [''.join((attr, str(value), "\n")) for attr, value in
                #          filter(lambda i: i[0] != '__builtins__',
                #                 sorted(vars(module).items()))]))
                if cls.verbose:
                    (t, e, tb) = sys.exc_info()
                    import traceback
                    printe(''.join(traceback.format_tb(tb)), end='')
                    printe(sformat('{0}: {1}', t.__name__, e))
                    del(tb)
                # @:adhoc_run_time_section:@ on
                pass

        return module

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Export Tools
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def std_source_param(cls, file_=None, source=None): # |:clm:||:api_fi:|
        # @:adhoc_run_time_section:@ off
        '''Setup standard source parameters.

        :returns: tuple ``( file_, source )``

        :param file_: If None, `__file__` is used. If it ends with
          ``.pyc``, it is transformed to ``.py``.
        :param source: If None, the result of :meth:`read_source` is
          used.
        '''
        # @:adhoc_run_time_section:@ on
        if file_ is None:
            file_ = __file__
        if file_.endswith('.pyc'):
            file_ = file_[:-1]
        if source is None:
            source = cls.read_source(file_)
        return (file_, source)

    @classmethod
    def export_source(cls, string, no_remove=False, no_disable=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''
        ============================ =========================
        check for |adhoc_remove|     sections and remove them!
        check for |adhoc_import|     sections and remove them!
        check for |adhoc_unpack|     sections and remove them!
        check for |adhoc_template_v| sections and remove them!
        check for |adhoc_disable|    sections and enable them!
        check for |adhoc_enable|     sections and disable them!
        check for |adhoc_remove_|    section markers and rename them!
        ============================ =========================
        '''
        # @:adhoc_run_time_section:@ on
        string = cls.collapse_macros(string)
        if not no_remove:
            string = cls.remove_sections(string, 'adhoc_remove')
        string = cls.remove_sections(string, 'adhoc_import')
        string = cls.remove_sections(string, 'adhoc_unpack')
        string = cls.remove_sections(string, 'adhoc_template_v')
        if not no_disable:
            string = cls.enable_sections(string, 'adhoc_disable')
            string = cls.disable_sections(string, 'adhoc_enable')
        if not no_remove:
            string = cls.section_tag_rename(string, 'adhoc_remove_', 'adhoc_remove')
        return string

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Extract Interface
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def unpack(cls, file_=None, source=None):                # |:clm:|
        # @:adhoc_run_time_section:@ off
        """Unpack all adhoc'ed files in |adhoc_unpack| sections."""
        # @:adhoc_run_time_section:@ on
        file_, source = cls.std_source_param(file_, source)
        source_sections, unpack_sections = cls.tag_partition(
            source, cls.section_tag('adhoc_unpack'))
        sv_extract_warn = cls.extract_warn
        cls.extract_warn = True
        unpack_call = ''.join((cls.__name__, '.unpack_'))
        for unpack_section in unpack_sections:
            unpack_section = re.sub('^\\s+', '', unpack_section)
            unpack_section = re.sub(
                '^[^(]*(?s)', unpack_call, unpack_section)
            try:
                #RtAdHoc = cls # unpack_call takes care of this
                exec(unpack_section.lstrip(), globals(), locals())
            except IndentationError:
                sys.stderr.write("!!! IndentationError !!!\n")
                # @:adhoc_run_time_section:@ off
                sys.stderr.write(''.join((unpack_section, "\n")))
                # @:adhoc_run_time_section:@ on
        cls.extract_warn = sv_extract_warn

    @classmethod
    def extract(cls, file_=None, source=None):               # |:clm:|
        # @:adhoc_run_time_section:@ off
        """Unpack all adhoc'ed files in |adhoc_unpack| sections and
        extract all templates."""
        # @:adhoc_run_time_section:@ on
        cls.unpack(file_, source)
        cls.extract_templates(file_, source, export=True)

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Export Interface
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def export__(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                 mode=None, zipped=True, flat=None, source64=None):
        source = cls.unpack_file(source64, zipped=zipped, decode=False)
        # @:adhoc_run_time_section:@ off
        if cls.debug:
            sys.stderr.write(
                ''.join(("# xp: ", cls.__name__, ".export__ for `",
                         file_, "`\n")))
        # @:adhoc_run_time_section:@ on
        if file_ is None:
            return
        file_base = os.path.basename(file_)
        if file_base.startswith('__init__.py'):
            is_init = True
        else:
            is_init = False

        parts = mod_name.split('.')
        base = parts.pop()
        if parts:
            module_dir = os.path.join(*parts)
            cls.export_need_init[module_dir] = True
        else:
            module_dir = ''
        if is_init:
            module_dir = os.path.join(module_dir, base)
            cls.export_have_init[module_dir] = True
        module_file = os.path.join(module_dir, file_base)

        cls.export_(source, module_file, mtime, mode, flat)

    @classmethod
    def export_(cls, source, file_, mtime, mode, flat=None): # |:clm:|
        cflat = cls.flat
        if flat is None:
            flat = cflat
        cls.flat = flat
        if not flat:
            # extract to export directory
            sv_extract_dir = cls.extract_dir
            cls.extract_dir = cls.export_dir
            cls.extract(file_, source)
            cls.extract_dir = sv_extract_dir

            source_sections, import_sections = cls.tag_partition(
                source, cls.section_tag('adhoc_import'))
            source = cls.export_source(''.join(source_sections))
            export_call = ''.join((cls.__name__, '.export__'))

            xfile = cls.check_xfile(file_, cls.export_dir)
            if xfile is not None:
                cls.write_source(xfile, source, mtime, mode)
                if cls.verbose:
                    list(map(sys.stderr.write,
                             ("# xp: ", cls.__name__, ".export_ for `", file_,
                              "` using `", export_call,"`\n")))

            for import_section in import_sections:
                # this calls RtAdHoc.export__
                import_section = re.sub('^\\s+', '', import_section)
                import_section = re.sub(
                    '^[^(]*(?s)', export_call, import_section)
                try:
                    #RtAdHoc = cls # export_call takes care of this
                    exec(import_section, globals(), locals())
                except IndentationError:
                    sys.stderr.write("!!! IndentationError !!!\n")
                    # @:adhoc_run_time_section:@ off
                    sys.stderr.write(''.join((import_section, "\n")))
                    # @:adhoc_run_time_section:@ on
        else:
            xfile = cls.check_xfile(file_, cls.export_dir)
            if xfile is not None:
                cls.write_source(xfile, source, mtime, mode)
                if cls.verbose:
                    list(map(sys.stderr.write,
                             ("# xp: ", cls.__name__, ".export_ for `", file_,
                              "` using `", export_call,"`\n")))
        cls.flat = cflat

    # @:adhoc_run_time_section:@ off
    default_engine = False

    # @:adhoc_run_time_section:@ on
    @classmethod
    def export(cls, file_=None, source=None):                # |:clm:|
        file_, source = cls.std_source_param(file_, source)
        # @:adhoc_run_time_section:@ off
        # |:todo:| this chaos needs cleanup (cls.import_/cls.export__)
        # @:adhoc_run_time_section:@ on
        sv_import = cls.import_
        cls.import_ = cls.export__

        file_ = os.path.basename(file_)
        # @:adhoc_run_time_section:@ off
        if cls.verbose:
            list(map(sys.stderr.write,
                     ("# xp: ", cls.__name__, ".export for `", file_, "`\n")))
        # @:adhoc_run_time_section:@ on
        cls.export_(source, file_, None, None, False)
        sv_extract_dir = cls.extract_dir
        cls.extract_dir = cls.export_dir
        engine_tag = cls.section_tag('adhoc_run_time_engine')
        engine_source = cls.export_source(
            source, no_remove=True, no_disable=True)
        engine_source = cls.get_named_template(
            None, file_, engine_source, tag=engine_tag, ignore_mark=True)
        # @:adhoc_run_time_section:@ off
        if cls.default_engine and not engine_source:
            state = cls.set_delimiters(('@:', ':@'))
            ah = cls()
            engine_source = ah.prepare_run_time_section()
            engine_source = cls.get_named_template(
                None, file_, engine_source, tag=engine_tag, ignore_mark=True)
            cls.reset_delimiters(state)
        # @:adhoc_run_time_section:@ on
        if engine_source:
            efile = cls.check_xfile('rt_adhoc.py')
            if efile is not None:
                cls.write_source(efile, engine_source)
        cls.extract_dir = sv_extract_dir
        for init_dir in cls.export_need_init:
            if not cls.export_have_init[init_dir]:
                if cls.verbose:
                    list(map(sys.stderr.write,
                             ("# xp: create __init__.py in `", init_dir, "`\n")))
                inf = open(os.path.join(
                    cls.export_dir, init_dir, '__init__.py'), 'w')
                inf.write('')
                inf.close()
        cls.import_ = sv_import

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Dump Interface (Import/Unpack Substitute)
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def dump__(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
               mode=None, zipped=True, flat=None, source64=None):
        if cls.verbose:
            list(map(sys.stderr.write,
                     ("# xf: ", cls.__name__, ": dumping `", file_, "`\n")))
        source = cls.unpack_file(source64, zipped=zipped, decode=False)
        return source

    @classmethod
    def dump_(cls, dump_section, dump_type=None):            # |:clm:|
        if dump_type is None:
            dump_type = 'adhoc_import'
        if not dump_section:
            return ''
        dump_call = ''.join(('unpacked = ', cls.__name__, '.dump__'))
        dump_section = re.sub('^\\s+', '', dump_section)
        dump_section = re.sub(
            '^[^(]*(?s)', dump_call, dump_section)
        dump_dict = {'unpacked': ''}
        try:
            #RtAdHoc = cls # dump_call takes care of this
            exec(dump_section.lstrip(), globals(), dump_dict)
        except IndentationError:
            sys.stderr.write("!!! IndentationError !!!\n")
            # @:adhoc_run_time_section:@ off
            sys.stderr.write(''.join((dump_section, "\n")))
            # @:adhoc_run_time_section:@ on
        return dump_dict['unpacked']

    @classmethod
    def dump_file(cls, match, file_=None, source=None, tag=None, # |:clm:|
                  is_re=False):
        file_, source = cls.std_source_param(file_, source)
        if tag is None:
            tag = cls.section_tag('(adhoc_import|adhoc_update)', is_re=True)
            is_re = True
        source_sections, dump_sections = cls.tag_partition(
            source, tag, is_re, headline=True)
        dump_call = ''.join((cls.__name__, '.dump_'))
        for dump_section in dump_sections:
            tagged_line = dump_section[0]
            dump_section = dump_section[1]
            tag_arg = cls.section_tag_strip(tagged_line)
            check_match = match
            if tag_arg != match and not match.startswith('-'):
                check_match = ''.join(('-', match))
            if tag_arg != match and not match.startswith('!'):
                check_match = ''.join(('!', match))
            if tag_arg != match:
                continue
            dump_section = re.sub('^\\s+', '', dump_section)
            dump_section = re.sub(
                '^[^(]*(?s)', dump_call, dump_section)
            try:
                #RtAdHoc = cls # dump_call takes care of this
                exec(dump_section.lstrip(), globals(), locals())
            except IndentationError:
                sys.stderr.write("!!! IndentationError !!!\n")
                # @:adhoc_run_time_section:@ off
                sys.stderr.write(''.join((dump_section, "\n")))
                # @:adhoc_run_time_section:@ on

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Macros
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    macro_call_delimiters = ('@|:', ':|>')
    # @:adhoc_run_time_section:@ off
    """Macro delimiters"""
    # @:adhoc_run_time_section:@ on
    macro_xdef_delimiters = ('<|:', ':|@')
    # @:adhoc_run_time_section:@ off
    """Macro expansion delimiters"""
    # @:adhoc_run_time_section:@ on
    macros = {}
    # @:adhoc_run_time_section:@ off
    """Macros"""
    # @:adhoc_run_time_section:@ on

    @classmethod
    def expand_macros(cls, source, macro_call_dlm=None, macro_xdef_dlm=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        """
        >>> AdHoc.macros['uc_descr_end'] = (
        ...     '# o:' 'adhoc_template:>\\n'
        ...     '# <:' 'adhoc_uncomment:>\\n'
        ...     )

        >>> macro_source = '# ' + AdHoc.adhoc_tag('uc_descr_end', AdHoc.macro_call_delimiters) + '\\n'
        >>> ign = sys.stdout.write(macro_source) #doctest: +ELLIPSIS
        # @|:uc_descr_end...:|>

        >>> ign = sys.stdout.write(AdHoc.expand_macros(macro_source)) #doctest: +ELLIPSIS
        # <|:adhoc_macro_call...:|@
        # @|:uc_descr_end...:|>
        # <|:adhoc_macro_call...:|@
        # <|:adhoc_macro_expansion...:|@
        # o:adhoc_template...:>
        # <:adhoc_uncomment...:>
        # <|:adhoc_macro_expansion...:|@

        """
        # @:adhoc_run_time_section:@ on
        if macro_call_dlm is None:
            macro_call_dlm = cls.macro_call_delimiters
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        import re
        for macro_name, macro_expansion in cls.macros.items():
            macro_tag = cls.adhoc_tag(macro_name, macro_call_dlm, False)
            macro_tag_rx = cls.adhoc_tag(macro_name, macro_call_dlm, True)
            macro_call = ''.join(('# ', macro_tag, '\n'))
            macro_call_rx = ''.join(('^[^\n]*', macro_tag_rx, '[^\n]*\n'))
            mc_tag = ''.join(('# ', cls.adhoc_tag('adhoc_macro_call', macro_xdef_dlm, False), "\n"))
            mx_tag = ''.join(('# ', cls.adhoc_tag('adhoc_macro_expansion', macro_xdef_dlm, False), "\n"))
            xdef = ''.join((
                mc_tag,
                macro_call,
                mc_tag,
                mx_tag,
                macro_expansion,
                mx_tag,
                ))
            rx = re.compile(macro_call_rx, re.M)
            source = rx.sub(xdef, source)
        return source

    @classmethod
    def has_expanded_macros(cls, source, macro_xdef_dlm=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        """
        """
        # @:adhoc_run_time_section:@ on
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        mx_tag = cls.adhoc_tag('adhoc_macro_expansion', macro_xdef_dlm, False)
        me_count = len(cls.tag_lines(source, mx_tag))
        return me_count > 0

    @classmethod
    def activate_macros(cls, source, macro_call_dlm=None, macro_xdef_dlm=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        """
        """
        # @:adhoc_run_time_section:@ on
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        if not cls.has_expanded_macros(source, macro_xdef_dlm):
            source = cls.expand_macros(source, macro_call_dlm, macro_xdef_dlm)
        sv = cls.set_delimiters (macro_xdef_dlm)
        source = cls.remove_sections(source, 'adhoc_macro_call')
        source = cls.section_tag_remove(source, 'adhoc_macro_expansion')
        cls.reset_delimiters(sv)
        return source

    @classmethod
    def collapse_macros(cls, source, macro_xdef_dlm=None):   # |:clm:|
        # @:adhoc_run_time_section:@ off
        """
        """
        # @:adhoc_run_time_section:@ on
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        if cls.has_expanded_macros(source, macro_xdef_dlm):
            sv = cls.set_delimiters (macro_xdef_dlm)
            source = cls.section_tag_remove(source, 'adhoc_macro_call')
            source = cls.remove_sections(source, 'adhoc_macro_expansion')
            cls.reset_delimiters(sv)
        return source

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Template Interface
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def std_template_param(cls, file_=None, source=None,     # |:clm:|
                           tag=None, is_re=False, all_=False):
        # @:adhoc_run_time_section:@ off
        '''Setup standard template parameters.

        :param tag: If None, section tag `adhoc_template(_v)?` is
          used.

        See :meth:`std_source_param` for `file_` and `source`.
        '''
        # @:adhoc_run_time_section:@ on
        file_, source = cls.std_source_param(file_, source)
        if tag is None:
            is_re=True
            if all_:
                tag = cls.section_tag('adhoc_(template(_v)?|import|unpack)', is_re=is_re)
            else:
                tag = cls.section_tag('adhoc_template(_v)?', is_re=is_re)
        source = cls.activate_macros(source)
        return (file_, source, tag, is_re)

    @classmethod
    def get_templates(cls, file_=None, source=None,          # |:clm:|
                      tag=None, is_re=False,
                      ignore_mark=False, all_=False):
        # @:adhoc_run_time_section:@ off
        '''Extract templates matching section tag.

        :param ignore_mark: If True, all templates are mapped to
          standard output name ``-``.
        :param tag: If None, `adhoc_template` is used.
        '''
        # @:adhoc_run_time_section:@ on
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_)
        source = cls.enable_sections(source, 'adhoc_uncomment')
        source = cls.indent_sections(source, 'adhoc_indent')
        source_sections, template_sections = cls.tag_partition(
            source, tag, is_re=is_re, headline=True)
        templates = {}
        for template_section in template_sections:
            tagged_line = template_section[0]
            section = template_section[1]
            tag, tag_arg = cls.section_tag_parse(tagged_line)
            if not tag_arg:
                tag_arg = '-'
            if tag_arg in cls.template_process_hooks:
                section = cls.template_process_hooks[tag_arg](cls, section, tag, tag_arg)
            if ignore_mark:
                tag_arg = '-'
            if tag_arg not in templates:
                templates[tag_arg] = [[section], tag]
            else:
                templates[tag_arg][0].append(section)
        if all_:
            result = dict([(m, (''.join(t[0]), t[1])) for m, t in templates.items()])
        else:
            result = dict([(m, ''.join(t[0])) for m, t in templates.items()])
        return result

    @classmethod
    def template_list(cls, file_=None, source=None,          # |:clm:|
                      tag=None, is_re=False, all_=False):
        # @:adhoc_run_time_section:@ off
        """Sorted list of templates.

        See :meth:`std_template_param` for `file_`, `source`, `tag`, `is_re`.

        .. @:adhoc_disable:@

        # >>> for tpl in AdHoc.template_list():
        # ...     printf(tpl)
        # -
        # README.txt
        # -adhoc_init
        # -catch-stdout
        # -col-param-closure
        # doc/USE_CASES.txt
        # doc/index.rst
        # -max-width-class
        # -rst-to-ascii
        # -test

        # >>> for tpl in AdHoc.template_list(all_=True):
        # ...     printf(strclean(tpl))
        # ('-', 'adhoc_template')
        # ('README.txt', 'adhoc_template')
        # ('-adhoc_init', 'adhoc_template')
        # ('-catch-stdout', 'adhoc_template')
        # ('-col-param-closure', 'adhoc_template')
        # ('doc/USE_CASES.txt', 'adhoc_template')
        # ('doc/index.rst', 'adhoc_template')
        # ('-max-width-class', 'adhoc_template')
        # ('-rst-to-ascii', 'adhoc_template')
        # ('-test', 'adhoc_template')

        .. @:adhoc_disable:@
        """
        # @:adhoc_run_time_section:@ on
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_)
        templates = cls.get_templates(file_, source, tag, is_re, all_=all_)
        if all_:
            templates.update([(k, ('', v)) for k, v in cls.extra_templates])
            result = list(sorted(
                [(k, v[1]) for k, v in templates.items()],
                key=lambda kt: '||'.join((
                    kt[1],
                    (((not (kt[0].startswith('-') or kt[0].startswith('!')))
                      and (kt[0]))
                     or (kt[0][1:]))))))
        else:
            templates.update(filter(
                lambda tdef: (tdef[1] == 'adhoc_template'
                              or tdef[1] == 'adhoc_template_v'),
                cls.extra_templates))
            result = list(sorted(
                templates.keys(),
                key=lambda kt: '||'.join((
                    (((not (kt.startswith('-') or kt.startswith('!')))
                      and (kt)) or (kt[1:]))))))
        return result

    # @:adhoc_run_time_section:@ off
    # @:adhoc_template:@ -col-param-closure
    # @:adhoc_run_time_section:@ on
    @classmethod
    def col_param_closure(cls):                              # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Closure for setting up maximum width, padding and separator
        for table columns.

        :returns: a setter and a getter function for calculating the
          maximum width of a list of strings (e.g. a table column).

        >>> set_, get_ = AdHoc.col_param_closure()
        >>> i = set_("string")
        >>> get_()
        [6, '      ', '======']

        >>> i = set_("str")
        >>> get_()
        [6, '      ', '======']

        >>> i = set_("longer string")
        >>> get_()
        [13, '             ', '=============']

        >>> table_in = """\\
        ... Column1 Column2
        ... some text text
        ... some-more-text text text
        ... something text
        ... less"""

        A splitter and column parameters depending on column count:

        >>> col_count = 2
        >>> splitter = lambda line: line.split(' ', col_count-1)
        >>> col_params = [AdHoc.col_param_closure() for i in range(col_count)]

        Generic table processor:

        >>> process_cols = lambda cols: [
        ...     col_params[indx][0](col) for indx, col in enumerate(cols)]
        >>> table = [process_cols(cols) for cols in
        ...          [splitter(line) for line in table_in.splitlines()]]

        Generic table output parameters/functions:

        >>> mws = [cp[1]()[0] for cp in col_params]
        >>> sep = ' '.join([cp[1]()[2] for cp in col_params])
        >>> paddings = [cp[1]()[1] for cp in col_params]
        >>> pad_cols_c = lambda cols: [
        ...     (((paddings[indx] is None) and (col))
        ...      or ((paddings[indx][:int((mws[indx]-len(col))/2)]
        ...           + col + paddings[indx])[:mws[indx]]))
        ...     for indx, col in enumerate(cols)]
        >>> pad_cols = lambda cols: [
        ...     (((paddings[indx] is None) and (col))
        ...      or ((col + paddings[indx])[:mws[indx]]))
        ...     for indx, col in enumerate(cols)]

        Generic table output generator:

        >>> output = []
        >>> if table:
        ...     output.append(sep)
        ...     output.append(' '.join(pad_cols_c(table.pop(0))).rstrip())
        ...     if table: output.append(sep)
        ...     output.extend([' '.join(pad_cols(cols)).rstrip()
        ...                    for cols in table])
        ...     output.append(sep)

        >>> i = sys.stdout.write("\\n".join(output))
        ============== =========
           Column1      Column2
        ============== =========
        some           text text
        some-more-text text text
        something      text
        less
        ============== =========
        '''
        # @:adhoc_run_time_section:@ on
        mw = [0, "", ""]
        def set_(col):                                       # |:clo:|
            lc = len(col)
            if mw[0] < lc:
                mw[0] = lc
                mw[1] = " " * lc
                mw[2] = "=" * lc
            return col
        def get_():                                          # |:clo:|
            return mw
        return set_, get_
    # @:adhoc_run_time_section:@ off
    # @:adhoc_template:@ -col-param-closure
    # @:adhoc_run_time_section:@ on

    tt_ide = False
    tt_comment = ''
    tt_prefix = ''
    tt_suffix = ''

    @classmethod
    def template_table(cls, file_=None, source=None,         # |:clm:|
                       tag=None, is_re=False):
        # @:adhoc_run_time_section:@ off
        '''Table of template commands.

        See :meth:`std_template_param` for `file_`, `source`, `tag`, `is_re`.
        '''
        # @:adhoc_run_time_section:@ on
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_=True)
        pfx = cls.tt_prefix
        sfx = cls.tt_suffix
        comm = cls.tt_comment
        if comm:
            comm = ''.join((comm, ' '))
            pfx = ''.join((comm, pfx))
        if cls.tt_ide:
            command = ''.join(('python ', file_))
        else:
            command = os.path.basename(file_)
        # Parse table
        table = []
        tpl_arg_name = (lambda t: (((not (t.startswith('-') or t.startswith('!'))) and (t)) or (t[1:])))
        col_param = [cls.col_param_closure() for i in range(3)]
        table.append((col_param[0][0]('Command'), col_param[1][0]('Template'), col_param[2][0]('Type')))
        table.extend([
            (col_param[0][0](''.join((
                pfx,
                command, ' --template ',
                tpl_arg_name(t[0])
                )).rstrip()),
             col_param[1][0](''.join((
                 '# ', t[0]
                 )).rstrip()),
             col_param[2][0](''.join((
                 t[1], sfx
                 )).rstrip()),)
            for t in cls.template_list(file_, source, tag, is_re, all_=True)])
        if cls.tt_ide:
            itable = []
            headers = table.pop(0)
            this_type = None
            last_type = None
            for cols in reversed(table):
                this_type = cols[2].replace('")', '')
                if last_type is not None:
                    if last_type != this_type:
                        itable.append((''.join((comm, ':ide: +#-+')), '', ''))
                        itable.append((''.join((comm, '. ', last_type, '()')), '', ''))
                        itable.append(('', '', ''))
                itable.append((''.join((comm, ':ide: ', cols[1].replace('#', 'AdHoc:'))), '', ''))
                itable.append(cols)
                itable.append(('', '', ''))
                last_type = this_type
            if last_type is not None:
                itable.append((''.join((comm, ':ide: +#-+')), '', ''))
                itable.append((''.join((comm, '. ', last_type, '()')), '', ''))
            table = [headers]
            table.extend(itable)
        # Setup table output
        mw, padding = (col_param[0][1]()[0], col_param[0][1]()[1])
        mw1, padding1 = (col_param[1][1]()[0], col_param[1][1]()[1])
        mw2, padding2 = (col_param[2][1]()[0], col_param[2][1]()[1])
        sep = ' '.join([cp[1]()[2] for cp in col_param])
        make_row_c = lambda row: ''.join((
            ''.join((padding[:int((mw-len(row[0]))/2)], row[0], padding))[:mw],
            ' ', ''.join((padding1[:int((mw1-len(row[1]))/2)],
                          row[1], padding1))[:mw1],
            ' ', ''.join((padding2[:int((mw2-len(row[2]))/2)],
                          row[2], padding2))[:mw2].rstrip()))
        make_row = lambda row: ''.join((''.join((row[0], padding))[:mw],
                                        ' ', ''.join((row[1], padding))[:mw1],
                                        ' ', row[2])).rstrip()
        # Generate table
        output = []
        output.append(sep)
        output.append(make_row_c(table.pop(0)))
        if table:
            output.append(sep)
            output.extend([make_row(row) for row in table])
        output.append(sep)
        return output

    @classmethod
    def get_named_template(cls, name=None, file_=None, source=None, # |:clm:|
                           tag=None, is_re=False, ignore_mark=False):
        # @:adhoc_run_time_section:@ off
        '''Extract templates matching section tag and name.

        :param name: Template name. If None, standard output name ``-`` is used.
        :param tag: If None, `adhoc_template(_v)?` is used.
        :param ignore_mark: If True, all templates are mapped to
          standard output name ``-``.

        If a named template cannot be found and `name` does not start
        with ``-``, the template name `-name` is tried.

        >>> ign = main("adhoc.py --template adhoc_test.sub".split())
        # -*- coding: utf-8 -*-
        <BLANKLINE>
        ADHOC_TEST_SUB_IMPORTED = True

        '''
        # @:adhoc_run_time_section:@ on
        if name is None:
            name = '-'
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_=True)
        templates = cls.get_templates(
            file_, source, tag, is_re=is_re, ignore_mark=ignore_mark, all_=True)
        check_name = name
        if check_name not in templates and not name.startswith('-'):
            check_name = ''.join(('-', name))
        if check_name not in templates and not name.startswith('!'):
            check_name = ''.join(('!', name))
        if check_name in templates:
            template_set = templates[check_name]
        else:
            template_set = ['', 'adhoc_template']
        template = template_set[0]
        template_type = template_set[1]
        if check_name.startswith('!'):
            template = cls.dump_(template, template_type)
        return template

    @classmethod
    def extract_templates(cls, file_=None, source=None,      # |:clm:|
                          tag=None, is_re=False, ignore_mark=False,
                          export=False):
        # @:adhoc_run_time_section:@ off
        '''Extract template.

        # @:adhoc_template_check:@ -mark
        A template ...
        # @:adhoc_template_check:@

        # @:adhoc_template_check:@ -other
        Another interleaved
        # @:adhoc_template_check:@

        # @:adhoc_template_check:@ -mark
        continued
        # @:adhoc_template_check:@

        >>> AdHoc.extract_templates(
        ...     tag=AdHoc.section_tag("adhoc_template_check"))
                A template ...
                continued
                Another interleaved

        >>> rt_section = AdHoc.get_templates(
        ...     __file__, None,
        ...     tag=AdHoc.section_tag("adhoc_run_time_section"),
        ...     ignore_mark=True)
        >>> rt_section = ''.join(rt_section.values())

        .. >>> printf(rt_section)
        '''
        # @:adhoc_run_time_section:@ on
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re)
        templates = cls.get_templates(
            file_, source, tag, is_re=is_re, ignore_mark=ignore_mark)
        sv_extract_warn = cls.extract_warn
        cls.extract_warn = True
        for outf, template in sorted(templates.items()):
            if outf.startswith('-'):
                outf = '-'
            if outf == '-' and export:
                continue
            xfile = cls.check_xfile(outf, cls.extract_dir)
            if xfile is not None:
                cls.write_source(xfile, template)
        cls.extract_warn = sv_extract_warn

    # @:adhoc_run_time_section:@ off

    # --------------------------------------------------
    # ||:sec:|| COMPILER DATA
    # --------------------------------------------------

    # tags are generated from symbols on init
    run_time_flag = None                      # line
    import_flag = None                        # line
    include_flag = None                       # line
    verbatim_flag = None                      # line
    compiled_flag = None                      # line
    run_time_class_flag = None                # line

    rt_engine_section_tag = None              # section
    indent_section_tag = None                 # section
    uncomment_section_tag = None              # section
    enable_section_tag = None                 # section
    disable_section_tag = None                # section
    remove_section_tag = None                 # section
    import_section_tag = None                 # section
    unpack_section_tag = None                 # section
    template_v_section_tag = None             # section
    template_section_tag = None               # section
    run_time_section_tag = None               # section

    run_time_section = None

    run_time_flag_symbol = 'adhoc_run_time'   # line
    import_flag_symbol = 'adhoc'              # line
    include_flag_symbol = 'adhoc_include'     # line
    verbatim_flag_symbol = 'adhoc_verbatim'   # line
    compiled_flag_symbol = 'adhoc_compiled'   # line
    run_time_class_symbol = 'adhoc_run_time_class' # line

    rt_engine_section_symbol = 'adhoc_run_time_engine' # section
    indent_section_symbol = 'adhoc_indent'             # section
    uncomment_section_symbol = 'adhoc_uncomment'       # section
    enable_section_symbol = 'adhoc_enable'             # section
    disable_section_symbol = 'adhoc_disable'           # section
    remove_section_symbol = 'adhoc_remove'             # section
    import_section_symbol = 'adhoc_import'             # section
    unpack_section_symbol = 'adhoc_unpack'             # section
    template_v_section_symbol = 'adhoc_template_v'     # section
    template_section_symbol = 'adhoc_template'         # section
    run_time_section_symbol = 'adhoc_run_time_section' # section

    run_time_class_prefix = 'Rt'
    import_function = 'AdHoc.import_'
    modules = {}
    compiling = []

    file_include_template = (                             # |:api_fi:|
        "{ind}"
        "# {stg}\n{ind}"
        "{rtp}{ahc}("
        "{mod},"
        " file_={fnm},\n{ina}"
        " mtime={mtm},"
        " mode={fmd},\n{ina}"
        " zipped={zip},"
        " flat={flt},"
        " source64=\n"
        "{src}"
        ")\n{ind}"
        "# {etg}\n"
        )

    # --------------------------------------------------
    # ||:sec:|| Setup
    # --------------------------------------------------

    def __init__(self):                                      # |:mth:|
        self.modules = {}
        self.compiling = []
        self.setup_tags()
        self.run_time_section = self.prepare_run_time_section().rstrip() + '\n'

    @classmethod
    def setup_tags(cls):                                     # |:mth:|
        cls.run_time_flag = cls.line_tag(cls.run_time_flag_symbol)
        cls.import_flag = cls.line_tag(cls.import_flag_symbol)
        cls.verbatim_flag = cls.line_tag(cls.verbatim_flag_symbol)
        cls.include_flag = cls.line_tag(cls.include_flag_symbol)
        cls.compiled_flag = cls.line_tag(cls.compiled_flag_symbol)
        cls.run_time_class_flag = cls.line_tag(cls.run_time_class_symbol)

        cls.rt_engine_section_tag = cls.section_tag(cls.rt_engine_section_symbol)
        cls.indent_section_tag = cls.section_tag(cls.indent_section_symbol)
        cls.uncomment_section_tag = cls.section_tag(cls.uncomment_section_symbol)
        cls.enable_section_tag = cls.section_tag(cls.enable_section_symbol)
        cls.disable_section_tag = cls.section_tag(cls.disable_section_symbol)
        cls.remove_section_tag = cls.section_tag(cls.remove_section_symbol)
        cls.import_section_tag = cls.section_tag(cls.import_section_symbol)
        cls.unpack_section_tag = cls.section_tag(cls.unpack_section_symbol)
        cls.template_v_section_tag = cls.section_tag(cls.template_v_section_symbol)
        cls.template_section_tag = cls.section_tag(cls.template_section_symbol)
        cls.run_time_section_tag = cls.section_tag(
            cls.run_time_section_symbol)

    # --------------------------------------------------
    # ||:sec:|| Tools
    # --------------------------------------------------

    @staticmethod
    def strquote(source, indent=(' ' * 4)):                  # |:fnc:|
        source = source.replace("'", "\\'")
        length = 78 - 2 - 4 - len(indent)
        if length < 50:
            length = 50
        output_parts = []
        indx = 0
        limit = len(source)
        while indx < limit:
            output_parts.extend((
                indent, "    '", source[indx:indx+length], "'\n"))
            indx += length
        return ''.join(output_parts)

    # --------------------------------------------------
    # ||:sec:|| Run-Time Section
    # --------------------------------------------------

    @classmethod
    def adhoc_run_time_sections_from_string(cls, string, symbol): # |:clm:|
        tag = sformat('(#[ \t\r]*)?{0}', cls.section_tag(symbol, is_re=True))
        def_sections = cls.tag_sections(string, tag, is_re=True)
        return def_sections

    @classmethod
    def adhoc_run_time_section_from_file(cls, file_, symbol): # |:clm:|
        if file_.endswith('.pyc'):
            file_ = file_[:-1]
        string = cls.read_source(file_)
        def_sections = cls.adhoc_run_time_sections_from_string(
            string, symbol)
        return def_sections

    @classmethod
    def adhoc_get_run_time_section(                          # |:clm:|
        cls, symbol, prolog='', epilog=''):
        import datetime

        adhoc_module_places = []

        # try __file__
        adhoc_module_places.append(__file__)
        def_sections = cls.adhoc_run_time_section_from_file(
            __file__, symbol)
        if len(def_sections) == 0:
            # try adhoc.__file__
            try:
                import adhoc
                adhoc_module_places.append(adhoc.__file__)
                def_sections = cls.adhoc_run_time_section_from_file(
                    adhoc.__file__, symbol)
            except:
                pass
        if len(def_sections) == 0:
            # try adhoc.__adhoc__.source
            try:
                adhoc_module_places.append('adhoc.__adhoc__.source')
                def_sections = cls.adhoc_run_time_sections_from_string(
                    adhoc.__adhoc__.source, symbol)
            except:
                pass

        if len(def_sections) == 0:
            adhoc_dump_list(def_sections)
            raise AdHocError(sformat('{0} not found in {1}',
                    cls.section_tag(symbol),
                    ', '.join(adhoc_module_places)))

        def_ = ''.join((
                sformat('# {0}\n', cls.remove_section_tag),
                sformat('# {0}\n', cls.rt_engine_section_tag),
                sformat('# -*- coding: utf-8 -*-\n'),
                sformat('# {0} {1}\n', cls.compiled_flag,
                                     datetime.datetime.now(),
                                     # |:todo:| add input filename
                                     ),
                prolog,
                ''.join(def_sections),
                epilog,
                sformat('# {0}\n', cls.rt_engine_section_tag),
                sformat('# {0}\n', cls.remove_section_tag),
                ))
        return def_

    @classmethod
    def prepare_run_time_section(cls):                       # |:mth:|
        rts = cls.adhoc_get_run_time_section(
            cls.run_time_section_symbol)
        rtc_sections = cls.tag_split(
            rts, cls.run_time_class_flag)
        transform = []
        done = False
        use_next = False
        for section in rtc_sections:
            blob = section[1]
            if section[0]:
                use_next = blob
                continue
            if use_next:
                if not done:
                    mo = re.search('class[ \t\r]+', blob)
                    if mo:
                        blob = (blob[:mo.end(0)]
                              + cls.run_time_class_prefix
                              + blob[mo.end(0):])
                        done = True
                    else:
                        #transform.append(use_next)
                        pass
                use_next = False
            transform.append(blob)
        transform.append(sformat('# {0}\n', cls.remove_section_tag))
        transform.append(sformat('# {0}\n', cls.rt_engine_section_tag))
        transform.append(sformat('# {0}\n', cls.rt_engine_section_tag))
        transform.append(sformat('# {0}\n', cls.remove_section_tag))
        rts = ''.join(transform)
        if not done:
            raise AdHocError(
                sformat('run-time class(tag) `{0}` not found in:\n{1}',
                        cls.run_time_class_flag, rts))
        return rts

    # --------------------------------------------------
    # ||:sec:|| Internal Includer (verbatim)
    # --------------------------------------------------

    def verbatim_(self, string, name=None):                  # |:mth:|
        '''Entry point for verbatim inclusion.

        :returns: string with verbatim included files.

        :param string: input string, with |adhoc_verbatim| flags.
        :param name: ignored. (API compatibility with
          :meth:`AdHoc.compile_`).

        .. note:: double commented flags, e.g. ``##``
           |adhoc_verbatim|, are ignored.

        .. \\|:here:|

        >>> section = """\\
        ... some
        ...     @:""" """adhoc_verbatim:@ {flags} my_verbatim{from_}
        ... text\\
        ... """

        >>> adhoc = AdHoc()

        **Non-existent File**

        >>> sv_quiet = AdHoc.quiet
        >>> AdHoc.quiet = True
        >>> source = adhoc.verbatim_(sformat(section, flags="-2#", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... -2# my_verbatim
        text
        >>> AdHoc.quiet = sv_quiet

        **Empty File**

        >>> source = adhoc.verbatim_(sformat(section, flags="", from_=" from /dev/null"))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim...  my_verbatim from /dev/null
            # @:adhoc_remove...
            # @:adhoc_indent... -4
            # @:adhoc_template_v... my_verbatim
            # @:adhoc_template_v...
            # @:adhoc_indent...
            # @:adhoc_remove...
        text

        **Empty file, with negative indent, commented**

        >>> source = adhoc.verbatim_(sformat(section, flags="-2#", from_=" from /dev/null"))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... -2# my_verbatim from /dev/null
          # @:adhoc_remove...
          # @:adhoc_uncomment...
          # @:adhoc_indent... -2
          # @:adhoc_template_v... my_verbatim
          # @:adhoc_template_v...
          # @:adhoc_indent...
          # @:adhoc_uncomment...
          # @:adhoc_remove...
        text

        **Empty file, with overflowing negative indent, commented**

        >>> source = adhoc.verbatim_(sformat(section, flags="-8#", from_=" from /dev/null"))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... -8# my_verbatim from /dev/null
        # @:adhoc_remove...
        # @:adhoc_uncomment...
        # @:adhoc_template_v... my_verbatim
        # @:adhoc_template_v...
        # @:adhoc_uncomment...
        # @:adhoc_remove...
        text

        **Existing file, without newline at end of file, commented.**

        >>> mvf = open("my_verbatim", "w")
        >>> ign = mvf.write("no end of line")
        >>> mvf.close()
        >>> source = adhoc.verbatim_(sformat(section, flags="-4#", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... -4# my_verbatim
        # @:adhoc_remove...
        # @:adhoc_uncomment...
        # @:adhoc_template_v... my_verbatim
        # no end of line
        # @:adhoc_template_v...
        # @:adhoc_uncomment...
        # @:adhoc_remove...
        text

        **Existing file, with extra newline at end of file, commented.**

        >>> mvf = open("my_verbatim", "w")
        >>> ign = mvf.write("extra end of line\\n\\n")
        >>> mvf.close()
        >>> source = adhoc.verbatim_(sformat(section, flags="-4#", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... -4# my_verbatim
        # @:adhoc_remove...
        # @:adhoc_uncomment...
        # @:adhoc_template_v... my_verbatim
        # extra end of line
        <BLANKLINE>
        # @:adhoc_template_v...
        # @:adhoc_uncomment...
        # @:adhoc_remove...
        text

        **Existing file, without newline at end of file, not commented.**

        >>> mvf = open("my_verbatim", "w")
        >>> ign = mvf.write("no end of line")
        >>> mvf.close()
        >>> source = adhoc.verbatim_(sformat(section, flags="-4", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... -4 my_verbatim
        # @:adhoc_remove...
        # @:adhoc_template_v... my_verbatim
        no end of line
        # @:adhoc_template_v...
        # @:adhoc_remove...
        text

        **Existing file, with extra newline at end of file, not commented.**

        >>> mvf = open("my_verbatim", "w")
        >>> ign = mvf.write("extra end of line\\n\\n")
        >>> mvf.close()
        >>> source = adhoc.verbatim_(sformat(section, flags="", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... my_verbatim
            # @:adhoc_remove...
            # @:adhoc_indent:@ -4
            # @:adhoc_template_v... my_verbatim
            extra end of line
        <BLANKLINE>
            # @:adhoc_template_v...
            # @:adhoc_indent:@
            # @:adhoc_remove...
        text

        **Existing file, but override with source /dev/null.**

        >>> source = adhoc.verbatim_(sformat(section, flags="/dev/null as", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... /dev/null as my_verbatim
            # @:adhoc_remove...
            # @:adhoc_indent... -4
            # @:adhoc_template_v... my_verbatim
            # @:adhoc_template_v...
            # @:adhoc_indent...
            # @:adhoc_remove...
        text

        **Existing file, override with non-existing source /not-here/.**

        >>> if os.path.exists("not-here"):
        ...     os.unlink("not-here")
        >>> source = adhoc.verbatim_(sformat(section, flags="not-here as", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... not-here as my_verbatim
            # @:adhoc_remove...
            # @:adhoc_indent... -4
            # @:adhoc_template_v... my_verbatim
            extra end of line
        <BLANKLINE>
            # @:adhoc_template_v...
            # @:adhoc_indent...
            # @:adhoc_remove...
        text

        >>> os.unlink("my_verbatim")
        '''
        m = 'is: '

        import datetime

        # # check for @: adhoc_compiled :@
        # adhoc_compiled_lines = self.tag_lines(
        #     string, self.line_tag('adhoc_compiled'))
        # if len(adhoc_compiled_lines) > 0:
        #     sys.stderr.write(sformat(
        #         '{0}{1}' 'warning: {2} already AdHoc\'ed `{3}`\n',
        #         dbg_comm, m, name, adhoc_compiled_lines[0].rstrip()))
        #     return string

        # handle @: adhoc_verbatim :@
        result = []
        verbatim_cmd_parts = self.tag_split(string, self.verbatim_flag)
        for part in verbatim_cmd_parts:
            verbatim_def = part[1]
            result.append(verbatim_def)
            if part[0]:
                # skip commented verbatim includes
                if re.match('\\s*#\\s*#', verbatim_def):
                    if self.verbose:
                        printe(sformat(
                            '{0}{1}Skipping disabled verbatim `{2}`',
                            dbg_comm, m, verbatim_def.rstrip()))
                    continue

                indent = ''
                mo = re.match('\\s*', verbatim_def)
                if mo:
                    indent = mo.group(0)

                verbatim_def = self.line_tag_strip(
                    verbatim_def, self.verbatim_flag_symbol)
                verbatim_specs = []
                for verbatim_spec in re.split('\\s*,\\s*', verbatim_def):
                    verbatim_spec1 = re.split('\\s+from\\s+', verbatim_spec)
                    verbatim_spec2 = re.split('\\s+as\\s+', verbatim_spec)
                    default = None
                    source = None
                    output = None
                    flags = None
                    if len(verbatim_spec1) > 1:
                        output = verbatim_spec1[0]
                        default = verbatim_spec1[1]
                        fields = re.split('\\s+', output, 1)
                        if len(fields) > 1:
                            flags = fields[0]
                            output = fields[1]
                        else:
                            flags = ''
                        source = output
                    if len(verbatim_spec2) > 1:
                        source = verbatim_spec2[0]
                        output = verbatim_spec2[1]
                        fields = re.split('\\s+', source, 1)
                        if len(fields) > 1:
                            flags = fields[0]
                            source = fields[1]
                        else:
                            flags = ''
                        default = output
                    if flags is None:
                        source = verbatim_spec
                        fields = re.split('\\s+', source, 1)
                        if len(fields) > 1:
                            flags = fields[0]
                            source = fields[1]
                        else:
                            flags = ''
                            source = fields[0]
                        default = source
                        output = source
                    verbatim_specs.append([flags, source, default, output])

                for verbatim_spec in verbatim_specs:
                    vflags = verbatim_spec.pop(0)
                    ifile = verbatim_spec.pop()
                    found = False
                    for lfile in verbatim_spec:
                        lfile = os.path.expanduser(lfile)
                        blfile = lfile
                        for include_dir in self.include_path:
                            if not os.path.exists(lfile):
                                if not (os.path.isabs(blfile)):
                                    lfile = os.path.join(include_dir, blfile)
                                    continue
                            break
                        if os.path.exists(lfile):
                            stat = os.stat(lfile)
                            mtime = datetime.datetime.fromtimestamp(
                                stat.st_mtime)
                            mode = stat.st_mode

                            exp_source = self.read_source(lfile)
                            source_len = len(exp_source)

                            start_tags = []
                            end_tags = []
                            prefix = []
                            tag_prefix = ['# ']

                            mo = re.search('[-+]?[0-9]+', vflags)
                            if mo:
                                uindent = int(mo.group(0))
                            else:
                                uindent = 0

                            tindent = (len(indent) + uindent)
                            if tindent < 0:
                                tindent = 0
                            if tindent:
                                tag = self.indent_section_tag
                                start_tags.insert(
                                    0, ''.join((tag, ' ', str(-tindent))))
                                end_tags.append(tag)
                                prefix.insert(0, ' ' * tindent)
                                tag_prefix.insert(0, ' ' * tindent)

                            if '#' in vflags:
                                tag = self.uncomment_section_tag
                                start_tags.insert(0, tag)
                                end_tags.append(tag)
                                exp_source, hl = self.disable_transform(exp_source)

                            tag = self.remove_section_tag
                            start_tags.insert(0, tag)
                            end_tags.append(tag)

                            tag = self.section_tag('adhoc_template_v')
                            start_tags.append(''.join((tag, ' ', ifile)))
                            end_tags.insert(0,tag)

                            prefix = ''.join(prefix)
                            tag_prefix = ''.join(tag_prefix)
                            if prefix and exp_source:
                                if exp_source.endswith('\n'):
                                    exp_source = exp_source[:-1]
                                exp_source = re.sub('^(?m)', prefix, exp_source)
                            if exp_source and not exp_source.endswith('\n'):
                                exp_source = ''.join((exp_source, '\n'))

                            output = []
                            output.extend([''.join((
                                tag_prefix, tag, '\n')) for tag in start_tags])
                            output.append(exp_source)
                            output.extend([''.join((
                                tag_prefix, tag, '\n')) for tag in end_tags])
                            result.append(''.join(output))
                            found = True

                            # |:debug:|
                            if self.verbose:
                                printe(sformat(
                                    "{0}{3:^{1}} {4:<{2}s}: ]len: {5:>6d}"
                                    " exp: {6:>6d} ]{9}[",
                                    dbg_comm, dbg_twid, dbg_fwid, ':INF:',
                                    'source stats', source_len, len(exp_source),
                                    0, 0, ifile))
                            # |:debug:|
                            break
                    if not found and not self.quiet:
                        list(map(sys.stderr.write,
                                 ("# if: ", self.__class__.__name__,
                                  ": warning verbatim file `", ifile,
                                  "` not found from `",
                                  ', '.join(verbatim_spec), "`\n")))
        #adhoc_dump_list(result)
        return ''.join(result)

    # --------------------------------------------------
    # ||:sec:|| Internal Includer (packed)
    # --------------------------------------------------

    def include_(self, string, name=None, zipped=True, flat=None): # |:mth:|
        '''Entry point for inclusion.

        :returns: string with packed included files.

        :param string: input string, with |adhoc_include| flags.
        :param name: ignored. (API compatibility with
          :meth:`AdHoc.compile_`).
        :param zipped: if True, :mod:`gzip` included files.

        .. note:: double commented flags, e.g. ``##``
           |adhoc_include|, are ignored.

        .. \\|:here:|

        >>> section = """\\
        ... some
        ... @:""" """adhoc_include:@ Makefile
        ... text\\
        ... """

        .. @:adhoc_disable:@

        # >>> adhoc = AdHoc()
        # >>> source = adhoc.include_(section)
        # >>> printf(source) #doctest: +ELLIPSIS
        # some
        # @:adhoc_include... Makefile
        # # @:adhoc_unpack...
        # RtAdHoc.unpack_(None, file_='Makefile',
        #     mtime='...', mode=...,
        #     zipped=True, flat=None, source64=
        # ...
        # # @:adhoc_unpack...
        # text

        .. @:adhoc_disable:@
        '''
        m = 'is: '

        import datetime

        # # check for @: adhoc_compiled :@
        # adhoc_compiled_lines = self.tag_lines(
        #     string, self.line_tag('adhoc_compiled'))
        # if len(adhoc_compiled_lines) > 0:
        #     sys.stderr.write(sformat(
        #         '{0}{1}' 'warning: {2} already AdHoc\'ed `{3}`\n',
        #         dbg_comm, m, name, adhoc_compiled_lines[0].rstrip()))
        #     return string

        # handle @: adhoc_include :@
        result = []
        include_cmd_sections = self.tag_split(string, self.include_flag)
        for section in include_cmd_sections:
            include_def = section[1]
            result.append(include_def)
            if section[0]:
                # skip commented includes
                if re.match('\\s*#\\s*#', include_def):
                    if self.verbose:
                        printe(sformat(
                            '{0}{1}Skipping disabled include `{2}`',
                            dbg_comm, m, include_def.rstrip()))
                    continue

                indent = ''
                mo = re.match('\\s*', include_def)
                if mo:
                    indent = mo.group(0)

                include_def = self.line_tag_strip(
                    include_def, self.include_flag_symbol)
                include_specs = []
                for include_spec in re.split('\\s*,\\s*', include_def):
                    include_spec1 = re.split('\\s+from\\s+', include_spec)
                    include_spec2 = re.split('\\s+as\\s+', include_spec)
                    default = None
                    source = None
                    output = None
                    if len(include_spec1) > 1:
                        output = include_spec1[0]
                        default = include_spec1[1]
                        source = output
                    if len(include_spec2) > 1:
                        source = include_spec2[0]
                        output = include_spec2[1]
                        default = output
                    if source is None:
                        source = include_spec
                        output = source
                        default = source
                    include_specs.append([source, default, output])

                for include_spec in include_specs:
                    ifile = include_spec.pop()
                    found = False
                    for lfile in include_spec:
                        lfile = os.path.expanduser(lfile)
                        blfile = lfile
                        for include_dir in self.include_path:
                            if not os.path.exists(lfile):
                                if not (os.path.isabs(blfile)):
                                    lfile = os.path.join(include_dir, blfile)
                                    continue
                            break
                        if os.path.exists(lfile):
                            stat = os.stat(lfile)
                            mtime = datetime.datetime.fromtimestamp(
                                stat.st_mtime)
                            mode = stat.st_mode

                            exp_source = self.read_source(lfile, decode=False)
                            source64 = self.pack_file(exp_source, zipped)
                            output = self.strquote(source64, indent)
                            file_include_args = dict([    # |:api_fi:|
                                ('ind', indent),
                                ('ina', ''.join((indent, "   "))),
                                ('stg', ''.join((self.unpack_section_tag, ' !', ifile))),
                                ('etg', self.unpack_section_tag),
                                ('rtp', self.run_time_class_prefix),
                                ('ahc', 'AdHoc.unpack_'),
                                ('mod', 'None'),
                                ('fnm', repr(str(ifile))),
                                ('mtm', (((mtime is not None)
                                          and repr(mtime.isoformat()))
                                         or repr(mtime))),
                                ('fmd', (mode is not None and sformat('int("{0:o}", 8)', mode)) or mode),
                                ('zip', zipped),
                                ('flt', flat),
                                ('src', output.rstrip()),
                            ])
                            output = sformat(
                                self.file_include_template,
                                **file_include_args
                                )
                            result.append(output)
                            found = True
                            # |:debug:|
                            if self.verbose:
                                source_len = len(exp_source)
                                exp_source_len = len(exp_source)
                                source64_len = len(source64)
                                printe(sformat(
                                    "{0}{3:^{1}} {4:<{2}s}: ]len: {5:>6d}"
                                    " exp: {6:>6d} b64: {8:>6d}[ ]{9}[",
                                    dbg_comm, dbg_twid, dbg_fwid, ':INF:',
                                    'source stats', source_len, exp_source_len,
                                    0, source64_len, ifile))
                            # |:debug:|
                            break
                    if not found and not self.quiet:
                        list(map(sys.stderr.write,
                                 ("# if: ", self.__class__.__name__,
                                  ": warning include file `",
                                  ifile, "` not found from `",
                                  ', '.join(include_spec), "`\n")))
        #adhoc_dump_list(result)
        return ''.join(result)

    # --------------------------------------------------
    # ||:sec:|| Internal Compiler
    # --------------------------------------------------

    def encode_module_(                                      # |:mth:|
        self, module, for_=None, indent='', zipped=True, flat=None, forced=None):
        m = 'gm: '

        if for_ is None:
            for_ = self.import_function

        if forced is None:
            forced = self.forced

        module = self.module_setup(module)
        module_name = module.__name__

        # no multiple occurences
        if (not forced
            and (module_name in self.modules
                 or module_name in self.compiling)):
            if self.verbose:
                 # |:check:| what, if the previous import was never
                 # executed?
                sys.stderr.write(sformat(
                        '{0}{1}`{2}` already seen. skipping ...\n',
                        dbg_comm, m, module_name))
            return ''

        self.compiling.append(module_name)

        result = []
        # |:todo:| parent modules
        parts = module_name.split('.')
        parent_modules = parts[:-1]
        if self.verbose and len(parent_modules) > 0:
            sys.stderr.write(sformat(
                    '{0}{1}Handle parent module(s) `{2}`\n',
                    dbg_comm, m, parent_modules))
        for parent_module in parent_modules:
            result.append(self.encode_module_(
                parent_module, for_, indent, zipped, flat, forced))

        if (module_name in self.modules):
            if self.verbose:
                sys.stderr.write(sformat(
                    '{0}{1}{1} already seen after parent import\n',
                    dbg_comm, m, module_name))
            return ''.join(result)

        if hasattr(module, '__file__'):
            module_file = module.__file__
            if module_file.endswith('.pyc'):
                module_file = module_file[:-1]
        else:
            module_file = None

        if hasattr(module.__adhoc__, 'source'):
            source = module.__adhoc__.source
        else:
            if not self.quiet:
                printf(sformat(
                    '{0}{1}|' 'warning: `{2}` does not have any source code.',
                    dbg_comm, m, module_name), file=sys.stderr)
            source = ''
            return ''.join(result)

        # recursive!
        exp_source = self.compile_(source, module_file, for_, zipped, forced)
        source64 = self.pack_file(exp_source, zipped)
        output = self.strquote(source64, indent)

        mtime = module.__adhoc__.mtime
        mode = module.__adhoc__.mode
        # |:todo:| make Rt prefix configurable
        file_include_args = dict([                        # |:api_fi:|
            ('ind', indent),
            ('ina', ''.join((indent, "   "))),
            ('stg', ''.join((self.import_section_tag, ' !', module_name))),
            ('etg', self.import_section_tag),
            ('rtp', self.run_time_class_prefix),
            ('ahc', for_),
            ('mod', repr(module.__name__)),
            ('fnm', (((module_file is not None)
                      and repr(str(os.path.relpath(module_file))))
                     or module_file)),
            ('mtm', (((mtime is not None)
                      and repr(mtime.isoformat()))
                     or repr(mtime))),
            ('fmd', (mode is not None and sformat('int("{0:o}", 8)', mode)) or mode),
            ('zip', zipped),
            ('src', output.rstrip()),
            ('flt', flat),
            ])
        output = sformat(
            self.file_include_template,
            **file_include_args
            )
        result.append(output)

        # |:debug:|
        if self.verbose:
            source_len = len(source)
            exp_source_len = len(exp_source)
            source64_len = len(source64)
            printe(sformat(
                "{0}{3:^{1}} {4:<{2}s}: ]len: {5:>6d} exp: {6:>6d}"
                " b64: {8:>6d}[ ]{9}[",
                dbg_comm, dbg_twid, dbg_fwid, ':INF:',
                'source stats', source_len, exp_source_len, 0,
                source64_len, module_file))
        # |:debug:|
        return ''.join(result)

    def compile_(self, string, name=None, for_=None,         # |:mth:|
                 zipped=True, forced=None):
        '''Entry point for compilation.

        :returns: string with fully compiled adhoc source. Includes
          run-time class, imports, packed includes, verbatim includes,
          enabled/disabled sections.

        :param string: input string, with |adhoc| flags.
        :param name: for messages.
        :param for_: :class:`RtAdHoc` method call.
        :param zipped: if True, :mod:`gzip` included files.

        .. note:: for |adhoc|, commented lines, e.g.
           ``# import module # @:``\\ ``adhoc:@``, are ignored.

        .. \\|:here:|
        '''
        m = 'cs: '
        if name is None:
            name = repr(string[:50])
        # check for @: adhoc_compiled :@
        string = self.expand_macros(string)
        adhoc_compiled_lines = self.tag_lines(
            string, self.line_tag('adhoc_compiled'))
        if len(adhoc_compiled_lines) > 0:
            if not self.quiet:
                list(map(sys.stderr.write,
                         ('# ', m,  'warning: ', name, ' already AdHoc\'ed `',
                          adhoc_compiled_lines[0].rstrip(), '`\n',)))
            return string

        # check for @: adhoc_self :@ (should not be taken from any templates)
        adhoc_self_tag = self.line_tag('adhoc_self')
        adhoc_self_lines = self.tag_lines(
            string, adhoc_self_tag)
        if len(adhoc_self_lines) > 0:
            for line in adhoc_self_lines:
                line = re.sub(''.join(('^.*', adhoc_self_tag)), '', line)
                line = line.strip()
                selfs = line.split()
                if self.verbose:
                    printe(sformat(
                        '{0}{1}|' ':INF:| {2} found self: `{3}`',
                        dbg_comm, m, name, ', '.join(selfs)))
                self.compiling.extend(selfs)

        # check for @: adhoc_remove :@
        string = self.section_tag_rename(string, 'adhoc_remove', 'adhoc_remove_')

        # check for @: adhoc_verbatim :@ (templates can define the run-time flag, includes, imports)
        string = self.verbatim_(string, name)

        # search for @: adhoc_run_time :@ and put run-time section there!
        result = []
        ah_run_time_sections = self.tag_split(
            string, self.line_tag(self.run_time_flag_symbol))
        good = False
        for section in ah_run_time_sections:
            config_def = section[1]
            if not good and section[0]:
                # ignore double commented tagged lines
                if not re.match('\\s*#\\s*#', config_def):
                    config_def = sformat('{0}{1}',
                        config_def, self.run_time_section)
                    good = True
            result.append(config_def)
        string = ''.join(result)

        # check for @: adhoc_include :@
        string = self.include_(string, name, zipped)

        # handle @: adhoc :@ imports
        result = []
        import_cmd_sections = self.tag_split(string, self.import_flag)
        if not good and len(import_cmd_sections) > 1:
            adhoc_dump_sections(import_cmd_sections)
            raise AdHocError(sformat('{0} not found',
                    self.line_tag(self.run_time_flag_symbol)))
        for section in import_cmd_sections:
            import_def = section[1]
            if section[0]:
                # skip commented imports
                if re.match('\\s*#', import_def):
                    if self.verbose:
                        printe(sformat(
                            '{0}{1}Skipping disabled `{2}`',
                            dbg_comm, m, import_def.rstrip()))
                    result.append(import_def)
                    continue
                import_args = self.line_tag_strip(import_def, self.import_flag_symbol)
                module = ''
                mo = re.match(
                    '(\\s*)from\\s+([a-zA-Z_][.0-9a-zA-Z_]*)\\s+'
                    'import', import_def)
                if mo:
                    indent = mo.group(1)
                    module = mo.group(2)
                else:
                    mo = re.match(
                        '([ \t\r]*)import[ \t\r]+([a-zA-Z_][.0-9a-zA-Z_]*)',
                        import_def)
                    if mo:
                        indent = mo.group(1)
                        module = mo.group(2)
                if len(module) > 0:
                    module_flat = ((('flat' in import_args.lower().split()) and (True)) or (None))
                    module_flat = ((('full' in import_args.lower().split()) and (False)) or (module_flat))
                    module_forced = ((('force' in import_args.lower().split()) and (True)) or (forced))
                    source = self.encode_module_(module, for_, indent, zipped, module_flat, module_forced)
                    import_def = sformat('{0}{1}',source, import_def)
                else:
                    if self.verbose:
                        list(map(sys.stderr.write,
                                 ('# ', m, 'warning: no import found! `',
                                  import_def.rstrip(), '`\n')))
            result.append(import_def)
        string = ''.join(result)

        # These are last, to avoid enabling/disabling the wrong imports etc.

        # check for @: adhoc_enable :@
        string = self.enable_sections(string, 'adhoc_enable')
        # check for @: adhoc_disable :@
        string = self.disable_sections(string, 'adhoc_disable')

        #adhoc_dump_list(result)
        return string

    # --------------------------------------------------
    # ||:sec:|| User API
    # --------------------------------------------------

    def encode_include(                                      # |:mth:|
        self, file_, as_=None, indent='', zipped=True):
        m = 'if: '

    def encode_module(                                       # |:mth:|
        self, module, for_=None, indent='', zipped=True, flat=None, forced=None):
        if hasattr(module, __name__):
            name = module.__name__
        else:
            name = module
        if self.verbose:
            sys.stderr.write(sformat(
                '{0}--------------------------------------------------\n',
                dbg_comm))
            sys.stderr.write(sformat(
                '{0}Get module `{1}`\n',
                dbg_comm, name))
            sys.stderr.write(sformat(
                '{0}--------------------------------------------------\n',
                dbg_comm))
        return self.encode_module_(module, for_, indent, zipped, flat, forced)

    def compile(self, string, name=None, for_=None,          # |:mth:|
                zipped=True, forced=None):
        '''Compile a string into adhoc output.'''
        if self.verbose:
            if name is None:
                name = repr(string[:50])
            sys.stderr.write(sformat(
                    '{0}--------------------------------------------------\n',
                    dbg_comm))
            sys.stderr.write(sformat(
                    '{0}Compiling string `{1}`\n',
                    dbg_comm, name))
            sys.stderr.write(sformat(
                    '{0}--------------------------------------------------\n',
                    dbg_comm))
        return self.compile_(string, name, for_, zipped, forced)
    # @:adhoc_run_time_section:@ on

    def compileFile(self, file_name, for_=None, zipped=True, forced=None): # |:mth:|
        # @:adhoc_run_time_section:@ off
        """Compile a file into adhoc output.

        Since a module that has RtAdHoc defined is already adhoc'ed,
        the run-time RtAdHoc method returns the file source as is.
        """
        # @:adhoc_run_time_section:@ on
        # @:adhoc_run_time_section:@ off
        if self.verbose:
            sys.stderr.write(sformat(
                '{0}--------------------------------------------------\n',
                dbg_comm))
            sys.stderr.write(
                sformat('{0}Compiling {1}\n',dbg_comm, file_name))
            sys.stderr.write(sformat(
                '{0}--------------------------------------------------\n',
                dbg_comm))
        # @:adhoc_run_time_section:@ on
        file_name, source = self.std_source_param(file_name, None)
        # @:adhoc_run_time_section:@ off
        source = self.compile_(source, file_name, for_, zipped, forced)
        # @:adhoc_run_time_section:@ on
        return source
    # @:adhoc_run_time_section:@ END

# (progn (forward-line -1) (insert "\n") (snip-insert-mode "py.s.class" t) (backward-symbol-tag 2 "fillme" "::"))

# --------------------------------------------------
# |||:sec:||| FUNCTIONS
# --------------------------------------------------

# (progn (forward-line 1) (snip-insert-mode "py.f.hl" t) (insert "\n"))
hlr = None
def hlcr(title=None, tag='|||' ':CHP:|||', rule_width=50, **kwargs): # ||:fnc:||
    comm = ((('dbg_comm' in globals()) and (globals()['dbg_comm'])) or ('# '))
    dstr = []
    dstr.append(''.join((comm, '-' * rule_width)))
    if title:
        dstr.append(sformat('{0}{2:^{1}} {3!s}',
                comm, ((('dbg_twid' in globals()) and (globals()['dbg_twid'])) or (9)),
                tag, title))
        dstr.append(''.join((comm, '-' * rule_width)))
    return '\n'.join(dstr)

def hlsr(title=None, tag='||' ':SEC:||', rule_width=35, **kwargs): # |:fnc:|
    return hlcr(title, tag, rule_width)

def hlssr(title=None, tag='|' ':INF:|', rule_width=20, **kwargs): # |:fnc:|
    return hlcr(title, tag, rule_width)

def hlc(*args, **kwargs):                                    # |:fnc:|
    for line in hlcr(*args, **kwargs).splitlines():
        printf(line, **kwargs)

def hls(*args, **kwargs):                                    # |:fnc:|
    for line in hlsr(*args, **kwargs).splitlines():
        printf(line, **kwargs)

def hlss(*args, **kwargs):                                   # |:fnc:|
    for line in hlssr(*args, **kwargs).splitlines():
        printf(line, **kwargs)

def hl(*args, **kwargs):                                     # |:fnc:|
    for line in hlr(*args, **kwargs).splitlines():
        printf(line, **kwargs)

def hl_lvl(level=0):                                         # |:fnc:|
    global hlr
    if level == 0:
        hlr = hlssr
    elif level == 1:
        hlr = hlsr
    else:
        hlr = hlcr

hl_lvl(0)

# (progn (forward-line 1) (snip-insert-mode "py.f.single.quote" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.f.remove.match" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.f.printenv" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.f.uname-s" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.f.printe" t) (insert "\n"))
def printe(*args, **kwargs):                               # ||:fnc:||
    kwargs['file'] = kwargs.get('file', sys.stderr)
    printf(*args, **kwargs)

# (progn (forward-line 1) (snip-insert-mode "py.f.dbg.squeeze" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.f.dbg.indent" t) (insert "\n"))

# (progn (forward-line -1) (insert "\n") (snip-insert-mode "py.s.func" t) (backward-symbol-tag 2 "fillme" "::"))

# --------------------------------------------------
# |||:sec:||| UTILTIES
# --------------------------------------------------

def adhoc_dump_list(list_, max_wid=None):                  # ||:fnc:||
    if max_wid is None:
        max_wid = 78
    for indx, elt in enumerate(list_):
        elt = str(elt)
        if len(elt) > max_wid:
            elt = elt[:max_wid-3] + ' ...'
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                dbg_comm, dbg_twid, dbg_fwid, ':DBG:', sformat('elt[{0}]', indx), repr(elt)))

def adhoc_dump_sections(sections, max_wid=None):           # ||:fnc:||
    if max_wid is None:
        max_wid = 78
    for indx, section in enumerate(sections):
        cut_section = list(section)
        if len(cut_section[1]) > max_wid:
            cut_section[1] = cut_section[1][:max_wid-3] + ' ...'
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                dbg_comm, dbg_twid, dbg_fwid, ':DBG:', sformat('section[{0}]', indx), strclean(cut_section)))

# @:adhoc_uncomment:@
# @:adhoc_template:@ -catch-stdout
def catch_stdout():                                        # ||:fnc:||
    """Install a string IO as `sys.stdout`.

    :returns: a state variable that is needed by
      :func:`restore_stdout` to retrieve the output as string.
    """
    output_sio = _AdHocStringIO()
    sv_stdout = sys.stdout
    sys.stdout = output_sio
    return (sv_stdout, output_sio)

def restore_stdout(state):                                 # ||:fnc:||
    """Restore capturing `sys.stdout` and get captured output.

    :returns: captured output as string.

    :param state: state variable obtained from :func:`catch_stdout`.
    """
    sys.stdout, output_sio = state
    output = output_sio.getvalue()
    output_sio.close()
    return output
# @:adhoc_template:@
# @:adhoc_uncomment:@

# @:adhoc_uncomment:@
# @:adhoc_template:@ -max-width-class
class mw_(object):
    mw = 0
    def __call__(self, col):
        if self.mw < len(col):
            self.mw = len(col)
        return col
class mwg_(object):
    def __init__(self, mwo):
        self.mwo = mwo
    def __call__(self):
        return self.mwo.mw
# mws = [mw_(), mw_()]
# mwg = [mwg_(mwo) for mwo in mws]
# @:adhoc_template:@
# @:adhoc_uncomment:@

# @:adhoc_template:@ -rst-to-ascii
RST_HEADER = '''\
.. -*- mode: rst; coding: utf-8 -*-
.. role:: mod(strong)
.. role:: func(strong)
.. role:: class(strong)
.. role:: attr(strong)
.. role:: meth(strong)

'''

RST_FOOTER = '''
.. :ide: COMPILE: render reST as HTML
.. . (let* ((fp (buffer-file-name)) (fn (file-name-nondirectory fp))) (save-match-data (if (string-match-t "[.][^.]*$" fn) (setq fn (replace-match "" nil t fn)))) (let ((args (concat " " fp " | ws_rst2html.py --traceback --cloak-email-addresses | tee " fn ".html "))) (save-buffer) (compile (concat "PATH=\\".:$PATH\\"; cat " args))))

.. 
.. Local Variables:
.. mode: rst
.. snip-mode: rst
.. truncate-lines: t
.. symbol-tag-symbol-regexp: "[-0-9A-Za-z_#]\\\\([-0-9A-Za-z_. ]*[-0-9A-Za-z_]\\\\|\\\\)"
.. symbol-tag-auto-comment-mode: nil
.. symbol-tag-srx-is-safe-with-nil-delimiters: nil
.. End:
'''

def rst_to_ascii(string, header_footer=False):             # ||:fnc:||
    '''Convert ReST documentation to ASCII.'''
    string = re.sub(
        '^\\s*[.][.]\\s*(note|warning|attention)::(?im)', '\\1:', string)
    string = re.sub(
        '^\\s*[.][.]\\s*automodule::[^\\n]*\\n(\\s[^\\n]+\\n)*\\n(?m)',
        '', string + '\n\n')
    string = re.sub('^\\s*[.][.]([^.][^\\n]*|)\\n(?m)', '', string)
    string = re.sub('\\\\\\*', '*', string)
    string = re.sub('^(\\s*)\\|(\\s|$)(?m)', '\\1', string)
    if header_footer:
        string = ''.join((RST_HEADER, string, RST_FOOTER))
    string = re.sub('\\n\\n\\n+', '\\n\\n', string)
    return string
# @:adhoc_template:@

# --------------------------------------------------
# |||:sec:||| SYMBOL-TAG TOOLS
# --------------------------------------------------

def compile_(files=None):                                  # ||:fnc:||
    '''Compile files or standard input.'''
    if files is None:
        files = []
    if len(files) == 0:
        files.append('-')
    compiled_files = []
    for file_ in files:
        sys_path = sys.path
        file_dir = os.path.abspath(os.path.dirname(file_))
        sys.path.insert(0, file_dir)
        ah = AdHoc()
        compiled = ah.compileFile(file_)
        compiled_files.append(compiled)
        sys.path = sys_path
    return ''.join(map(lambda c:
                       (((c.endswith('\n')) and (c)) or (''.join((c, '\n')))),
                       compiled_files))

# --------------------------------------------------
# |||:sec:||| TEST
# --------------------------------------------------

doc_index_rst_tag_symbols = ('adhoc_index_only',)

def tpl_hook_doc_index_rst(cls, section, tag, tag_arg):    # ||:fnc:||
    tag_sym_rx = '|'.join([re.escape(tag_sym) for tag_sym in doc_index_rst_tag_symbols])
    return cls.section_tag_remove(section, tag_sym_rx, is_re=True)

def tpl_hook_readme(cls, section, tag, tag_arg):           # ||:fnc:||
    section = section.replace('@@contents@@', 'contents::')
    tag_sym_rx = '|'.join([re.escape(tag_sym) for tag_sym in doc_index_rst_tag_symbols])
    return cls.remove_sections(section, tag_sym_rx, is_re=True)

def adhoc_rst_to_ascii(string):                            # ||:fnc:||
    '''Transform ReST documentation to ASCII.'''
    string = rst_to_ascii(string)
    string = string.replace('|@:|\\\\? ', '@:')
    string = string.replace('\\\\? |:@|', ':@')
    string = string.replace('|@:|', '`@:`')
    string = string.replace('|:@|', '`:@`')
    string = re.sub('^:[|]_?(adhoc[^|]*)_?[|]([^:]*):(?m)', '@:\\1:@\\2', string)
    string = re.sub('[|]_?(adhoc[^|]*)_?[|]', '@:\\1:@', string)
    return string

def inc_template_marker(cls, as_template=False):           # ||:fnc:||
    sv = AdHoc.inc_delimiters()
    template_tag = ''.join((
        '# ', AdHoc.section_tag('adhoc_template_v'),
        ' ', as_template, '\n'))
    AdHoc.reset_delimiters(sv)
    return template_tag

def get_readme(file_=None, source=None, as_template=False, transform=True): # ||:fnc:||
    file_, source = AdHoc.std_source_param(file_, source)

    template_name = 'doc/index.rst'
    tpl_hooks = AdHoc.template_process_hooks
    AdHoc.template_process_hooks = {template_name: tpl_hook_readme}
    template = AdHoc.get_named_template(template_name, file_, source)
    AdHoc.template_process_hooks = tpl_hooks

    template = template + '\n\n' + __doc__ + '\n'
    template = AdHoc.remove_sections(template, 'adhoc_index_only')

    if transform:
        template = adhoc_rst_to_ascii(template).strip() + '\n'
    if as_template:
        template_tag = inc_template_marker(AdHoc, as_template)
        output = []
        output.append(template_tag)
        output.append(RST_HEADER)
        output.append(template)
        output.append(RST_FOOTER)
        output.append(template_tag)
        template = ''.join(output)
    return template

# @:adhoc_import:@ !use_case_000_
RtAdHoc.import_('use_case_000_', file_='use_case_000_.py',
    mtime='2012-10-02T05:03:59', mode=int("100664", 8),
    zipped=True, flat=None, source64=
    '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'
    'BgRx3b34+QAA')
# @:adhoc_import:@
import use_case_000_ as use_case                           # @:adhoc:@

def get_use_cases(as_template=None):                       # ||:fnc:||
    output = []
    if as_template is not None:
        template_tag = inc_template_marker(AdHoc, as_template)
    else:
        template_tag = ''
    output.append(template_tag)
    import use_case_000_ as use_case
    state = catch_stdout()
    use_case.main('script --docu'.split())
    output.append(restore_stdout(state))
    # @:adhoc_import:@ !use_case_001_templates_
    RtAdHoc.import_('use_case_001_templates_', file_='use_case_001_templates_.py',
        mtime='2012-09-30T03:09:53', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        'H4sIAESf8WEC/+19/XfbRpLg73z3R7SlzQNgk7SoZHNzSOSx12tP/DaJ/Wxn5+XJDAyB'
        'kIQVCfAAUB+znv3br6q/0J8gKCnK3d5wJhbZH9XV1dVV1dXV3fuPnm6a+ulJUT7Ny0uy'
        'vmnPq3K0TyaPJySrFkV5FpNNezr5E6ZA+stqfVMXZ+ctCV9G5PBgdjgmf62Wp2dpeUY+'
        'ZOd5nddj8r1ImvIkkrbkbHU9XeTPRvsA5uN50ZDTYpkT+LtO65ZUp+TF4ocqm3b567o6'
        'q9MVFjmt85w01Wl7ldb5d+Sm2pAsLUmdL4qmrYuTTQuQWpKWi6dVTVaA+OkNgIGkTbmA'
        '5tvznLR5vWqwHfzxl59/IX/Jy7xOl+Td5mRZZOTHIsvLJicptIwpzXm+ICcIBiu8Rgw+'
        'cAzI6wrgpm1Rld+RvID8mlzmdQO/ydeiCQ5vTKoaYIRAAUC7JtUaq0WA6w1Zpm1X093z'
        'roMLUpQU8Hm1ht6cA0Do31WxXJKTnGya/HSzHBMoCVD++ubjD29/+Uhe/Pwr+euL9+9f'
        '/Pzx1++gLIzupiX5Zc4gFav1sgDA0Kc6LdsbQB0q//Tq/csfoMaLf3nz45uPvwL+5PWb'
        'jz+/+vCBvH77nrwg7168//jm5S8/vnhP3v3y/t3bD6+mhHzIc0FZgOGh7SkdHSDgIm/T'
        'YtmwPv8Kw9kAZssFOU8vcxjWLC8uAa8UeHB9s33MAEa6rIADsYdQtiPhlLw5JWXVjkkD'
        '+H1/3rbr+OnTq6ur6Vm5mVb12dMlA9E8fTYGMIDfVV0AN7XVrny9t7f3aQTDkGQp/HNw'
        'MEvaHOgLQ9wkU+jFhPwCFMBM8vmjyPnMUF5U2WaVly1lqelodEQ/hBw5PtBGepbHhPS0'
        'dfz23cc3b3/+MB9Bh+gHhrqCaeap09/g6C3l2WYkEwiZTDScWSPkjA4PkO+XD6+Sly+A'
        'Mdrr1uwdVhZNE+UjK5/gFGuyuli3RBRk1bJqtUapoX7SxXmVEZHDqk0piudjqHKeL9dq'
        'cZhQAPCGcQnNXOUNUnQ0+iufHzg12TRtxpTzOC6LKm/IFU48TNT736Q3wM2jt5t2DRAA'
        'NK2XrhjPb0qO3wJlFJE/BLbAO8B8z7/EmyxZ5JCanORn8ZdnKBAEpV5dt3WaYWMon+0P'
        'Ex9iSAnSUAiF4hSEJ6ACEh2QKov1Omc4Vig68us8o/IFUAMQfCamy4bmppcwUdOTJZ0S'
        'RVm0Rbos/gZiLZ+eTcfk/UsqxxshvbC/y2V1BZqDvKPaRFIvPy1KREyOKfn8+b+eTjfZ'
        'wcG0zj5/HgNti+wc5XYDSNHe5guKfcGJDzMZEKvzdHEDJUA0smZVwsEAMsKpiXm5wEQ3'
        '4bZ8oNKXL1/iJs9i+MslUEuF+i2AjdQRJkckHCFTBvvk+zggAeXlhHILslb87FMZiAJV'
        'V0AQUMsv+vKjkUogtd2h1YCEarVt2PR3J6J0QHY0yaCgU4DqxkrkGzdcF7o4kV5SLj+v'
        'rkrUmCnoR7QwGhIygMDo30RsygkcjL59P5zSAkdHx9rC7Fu7Be4dR9juu5xoKHSKEiUT'
        'kkLvPOC5G0vY7VRM6jlh78g3bX/bo1Wa1VUDEP+T1VCnUwC2qvJzbJQALNUS8NMsAbiq'
        'JeBnV0IwKysgfhn5EoD4ZeQznlCKsAS7lMRVSbBL6c2xBFbq76MRyFuySosyTOuzyyhm'
        'lYOA656a8gTqv6f5dQqEzp/qCo0L4KqGOrTu2bI6AcvrfUvtdJrEv0/loLAvI5oJYnuZ'
        '89bJMzJjGPAcTD2ezadNi1MTbaAwmJwHERpgzjzM7CDgZ10XZRsmCaCdJJGWVeftpi7J'
        'TG0xdIPNAr2qt/3F0IJtEBmYooJMwAIF8z/LgUqCbE27SFhiAlMnXUFnaFGjN4A8mxEB'
        '1X8w39hQNGFEBzGo28STr+OBH2l6HHF8rBIWmvk1mo4c05D90THMl01uN9WDt10YP/vM'
        'KKNLmlXVtCTLa1gmlMsbcgpGiLPOaV2tuAnITVyKNK7iVE41Pz7O7SHXz1WZm+Pi5QC7'
        'g2BYQX52jmbUClY/pE3P7PaaS5U/8hYk0bJYwYKkBv0VBqCZxiSInwGLWVVx+iZMyHcg'
        '0GC8BBmasP45R8+q3P2Y1jmIYBj1QJHLiIKiIoNbQNvo0J4PhyY6dga0KcG8Xkg1wft2'
        '1BUfCGoJZmkCo5HU+aq6zMOuEKB2/Fs8fwI4fqw3YPOGQbXrCOwEveiBLgDS9amYjcEE'
        'KvT1WNSqc52bwubSLmzJTc7mchbA7MRp0CtWeIthNOWJr+E/KdqEGIyGTaXMNZX8lBBo'
        'DO+aV9j/t5vBxT9m8NYZPGyO3W7g/Lz5wENX/bdghD9CHK7SddjcNGi45XXNmkaWgh9V'
        'DYZ4eVHiioj5jshnwKVpa2F4RkCdz7CSUdguvy7acMZ+88YO7sVJ8YG6XG7pobhl+27v'
        'Vec9YxKW+Ts/Uy9KkXFj7Y1wK9Glx+ckjnd16xSx6TOQRZV1FofAy9abEtJXefxcTaQS'
        'RE/i5aC5MxA0NM+3PyLqiMkePyeHB4eHk4PZ5PBbMvs2PpzF3xxMZ/88O/x2NuIWK7CU'
        '+FrJb3U+UuB1PhQVM7lCfk4mWQqqaQKcCZQatfUN01/UPM4+tLBWOnvzVpjI8jdYyQkd'
        'gn+5afPmzduxI0ukjPLrLIdxfENhvKIsT9uQjckG76c9NkPcbcqmiko0wkHu1oaTmB66'
        'Z8u0kauKsDr5jzxro5gM+bDZmS0bnJ20A1RlKabBEYiR50wzPeeCEyYzToeeUoz8HO9k'
        'XVdZ3jTJeVVdUA/J3zkJYSHf+foh43g+4jl0YbcoakgMEraITJKgq5bJ3ClLPQUY8BN1'
        'KftdgdhFq+81rOvykeC5v+Wlnva/N0XeyiRMuczrk6rJtbRFfrI50ysWZbbcLHCBDGKD'
        'oq5gXuagNNAnrfaW5uA+kpXDOnSV1gZy6CnhnW8oYySbtliqq1QsUTQsE0fesA657C6a'
        'ogQpV4IigjJjcpI2OavTiXxtstAOCrB7e6pioGz/M2hFg+kHYNODEdShLhYLU5wqkdbd'
        'ZJOFHHlnZzdlgZKVlwGOpGIw6OkpQhzeSSgNo7RMVyeLlFzH5Frmgkxvb9bIOfgn5GB1'
        '7CHtMl1ucgP3QiEcy6ceFOqe6EhCc8aiHT91E9mKi0A0Z2QkNuhdy2D1cF4tQoFKJNsa'
        '6wU2GZ/joqRSkJLHxbWsxnMVkORyLunSMzBjVifVMqlq0HhgMkkRM4a2IOmITg8m3UB4'
        'xaclGBayM8vFcoXmoKx1fDDvemplzuYjbQAAvk5TDq/Op6DWUxhTTDCIahaptSKcvEEw'
        '/Y+qKEMKAIipdZLWEOShwtygDq4gmvUSbDKQ1HSyUJJDsoMqimg3qFOccoay+gmQtD7A'
        'b6ULFcvjpkMo+xL8dvzbp3L+OAw4LkHEEv4JbMkxVvlJJUSzWbadpKTkTZuW++EPZCLr'
        'HSRBX6eLnFpJwsVnyCy2a48OPGjrFEwsHNawrgSJjBlCDT10qVVsVR0eGN5Cignkwhcz'
        'j6E/TddrzAwpvUUzx6IfMQU7j3qrsuUer0krxJD+ZGZWU4hD80e7oaKC40zIKvbwGZuF'
        '67Ru8gTtAMZuMLRnoM4wQefcI3S5jCmjZcuVwmjWp5tzvI7CtQz1dcLtGVog0nzyip3h'
        '9PNodghyjWHDqLBU/D3QeqSEQAh6a/tXVMhH3YyHdT6u/ZYrkEUwRWDJHw1xUveA+/Sp'
        'saFQiqoWUP+MN8B3U1/NUHQm+jCuOXk7Yd1hhTJAl2pBRKWALcERww7yikuXJk/r7Dxk'
        'DWlMF6ndWVXGZgsTXTBpz+pqsxaLVjddeWG+bySEzZr1TBFr08dMolFMAiD3Y5XamAFL'
        'Z4725iQUQKBsoGM+pVmh1gON2y0xrEOmbe9TdDhozLcmdrim4ldm+2e44Vyg89uYLXyG'
        '2kY+n5mO+S7LJKjckZ9CxzQcU+ax4WrUMZcfzilqr1EMDFS1L8huL1q8TmPnAsdsQhEL'
        'kDO8ASdwn8TagYxyM9tDJdeQWpxkdLKHkyxHFeUlo765CrVZZ7cODkcPlmcGcgNWxB16'
        'HUsCnNOibtrO5kfpT8IwRMmKlhu11EEURnQFEzJJT54QZtWpgFA57wKHATmeaLZBtcH+'
        'a2Q5DiWavHkQvKJBmmJZF9Z2JTSJLYIt5Zy7IzLw45njc5PTWDmNgx6bXeuTZMK1zk1i'
        'TfX02sQ6/ynY+NYgThalTfRLWkaDnVC8NX42xQegiPoCO9bsuqwwUbQte2QnjhOyFKLY'
        'LWLshuzVMK8MrOxa5aoGsCgJLL6zwYs4YXBQgRD6qTAm53m6QHJJqtikKMpE9Fp1H+Hn'
        'pFrcJCzeS6MUL2+kKkaEbrD8roTV0GehESLBKqtj2A2CYwe2bItyY4UodLCdERqC2u6I'
        'DEE1uQrSFykdS9hSz21uu4C6OMsPoRvgAZzZFZbYNtscALzYPbCpq3Vu2+szwm6lg2/1'
        'aUA/5H4oXWMOW15qndu61uxdS1rCVFnqetFwK4BB+pBTTMdJ+zVEwyVsEfEHEssYth5S'
        'uXocoVQYpCj/32MLh959AM5QSfaHM4c9fvfLH22dlg2ovZVqq8jEThJuWWj0+VcM0lhL'
        '3t/FGeUym3rsh17FPzIHDgnSZzPadqLbYDhZVid+9X6P5gRvSI5riAl9flQ9XzqNhReH'
        'FbZ1FC03iNt0fdvLcAM8oKTP/r8tTwhVvIOJ6OUUdb3iQPWP5o8tBqNBDUTLWcZpjFL3'
        'TR90BDdW4ets6rKJ3EzrLvcgjK2EomFMk25FGvtRtMRim1R0rX+cu2iSWp3vAzsZS/+p'
        'u3WdELbR7QWL/8o4MCfwyKXITEXjmPJOZbabv0KEAvbQf2eyeymhSIUH66hqD9yO1/7B'
        'WoLiPof5UOrvwGl/JGPt3k0WTudZE+/Wxx11LmtZ27H+/1XhdttV5jqALUpsE04BzivH'
        'XpNJEhpPU1k7X8M8OhqcyTfDzgYpVGLHExfWRp1WmoL/nhz4UaD7i+4ICtzZg/89JuGE'
        'QYrs0AmPrVxfsz3CwJRnDtuG4vhsJxwRtZ3woN1gTfVh5JhAD2YEgYg+Web3IjY4KCs4'
        '5rfwmHxqP9Xzx1G4T/4cWVQUOGyQdsGnT7Ngm7gF+3IZk1C2SMndgeHExlJblI/s9zDB'
        'zAUwDza+hpl9kmTneXbh6PL88adW76ustigahire6pH3cpmss4JJyGW8v8UoPP6N0vpT'
        'Of/yT13r/vEXqHT2O+MARhfFd8pNLc/qjodVOIWj2JK3YCrHM/Dkklycq4QVURC8siH7'
        '90FonrALFPJL49ghB8mDV+1pviyaNnQeE/CvWcNgnyzamDZGmwa9jzRe1xJBDI/AkwPO'
        'QMNw5Noc9PAFZWonLoBFIMdoWvOQiog8oW3b+DsI3rGTvVRmAWQaZib3dbFl7oGRoF1h'
        'KJqecCocugOsoAhI4QHlLgWPKWOK0BBuKa51kn2xl7kSw0MHFB+ZpMCv8/RipN1vopNL'
        'n6ZafUXnYaxQVwdY6AvOZAwcjNTIwZFt1WBkHj8Lh2znDKxQrKN4othHiy7f2KhkHODo'
        'zp3HHfSUln1osQWzwigYEfCLlRyH/JY5XkF0skzLC7qYbNh3+yiToBVXpZRSAywfWS+/'
        'bumWmhyefTbtm1bMdiv+SAzuopMLxizsFcf3Y8b3KbyRKYUsTTBEE3oCYXCVdS99SM8h'
        'Hw+W4xqV/kDQC+fW3J3XFb4QZQWJ3pBtKhkTdtZIHP7cGmLjDEpmlXWOzAHtJqenNXQ7'
        'ESdshvPVVUs6CmTIfIaBMK1HYi7bpLO0UrCjYpKCJe9xHZ7XaukYE8J0l/1lR3NatGZv'
        'a+kWacwqMVPpeL4zyQA3pNXs8H96aMUUIZcpiF2YOTbX0QwhR0dUTrjhyIF9cmQcelZg'
        'dKN/RA79axY/BQQz0986mkbAaTA5fjyfTB/zQ3MYcAnK6DsaYxtNH9NcPMCtA7IHmYLV'
        'rmJwRKuyRgbHq8ri/AyLJexofp+A1cLnmWTaOlP99q6DfRSxu8kweM2OPZZzkdUf88Ls'
        'DAu77SVt0ratZYGA4W0peHEBCPvCDwfQcDWXMLKXh+xekb7l4QORC9iTtRVap5N08TWc'
        'ZAzeNpLxVu+PZHjlmUYwfqcMGxsW6x1vJ5nE05xBSEgKEq1i9gXFyyQwl0bsTrevkTAg'
        'xE82p6f0FkRxCSfKwJOiTOsbdt/U1DTEJEHZ+qiAlVvAoLiuXOjoKopPWeEpEiQcFOBv'
        'gzDquvzSNw5ApwCkArkcctoH9YnjiHvX3qkLSQZpmi1h+Wjiz8+6vnWchuts6MUGb00t'
        'aXfYL1iO4lEz77U6uPRhJb0SXmV1VnSMB0LZlR1B1FuPlZ+K0sg39FvU4ysEjBzNifOn'
        '/SG0Nq5TWRXAMPoHUU/z2jCZIKaea5H8ClGaVu5IhTotmlyMasjxYxMOb5Glw/o5gGU2'
        '3hXAKIdr7s+6sGIT3asUjANcxh0hQ6WMdpeCKmaE+FvhOXge5rJCwePdK8slgRE9XeKb'
        '6A2XP7YAqegdHz0SRBYTkoN2MsyH32PllAYG7B6gytT+CHrFM7md8ExwNn62ULoyhRJI'
        'mx7sPLKIGlULytE4NO7zGxVqNygm2sYaNhhkmX44/AD/Im1zLOy0doGJ5MldCtIzv72D'
        'RXk8xfs6VvS+L4QxZXtHwdQjcviw/TuK155xE6AFWG8h2vKB26tEycS3eNp6jT9Dhm/w'
        '1a+Tr1aTrxYfv/oh/uqn+KsPHnQZDDD4BSWn+M8iX7ZpuCrwEhqQEuWiOcKtnlXjXlco'
        'VhGFN+6giS8+0jd8F4nTtq1PaS/2vmr2dgoQbhsvJYHlNhQoZ7kQY2vbpvdYL7PArrGG'
        'JtSuF0WteaC3mptYwy3kr9k1CVTWdRcnOCWc425AQkWdWtovArkspwVGJhQgD16UgFf2'
        'gZrcNLnQKCpsUQhdM03o0tWUVuTIaMQeMFFOQKRrQSQFp3HXrFkSWsa/IU13Ykev9214'
        'AdMKXVSUntVlXrPruukdxKboCdXhoNc+4IEfxX8fdcf/MZVeUrGLT5+4Pel7+9DfmOyx'
        '9URCLzdC22QvxpvWS1xrUnJ83hO86Abzmd1x3ExJc1Gs11hvOp1+Kvc8GwGaUc85UpAT'
        'ftEYEZvglJAG0aG0QXMosUovcsjg2aZxQQH3zMJ1CpOwm4PCovgbXka98CxgXLOQ6Qq8'
        'WuPbb8bkDOqrnWHgDB1ZoM9AuxPG0HZnf0M1irCmf4F/XrPNY6ZMx+R/jRGEVYNrVa95'
        'Y1dwKdpuuVBUeBMWNeXNMpBl1nWYAsMNLlmUkXF68u03fMXqLan7AoK0yYoi2N3C3JRO'
        'PsChVDjBXNfuxgYGztA/4QQwsXbQgXfQYaIOZS2XleVlsNrHYBI1ZBzHOtLLTw5e8Swf'
        'NIa5nwUEH142tGAOUtHH1wtU0om1g7KOkIP7JU7XBbCGI75XrjUMNsHriMRBaj7YZiy5'
        '0DydL4ZZAtwIMDS2RrRr8UKJY1FHCTIasi2865Zw2KM+GH1REXS6A/SEoRK0gVVnnDXZ'
        '2B853diWiXZoWFsSUoIYq0Fh9vfEyglzlh1dxquqxEYK7gilbbKL5LdWCcqa0LJU0R/A'
        'W7dcdjwdzSarnjTBe+Qtx8cyU1XA4giyo8+xw3iw8Agfhxo6oZN6xwfxt/MocsXpMEzc'
        '1fri/mjf/q+ax97hV4ZBue2CusnYDGA/kgaIsg5FZ/R9b7lItWe6WJjZPIL3z+EXWC2t'
        '1upFNjav7HNKHR7MZhP4/+HXH2d/ig++iQ+/PZ4ezv70zwffzgeQZLuTcugKd8DKtndF'
        '61jJ3mUFu/vK9d6Encoz8uCw4BIX+TAvOy+WC16O1jlWQyAghcd2TPn+WFcOYyWUSwaW'
        'i0TQzXJE6pTfztJSIXC5LMW05pbh1/IzHCM7WBFgSv8a9y8fs8Lzcdf3McfHmEbOLpBH'
        'R11HB9usHr+sycZ5Fir9ZDUWBSjzXvmm0U8IOUi5BxGn9Mt2lHajidyxwkgvRdvi9ZIv'
        'gPbD7pRU1GRj4LEGSCNLQt6s86bz5oxJ1fRsIgq3PK01/Yn++mjfhid4T/Kvw4vICnhv'
        'gVFACFtnu5xTIfPHBRSGdbuVkoSrtUTRAg5s2DRT+V8Un7tkaKhcTjom/5bf0G+R180J'
        'f/ytQua0zK8SltCDpxM9exRcG+jGiEkLc6hGRM8KczgpXl3bU1cruyKilPNWdfoSXXla'
        'YcFVWl/gS1QN3r+CrLoY+Tyl2xTybIhv39c6WPI3d0fhQBePSIW+bS8dPfaoxRGVCOYi'
        'j8toB5Axq+cuT7NocS4AsbwlyGUPUT66Hr5YUTGds5C7Re7boXFsJMYezk/4Is3YS/RM'
        'e1FBCVOcrm+cTwX4mqC/9MBF3QeZZniXbqiURoE5fZ+8/TdPMxi9xRxu+E2t2eOt52Tc'
        'xkj+49XQFLTHdGvk675oRpZ2jFqHjldS32GyDOyncRsk5depNJAEIFcZ3Kw6kn3tkX9i'
        'Wpn2hTZT2RYGGEcKBubrP57ZLFjdvhLGkpmuG9FaDzzLo+5kV24ASka1bIVes8XgYE+D'
        '9sD8ntyrDa+XfxViqKg9Iw6b0+ZoKhmqEuNkL+j45Ff0zdiUvZLK3jDC1xr7IwN6tx6Z'
        '5bnUxLAIVfBW4hbGCxFes2UPUpp+W4MeqEi/C8ObXXBcgGQpfxtx1pjhrx31M5t7PWpJ'
        'Aa/iNTEfEPkjdte2aSfznS+2Ejbe+NIKRbcgiTA7da4YiwgTh3bSlwPcOcQNxT63nYF5'
        't3eq+SWsGBCHlFGln80Kgr4WYUW1LYpe1Kd/daW+JTZHGyo1xs6QfSIA3xi8nhBH7c00'
        'LVa9rHjAuTh6Dgk8TL4nZl27rjmrlst03XRvAhkXNnOWly3Fjih22Wk9rF5e564+hxFE'
        'o9tUZgueW1ZmrpxbVpZvIlwGLqpwcveQxTzBaMDnAMxIG+1KbfPQhQGCtRDcatAcZ/+d'
        '40Zf5PEM5NCznGwctk3+rd77u8hGXkZQciy2mXrvVHPMc/vghsFrSpOXifFehBlLoO2S'
        'GGW14wYc2QwfolWuP9b3dgLhulSRYC9Hq11FP4fReZ1NjOLdDcd4m/UTfr+xXigaBMBS'
        'KngrfTh/HP65iTqQ2Ml++E4Fu88fVWFkBu5RadamF3lDMjyOSR+CLxpHeF2ehXqr0yU/'
        'wDjuXp0ck2WV0W/uwFt6EIs+QeQxtMwdvHDv0aNHVj0Cibgj18chBn/1ahJabLcJ6L4A'
        'mE9lzyxTsZSvxYRGACjTa/xu8a3q7/43kO6yg3Rf26L9xoyxM0xLYniBEouDP6nQtmOz'
        'ZHHtQcKEPmWTJGD8mLZP0YhnbjSh49iulAWVl2/4bsXWPQ/eAXbt5royrlqnyZaXEb0f'
        'egwSFXyPaenIOiloPulz3IGYb++d1l4QGNfZILyh+HU57AEfL6byiaE+THXfk7chOeyK'
        'G05pytji4O4oZfud8f+AGakHX+n7RR0gf1h3xh+AQuTwq8a7mOU28HklrYYAgYa7AYnG'
        'SkKauYnKxRM+wMn6A0v2OsdHqm90dd9J1/64TFPuqaXF21i+wn0rORumjtLIYZ0o9g3f'
        'pxhu3wywcYQxHvVswGmLFmGpGNhZupPW2WbdCIUQRIajeVB4jhgKK7hcRuj4fQw7BbF4'
        'Is+91z3cJr5Hi/NZu+J8RI/Z0ZD+IFEtXHTTiNAgZVjGMj7IOq2q8xkalwbnuX3ABZpj'
        'y2VjvhCeeLa8tpijeqFoMBD3LRaaWaqSYWs7Xv+dZZ6qTD/APJUmqo7BAMt0J+v0Dhaq'
        'P7T7H/Py95+XDo3IVOU2df7HrsovuU7h9Thza73habp+UbZazHMLPsvYZQtxtFi/2b+G'
        'oT7YDBhsArAXYBP2vpFH0RrPxQaRWbtH5zqdFp3DkC11FH+h/saTC77jcWWtEWVJNtYB'
        '0Iuuj7oegwA9K6sanY71hdEy3iWg1jUumfDIkgA6zvzduK4xZUh+CxmSMxmi4RKNBltl'
        'mm7EFRc971M61yex64oZ5/JAQJrHf4gcy+ocI/mUNSR2CYWRQMwRQiwRLOUBQ23x4r67'
        'Qps0Knx9BYsHKwJnW1xpBZ5cM7BdFzFSIPXd1LBZre/fLXGXsNYHihzHjj9U3PjQ0wJ0'
        'MHhUOH6VdhH9hZFnDkXmPJgnK3gui5fZR8behLnqVPHwXCkx0qCaC5+A0Y3eJhSY4xBM'
        'Gf+pqzC1RY+BrBbZVnHkN4Ylvr0QMXgSH02WHQnwGtq/+5/1tazjji5bbGNqE6uouJ22'
        'Ei3r6eB+m/iWtrB4ok20etxRYr6NmbtzTSt8jt1rmzHduv1dT/f19Xex2tiVsO5p4jFr'
        'QnXGfOE7JmuM9UCucj02KVE33WGWp0Md/R32cVwP5Rg4OGenczqaWy7axCpKHUeLYsrr'
        'TGpB82lEY7ZqRY0gtG33/Trf7KTqkNpWlPPQn4t/TSNFwH7E8+X5V/pLczpPXPF0ehOd'
        '1MO7m2hqFN2hyUe7NPloeJPxsNeybi2KB4rjW4jk4Vtmg6XuDpL3YbfLaH0a0UD7Yby5'
        'GTz/EuMgxF+eceuQFb0G4WsW/V4Ufa4Wxbz//Hv/ohp4UwRVaJ5yFa3lSliJCgI80Xen'
        'vl7fc9JIL8NPerjoYUMWSPRBlmVUyAb5zEMDtf4yDqvDDpuw75RmjXIlO6PeFKCtrBuJ'
        'WJVOzXTP5tiABR2sVb0GyPVach8sW091JTTpQi/jlM1YN3Ia42W+bMyuWVUhsHeLWboD'
        'VJaIN5M1BIxnoNnXrt3A5EFBLDDuqW2vN3K9cyNydHdrCQup7dgxwbQtexnTdW08vM51'
        'HyzZg+EVzcsVjBvbtWF33d0u7TJ+YztSwzbEhi6SztOGdWKR94mmHaTQvcsKyVh34qQO'
        'XJ5k1YYeoMOTasIkZG9dyF7TNu0zr7LyM3LQQ9UUtN4lBoj9fsL+/kVy52NyMYWbH6K4'
        'd79P0Xfu3lvwFO+qtFDV54VJ6K2gB1saAXzigkVLxnkAOF5gccLoGE/3G1kPazeXu09O'
        'MxBzwMQkD80zd+OXXQf51uNkjPXtGMY12Pc64LjMlsGl28Oixx6Xlev0gHQIaO9S4TR8'
        'MAdAt5Y3V1SIRux6nNi/DxLKDYfkMvrzF+4+YL6UznFgXJLtP6nX25bWlA+2Ri5TAXjU'
        'sxn/pjz53MMluOnShdBtZ5BBXOJmEE9hdatmMCep3VO4yuD3kffIg+6XwfY8xLeiq/W5'
        'vCn5k6U+2W8+S2XUZ9lBTwCx7NJdXE9H/Q4oyQBs2akuo8zmce1kodTnaTILm96mzg9h'
        'lbSdTeMej5P10qzzZQXvI1MdYPV+O8NLI97ykmxWV3iYLTmvqovGdUZO9M1f65jDnhsP'
        'z6i9tZ8O6ebMLXvCT6LLkXeAEVkSQ7xH/pgjOKfIzYdIQwsOsIDxILom820BLh9kQyd3'
        'eByCqSdjvlqABku7lj7tzlb+8Evrm1jhz/uiSBxtaE0Mh83lMQPY97Cs4Ae6efa7it4/'
        'WKKq8kXs9Hvjtk0wRzosJ4N0w8G8/TB+F5RHxuSSjxz8vuw2yNs67TCYR25OoOPSgCmQ'
        'L2y/AG3hErlOA28zhq33LvKbI37d0kUbk+DLF6/3gRZH3nZrzzCkLwWFF8iipkscD0La'
        'GY8C1+Y5P9FXLjgsXxG8lZIWOJ7FeI+TCstxObk5LDDU+HaOfW8lo0YL0yImIf6BLtM7'
        'RXWjKdgSwIQKy1sZT1iNR+5IAI0fotvwQ9dXGF50Sd912LuxdQ/srqMaRWL07KEbKrJg'
        'EckEQYLxDZua7iBue+PFFlmrK1QlB2Oyt4f/KS8y0fdKMfa7WkZD75Zh8CtDJC4z4ZSp'
        'lvZNz1fAwuR7KOS45oHmQd3MlYWcRfbgf489BQ5pgSNHAflEx1LrLwrDMNr5Ih2zv8Kp'
        'dGUtFAH+mLbCBrZtk4KePe5eMYUkbsZ2RxIgbV3np8W1ltRsTmXSAM3WovE8ULVtXXo6'
        'VdvDqTPDZl6fCne+pFRnxKt5jGSdQwcI3WVysmtOEEgyH32hVbqtYfhNHwk1pjxDySgG'
        'iVFkOlkYD9itoKhQne5r+oQGkVc69D9NI+pvC5HcJ+/QVieUOzojAX/pTxW16yUajOIS'
        'oFCoiVgKR6dsdIhGJgSFDBQiUBkULtewfX5s2RB0TM0XqOPrtDzLw6+juY67sGlDWRn1'
        '5ME8DF4y0mA4WZc3Y3kfhWrTMg955s061yQ7a4i/x3as0d9u1qtegCccipAhiYw1mYh5'
        'QhyvKaqjwmxjx75E9yqjAcAigF8Jsj2f1lwxDm/hcFsL1LLC6bqlgcg6j9Baa0FqHQyS'
        'IfNB87FwTAj84Bqe7R4zZsAzbsZlNLiRLoLIrCuRQF633kz6MFi1bCib55fQDtg6tB1H'
        'uIPaDFYCesuX0IO9iMYhOAPiOxR6Y2at0o+OujZ7nmzRZ6MpNmOkNHmyP3lCX5YMGJrR'
        'bcFNkUclipAQRreE21NnUJeCMRuFmTIK+wiRRl/EQdSLlt4EAhqARg88lc3koI1uxwj3'
        'NKL3OZJycvLpOLdzhZhmzarq7wNe5shBVJt2vWkV0xhUdrrgr7zpMn02DyP4q+oJkare'
        '1Lm6mkkYMx3IzAlk5gRyKIEc6kAOnUAOHUCafI3mBOGEPs7WrAzYyFTQrKkQFSDU1tML'
        'fNb6Ksm6m4nhZ+zZp5epHOHjGC9fDVdXE1wAQEW6on16CItxwn7JvkXRcby6MpbXAQnG'
        'FtCZhDqTYGcCbM+6lJXrRoS1OBvS5KFs8lA2eTiwycOuyUPWJEpnodFsUvsILb8MIVzf'
        'R++hQRU3UbaCEwSRHVMm2V/yMq/RhNHNTDbfdLXK0jqf5DryZHV8GarKNzL2rKwLW3oa'
        'ULKFWSdaQSIxsxPHB51LCHkeDcGbL/64dOnf/zEO3dDlmue0gbZyu8tmobXrox808N/D'
        'ytcCqmv7YRd+/c7MYYDFfoxKBeW7s10WXMq7j380I7LLND37MoiV3ZjQFzarNaFHzNKr'
        'XaM7N/loYJOPtjXp37tQtpFaZVepOe5qzwf4LHn14yCwrmoK5hYz6NtX2pKlc4ZwY0gt'
        'p9//1WHYTzSlVXp/Ez2cIhLHeouWSBC52y9y2W1jeIg0GCoM+tQAv9flwbw/Dzrzf5dr'
        'nVCDgCI47TiDPf1MHdnWhoV9PyLW3R5vj6Xce44sh2ZRycBGcGCku+90N+uQ902Uu5/u'
        'FoTZ7XIkxVVOYzDp+zlNvjzl04fffl/VifMUXgUILNSIvVV7bh6CZiC6excBuCekhpWk'
        '0DzhQ/vkeew8Cxw/V/PYLW/bkvog7AZd3HqHaWjJteL+BoLXtfKLcdEu4qdyoRiPAq+a'
        '7ntzgz+qJkFvJPNLwsjgDyxzSoJ3Lz7+EOBcqDDQ47Ko8STdPuNmtRbPO2YV5lAEQIt8'
        'PDrAYYqvwpLjQPg1RdwtimZaBIXpWYl9NYJddIWOdNdPnsv6n8qrLEb78nhDd6u7gKgA'
        'V0PkO3JJjsJ2RLoo17WgHqKwW2F3MjWN0nVGkIQTxB5PTPwSb7KEPqDQFgnM4/jLMysZ'
        'yMeSi1iNlImfIQRQVylZ19UZcPoIBlKck6JCJgFBWpRJwh8jTJtEXlnf7XhgEXpWNa3P'
        'LiMulWCMDqJRZxKoValA5TEkMp0VY3eWwoAamJLJN5g82fkjibHIm6xOTvIzRgrmNqjw'
        'nlCwgICVU9yXZC8q40lyeuZ4gfycdpJ+kYOGr+kZlhjGzYBtUJ8lctpD6kbv0nPskjlS'
        'HD0qW7JEyh1UBf/1dLrJDg6mdcZ0QgdQoAcgu0K8zOTxhL9jHxP6FjqmCLmKXU5ol7EB'
        'nsCgpzA253nd5dKf/pZ350WTHPc7vGInQJhfGDm0ogekcANijLc8t90l0J8/d4T7LJ5f'
        'HDPBhoXwRc2gIeeUVcTVU6gJUdfRybgjN8gYW3GVjgi+MmJ5/dn0wNOGnXfC4059rCSg'
        '0IcuVYOmu8jHtFHFnbzRrgO7He3m8n6H+n2eLowRHNPIlsu0WOLgjKlIAvbGILrLtC4w'
        'sdl9Am+bqu6HWNV5zCwH7WAfZEvrQ5BNvZGYV/eduacn+iSMnlN8vlfmu0ui1zX6xwJN'
        'LsQEXyjXkiK1sCYmWGEtKfJxj5d9bskZrUOzMVf2y7c/vXvz46uYvN+UBE1uaIDbk1Bm'
        'SkLUfSUJm/Qyn7C3wiP00NIS+KXMQFTs8d3b6dM9Fhw8wfGclFXZyYOQ1Z7I7Cgie11r'
        '7C6uAWiRZ8A4SZbCPwcHs25STtc3D4txDyLbOyOXxg+DsmhuO2ILaow9BE7Q0iB0yBfQ'
        'KqenD4cVNBhS3ZY3LZnUBAXn7DtUdSXJs/OKBP/65vXr4DuKFplsWAEy+Y76eHiRDx/f'
        'vn8FZRCfZxzCaRFt7/F5vlw/UF+xqW0IMfBf747R17uj1IfL04qAAd08BGV0NJ5M9p/Q'
        'Vl8K+Jj5PyDpR1Qh5N+lysTlAr4ny2kGP3nMzYR6NGKyt79nJk7wEWvMeaJmZdVysypj'
        'ckAXbxvsTj6hR/1i0kLaK1AHo/8D6Qb8f6baAAA=')
    # @:adhoc_import:@
    import use_case_001_templates_ as use_case             # @:adhoc:@
    state = catch_stdout()
    use_case.main('script --docu'.split())
    output.append(restore_stdout(state))
    # @:adhoc_import:@ !use_case_002_include_
    RtAdHoc.import_('use_case_002_include_', file_='use_case_002_include_.py',
        mtime='2012-09-30T03:09:58', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        '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')
    # @:adhoc_import:@
    import use_case_002_include_ as use_case               # @:adhoc:@
    state = catch_stdout()
    use_case.main('script --docu'.split())
    output.append(restore_stdout(state))
    # @:adhoc_import:@ !use_case_003_import_
    RtAdHoc.import_('use_case_003_import_', file_='use_case_003_import_.py',
        mtime='2012-09-30T05:38:54', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        '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'
        'VMf3G+cAAA==')
    # @:adhoc_import:@
    import use_case_003_import_ as use_case                # @:adhoc:@
    state = catch_stdout()
    use_case.main('script --docu'.split())
    output.append(restore_stdout(state))
    # @:adhoc_import:@ !use_case_005_nested_
    RtAdHoc.import_('use_case_005_nested_', file_='use_case_005_nested_.py',
        mtime='2012-09-30T03:21:59', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        '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'
        'AYrLH8ec8QAA')
    # @:adhoc_import:@
    import use_case_005_nested_ as use_case                # @:adhoc:@
    state = catch_stdout()
    use_case.main('script --docu'.split())
    output.append(restore_stdout(state))
    output.append(template_tag)
    output = ''.join(output)
    return output

# --------------------------------------------------
# |||:sec:||| TEST
# --------------------------------------------------

def adhoc_run_time_module():         # ||:fnc:|| |:todo:| experimental
    import imp
    if 'adhoc.rt' in sys.modules:
        return

    file_ = __file__
    source = None
    exec_ = False
    if file_.endswith('.pyc'):
        file_ = file_[:-1]
    if 'adhoc' in sys.modules:
        adhoc = sys.modules['adhoc']
    else:
        adhoc = imp.new_module('adhoc')
        setattr(adhoc, '__file__', file_)
        sys.modules['adhoc'] = adhoc
        exec_ = True

    if not hasattr(adhoc, '__adhoc__'):
        __adhoc__ = {}
        adhoc.__adhoc__ = __adhoc__

    if 'source' not in adhoc.__adhoc__:
        adhoc.__adhoc__['source'] = AdHoc.read_source(file_)
    if exec_:
        source = AdHoc.encode_source(adhoc.__adhoc__['source'])
        exec(source, adhoc)

    RT = imp.new_module('adhoc.rt')
    setattr(adhoc, 'rt', RT)

# @:adhoc_import:@ !adhoc_test
RtAdHoc.import_('adhoc_test', file_='adhoc_test/__init__.py',
    mtime='2012-09-18T09:26:21', mode=int("100664", 8),
    zipped=True, flat=None, source64=
    'H4sIAESf8WEC/1NW0NXSVUjOT8nMS7dSKC1J07UAiXBxObp4+DvHh7gGh8R7+gb4B4W4uijY'
    'KoQUlaZyAQBLQbhtNAAAAA==')
# @:adhoc_import:@
# @:adhoc_import:@ !adhoc_test.sub
RtAdHoc.import_('adhoc_test.sub', file_='adhoc_test/sub/__init__.py',
    mtime='2012-09-18T09:26:21', mode=int("100664", 8),
    zipped=True, flat=None, source64=
    'H4sIAESf8WEC/1NW0NXSVUjOT8nMS7dSKC1J07UAiXBxObp4+DvHh7gGh8QHhzrFe/oG+AeF'
    'uLoo2CqEFJWmcgEAQobQsjgAAAA=')
# @:adhoc_import:@
import adhoc_test.sub                                # @:adhoc:@ force

def adhoc_check_modules():                                 # ||:fnc:||

    hl_lvl(0)
    hlc('adhoc_check_modules')

    printf(sformat('{0}--------------------------------------------------',
                   dbg_comm))
    msg = ((('adhoc_test' in sys.modules) and ('SEEN')) or ('NOT SEEN'))
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'PRE  sub import', 'adhoc_test ' + msg))
    msg = ((('adhoc_test' in sys.modules) and ('SEEN')) or ('NOT SEEN'))
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'POST sub import', 'adhoc_test ' + msg))

    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'dir(adhoc_test.sub)', dir(adhoc_test.sub)))
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'adhoc_test.sub.__file__', adhoc_test.sub.__file__))
    if 'adhoc_test' in sys.modules:
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                       dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                       'dir(adhoc_test)[auto]', dir(adhoc_test)))

    printf(sformat('{0}--------------------------------------------------',
                   dbg_comm))
    import adhoc_test                                      # @:adhoc:@
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'dir(adhoc_test)', dir(adhoc_test)))
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'adhoc_test.__file__', adhoc_test.__file__))
    if hasattr(adhoc_test, '__path__'):
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                       dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                       'adhoc_test.__path__', adhoc_test.__path__))

def adhoc_check_module_setup():                            # ||:fnc:||
    '''

    >>> state = catch_stdout()
    >>> adhoc_check_module_setup()
    >>> contents = restore_stdout(state)
    >>> contents = re.sub('(mtime.*\\])[^[]*(\\[)', r'\\1\\2', contents)
    >>> contents = re.sub(' at 0x([0-9a-f]+)', '', contents)
    >>> contents = re.sub(r'adhoc\\.pyc', 'adhoc.py', contents)
    >>> contents = '\\n'.join([l.strip() for l in contents.splitlines()])

    .. >>> ign = open('adhoc_check_module_setup.t', 'w').write(
    .. ...     re.sub('^(?m)', '    ', contents)
    .. ...     .replace('\\\\', '\\\\\\\\') + '\\n')

    .. @:adhoc_expected:@ adhoc_check_module_setup.e

    >>> printf(contents, end='') #doctest: +ELLIPSIS
    # --------------------------------------------------
    # |||:CHP:||| adhoc_check_module_setup
    # --------------------------------------------------
    # -----------------------------------
    # ||:SEC:|| no:module:found
    # -----------------------------------
    #   :DBG:   module                 : ]['__adhoc__', '__doc__', '__name__'...][
    # ------------------------------
    #   :DBG:   __adhoc__              : ]...
    #   :DBG:   __doc__                : ]None[
    ...
    # --------------------
    #  |:INF:|  no:module:found.__adhoc__
    # --------------------
    #   :DBG:   __adhoc__              : ]...
    # ------------------------------
    #   :DBG:   __module__             : ]<module 'no:module:found' (built-in)>[
    #   :DBG:   mode                   : ]...[
    #   :DBG:   mtime                  : ][
    # -----------------------------------
    # ||:SEC:|| adhoc_test.sub
    # -----------------------------------
    #   :DBG:   module                 : ]['ADHOC_TEST_SUB_IMPORTED',...
    # ------------------------------
    #   :DBG:   ADHOC_TEST_SUB_IMPORTED: ]True[
    #   :DBG:   __adhoc__              : ]...
    ...
    #   :DBG:   __doc__                : ]None[
    #   :DBG:   __file__               : ]...adhoc_test/sub/__init__.py...[
    ...
    # --------------------
    #  |:INF:|  adhoc_test.sub.__adhoc__
    # --------------------
    #   :DBG:   __adhoc__              : ]...
    # ------------------------------
    #   :DBG:   __module__             : ]<module 'adhoc_test.sub' from...
    ...
    #   :DBG:   source                 : ]...# -*- coding: utf-8 -*-\\n\\nADHOC_TEST_SUB_IMPORTED = True\\n...[
    # -----------------------------------
    # ||:SEC:|| adhoc
    # -----------------------------------
    #   :DBG:   adhoc                  : ]...
    # ------------------------------
    #   :DBG:   AH_CHECK_SOURCE          : ]...
    ...
    #   :DBG:   AdHoc                    : ]<class 'adhoc.AdHoc'>[
    #   :DBG:   AdHocError               : ]...adhoc.AdHocError...[
    ...
    #   :DBG:   RST_HEADER               : ]...
    ...
    #   :DBG:   __adhoc__                : ]...
    ...
    #   :DBG:   __file__                 : ].../adhoc.py...[
    #   :DBG:   __name__                 : ]adhoc[
    ...
    #   :DBG:   _nativestr               : ]<function _nativestr>[
    #   :DBG:   _quiet                   : ]False[
    #   :DBG:   _uc                      : ]<function ...>[
    #   :DBG:   _utf8str                 : ]<function _utf8str>[
    #   :DBG:   _verbose                 : ]False[
    #   :DBG:   adhoc_check_encode_module: ]<function adhoc_check_encode_module>[
    #   :DBG:   adhoc_check_module_setup : ]<function adhoc_check_module_setup>[
    #   :DBG:   adhoc_check_modules      : ]<function adhoc_check_modules>[
    #   :DBG:   adhoc_check_packing      : ]<function adhoc_check_packing>[
    #   :DBG:   adhoc_dump_list          : ]<function adhoc_dump_list>[
    #   :DBG:   adhoc_dump_sections      : ]<function adhoc_dump_sections>[
    #   :DBG:   adhoc_rst_to_ascii       : ]<function adhoc_rst_to_ascii>[
    #   :DBG:   adhoc_run_time_module    : ]<function adhoc_run_time_module>[
    #   :DBG:   adhoc_test               : ]<module 'adhoc_test' from '...adhoc_test/__init__.py...'>[
    #   :DBG:   base64                   : ]<module 'base64' from '.../base64.py...'>[
    #   :DBG:   catch_stdout             : ]<function catch_stdout>[
    #   :DBG:   compile_                 : ]<function compile_>[
    #   :DBG:   dbg_comm                 : ]# [
    #   :DBG:   dbg_fwid                 : ]23[
    #   :DBG:   dbg_twid                 : ]9[
    #   :DBG:   dict_dump                : ]<function dict_dump>[
    #   :DBG:   ditems                   : ]<function <lambda>>[
    #   :DBG:   dkeys                    : ]<function <lambda>>[
    #   :DBG:   doc_index_rst_tag_symbols: ]('adhoc_index_only',)[
    #   :DBG:   dump_attr                : ]<function dump_attr>[
    #   :DBG:   dvalues                  : ]<function <lambda>>[
    #   :DBG:   file_encoding_is_clean   : ]True[
    #   :DBG:   get_readme               : ]<function get_readme>[
    #   :DBG:   get_use_cases            : ]<function get_use_cases>[
    #   :DBG:   hl                       : ]<function hl>[
    #   :DBG:   hl_lvl                   : ]<function hl_lvl>[
    #   :DBG:   hlc                      : ]<function hlc>[
    #   :DBG:   hlcr                     : ]<function hlcr>[
    #   :DBG:   hlr                      : ]<function hlssr>[
    #   :DBG:   hls                      : ]<function hls>[
    #   :DBG:   hlsr                     : ]<function hlsr>[
    #   :DBG:   hlss                     : ]<function hlss>[
    #   :DBG:   hlssr                    : ]<function hlssr>[
    #   :DBG:   inc_template_marker      : ]<function inc_template_marker>[
    #   :DBG:   isstring                 : ]<function isstring>[
    #   :DBG:   main                     : ]<function main>[
    #   :DBG:   mw_                      : ]<class 'adhoc.mw_'>[
    #   :DBG:   mwg_                     : ]<class 'adhoc.mwg_'>[
    #   :DBG:   namespace_dict           : ]<module 'namespace_dict' from '...namespace_dict.py...'>[
    #   :DBG:   nativestr                : ]<function nativestr>[
    #   :DBG:   os                       : ]<module 'os' from '.../os.py...'>[
    #   :DBG:   printe                   : ]<function printe>[
    #   :DBG:   printf                   : ]<...function print...>[
    #   :DBG:   re                       : ]<module 're' from '.../re.py...'>[
    #   :DBG:   restore_stdout           : ]<function restore_stdout>[
    #   :DBG:   rst_to_ascii             : ]<function rst_to_ascii>[
    #   :DBG:   run                      : ]<function run>[
    #   :DBG:   setdefaultencoding       : ]<function setdefaultencoding>[
    #   :DBG:   sformat                  : ]<function sformat>[
    ...
    #   :DBG:   sys                      : ]<module 'sys' (built-in)>[
    #   :DBG:   tpl_hook_doc_index_rst   : ]<function tpl_hook_doc_index_rst>[
    #   :DBG:   tpl_hook_readme          : ]<function tpl_hook_readme>[
    #   :DBG:   uc                       : ]<function uc>[
    #   :DBG:   uc_type                  : ]<...>[
    #   :DBG:   urllib                   : ]<module 'urllib' from '.../urllib...'>[
    #   :DBG:   utf8str                  : ]<function utf8str>[
    # --------------------
    #  |:INF:|  adhoc.__adhoc__
    # --------------------
    #   :DBG:   __adhoc__              : ]...
    # ------------------------------
    #   :DBG:   __module__             : ]<module 'adhoc' from '.../adhoc.py...'>[
    #   :DBG:   mode                   : ]...[
    #   :DBG:   mtime                  : ][
    #   :DBG:   source                 : ]#!...python...\\n# -*- coding: utf-8 -*-\\n# Copyright (C)...
    ...

    .. @:adhoc_expected:@ adhoc_check_module_setup.e
    .. \\|:here:|
    '''
# :ide-menu: Emacs IDE Menu - Buffer @BUFFER@
# . M-x `eIDE-menu' ()(eIDE-menu "z")

# also remove __builtins__, _AdHocStringIO ...
# (progn
# (goto-char point-min) (replace-string "/home/ws/project/ws-util/adhoc" "..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string "/home/ws/project/ws-util/lib/python" "..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string "/home/ws/project/ws-util" "..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string ".pyc" ".py" nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string ".py" ".py..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string ".../urllib.py..." ".../urllib..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string "/usr/lib/python2.7" "..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string-regexp "#   :DBG:   __adhoc__\\( *\\): \\].*" "#   :DBG:   __adhoc__\\1: ]..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string-regexp "#   :DBG:   adhoc\\( *\\): \\].*" "#   :DBG:   adhoc\\1: ]..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string-regexp "#   :DBG:   module                 : ..'ADHOC_TEST_SUB_IMPORTED',.*" "#   :DBG:   module                 : ]['ADHOC_TEST_SUB_IMPORTED',..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string "<function _uc>" "<function ...>" nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string "<type 'unicode'>" "<...>" nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min)
# (goto-char point-min)
# (goto-char point-min)
# )
    wid = 100
    trunc = 10
    hl_lvl(0)
    hlc('adhoc_check_module_setup')

    mod_name = 'no:module:found'
    hls(mod_name)
    module = AdHoc.module_setup('no:module:found')
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'module', str(dir(module))[:wid]))
    dump_attr(module, wid=wid, trunc=trunc)

    hl(sformat('{0}.__adhoc__',mod_name))
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   '__adhoc__', str(dir(module.__adhoc__))[:wid]))
    dump_attr(module.__adhoc__, wid=wid, trunc=trunc)

    hls('adhoc_test.sub')
    import adhoc_test.sub                                  # @:adhoc:@
    module = AdHoc.module_setup('adhoc_test.sub')
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'module', str(dir(module))[:wid]))
    dump_attr(module, wid=wid, trunc=trunc)

    hl('adhoc_test.sub.__adhoc__')
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   '__adhoc__', str(dir(module.__adhoc__))[:wid]))
    dump_attr(module.__adhoc__, wid=wid, trunc=trunc)

    try:
        import adhoc
        hls('adhoc')
        module = AdHoc.module_setup('adhoc')
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                       dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                       'adhoc', str(dir(module))[:wid]))
        dump_attr(module, wid=wid, trunc=trunc)

        hl('adhoc.__adhoc__')
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                       dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                       '__adhoc__', str(dir(module.__adhoc__))[:wid]))
        dump_attr(module.__adhoc__, wid=wid, trunc=trunc)
    except ImportError:
        pass

def adhoc_check_encode_module():                           # ||:fnc:||

    wid = 100
    trunc = 10
    hl_lvl(0)
    hlc('adhoc_check_encode_module')

    module = AdHoc.module_setup('no:module:found')

    hl('IMPORT SPEC')
    ahc = AdHoc()
    import_spec = '\n'.join(ahc.run_time_section.splitlines()[:5])
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'ahc.run_time_section', import_spec))

    for_=None

    module_name = 'no:module:found'
    #hl(sformat('GET MODULE {0}',module_name))
    module_import = ahc.encode_module(module_name, for_)
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'module_import',
                   '\n'.join(module_import.splitlines()[:5])))

    module_name = 'ws_sql_tools'
    #hl(sformat('GET MODULE {0}',module_name))
    module_import = ahc.encode_module(module_name, for_)
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'module_import',
                   '\n'.join(module_import.splitlines()[:5])))

    hl('EXECUTE')
    exec(module_import)

def adhoc_check_packing():                                 # ||:fnc:||
    """
    >>> source = AdHoc.read_source(__file__)
    >>> AdHoc.write_source('write-check', source)
    >>> rsource = AdHoc.read_source('write-check')
    >>> os.unlink('write-check')
    >>> (source == rsource)
    True
    >>> psource = AdHoc.pack_file(source, zipped=False)
    >>> usource = AdHoc.unpack_file(psource, zipped=False)
    >>> (source == usource)
    True
    >>> psource = AdHoc.pack_file(source, zipped=True)
    >>> usource = AdHoc.unpack_file(psource, zipped=True)
    >>> (source == usource)
    True
    """

def run(parameters, pass_opts):                            # ||:fnc:||
    """Application runner, when called as __main__."""

    # (progn (forward-line 1) (snip-insert-mode "py.bf.sql.ws" t) (insert "\n"))
    # (progn (forward-line 1) (snip-insert-mode "py.bf.file.arg.loop" t) (insert "\n"))

    # @: adhoc_enable:@
    if not (parameters.compile or parameters.decompile):
        parameters.compile = True
    # @: adhoc_enable:@

    if not parameters.args:
        parameters.args = '-'
    if _debug:
        printe(sformat(
            "{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
            dbg_comm, dbg_twid, dbg_fwid, ':DBG:', 'parameters.args', parameters.args))

    # |:here:|
    if parameters.compile:
        output = parameters.output
        if _verbose:
            printe(sformat(
                "{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                dbg_comm, dbg_twid, dbg_fwid, ':INF:', 'output', output))
        if output is None:
            output = '-'
        compiled = compile_(parameters.args)
        if _debug:
            printe(sformat(
                "{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                dbg_comm, dbg_twid, dbg_fwid, ':DBG:', 'compiled', compiled))
        AdHoc.write_source(output, compiled)
        return

    if parameters.decompile:
        AdHoc.default_engine = True
        export_dir = parameters.output
        if export_dir is not None:
            AdHoc.export_dir = export_dir
        if _verbose:
            printe(sformat(
                "{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                dbg_comm, dbg_twid, dbg_fwid, ':INF:', 'export_dir', export_dir))
        for file_ in parameters.args:
            AdHoc.export(file_)
        return

    # |:here:|
    # @:adhoc_disable:@ -development_tests
    # myfile = __file__
    # if myfile.endswith('.pyc'):
    #     myfile = myfile[:-1]
    # myself = AdHoc.read_source(myfile)

    # if False:
    #     adhoc_check_modules()       # |:debug:|
    #     adhoc_check_module_setup()  # |:debug:|

    #     # import ws_sql_tools
    #     # ws_sql_tools.dbg_fwid = dbg_fwid
    #     ws_sql_tools.check_file()

    #     import_cmd_sections = AdHoc.tag_lines(
    #         myself, AdHoc.line_tag('adhoc'))
    #     printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
    #                    dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
    #                    'import_cmd_sections', import_cmd_sections))

    #     import_cmd_sections = AdHoc.tag_split(
    #         myself, AdHoc.line_tag('adhoc'))
    #     adhoc_dump_sections(import_cmd_sections)

    #     pass
    # # |:here:|
    # @:adhoc_disable:@

    # @:adhoc_disable:@ -more_development_tests
    # # @:adhoc_remove_:@
    # ah_retained, ah_removed = AdHoc.tag_partition(
    #     myself, AdHoc.section_tag('adhoc_remove'))
    # hl('REMOVED')
    # adhoc_dump_list(ah_removed)
    # hl('RETAINED')
    # adhoc_dump_list(ah_retained)
    # # @:adhoc_remove_:@

    # # |:debug:| def/class
    # ah = AdHoc()
    # ah_run_time_section = ah.prepare_run_time_section()
    # printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
    #                dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
    #                'ah_run_time_section', ah_run_time_section))

    # # adhoc_check_modules()       # |:debug:|
    # # adhoc_check_module_setup()  # |:debug:|
    # # adhoc_check_encode_module() # |:debug:|

    # # |:debug:| compiler
    # ah = AdHoc()
    # compiled = ah.compile(myself, 'myself')
    # printf(compiled, end='')
    # @:adhoc_disable:@

    # |:here:|
    return

# --------------------------------------------------
# |||:sec:||| MAIN
# --------------------------------------------------

_quiet = False
_verbose = False
_debug = False

# (progn (forward-line 1) (snip-insert-mode "py.f.setdefaultencoding" t) (insert "\n"))
file_encoding_is_clean = True
def setdefaultencoding(encoding=None, quiet=False):
    if file_encoding_is_clean:
        return
    if encoding is None:
        encoding='utf-8'
    try:
        isinstance('', basestring)
        if not hasattr(sys, '_setdefaultencoding'):
            if not quiet:
                printf('''\
Add this to /etc/python2.x/sitecustomize.py,
or put it in local sitecustomize.py and adjust PYTHONPATH=".:${PYTHONPATH}"::

    try:
        import sys
        setattr(sys, '_setdefaultencoding', getattr(sys, 'setdefaultencoding'))
    except AttributeError:
        pass

Running with reload(sys) hack ...
''', file=sys.stderr)
            reload(sys)
            setattr(sys, '_setdefaultencoding',
                    getattr(sys, 'setdefaultencoding'))
        sys._setdefaultencoding(encoding)
    except NameError:
        # python3 already has utf-8 default encoding ;-)
        pass

def main(argv):                                            # ||:fnc:||
    global _quiet, _debug, _verbose
    global RtAdHoc, AdHoc
    global adhoc_rst_to_ascii

    _parameters = None
    _pass_opts = []
    try:
        # try system library first
        import argparse
    except ImportError:
        # use canned version
        try:
            # @:adhoc_import:@ !argparse_local
            RtAdHoc.import_('argparse_local', file_='argparse_local.py',
                mtime='2012-09-18T09:26:21', mode=int("100664", 8),
                zipped=True, flat=None, source64=
                'H4sIAESf8WEC/+19/XPbypHg7/wrsPK5QNgk1363V3elhC+nfc9JvLuxXbaz'
                'VxVZy4JISEJMAVwCtKyX5H+/6Y+Z6fkCSdl+m2zl3W0sApienp6enp6e/niU'
                'ne36m3Z7mr3rq09Vk/3LLPvnqr8pt6vslx0+ml3S7/97fVvW69myvf1+Nhqd'
                'nJz80N7els1quq6bKtuU265urrN1fbktt/ej0fubustu29VuXWXqr7LJ2k0P'
                'X1XTuuk29bZaZcsBCJnqtD8djTL13zS7UZ+tqy67bPsbAFS3TblWQFfZpu1q'
                '/XN7vbutmr7jRput6n6pWt3U1zfr+6xurtrtbdnXn6ps15XXVXZbdfCvbtDt'
                'Npt223eIS7XtEIdsVXebsl/eZH2rvric8ksYYpVdtet1ewd4wyCzrr7drDX0'
                '6nOJvxBKt7vtFAZ9dQ2Ar7btrXpejRwSwHjutnVfQc9Vtq263bqHbsvsql5X'
                'p0wOQiCbw4Dx79kZj/wNvhnjV/DfquqW2xrJNc8VBgjWIKGwgt+MQgYo5IXo'
                'YVauVgtNVAs01wDyiSJgX34qt3N4pn426utunj9Vf/b3m2qunk5Mu5tqvZnn'
                'ihG4PQzssgLC3FargzqeTtfttYK9qq5KRZl5d9/Nun7V7nruzxDk14pc79WT'
                'cX6XFz4KMGigZ3Z3U20rpAHQprtpd+sVoARz0FcN4wRjUsRm1PAfQK4b29cz'
                'hdcMZ26cP+7y7DEAHOMbTazC+3q5brtKgUAu4nWybJu+VKsDUbKctdldrutl'
                'tlyXXVd1Zk24k55NpxmCUgAy9VStoE2rOldwttGFNsvOsCNDHM2u5WWrFoii'
                'xl03QUyc2Shgzm/aFfD7rlOLWM3ipt3s1mVvQUEr5tK7Wq3Ycgks2CEue1fv'
                'DMbRhLCY6KL/uvnUfiQUFOk+VVtiaJwwYm4DxaGAIkuLEunyj9WyZxT7fltf'
                '7tTam/kEfrHdtoa+1edlhSPItmUN47+892eCwHbAXs4wtoCaggDgOurVEirv'
                'NJVm2Qv6gju4u1G8auBoMSlWLgsPBXpZ7q5v+ghKQOvqFrh6ZSCVnQtAC0Mz'
                'fr2IYOhn2ZVCr1VcBXOoFmDdIBbqdZe1V7ieOl7Ry22lmGF1GIMpdu/LZklQ'
                'TI8wGAW7XpZrJbg3wPgrhbDDFLjiDdtAc49RobGYTaSunsbLsqtoReGAmFnN'
                'DLw3fWvWVRiZ3rtqrSaY5h5wA0p0in0axXfr+mOV5Z0iVbXot7sqzxT4vNxs'
                'qma1UFza9bkikzMQ6mJoKLPst+2d2oy3E8T2Ggm8tcy9U/3d1j+VOELV2p99'
                'GsMEti+WIvgVUeS2vDeQ1Ozh3AK1YXlqwkfxNKT9rRKrv8attQcU35Z3P9qN'
                'J3z5vvrcu09N/xrxH0nCd85nMHf2hx6IWh7LGwNADQYG4SJ+pRstsJGgtGJY'
                'yaEe3XC6tjvg+5k7SJA+AJl3IjuAgbEjRWPDz/pqvRaiwABrWsRwqbSf60qO'
                'BBgOGAH2M9X6s9r/FPADqahYq7O6kGIAtR53vaUJj0ksNiQSdqam/Ezh2oI0'
                'MzOgNpxeaHsoiBTl6lUFSh5qRACYOlspjaGGZTk+W3ctDJEVpCit0rRUnbTN'
                '+n4keuJ9Uk06C/amVDINuAbQP3vzEpje4Qcjqutu1PW1GpkAB5pKDPdZAdrv'
                'aLRYqAXZqeeLhVIP8uez72bPc/VUiQ18co4EzF2eyifuUxT1/kMQgc4LLRf1'
                'b4cWfuvorOuPBmgqPglYVL97BRTdlEuDCckQ/ev1qxeL128Xv3v99oV59Ob9'
                'y9evzv5N/35z9vbdi7emrxe/O3v56kf74N3v37x5++LdO/37Dy/evhYgL0aj'
                'kZoUpaSrmdrcw1wv4A/9sO3wUdvpB7DnqgdKePMDpTPiE/WvfgQL6G5bbvC5'
                '/jEaoY5+XfXwJONP9U/4cjRSStbpiDaEfkSKQQYUwrmjN49oe7lXKkuT/TL7'
                'bvZPsOmq80R9Wa/r/j4bq7byoER6gtpSlpX6+n8WBAZxwS8ZkXcVIgEdWzRg'
                'U6N9KIGN/UDxp/pDDkFBVcrBw0ZBXynBwWDGShPelpfraqImAFZJNf91ue4q'
                'Hg38x4ebudowu958X3jvZwBvbJ/WVxqghSS+5ndjCabfbRt+r5gHcFzAzg69'
                'jdXyZ5T4u5uyA0UQXkyyfIFfLhZ5AZu4/w6JCS8VWM22IAjmc/1rPs9HI70A'
                '4NWv8pFkaHj0JB+JVQNPnuYjWiTw42w2m+Ujs0zgET5Z/P7V2xc/vP7Nq5d/'
                'ePHj4uztb94tzt6/x/eLXbOtlu11U/9UoRLRKSweZfOh/9T73/fEkFe7Rqs8'
                'SgazjN/bfkS61OJMq9G/bddKjI5JwDKRldg8u1RspxQJqYCh+FeH9U9K8CoQ'
                'arFutosFaxegrOlHWvWnycLzNjEz7kBarp9a1vgB4AMvj2Hm5rAfTDLxpyJl'
                'YXqxJwDcXZSwr7a3qApVNe53StsrCeXpWjHa2rZgYbX4eKfIvcBtRx1TW2wC'
                '1g5FAq2za31XDWpVL3sYJ5NmZBaRHq+SDesrsWZA40Xoaprhb3o/W+CzxcJq'
                '9goJrY+qfejCvIBVrF4CvaDpbKHkGR+r3PUkIMxIdx0DSnCkLQoHHBHyU7ne'
                'VS5YpMUhgNWJef54C4fmsQBWBGtYfTd+3BX4oaGEWonq/8/+qI66YwFbtbbU'
                'FNh4BGXILLQIdz0tSiTdKvR9QANgzi+0gKmabqf0fxwIDgr3zIkkFjdXAk1B'
                'RbkSfPeqbaoC9gT441ScPhLfE1wpzhKgQWIFC1o9+bXVLmH3j3zDy9zRDYI1'
                'brU0PKxUjZLtCNQ1uqF8MVonqrKaM4jmr5V+h2sGWR51N0UMwgD+EKqa1v2U'
                'kqeOnaxNk7QgPZbFCx7Z8OiMUDxVNanxxZaoOgD3vEQnDotn3N915HHdrBRs'
                '1VadkaGX+XeRj27Lzwsgx0JbR+bf/VPks7t61d/MkUnYJkRbNevvwCfmoIDf'
                'yl0UH4S8hVJGqwRBZ0qY1Oo4qtSrWdV8qrdtc57/8Prffv+7V+/yi8Jpw3rE'
                '+F+re9QjJtm/A3fi30Ua/P95NgofT+fZdyN5+FarFOgLRjn1j/fGJzEi7T7y'
                'WgT0Vk2CZ14bjTAR1nu53G231OGKEHjmfUDbR/icTtiI0LpqrrGHZz70bdv2'
                'i65aMqb08B39JnYkyZFAym8pwfldqbN1T4JD4dQvb9DqrDYnuAXYqDPJeJt/'
                '6J7mflfrtrleXG6r8mO6WQP/D5qygjkf/o+/4mGi6CDq0jqVS/0wWLiICYQv'
                'zqOT+HSe4K/o1KqvnwthoQTPof1M9/YDChkcZGKtv1f8ovbDl/RrVYEpDo2U'
                '1bq9y54pxTGG7dRgy1qc5iYj2cWNgi/77Gl6AvYL1e9ECfNypUSPFk5ySWO/'
                '9gA+t83Dzwgc2d4lBcwH3I/6gv8KP8FtnLQgZxDULa5xf17MieeWb0iIuIqM'
                'epk4Iv3KQVaJVDDbhGI1HLye47ErOkGX0atTfAuPF6oTYZjROhio7BMye2sV'
                'DIcdIgBfjp/Al26f8DnSQnWMutS5+HKwD0/ufwk1eJUUI28mWJlRgG5Q2Scj'
                'jpZjd+oYXN1u+nsfD+jYjCvsXWuVud9duVqxvYuYK9Jf0zbTaJ8OV/LgzdkQ'
                'hFbsgzh1gk3EJ5f7QdDero388ZPucXf6oUHV2W2mhIVSoCVW3j6+7iK4CdgB'
                '+ZB9BcGmICzqcp011R3cM0wc4gJNtHFxFJkeYka1XeRGqkzsrCrs1ZsLqaOD'
                '4Rzea+Fk2DYpeBlPYmd9KBmLhnv3KH79O1Jss8tdvcbBHbYrWdtJr1a3Rofx'
                '15NyGtVyxnLnHVIIoiO20H01xNKQSCOE5URJ0kNUC6FPwNjg9kOObN9smHH4'
                's+RtBfSRKzmgPxgCWOp4/PCn6BKWNFr1IitUvghXZkAg+MnkIUP8Ofxz4aGC'
                'Jx/GBf+e2EuZ622726h/N9vqqv7s75kKVTo2ebgGx2rY5IZBHzwQDQa3CWcc'
                '5kqKhkIdudjSsxluJgHO/h5bwxFQHdfgJneJqpy7u8GJ274zTMF4srpsP3DF'
                'sYUJ+78LasyoXwSbabe7pHfWnAHWyYVWAhbmg24cjD/St5YoXv8GShHsd7vN'
                'quzpvkedBOrb3S1KvIyOBIkx2gODajM+V7/GvHPjhi0Q8nZsJqJpHoJ8GtU1'
                'Y9wUOb4ANom3kTNt8j8HyyK1ZSOZ+LoK7MoHc3zJAvGc/rhIsH3n8L3cUtCy'
                'ZtiG30dEh7OImAH2bC/8FmwuU3H/d9DmMjpA3WW1LzwNSrHv2uBDjcoBEp7/'
                'Zordx3jow318vSlirfGGEWxAG/g2LxTnwb++nQ11BbvjW8WYZ2eD2ygbAgMr'
                'Xc7WwnP4LMmB7BTQw2xKeMkGiir4PV2bb4O9xVFSpJw9aFdwRSw9i1tv+J06'
                'b49zhHma5YU0D8kNBSzT9VVdraB/uodNbjxhV/Sadx2lWoLhdAwWmbm10fhd'
                'N61xAOrAQG4dgMgaV34q6zXdHJne/7jretfSU60ldoAZ0h3QjC49jWn+GPEr'
                '0EXrEHQtrq63UoDsslwv0QeK+hrA1J+u9vpIxAi5brOue4Ef3hAKBJ3P7WfO'
                'dQAiIMYUvDxAqrm7PnWkF8tpdLUYZPTOqMWg/2H87OEh7QPxyIS6uDoFKB2D'
                'ZoHvR71Rwkk/qlx0C3c+xV6kmYq+H1saP5X46ZVcxBlS312cd3avPkfjsdPN'
                'BR4uL4Lh4bU17HYEEKUgfFr3OXhjtRmIYte6q7RTY72Utszp/l1eAQa9gkWS'
                'Gif8wp6L7HsB2dPzeCZgP9BLARzwAPcNrJ4stGqwp1u/2FbX1WfYG7b5h/Hs'
                'ya8+FE///OEc/rhQf7x7mo8i7JWcmvhkMEf5rfZOou6NqE4WTtBolUI7FshP'
                'LErxfve2N8iF7dkYaPjI4FMolcB2vLedwQPbmQ5jEwnbL9/t4BSS03ZThTMI'
                'ex2ovfgWh4QOf2R3iB935H/YLBRK8nX6rbNNpq0sEhhol+CQIFh8mj2PNkmL'
                'pggwGnEamK9rdKdDWoYB/jR7zksQGvkrcEiZRsJqwant25YX4HVR7IWQpv0D'
                '6aCbaMxwWPuJ/HQuiPA0AZsJNzxnD6PJAzitO392ga4v9Oe5oM5pnKSsvNI6'
                'iyxKRKJFk2J30277CfuPq52API1TWldsMw+FPKog2S/n2bPZ//5f2ZO9nGaM'
                'loqA6vNxCqKariRRjSjbQ0vVixUyuHdeKLimtS9xij0soEamj+sst7Ro1JAS'
                'fICqnvn4QUgHXQ0jvV8KofhE6HuYBvQE1dkOTOYZqHtqR2rviOGOUMy8eRfT'
                'HtfjeOezu6igwegw4rlTk1z8Fa3hDuTk8wOIdnEsmwQMV3wzTnNnFhZUSiyg'
                'MZ4+R50rrgwYbVQdtq2465zDEIs4lCV8sMwjHjqPOzzkw0UDteBzXOT06yjY'
                'rmHF6FunI89YiM+BOvWSPUhqIFR9ZT311YiptWmLP3V/qPY6PoUNqELw/E9/'
                'cew5ui8Gd4CXBFrwITCL4whgFj+Psfls4WChpH7UYcJ6SURuhFo10GZXHXBB'
                'o/gKPTwBHZK3MSSK9EmuO8fGpwrQBWiEseanSW3GnhkPbxdMFNjKkmdDccdH'
                'XWyr/9xBUOGg7kQEQXMozvmwmsQfESUuQM/Is/M82WRYGkcAKngD4PTHNANZ'
                'fpE/YA/4KmMef90xjw8fc5EnWayGIW0hMGKs2fz5BPi+ON0Lvkbgf86lfFsq'
                'dQliBuA2QoSrgWHAN/3pXctzrKwngu+rZncLbm/V2NqKfQvObqNEJMWpaPsy'
                'mpVuyy1EtaGoBV0yuA6/hfipPysxpjApewgVo4uLEN4obqbRlzPxyyQzRq0O'
                'u+5EAhwTdKa2sHGNJ0dF1ZRmQJ9u2o36dBRVnhxwqBseDpJUSY9UHAFMk7q9'
                'zmJGXOzZWg73mrA2JOJdWxE4heo7BIazqrq+SGhdaJ4BixoJrwkiRoacdgdu'
                'MRH1w8yeEavD8pQN0njSQEljTNPn0+f07CJPrxUeJn7//FS1iA1F37swYuyN'
                'nbqACfiKDniJOaMo3W2nzi/lPcCkaE8i0kYT4nJbLj9WfXfAnuhMrNmkvflW'
                '5ErMGfT7Wseurtqqa/I+60uFUUmet9oTSi2s0wgIiJTDwxdEMXtGOXd1NnSb'
                'qw5bp6OBqeFIYwf/Q3AHnLujkIbwAos5/jziTKD9UedyZcyUsKq24/jGDuO3'
                '85ReaQy52EOljAg1dig1kb1E1+ktzK06Da3b9qONWtarFySG1jmANnY1jxJ6'
                'Co/eNEL3Z1o46Kp00KrWozp/3F3AoPAS65uvzEcsazP0wDKZA5pqCS4v23ut'
                'kI+CHVrHA5GotuFA77c73+yHCJzXp7g7n9u9+kLigQeakh28tTxEFz/cLtFX'
                'VUQugi+HtLLjBTEiB39oextNKjywBpwLZ/jLdVU2mToNeHvu7a7fYZiwUt/X'
                'uw4yS3hnj3aD9q9tfv7hfCx0OIz/5xcXhXjBOIMxGC5NtzkEPWS00ivF9Nv8'
                'w/OcPVrSjTIdKoH9HNpKrZUnZrFAZ9i6gOb7G38Yj8//488XT4oPRT7cIfzD'
                '97wOlfkYicHd6hP/eInPgmPkoJePvlfLMURIvT4NLkMYn+S925denHgmkcFv'
                'dTwKSbx6vabRkWORRcCYB+iCHK7IE6frlJ/OIxvexKlGWCjRkLRXHuWRWJeX'
                '1dpxF3A85esm5eCh0Ptu2Mkj4YBfuL3FqR53z2ckdBMX22nC5zr7zm8PnnHo'
                'njzscBReOz7KblolGNebX/DJC6QvxK+YDC8gmiGhS2N9IkfxrSJ0s+h3m8Az'
                'TjpyOtjHLi3NuMgplEw1CqocABqQzdakcBdDQcdOZzibUvHKXeuLXlSrwfDg'
                'dIw2ZDlFDxoeL4IjBzt90mWZHm4kKIeUTSfg4hHaRQdI0YDkcGYw1IO+3ZwN'
                'DMJdHJFzLqYbqCtOvCF2U8cT1xx1HVQuPC8JilkGx2g8WMLGaAFOkOHJBtle'
                '2ZQFCZ/B0K1owVKaKFh93iiuI5+kmHEIW2gDKTVBVwk2sRqAEyFailFSEZIk'
                'H0sa09zZ3sCgVwTOE5xuRn73/PRiz3Hb6dOZSOqU76LEHLRbliosT7TOL/I/'
                'mSMLmAbpRqjx3FSs5OF5nqlvO/iW3LFOB8gE76NcgX4yzT1mzjLWXdZOa85g'
                'oRjnrlqvR1/VDdPBLyLF4x6YRgmBXF7N9TpwGHG2aOF6RpfnqX3Y8fxMus4e'
                'aIXgpFsTw+D8YGGCA6K2iLF31cYj4cajAQkmDF6jr3gu5uPlJHYiPuw0THPM'
                '9yhRyhX7MD7sNCxPwpPkOTh+Bj7u/PvFZ1+bY2tho+OPcM/yRNEhp2ePyPo2'
                'yARmB2sjZFi5KMzg9HdRB3N+l750Nxkm3AauzON3y5sWL5SSwOgDGDAuBPXv'
                'mB6RjzX9LSjNAC/iGOV/etz9BaiaT5hEAn4xsBINBI9Csdi2sVIR1gpk/ZN/'
                '0objbqcTEYwJ5iTDz4tkoBSn0NjP7/y9gVuAv4BBxRekhGtEbuo4+0O4Aq5Q'
                'NT/sF4o+nFFK6EQ9Nu0k0sIQfUsJK7nLiDCdCyQFUVt1joEpE4oMwM3g/2az'
                '2UXQwXf7kLbpSdKUMOCPhW5Sm6RgY7qTQRCULWUANwAxRFWfi4llcKHjJMMK'
                'X9j7Jtl/kVrhWvYxrMLr34GRylZj1oRUehPqA5ilMNAVrRiqC6MWTbKkTUMn'
                '8MjQS6DrxwQlFBf0/By+vRi+OFpVa+fr4/vSeXYkFEy4Q1lO8iKqB1j05s7P'
                'MDuKGQ7eM+UsqfNin/DH7Q6mdmKddmEb4B2ArYnQsYF5cREcLdz3CpwAHlcy'
                'gW3wFEC7rZ5WMv4qcIJPkhpygmkCJwboyzaze+fCfTHyvBZM1p+I5wKk4htY'
                'a4lwxugxwEViHGGE+7par2yjSE9hqKBzPrSGxAnZwiS15Dk0TI1AMS6ZNnoa'
                'A6c3qSbD2Az+Zyy7krugMf4FGBnr37fDDHofe11iEC9P1JztF0cEcMGkdNV/'
                '7qz1Y65dttwEO5LVE2yrj2jWajDSmWkG8tuNnV82XQ081klpRGpAzCsJXWFG'
                'XjjCiuCrupFn67+JhDXHcZQfLGU8YtG8IE0bZMyHJUQrCG924PbEzkiQTnA8'
                'ME1HToyYFEibqihpLEx/C7NyqOwRVyCS2JbMg9kfH8T6mCdUH17xeIwJfp2M'
                'TX8LJD5QqHAMohQq7kWSPnHn+ro2abW0Oqom32DwtjASKPwWrNdm5/q0MHF0'
                '/IuDw68y44mnzzNN0E/cBoC0IN8vbnCaWQJ0RSIkM5UlUD0newt5bJ4Z76TU'
                '9yObbo3MZw3m8ON2NnWa4cXgpMZ4GfcpOjjoxMUpOwi3yvJ/tCnlYi2KCEx9'
                '/mTmQKepiZnxyO7lNYyABEPR8fCg1ShUtiRFfKGBatv4hU5tLtI1NpSunMIL'
                'MbE3StpttusofYedAxNm5UYYFCKRIxukKFugFhM2ozonVWaBpNbo7vqWEu+A'
                'EZomPchbzBnfOZ8zpJJclpiYvu735m0zDSe6Uz8vhf5Ap11MM6XbTgvVuQYs'
                'UVBkCJM76uwxbo9RE4QJWFRSSePd5XsPtNDAUOrx2Omo6GCFR4A5Zhp9Sc7f'
                'zeVQ9yiDTm/zcKThTmayIO9nTHWOYfcWXQegdMpaCP+XEjNnzoApzOkkFFzq'
                'AWdHTyVANdjSZYKf+NRi+jLg2Jv2TqIaQRQ32jeUbpdTVPMqYqx03mrYFndc'
                'hUCtRS9/uQICWTurjpZGJVcPQmuqasUlHKCFvfQwbILkhfhqcHZptxZBU8GE'
                'PNPtELB8Q/axur9rt9KzlX2PNFltanW6Ilp3lBQfXTVtJlabpt4UCmBK/Cv3'
                'YHYT4WA7zbydECsYgNUBADpVD9iVUH/oZpPH5WzKgqjpbpd1qeURSS/eYGXf'
                'KLa5zoBViESCWaDFjWIT0m+oWgJP6VjeWEypoIqBtbu9hJzlV37hB0NiLDSj'
                '8R15sQOd+mo1y/753mStx4k1U30H+c8vK/MpOSswRzjASH7r79lhU4HOXmOe'
                'XNYV62a53q0iBuJp9iob2zowhe5RiToxmDE6F+gSPiXOXhGBlf8qtwB+qrYt'
                'sKocWBdr9CTSCPn7AQg8FbDkUjkG1CuTBx/vbeurK6XnQprgy6q/q6pGVhug'
                'XAdYauc57Zll76XN5NIiZqLNwo5P3YSKjNhtVv/HvUwYZ12hBrf+YZDOisDV'
                'rtmYvqdSIfprfS3XGkXApKbQzkiRhAYg+rC0FJuIiH54ode0zIbeyiQCHoUJ'
                'KGAGGwdcz8VR3nM1Ej44RUqzaEawwoSlv6jHgoacdiK+QWa6gmoiIJzA7khl'
                'lvKrdVviH5BQc119xiIjpbvgOce5roWAtCmXsJF2/uW21R2zl1eob7ibuUYA'
                'a1x1JEec6eXbM5SyzCIkqPSx0RFMIOPbOxAYL6+MxdXtsbzCIg9xMoKFWIGp'
                'GktEvbuUGzWPm20tixEhXdXsQI0MoWxqhuUqO+gCqqe7VFqblrUg5T1Rih40'
                'vtQ3LnTAENud8cFg3ryFJCbl+q6877DqlWXvPuBufzut8RQN5S4UXiWsvqvd'
                '2i2mJAk1iuld7kLAAx5zrsi8zEatS52s3Kv0Qm31QUfucLSGUBPR3j+EGpQ1'
                'shsMiaUw9Q/1brkPAeSwj+aeeNmJsi7Q8wNSM7uqQeQD6DfymGRhyKtmf+1T'
                'L3W9ssRrLGSUgktLK/VaMx2VV4h8gBXPEo118TYvBQPq5p7+NPeo5n6MCs88'
                'MwdP80KbMvBf9xVtCXMinA9OO0zwX+5rlLSUAN8DyWLI3Km4r80CnRuyuR+I'
                'LFT+YU5fLTvX7XuSy1P1GV0HxshSl5C5J2mR571nSD3/IZWSClojvfzHvS0d'
                'Y9vzFZT3GAbvP+NBi8cXQep7Tt2vE87T6RrPdYVz84dEuZCLlUps2NRdHSQS'
                'FgnraQuZuAzo8ywKcVCiXmqrYLWis+NinM9MJwVKd65wlRf2zLl4BwW7+Cx3'
                'pk2DfxcpX0mkgG9bwo2LZs6GPY+J3enyr0c1mi8jcQdVW8D32bNfAMT7dpfl'
                'w0aH/Kb8VJnEwVC/EyCaMPOs24Gdu+OO9gGDcm6ZQYsEGNcbI33fKh+541RC'
                'n4rrZavBZ/+Q9ApJEEaT4fGWCpJuNkot4MJyjw0sYY7agaOZZHBKBwt1Q5ir'
                'R2leng+xNnD1PGRt4mr838ko5Gj8Xx8QcXNQTs3wMipwsUv5Of87GUWZWP8x'
                'CZSOOWazjTlWzo1j0NcWU5HSHWYD1SB8ofQDkOtnl0yRSTpE7nwTfUQwsCDG'
                'z8PFz74GBx/KjT83w1lFzGc6OMBoy6ZP+J+D/TQ5U2x0OJ8lGMkO8FvzEbEM'
                '9PdtOMaZNyTHX8PEheP9OvMmBvjzTFwE0a89c2foa/135fOvS/kkD/ik9gnp'
                'JPYpjPr0DBccaEVEZU0bV4z1kXqa7Nc/ycAFWJFGWZoCvn8bOqhk9L8rof9V'
                'SqiuiIOFU2fwP+NkwTqhLJzL+DanVobWWw9TOrBpIP3+ruXKJfLfW839W+d3'
                'qTY/jOd/aHfNz8/tX42rQ7YVA/ovYdi/0uNXU90prtth+odDeO6Zm8B2mKkM'
                'cMFY4ND5bfnKFDceYLCBTwZ4yOL+rVlokFui/PUNeYTazZTO1gSlNvhd9bnu'
                'havv4t+p7vy3m2gubJ/W/78OH5x04AoFIUnb8jbvdLfa0QUUVBj6ScgrDgX+'
                'qtnFuUjSA5zroX51brI9yA7lQUB/EfUstM2Z9XwAsnIjf4JXYDbKsgi/nZlq'
                'XAwuzuHaq9C2cwrQSFvH7pJc3LroGtC7LCnlb7pqt2qjHya8QukuC+fPC1ai'
                'VB5sj/CQmMU6ZN70oVhe9djz/GJCbGhxCOXOF67uRG1imooFEu8Bi/4InTdS'
                'y3dh6tZESvpKzAzf0U/vSwz14/e35cbN6cspWDjezsa4ybQGibn9eZQaCmSN'
                'nzCj4/tCBRuWJQFzGP/JE7rQdvJFKV2EkoVrx08QzR16g3vV5ZSMofYUXwmN'
                '8iIubui7c/rmws3WF/CGqV0uktmg7yQEleCSm2o/MOleSZH5QTwHXnTDjTTh'
                'EK1mxcOA/KL0fRHLCVC6BQtjUkcIlEhIoseR+pjhgI8NG1P4kKevzitV99oT'
                'SnGHJ2QNhnL9jM1kD68kGVvbVUGkKj913SK8+NMwZCE6/G+kYGkHfmoCaT6F'
                'h5Twc+H3z0+dJEfA/YLc5M1whScLtZaFI4n24keXmMGon2HlXiBduIjY7E3u'
                'TASxvN6s+xMqerjw43l11fZYIivRbiJioaOduNx+211zXbLmYwPFBRjDx9uM'
                'mR2CEChtoeqriJgi3YAV4gsF1s1UT67sHFq2rW7ZYbXd6PzwvEQM5SV9yeWg'
                'uc92zbZattdN/RM4Z3NbTvtFPpVqwlrrs9u3G5k3DAtr8wCXJQReLesVeIiW'
                'uERXrXGHu3U9hogVXKbUZwT4Z4G042Qw9iuxLtyEFvYTT9WDFAG2zUzxIyu4'
                '48XvX7198cPr37x6+YcXPy4gzc3i7P37t27pVw4X93k40bYwWXosPkU88ALi'
                'PvaGXfy6XlfwoS1Rzn6Avy4hpuCeYvJ1vNJVLRxhVSsWMi91SAH4eWqIaK1X'
                'H9VLTOwJASLscggm4CCggaIy3LgLp8hjwdGN6bAF4VrZriryojWpe1b1ksaA'
                'USOYE3mNYUHkcglpOsGT9ow9e333SszVx1647DYJJdEURGyqsINCx+TMavG4'
                '3F1Brhbt4gld5hAL2qH/nHp7pUYJXzgde525smNfx0NRWkCWeb5VwoYRi7os'
                'LpB6c/zae6PHM9cAkpsMZzSSmg+ODNx1y7X1ZT2ZnqAvbpd1992s61d/qptJ'
                'u+v/4uwEnMZJ6TXTPAgRVQOyuc0A6WQqnQX3UTdh5vL87lgoCssDsvgYYe0M'
                'GWUW0vnxFsS07TaMjAguj3xBDSK6xYgRN/+99vFFTkfREmyvekZPY4mnkL90'
                'niqL4cRtOpxmaQiQcxaDAKswmE+H8CZ7d9SPSGYRAAuykrwn4bKxbggq3z26'
                'qYr9sP3Hnc7/OwaxNdanF0qFYrN3FcmYXS9yF3hf6ZhvTFhnBrIOEuMNt2dx'
                '/UpvEAOBcu8woluLae3/h+EJJh6Mhajx8uwypYGV67q/xwg4E2BFvreAsVYR'
                'OQIHQssp/gFAIDBepSZSrjxMKEVOSdLRNXas6ALv2Ik+AqEaxoy1WNyU3c1i'
                'oTiConUtBtV/mv5x5YQ6NW7rON0gd/AXfSnBNNU+MMBb+AWWEQwAcJBHZ8B8'
                'rO5DIOqhlU0LiBxdLMTFH+n7P+h4EbuVH2zqEDk4onYOODaq84UiQuS1CT+N'
                '2vX0PdjVGtC+Ueyzduik7+u8QQSGgmIU+MqblJxzOYBE3LHIHug9chvIwaIV'
                'xf4MHO+dMZEPvvPIP/kovX9bXdewUHyn+oV9QcYWJ5MmvKp0EoLAHZ/eqh0G'
                'XyvhR7Ef0lW12NsmR409f1izBXvRh66WB0MAp2ADwHqVHdz+Ci7bDADh3nQA'
                'BDIUQGPpWXFwQzv64Nb5ABh49QSNxd3fAc0owEDeVB3QiM3G0M6x/B/QlI5O'
                'HVLYM+q5aV9RW3EixDiAS6+OTC8YCMdq1L5Se/EjlGmEPnIT25sqDO1W1l+T'
                'adO9gkL0yrFriA/ddeZVHHCSsdO7GGxdumBhShc4Hzup4imlTAJ/89rHy6SY'
                'h7DqihS9JjuhQZ1gXY0uW9eYKbaprtW++0kHOfvGKH67oLc6rxWXH4AgSKUq'
                'jrf5f0w/rJ7+jz/DP08+zOBvNyuxRqOlNB1uhmJbIRPP9Fj2A7HTvQtAhAdG'
                'PFIMKoXHdi1Y4OC4DyF+SvZy+Gq1qns/2gg2+WBgXqHuEfUW1azo1VsSv5Re'
                'QKbRGWgFO6tZKrR9sxS/Z7MOJ8N1zta0r9Nnxqhkpb+0H3jQ/vSXIoBwjl2A'
                'QZE6EXu+aQ3m4yH0pD9DyrhoETx3gFygcdoFVAzRO0p9o9ba0OwllESBCPC9'
                'c5GYGUVHs6TSqqa79Ga7zQpqjWlTbpCIu6vsKsbFgxxvLPjm/AWk3qxdkxja'
                'GrfVp7rd2XxQjiHMBpw31Z2TV9wtBujIu3TKpK5PKdCotrmZlbSV/lw0F/Fl'
                '15aaTEzMhX36xRjOKd5RVPHxkz3FywC7uet8Vc7hXTO7wKpkFqZKbHv4lN+e'
                'rVZybh0tbLitvhsyNixmQ3SmjHGjzqaC8yMbEtaz2YyOO3NecOpBEW/gZZn2'
                'fg4DMqc1w/lNKxIR0fEZpD06rNZUtwmjqsEdFnIO6OdqUiWg3uQ1t5tC2bip'
                'QyYmhYrtUWoAPEBb/4cV9UB5DxLCbymTF9bSALID6z0nvttiwTIo8cZZohBC'
                'yLc4cNWAQ6oHVlfo8YtcbijT38Ft2pWT4ckMzrsfoz7MXgFL0TbSQbM+Uzll'
                'DWCDvquhftFdlcM2zSzd2MD3gLChNSeCh25+CBbER3pxQ5ULTQ2obSuv4aZk'
                '9fcXNVjpdGSunqgY/TmMWl+K4lxd+HOpxaMrIsKJtFCo4wszft3mnERlYFGM'
                'nz8HhVqys+DMGr/FLGVWo0nkNtO762LlVjsE8LVmq2un8dWmf7HJC2qhU2OM'
                '5dfFPs93fWnFuJ487k7AvubA8BA06QSDu9bowQPzWblZIzDWnUmv0R5Jn/QF'
                'WNF9dYxUJw771lsNp8CwPwYIYyDvpcrjrY8e3t6Z9qP41oYyfxlWUPJ3HjqS'
                '7N1/qFKzOg3oW5XfDDQbOijpu3f8FZhVqbyfg2jqFJXW3Ayuv+OmL3TL38Qa'
                'HnpqOwpzSf9khbBt1bXrT3Q20mfgLnCmqZYfF/ptrBoWlnppTRiNU3rQ0bb0'
                'APyiPrqggkkrQ8zuFidcVZ/lssFsaPd+bq8aM8c4mt9DCmUMHM3PnacXZv3H'
                'XAmu1uU1bs4houHRUx84vxh5c4GSOFLP8F9XDYvk2WaJccBBNp5g9ICGmh8w'
                'n3CiSqDOneZl+3Z0bOdkCZWT9zC+y5TUJBRSuIIMTy7cPOvmubOedOUttrJA'
                'etu6X8tqlfCTS6UHzmtOQfqI5AqmmcqiI0xM0+wCH7jwW5YNzO1ttb22yRem'
                'WOONUcd4thJSxD3e5odd/MFNlMDIK5XlIXcuvoRFJKQXkRKoU5VwijUOX7U6'
                '2brlVw8hpJmpgJph2SAu72oPu0RbPER3WhUs+4lVWz0YxlsNTskEC1ebDgg0'
                'yORdpJKsN6WsR+6d1j2kJS0t3HGjqxZbzQWESaLgr7nU4I+H72kiFy3cLrh/'
                '8acFZtfKfe2TUW8tiYOKAl4R7dliT9VdSzr6BKg2RFR/85Ozur9c7KPs1ev3'
                'L06R3wbUiwzK6GbXmAGdZsU7s8o5AJI0nJIbru4xlxak/mQfEqouQnfu5WX7'
                'qdq7VpJaiFeobNdXnxda4TGsltSZRsmQJCKw/nkcGyAW35AZxCj9ucdkphIn'
                'Soau8+NtGUsXNxevQEJ5WBmM0EpUut7KQ2p24jxujWQJR2Asiw2RTDbjnZ8k'
                '0Tn56q+SZge98ZzITzGtI9+yiGy0jt2hO4m5CNq0wb6/yW25/RgzW6BnlB3M'
                'FaTkW1clJItFu5DjsoIJ/IL8YZ7PM2XsKrSQTmVyjztDGyoAc4H2s68XrwiU'
                'tvTsNzike4yrW2FSX9wLm9ZTYH1FDHNGU2cT4QGfBbEPPnv6Zpp950BZ1pir'
                '2EIaxdZ4fwYYBnnuxD0ZtFsMfRBXwgMyP+KjvdDw8YZp1YJJkerJIiEhk6mN'
                '3/f96oXe7XQK5j+tE0pD4oCKpxeWQxSlzJ0O5CDIMehfYovWRiVX0IU3ogeS'
                'v7Bnwk3bO/eoj+gR7NFVkxOxgiGQbqY0VQ4nMRiS0io4oRuI4NBHD/cU5E/E'
                'AyeByyK7sLPvs+fxk1LQ0fNDOxpg48QAnSM1uHjCMq2bkkvPTqdXbTu9LLd5'
                'Nv0+y9WPBf5AeTP9TE8/56OoPZOiKCi9IV9jBFbNWIgIkCscQKyARte7H6mu'
                'Iy2l53/a+zEKbRiQSILptpytqd5SMGVFbGlD+4GVi9ITKGX2KyuE+DL9mDPZ'
                'AIeL8cz4UnCcT8GlYpGnzuN0DbkKN4oH7gjRWq64OwTGXnZDMyCjV8PGLCt5'
                '0viKBCVVYzfJbFs1jdxKu0ExK/YG8dxD5T6l3aC5xIbvbOKVH+bHaFzVIS05'
                'd2PscAsKoYq6e6XjRbSp0HFSDPorjqn9Fmw4Bhs0Lu5w3HiVdxqybYJlo6OS'
                'dPdskp6ZR8zBVd2Qiq6XD1UP0TNgc/y3roMefuG7anwFw1zQbMDSGIoIFytz'
                'JXCInXIPLLNd+Lez7md+Ge0h6zElJJJ9nI6G7AHO5Z11sRpqYs5CXkeSVfx1'
                'U4mwIqe5einIJ1ayrfMCljP7qatajVUTiGssRgG2ZncRzt8OmQ+rsRew3SSL'
                'lEBM/kcHTX+c0rE8En6lKaRp8Ngf1RCpmT8OIrbDVmCPxVUbUnvAPD5xj9R+'
                'J4G9j/uR/n+2n1HEH8VTsNhuPLC/DixP3Jc89NnzI7BKiloFTXuHqfH989hE'
                'j6bu3bIt0jatjRIQOIvip49pJwfWEffvbGae6d1slsYX3Lm3C7yq0z7hFvMJ'
                'G8LIiVjav+hJ9LiIRholoW7rDutZhSfcSyW+YEMJjLQGCik9VqmwjnDeJ1ZA'
                'aBmVC/wje5rfXCqPTtO4Vqmb+ZfwTlP/pZe0DYltcx448+T7ukdajuU8SCtw'
                '3NWCTIU23MNL/I6Gb7a++q630m4XeLCiK2Z224K/lq0tZAz54ZxGfNsdZk44'
                'w9v+Q7Pdga69omH0k7TzrWipnx7pcfrB31A1vMGGR10r22D5IYaK2C0Hpjt1'
                'c/xl14BD+MWl2RCK/j2iFnwJJwC338PEn5u/KxxKvKsgYMVeXh5ZPmEhr+jt'
                'kjqGO6yPpe4icZ6IXKRYka2zU2oOPeBcEfHc8cb018GUPk5fjRHdCOYgSm+S'
                'xfZkdrp8bSP2NhQUGK9ph4H30ap2g0HRmHUkUk6N80aJEqUQ4KrY4NP5M6G5'
                'goc+aKcYVk1/aoXVtix3fTu9rtSw0H6BWpJhqMKt7WbCtxCifKAQu9PpADR2'
                '4Dkq2lebes3DgZrdVy2UQvLL7Ti1pSUl1C4GDK5acyCL6q/tUgWmNuCwydkO'
                'sH5QJWCZJEvsRadgOkWCOYkSTiqkJsMQdFEu2MFLxp4pQD9YqyseqdkYG/hs'
                'ShhAcgj4XRwIDL7tRD0yVydfreqBvgLnRuYup9gx3cOt4xCC86mC8C4est+y'
                'DSVyCp7iHa+uxXQGumg2vfnHKT4RR42jyhsB46XyMCH7D2R1c1Xm8BPi3tTb'
                'PVnjmHshxdUodn6V7Dh3eHFPbOcczJIRkDGOSiHns8RAXmzXUSFHm0Gsfz23'
                'mAtdnmLdJGxxr9r6dgPXV0pFbpz7KvhPP5zBH+GlueIWYOYT7uNEVMdt/UwV'
                'NUR0KPosQezNHD9+Ae4N3IZiXH7qixPHiR/d9GmHmYvYPc0fJ69OyHP/JAUO'
                'an1W5Ur9Ncl+ZPxUy/9HAy+8dF3OEcUd4PARZfCEEjGcOIy0J7o45KgD4o1D'
                '9hrwgDGBeeBSSGlOUFiL9GmK03D3jN6s4BulTbXdbFP2N7NLNcdY0njh7KN+'
                'mDE2CpO07dgMhv+6r3jPm7P42JcS0Xntb1NzX1J4n0d3kXlcFngR11oUz83K'
                'HTkxKoEfi+sy5eess24KDJF8XJTyGnNByIsiekCMNA+30bBxt7vkwFcniYAX'
                'l02pcGQixHql4NX9/Tjq+anvQ1y7pBd6y17nZHTR8AKXYKQ05mfg+bcqDJia'
                'KoiiK7f3otWYKo5XnzdqPdS9YX4l1JRCu91CdqXrdXspCBPaNMAhZYqeKOm7'
                'U25kMxKqFgPRJcHnErK8JDShFcxdEa9iR4qOEmlVuaen+Y29s+JnT757Gqvg'
                'Zs81cx1/vT9FK25dit06SjykRIhU/0xyVsl7eoQ8p188wE/RAZoNJTlGu+Xs'
                'H6belCTiSWIcnLA24HdSfqTLkfo2MNPwEQq+rButMMW8z+Pex9TAc631r/kE'
                'oTm1GBT4DE1GB17xkWbXdQdcqsdjVvXv4rCoxjdKCPX3JvHOYXG2X1CuEVNT'
                'egURcY+LVG7UuoP/Ks6xubeTRSo8esZi972WI1+9LuMRAdA6OdA/isRAHKT3'
                '4ABoGJfdv9KBNCaUQWx2SX2aFBFdEZJd3LE64K1ivhoSDxkw7sbqx7LYLJCk'
                'kejKw3L/UmKREOGUQiPX407GyucyG6eSWDZdU+GcGHK0egsnSnAfdZgu5eWn'
                'zeaLsfR6IHCQhmR3ydYaR4/wToRBe4fd6XYqdr/lKCIpZ3PyJZfdDSXnSgGW'
                'KpeTDxJUViPxeLpcQxCXeTYpRruP9WYjdZxHEeMFinDtAHmCAE9PviAZrkyt'
                'bS+7Y4m1UeY6+mU0wlZvC0XoMGzbJF2547jh9OFYx1btn0hsJtyDYq1oPLDI'
                '9ptI9D0jf6nhlLedttRGgkUFaZx4M255WNyoyB0TsQ47oGJJvFMBfJZv0+7Z'
                'yTgnd+h7bcrHGNwPjXgDd5AhU3hqvYpJGWyfGovjDjycVvg84fkwkOoh5qUZ'
                'JcxF2oH+Z0EqeQl/xN5tt+8fpJnemIm0Ef/YHVxu4pSqVjht22JzNlFt4J6H'
                'yw4sDyYxQiTj7VCq20+nqYzDIpmvkeCeT46nJ5C7Wa69cgB6EfIpFDb3Ri3Q'
                'PXzsjyhLgzjVYt7Re3Wovs2c8uk6oUN0E+FMB9aE4yWy1vBt5hrMyko3HqzX'
                'BEcBrKCnv492a1/PRa7HQHkCVwtmdrshg1EfDiF5qC49OH3MUOJtsZJuys7P'
                'XyzAFEmP7HjCl3R33rnLxAUH+V8ifdVdzWmKx26jSQYWu2SIbrxfqyhQHSLt'
                'eBVYSsLDWz9AKj+HkjvlHl/tnfJDclykZzAxdZEBiCq4XlaMSEJxV8nXR312'
                'wRJpxFB4dGk3WzfJd+dm5T9I1PHwI0NPJd+OeGiBSsopuY/I4l1ETAnrQxvH'
                'bIkeNQLnYulw6I5C0VkLOvXxom6u2nFx/vwiJc7VQhmrvwrHizwpr2Np1d3k'
                'COgRj6l4naAeYANMXKzOAYotILt4cGKNW6mTZ1c3F7x2TSrxGNUtANgCb0O9'
                '3OpueCTcZA56TfCO4yVkdvOA3UNuO7Vo2+Vyt8WzT5CSRV9yhkHXMhrUZqw+'
                'LJLUd+8SsDwHhyDEs57w13YjqRo1OLjpH6fhFAkPax6bP1x5pJfdhTnzHUhm'
                'Ccquz0/r49vUUDnu1BVcnoM7XU3rZMg2AoElm3Y02+CRrHHSJtbLG3QtLZss'
                'f51boUdxmgweuL+hZBwTuQuoNmdBG81hE7BjlGSVl19AuFEeD9Nb8DhcFgtH'
                'AMu799zzxRJZ1HTWhn/cpeOxj33nMo8Pqwi8iNl9QA3nqicnASoF3ExjQWhO'
                'tQbKGu+njR8aqPY4UqQs4scMZxw+9nENYm9nZ3nglSzSdmmLGYhJaygLojA1'
                'o6xAAhJDUk4XtKVhzi3DZgcYmplb+t0GDV9yf9VHSDF5xSgdc0cgoiqvNSog'
                'WeCe6CyMnowjmGTp8/rCBpph5/v6fJ0fzSD80BEVcMQh40kNd29qsq4pVaqa'
                'NTDOsOXFlQyShQRK9sAURcO167TNp2qLif/FRsqcImJhgTcojUH5sepEsL8w'
                'r1SN2CGUPB4X7ku17rSaF3zo3IJCH659YmLvFI1iMFh0yMcI7GaBrcNxE+C6'
                'GYGK3iVRCBaeyCBWd/Y8z4pFCa5mFZssaZvXaT3X935grUJdZgUtu253S25q'
                'ZW9TGsAPnQIvdpR5xK5UFOmsdJY11gmHgqhqSZ+w7n8SkYIOTfQAnONPTMOP'
                'T3KS9lowmpsWqyIE+7vMrqC29OTRMAIrhVf6zGbsFsG8mUkNLBfhRaiOD0Re'
                'Eo/GHo5pOINRP2geEWADdoRlJLNyKercKV6oV8QMywoVUHNsJl7xYIyr2fWM'
                '/THjh9Q0v6TP445R1D2CSECTLB0gbcI2lbBiIeYo6uh36SSqdMUVyBnIv676'
                's5sSxrEvcOsLlYlrThxmIJJzxRUmLO1pzWPT0cBeGN91RL8XkeCmIA+rdsKA'
                'E4i/X/khSoTkvfTJtK4tvOlg4SC7A0R5YPr5/iese2S+79SzbHqfTX/iHJ0m'
                'watNFOOsKki2ZO6e7A2I8zgyfBqYp0iiI94NHPTAvc+bLBOddQdupDvUa3xO'
                'oFsmP87KMTANKx7qGLAtrZ+55T1nOuOL23jymA+x8HR8EFJtN+43Vn+HfOCK'
                '1ymttB9a5l6e5Z3ONeGcOzEHL/BvjBQOrw1mIdUqia647U6sEVyhyhoE1Fny'
                'Q6WY5npdTVdld2MOOqCMoB7StAlAYu9k+pAV6RbKy4Ugu8yvyiSIRzj1Zb3W'
                'fzvhffGEWnvTC0dOHky4efYMhxjknUgnGU4uGhM6bPdOX6qmtx/oyJdZftqF'
                'pEoNQSjQ/qnDQUPNoaC6J9mcpup4DYfVV9KRPo6CEm2ceG4g2GvI6BuEgjtw'
                'h4295o7SabMv5NuVLA4RfLok26YPO2FCgOumhWCiQJ7E01ccp5RIZA9c6qoJ'
                'xLBUn9VvTghuJdxdlX+qEmC6HWb8v9qBaktJNFdijf6CrMTwYN22m7ggX/vr'
                '73mail3fIl95kjvJDFyITJLk4oFLlwzShy7eS6Xuf0wR35xUlFLX7i49+apU'
                'RJQ1fLRIwfBZZ3Q8T34pP34xL7obrNISvv4Ga8JcbbBRzP5isLEcPdnDvGna'
                'Upqow9iUStpWK20l6KjWlW9ZIK3m9OKh237QTTHat74UygbwaGB1BbrXKUBJ'
                'YPqVllhkeVkHNVOzjy0pWJwGtnThU0KTog4OaN31j24CiMNTWARIIb1y9eSu'
                'w/OPHFsi12J0jOLETY0jeUzjNpnwjBZVc1snNaMhiVKn3khnoeqq55yYqK2t'
                'fsGnqg5qXrqpDR9hZgA+wAnnFmF0OspF69ijpQwi8PQJebSUmLmnS3fCuSgM'
                'VIdp7h2iqGcKSFdferZIWmZg0atFuhl38XX6/WhowQ+td0LXW/VmUXZmuXM/'
                'Y8cRze8ozB+3hmoW7dVVaG8U5khgXsw2/Cas7GEt13rtSU/YZoV5iXHdiKU4'
                'tDRYjKkF8VO9cYdjh5240I2JIiagJ4kNqFBIOR/OBwRgakXuobLkLTQgqjPy'
                'HyFim5acJ6Z8a4IjtHx4+V5BJeh5forl7MUDrrBiaHwxGj4ye3ZsWG/uylEj'
                'eW1MHeUaWFDx1vp+kqkO1GlOjRxckB1XA6w2jYyCCUijBz06+XtF3cS0qQPc'
                'KHWY0DYfz1Gq/LwIPkNI6s04CmDI5S8Nbmp1ALKeSLx/OU+1DIxhmt6+tIJY'
                'wWqlA6obiLGOXBvB89R4IQFTaIcI7GrmfpDuqZo4lWMGDWrxvaMcXQQ2TUmX'
                'f5gnMY4EY1hqLKDIox7Yvh0hppuSYUbaLzyqghVSWnW5kwiowGyRrXZbPU9y'
                'p2Tvwxjl4kP7XtJqQB01lIiCSaUl7+tmVx2r+e7pahSzEzLp6MLeJwq+h8B+'
                '9DnHWkjqgOTvQr1Q7NqrSIkqOmjcwf+gDIn4eUTYj80+B4gRIoD2VEntRSle'
                'DvciNnGyw0NwPx+neQp8SoSELI3bObgqmjMUrnSX3m6ng6b82EaBfnFiht1M'
                'ECj89d4xkmeTB6znR9E1avjMnHTNzabPJt0oPiHuBGvcPCcUp2840et+haLE'
                '2UCcnvu2za6qO9dB1mb85RJcs1FcPgxF/zDkZJiPzXAOqJq8N/rWE7H7Cp6q'
                '8RQ37gUALz15kxwXO6mrvqEbPpcq4mZR5pfNi+xx5l3vJUnEsSU35QotaCx9'
                'YrR6mBuYqYGRpt1Dsvp7ly4PubFNWLt09TiHd9QiWGGhTcjwACsB5+CIPcaE'
                'Kh413UeQaLi9ZWGMCPZuW+NmD2NoQ7648rxpfZbbx66eaz7So9iXlNj6qLMz'
                'SXIPDH1TWQzKdE0R/8vAe9RxGaUyG2LU2kMUUzfU0mQCFnfX69PLMJt05QoU'
                'Zfh6W13v1uVWXkrhiYuPrLfZZbn8qDMFRY6ojmOaqDaZdmYN+dYbUnhtWYQp'
                'OI2LbYpgwrZZU4ad3rcDx1dRNCpaH6NxNvH+pJJeTOfoXhlrlIQWeu+ep43v'
                'el4xGIcLCSAqM2A2CItTO14Pb7vxHn9/BmXmiK1ICw1+0bfGxxwf7IHnjUNM'
                'XnHguA/1Wh66m5MYhBpIvO1V3cC+Mjg9TOXluu2qcRFRQtEV/eXrRPT7wc7o'
                '+53SA9mlzY5WSXMWpxZULnGsmErOu5VU3uybaDV+JePdPMO6m7k3YsHzysbw'
                '7YVxXrzC+jd1J4p4pfxDsdKJMBdaW6rzJtj+qFOqEk+F7Zzv41jHi3MiE1gv'
                'JtjIQaGFipfoI4mu1tShVEkJg0TMFKBC4SLgyhzwCjaBPZMuJ6uVcy2ZF2Ga'
                'Cl1nxm2lzoWY+nRv61cvdA2ZAICth5OC8JdRPOJIAnpsvRLHXYGqJWsSjRP9'
                'YTUGSSThg0ffJ8KW9lzKpdYaJ/For2QqSbrQ9ZcHWArx1YwC2J87USUJG7iz'
                'YLr9KwbTjFQdKMPreypnUzVOmSu8w7i8RwMrZqcmE6sbAWAvCKzVMcqtqi+a'
                'MU/XqGEb2ZbNdTVGCynHR0yyZ5Ns+tzbOfjtgmy+Ok4CQxpGCQ9mnfX80EV9'
                'kFbr4HER8QNzpMKwPPBUIbOkh4q8Ayn1JoWGZV3oBdC0mptgIrWpR9QL71zh'
                'MKy+wrISk3xrA0WW0AninqytwtNbHTbU6SxACN5u+ntjTGLH/NuqbPStWbT4'
                'ua1jzuCjSaX8JFXk+a/rrjtlh0jRjCJwSPeHlepJoxVaMutOn3G1Q6NOJCFm'
                'y/P/dIM9jin24GWojRd4sLCjtxjhrj2Jz4CaeDoqsNOarah0BP3Xjh5dRDxc'
                'jqH2ZXUFTnTw4mR+Ioi/h9z5PHcPS6fpElCBi6ttRWr4WEGbZM+Lr1vD46Cp'
                '3ePI5c3wwLDcqsTlFvUzJYqub9Cqo299eb2p09ag9yHfgoqKh85a0LX7CKQ6'
                'a1ZbBbcvXXuD9CR2L82dN/FjI/KLSeejsUARO4nwEUYV3V7W17t21/ns6nQX'
                'Kc+l3TaPqNshL3qHmM2a2ql3b1egqmpy4cZiyTzbnh4mfwuJD/hCgXYziCYI'
                'aqw9Ivdb4RFH7MlK0YS09666BjWn1B6z1227kuF/XSuXpb7kdVcnesBFyB4K'
                'CvnBxHM972IiJe6b/khElsHuQE7aMsxskl3uevgEinFzZa3S1OMWgEhtPFQa'
                'PlJKmMK0E0HjGuaUIE2xK39OD6zbHd3DxS74oILdgzs0Z6FDT2mylR2hF+TZ'
                'oEhOdRzpQARawLxJj7put7zxL4EfkXAyKZ+ycX+Dgk/Bvq2vb3rC2qmSCIja'
                'JGFBJhDK7xHfUL0MNlqKkd6VqrUu9fEgEdXRpQ/hKleuStjE9I2h2stGhzuO'
                'J0ofUsOo33jcZ9xuyU6DZDinVvviwSd7N+fBUFGTvHNYhHtdB57g0eJfR2kA'
                'PnFnOL8dTO7YwTVhsfsaGoTYZQ5QIuLhJXj+YTOhv6v4mqTZTJdqGWPm+gby'
                'UTdotdcW3jqelAAWu9nyQ4hcrxcT/WEmdqrpJIA5OpBa2qpTd1s6ktfTMRKH'
                's9o+NkNbwGIQ3vnpdxeRNkNr5/w7mSro27Az7OgR7P8LeTmky6EcHXXj/++/'
                'eLHABJzJqQR91Wew1+7L/2ZU0V1jrZlyJzvVOmg65FImxGvXaweIpwCmDB+h'
                'dSmRGA8VBDjMKP33Fg8jl9W6vZtonz2QJhiYi4sEEjW4+Wt00gyKRuQDaoUq'
                'JiegjgXUN9qLUxpFPcdlbVkdY8Q5xqh15DikdS2Wr4GEwzReycxhvo09H0+f'
                'nE2fFLmT0QmH/FO1bTMsaF1FhDKuAx7J3Jqk93f2q+HeMHRuX3eyEPr+Ls/P'
                'phfRPvGW+sAupdl8/yCTXYJDkDVBm7DA7d7+37743dnLVz++eLuv9/Pp2ev0'
                'cM0NE3kiKX66vH84Um/O3r7bjxHQI44UJSiQ9WzAZHBdbbsBSRPr4HEHXAXe'
                'AtMnfE6HbDRP6OMisDaRu38YuD2B7C1uJoUjs2j62Dm/RYnlJ3mYOvXQttw0'
                'LjR9aWPcHASsfVkk+TVWz+LrRcyAfliuSFcQc3qL5D2iI47RCV/1dq+mCIyA'
                'Su8jHuMoEMwZC1G0buIgOzXEmqyenVPbiV08F0M5t87JA7DznC3wVA7eudBl'
                '5JAmsgXDbc5qB5lVTBoDtUNUTTRLdGCyJl3TGUhStB7GjPAf5eaYi2qd3SG+'
                'E16zWN4PN20hNtiTrVADTeUnxF9FIqU8VXyONnA25IqZfZ4/yTOI4xZmiYkN'
                'xEMnrabVRcymcA/u5emc+GlP2BqCooNZlFKs9Ddl42rwKCjHh0yw3MzgA2/4'
                'yVywRTo5ppOwMn55dcD87mEM4Yrw0MnydJjMnEQSa4q/d1OIGLOiFCpoVAzJ'
                'DUKBTDh6WSUlwmRgjPv4OJV26hjaGJklLqpNnJjaOnXyElO3tgnYz+e0hA6h'
                'R3OeXJZ0ofnJE4yOLLRiegBXkOeIr04GAZfUWyGPomjHtIyH43zEfLiVkYTG'
                'QjV1QFkiJJlFFYc6jjvhAvo6aJsvsO3pMfIyfdTC2VL6oLu4+BN6GNnYk/u6'
                'kE5ArAWEOwoPMSyte7/AdPlcS4inHX45Pwp/x1ws1USAS87YQC4SGaEfb7UU'
                '1G3yo7xI4LbE9BHJaIa0o0mNpDODpukUscbya3pIXXhp9N6rD1+QJxHXH6z8'
                'RLReRlXTIsxOqzrWKWEdyucLdDJeLHL0XnbeelHKRGbwbgt94h7urCNGqfjc'
                'VnAFO1/X7hv52DSfiLbFNxw/5BVo6A7hccdLMswnsJ/RuIiL4IEHLtbAHiIl'
                'gbteads5DRlbw7Zldq1H9/KmxcScY1CMN9USfReLiDKuPxSKCFUDQ8ispLvf'
                'nkZuQVmztFewt+VmDFMz8Rrvmx76DCYnG6u/oaYq5hx7zF5q/W7zAK7dV8sI'
                'ilxOuQjGwQn3zeRxzQxbjEPM1uG1RPZV9nBCWSaDTlh7QjmCG7NE+Y+RP0J8'
                'fPQA5ZWrU5Pw5xyxk3nfVLdJoNJXn8mrduZUwpEugTIc3GZRg5WjziPbqSKa'
                'OqvoOJxIcJKfflk+7RLlaMiKvegqGerNOZOxck8xUCoGx+Q0iVb5CRsaddFt'
                '7SVpTgCAUEuNr0NArwJliv70mTd9Ol0yBr2gdKDmWXnZfqoeytxsQPH5O1X/'
                'daD2a/4ec7xIqCxR3DKvYMjqnQKxuVdYbLBerDoYr9vmWv2AGDxwSl3NvNJk'
                'sZKtXyqZ7OQw2seLE6+neJ2WWNXRMdZUNvVPh6W7lO2mcvYBkt0WEYFGQi5N'
                'MLjFTzCr9lIMU4mXkqIAFtS9un4lc8txMmTsg8tfjcWYud+COhXEoxZGFP+8'
                'SNFMJnCSKyiB1gMXkwP/r3At7SObpkxIuUijia6Glpxafh8Yl9JTHpl2pZsH'
                'XDG729aQjJ/gp5YXP33xud6/pMxAIYEVD09tY/2umz8zAz10iDEyG1qJcdmJ'
                '4UMPdI2dCspz3I8kuEDh5OSEIxwZkSw49L0BPMDk5Zawq5tlu1UsRJXnMXaI'
                '3yjOI/wcEyJg180s2JdX2X27s6V0OZ0suTyhFETPLr6PAQ2dBSZci4iVTO+r'
                'Go0hmD4MAhCDMJqZHLJfYtrKvyh1aYsG6n43waN8d0pkhTvkDw0q7GMjrS2Z'
                'i9H/BywSRHHvVgEA')
            # @:adhoc_import:@
            import argparse_local as argparse              # @:adhoc:@
        except ImportError:
            printe('error: argparse missing. Try `easy_install argparse`.')
            sys.exit(1)

    parser = argparse.ArgumentParser(add_help=False)
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                    const=sum, default=max,
    #                    help='sum the integers (default: find the max)')
    # |:opt:| add options
    class AdHocAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            list(map(lambda opt: setattr(namespace, opt, False),
                     ('implode', 'explode', 'extract', 'template', 'eide',
                      # |:special:|
                      'compile', 'decompile'
                      # |:special:|
                      )))
            setattr(namespace, option_string[2:], True)
            setattr(namespace, 'adhoc_arg', values)
    # |:special:|
    parser.add_argument(
        '-c', '--compile', nargs=0, action=AdHocAction, default=False,
        help='compile file(s) or standard input into file OUT (default standard output).')
    parser.add_argument(
        '-d', '--decompile', nargs=0, action=AdHocAction, default=False,
        help='decompile file(s) or standard input into DIR (default __adhoc__).')
    parser.add_argument(
        '-o', '--output', action='store', type=str, default=None,
        help='output file/directory for --compile/--decompile.')

    # |:special:|
    parser.add_argument(
        '-q', '--quiet', action='store_const', const=-2,
        dest='debug', default=0, help='suppress warnings')
    parser.add_argument(
        '-v', '--verbose', action='store_const', const=-1,
        dest='debug', default=0, help='verbose test output')
    parser.add_argument(
        '--debug', nargs='?', action='store', type=int, metavar='NUM',
        default = 0, const = 1,
        help='show debug information')
    parser.add_argument(
        '-t', '--test', action='store_true',
        help='run doc tests')
    parser.add_argument(
        '--implode', nargs=0, action=AdHocAction, default=False,
        help='implode script with adhoc')
    parser.add_argument(
        '--explode', nargs='?', action=AdHocAction, type=str, metavar='DIR',
        default=False, const='__adhoc__',
        help='explode script with adhoc in directory DIR'
        ' (default: `__adhoc__`)')
    parser.add_argument(
        '--extract', nargs='?', action=AdHocAction, type=str, metavar='DIR',
        default=False, const = '.',
        help='extract files to directory DIR (default: `.`)')
    parser.add_argument(
        '--template', nargs='?', action=AdHocAction, type=str, metavar='NAME',
        default=False, const = '-',
        help='extract named template to standard output. default NAME is ``-``')
    parser.add_argument(
        '--eide', nargs='?', action=AdHocAction, type=str, metavar='COMM',
        default=False, const = '',
        help='Emacs IDE template list (implies --template list)')
    parser.add_argument(
        '--expected', nargs='?', action=AdHocAction, type=str, metavar='DIR',
        default=False, const = '.',
        help='extract expected output to directory DIR (default: `.`)')
    parser.add_argument(
        '-h', '--help', action='store_true',
        help="display this help message")
    # |:special:|
    parser.add_argument(
        '--documentation', action='store_true',
        help="display module documentation.")
    parser.add_argument(
        '--install', action='store_true',
        help="install adhoc.py script.")
    # |:special:|
    parser.add_argument(
        '--ap-help', action='store_true',
        help="internal help message")
    parser.add_argument(
        'args', nargs='*', metavar='arg',
        #'args', nargs='+', metavar='arg',
        #type=argparse.FileType('r'), default=sys.stdin,
        help='a series of arguments')

    #_parameters = parser.parse_args()
    (_parameters, _pass_opts) = parser.parse_known_args(argv[1:])
    # generate argparse help
    if _parameters.ap_help:
        parser.print_help()
        return 0

    # standard help
    if _parameters.help:
        # |:special:|
        help_msg = __doc__
        help_msg = re.sub(
            '^\\s*[.][.]\\s+_END_OF_HELP:\\s*\n.*(?ms)', '', help_msg)
        sys.stdout.write(adhoc_rst_to_ascii(help_msg).strip() + '\n')
        # |:special:|
        return 0

    _debug = _parameters.debug
    if _debug > 0:
        _verbose = True
        _quiet = False
    elif _debug < 0:
        _verbose = (_debug == -1)
        _quiet = not(_verbose)
        _debug = 0
    _parameters.debug = _debug
    _parameters.verbose = _verbose
    _parameters.quiet = _quiet

    if _debug:
        cmd_line = argv
        sys.stderr.write(sformat(
                "{0}{3:^{1}} {4:<{2}s}: ]{5!s}[\n",
                ((('dbg_comm' in globals()) and (globals()['dbg_comm'])) or ('# ')),
                ((('dbg_twid' in globals()) and (globals()['dbg_twid'])) or (9)),
                ((('dbg_fwid' in globals()) and (globals()['dbg_fwid'])) or (15)),
                ':DBG:', 'cmd_line', cmd_line))

    # at least use `quiet` to suppress the setdefaultencoding warning
    setdefaultencoding(quiet=_quiet or _parameters.test)
    # |:opt:| handle options

    # adhoc: implode/explode/extract
    adhoc_export = (_parameters.explode or _parameters.extract)
    adhoc_op = (_parameters.implode or adhoc_export
                or _parameters.template or _parameters.eide
                # |:special:|
                or _parameters.documentation
                or _parameters.install
                or _parameters.expected
                # |:special:|
                )
    if adhoc_op:
        # |:special:|
        #          compiled   AdHoc RtAdHoc
        # compiled                    v
        # implode     req      req
        # explode     req            req
        # extract     req            req
        # template    req(v)         req
        #
        # uncompiled --- AdHoc ---> implode   --> (compiled)
        # compiled   -- RtAdHoc --> explode   --> __adhoc__
        # compiled   -- RtAdHoc --> extracted --> .
        # compiled   -- RtAdHoc --> template  --> stdout
        # |:special:|
        file_ = __file__
        source = None

        have_adhoc = 'AdHoc' in globals()
        have_rt_adhoc = 'RtAdHoc' in globals()

        # shall adhoc be imported
        if _parameters.implode or not have_rt_adhoc:
            # shall this file be compiled
            adhoc_compile = not (have_rt_adhoc
                                 # |:special:|
                                 or _parameters.documentation
                                 # |:special:|
                                 )
            os_path = os.defpath
            for pv in ('PATH', 'path'):
                try:
                    os_path = os.environ[pv]
                    break
                except KeyError:
                    pass
            os_path = os_path.split(os.pathsep)
            for path_dir in os_path:
                if not path_dir:
                    continue
                if path_dir not in sys.path:
                    sys.path.append(path_dir)
            if not have_adhoc:
                try:
                    import adhoc
                    AdHoc = adhoc.AdHoc
                except ImportError:
                    adhoc_compile = False
                    try:
                        from rt_adhoc import RtAdHoc as Adhoc
                    except ImportError:
                        pass
            # |:special:|
            AdHoc.flat = False
            # |:special:|
        else:
            adhoc_compile = False
            AdHoc = RtAdHoc

        AdHoc.quiet = _quiet
        AdHoc.verbose = _verbose
        AdHoc.debug = _debug
        AdHoc.include_path.append(os.path.dirname(file_))
        AdHoc.extra_templates = [
            # |:special:|
            ('README.txt', 'adhoc_template'),
            ('doc/USE_CASES.txt', 'adhoc_template'),
            ('-adhoc_init', 'adhoc_template'),
            # |:special:|
            ]
        AdHoc.template_process_hooks = {
            # |:special:|
            'doc/index.rst': tpl_hook_doc_index_rst
            # |:special:|
            }

        if _parameters.eide:
            AdHoc.tt_ide = True
            AdHoc.tt_comment = _parameters.adhoc_arg or ''
            AdHoc.tt_prefix = '. (shell-command "'
            AdHoc.tt_suffix = '")'
            _parameters.template = True
            _parameters.adhoc_arg = 'list'

        if adhoc_compile:
            ah = AdHoc()
            source = ah.compileFile(file_)
        else:
            file_, source = AdHoc.std_source_param(file_)

        # implode
        if _parameters.implode:
            # @:adhoc_enable:@
            if not _quiet:
                list(map(sys.stderr.write,
                    ["warning: ", os.path.basename(file_),
                     " already imploded!\n"]))
            # @:adhoc_enable:@
            AdHoc.write_source('-', source)
        # explode
        elif (_parameters.explode
              # |:special:|
              or _parameters.install
              # |:special:|
              ):
            # |:special:|
            if _parameters.install:
                _parameters.adhoc_arg = '__adhoc_install__'
            # |:special:|
            AdHoc.export_dir = _parameters.adhoc_arg
            AdHoc.export(file_, source)
            # |:special:|
            README = get_readme(file_, source, as_template='README.txt', transform=False)
            USE_CASES = get_use_cases(as_template='doc/USE_CASES.txt')
            sv = AdHoc.inc_delimiters()
            AdHoc.export(file_, README)
            AdHoc.export(file_, USE_CASES)
            AdHoc.reset_delimiters(sv)
            # |:special:|
        # extract
        elif _parameters.extract:
            AdHoc.extract_dir = _parameters.adhoc_arg
            AdHoc.extract(file_, source)
            # |:special:|
            # imports, that should be extracted
            for imported in (
                'use_case_000_',
                'use_case_001_templates_',
                'use_case_002_include_',
                'use_case_003_import_',
                'use_case_005_nested_',
                ):
                ximported = ''.join((imported, '.py'))
                ximported = AdHoc.check_xfile(ximported)
                if ximported:
                    simported = AdHoc.get_named_template(imported, file_)
                    AdHoc.write_source(ximported, simported)
            README = get_readme(file_, source, as_template='README.txt', transform=False)
            USE_CASES = get_use_cases(as_template='doc/USE_CASES.txt')
            sv = AdHoc.inc_delimiters()
            AdHoc.extract(file_, README)
            AdHoc.extract(file_, USE_CASES)
            AdHoc.reset_delimiters(sv)
            # |:special:|
        # template
        elif _parameters.template:
            template_name = _parameters.adhoc_arg
            if not template_name:
                template_name = '-'
            if template_name == 'list':
                sys.stdout.write(
                    '\n'.join(AdHoc.template_table(file_, source)) + '\n')
            # |:special:|
            elif template_name == 'README.txt':
                README = get_readme(file_, source, as_template=template_name, transform=False)
                sv = AdHoc.inc_delimiters()
                AdHoc.write_source('-', AdHoc.get_named_template(template_name, file_, README))
                AdHoc.reset_delimiters(sv)
            elif template_name == 'doc/USE_CASES.txt':
                USE_CASES = get_use_cases()
                AdHoc.write_source('-', USE_CASES)
            elif template_name == 'adhoc_init':
                import use_case_000_ as use_case
                use_case.main('script --template'.split())
            # |:special:|
            else:
                template = AdHoc.get_named_template(
                    template_name, file_, source)
                # |:special:|
                try:
                    template = AdHoc.decode_source(template)
                except UnicodeDecodeError:
                    pass
                else:
                    template = AdHoc.section_tag_remove(template, "adhoc_run_time_section")
                # |:special:|
                AdHoc.write_source('-', template)
        # |:special:|
        # expected
        elif _parameters.expected:
            AdHoc.extract_dir = _parameters.adhoc_arg
            AdHoc.extract_templates(file_, source, AdHoc.section_tag('adhoc_expected'))
        # documentation
        elif _parameters.documentation:
            sys.stdout.write(get_readme(file_, source))
        # install
        if _parameters.install:
            here = os.path.abspath(os.getcwd())
            os.chdir(AdHoc.export_dir)
            os.system(''.join((sys.executable, " setup.py install")))
            os.chdir(here)
            import shutil
            shutil.rmtree(AdHoc.export_dir, True)
        # |:special:|

        # restore for subsequent calls to main
        if not have_adhoc:
            del(AdHoc)
        return 0

    # run doc tests
    if _parameters.test:
        import doctest
        doctest.testmod(verbose = _verbose)
        return 0

    # |:opt:| handle options
    run(_parameters, _pass_opts)

if __name__ == "__main__":
    #sys.argv.insert(1, '--debug') # |:debug:|
    result = main(sys.argv)
    sys.exit(result)

    # |:here:|

# @:adhoc_uncomment:@
# @:adhoc_template:@ -test
# Test template.
# @:adhoc_template:@
# @:adhoc_uncomment:@

if False:
    pass
    # @:adhoc_verbatim:@ # docutils.conf
    # @:adhoc_remove:@
    # @:adhoc_uncomment:@
    # @:adhoc_indent:@ -4
    # @:adhoc_template_v:@ docutils.conf
    # [html4css1 writer]
    # stylesheet: README.css
    # embed-stylesheet: yes
    # language_code: en
    # @:adhoc_template_v:@
    # @:adhoc_indent:@
    # @:adhoc_uncomment:@
    # @:adhoc_remove:@

    # |:info:| The following list is kept in sync with MANIFEST.in.
    # This makes it easier to avoid discrepancies between installation
    # from source distribution vs. installation from compiled script.

    # @:adhoc_include:@ MANIFEST.in
    # @:adhoc_unpack:@ !MANIFEST.in
    RtAdHoc.unpack_(None, file_='MANIFEST.in',
        mtime='2012-10-26T12:21:09', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        'H4sIAESf8WEC/3WSy07DMBBF93xF1khxSys+oBJBYlEWwN4a7Ek6wi95JlXg60lKSZNW'
        '2XhxzrWvNTYF41qLxX73+vJcvX8oCsUd/UP4wpocjuCt2j3tK2WYr5F0MiKwh2hU+r6A'
        '3CTIjNpFA25qbDSrm5YBahYQMqvTWaWLTSy3G0UmzlIXq/jYzJSJob5uomCxU5llRn3f'
        'rz5hDn9KD8zQYPm3iQ9T3Qo5VkPFSAN45AQGtSUj02ZGadMMSKbQ1DF7kNuRtP2cDPTL'
        'er3WC+JBC/rkQJCXIht9hkuBrSafYpYl/6gDsqA9+YymzUzHYRyTR+6vwVLczxPYnedE'
        'vRv/wi8ZvSj5aQIAAA==')
    # @:adhoc_unpack:@
    # @:adhoc_include:@ Makefile
    # @:adhoc_unpack:@ !Makefile
    RtAdHoc.unpack_(None, file_='Makefile',
        mtime='2012-10-17T07:01:02', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        'H4sIAESf8WEC/6VWbW/aSBD+zP6KOUqL3atNXhSdZI4KmjjXqCUgIFIjneTbrBew8Ju8'
        '615a5cff7BqDwSRFOT6sdmeenZl95gW/Aeu9BRFd8XkQcnUgRCapJzLmBxn0wCaV7UMQ'
        'F9tOLrJOmDAadlBGyPh+9nl0601Hd5NLdwq9fcHvPaD+MmF2+oOQwdXn0aU3vveu3LFW'
        'DUv3E3dwNXRtJgT4CctlEAqbJfEcBJd5qi7X7iKuoyCo1Hv1FPuBSn0oDR++piOywmSR'
        '2OL7Qos8IakMqirr/MwOWFK3IGQWxIt5kkVUepqKg/HRbJHSTPAXIDGNuEgp454fMHkQ'
        '0jLupq53OcBl9m2mxSYhNZmC5uiLUVxOTk48ZexXqFNP8igNqeTiKPyZF8QszH1+FPrc'
        'C6I0yeRR4Asv5kJyX4OJ+202GXhXN9MZFhS5/OoObq9vvuryqhw0O+tyG09Gf00GQ+Rm'
        'FzAc3N5cu9PZnvg9umF7sip9KopntRXaXsRt6HoRVdL0Iqik5wCIYbh6PdXrmV7P9Xqx'
        'h9W17bElZysvSvw85F7RXvxYoNw0fEk4qCSkVIr8QUh4+8EPhOy8/bBJzHoOmFi0Kp9l'
        'Grf7yhTYldZMPKPepn5Pv60idF7Ehfw5oNbtUGpoTXkEy2JJlKqR1PoTPrb6pMGWSAH8'
        'cXEBeCI+n9M8lA7QMCQEFwc9bRybSmzphtfKYuuU400+ynK7lFGoBw8OVv5oZ6KYW2Wf'
        'TBWWEBZyGjukgaUmwfoJ7ZaxzZTZhqcnyCKwsjnsKAgJYpxnW/8q2Ea0UiPcShFbjHOT'
        'NPpGQ//+Jo0Qeei167S2u1C6b7ZaCtVEv+oGjkBIs2QBQQyFpouPWJsD4GyZQJOl2mVL'
        'Azeem9016LC6W9jwk5h3NwFun+XAzvtgLtMiww7+h9GFsDKGpC147KmTLZaY1rJnNaCm'
        'xacwXtqoMNVfV05ZH86mcDDYnWFtVq6pK6SR/pDLJIZnS0tlz1Dpw+z1u8AfAwmn5n7B'
        '4dvKAvgNrH+hI7LvHRR20vxB5UFTY2A0w8EX14SCwN4OapcspLFSg4dqE/+FSQMr8kwB'
        '1pGHCV1ZPKJBaFHfz7gQXOh36CC3NpxKZ9UJKJPQw9d/1ORWO+AVd3f6ZSc5B/42jzFq'
        'j7H47x3VjMrBunUMYL4Swbt3G6YVOWYRxbMfD5g5o37zWTiaewNPzpJn3HnCrRP43Ip4'
        'nDvgRpQJuLlycVpiuw1RCBZ8yudznkH/0931tTvp4xUbhtYj/MMRqW+2wTCNzQmaP5va'
        'ibLswOVoOMaB4YBqBH3ZCLkEw8BvFwFNJW2aJhhl3eImZviF1VTfWmCtoKm+coRpHrKp'
        'm6BmU0lfb3NdyXWza8XrLasRUrOKwv/xfqyg+vMT9nqL+t+gblOLX291Kmns08yvGz7W'
        '5n/r1+bDSwwAAA==')
    # @:adhoc_unpack:@
    # @:adhoc_include:@ README.css
    # @:adhoc_unpack:@ !README.css
    RtAdHoc.unpack_(None, file_='README.css',
        mtime='2012-10-10T11:38:17', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        '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')
    # @:adhoc_unpack:@
    #                   README.txt is generated
    #                   adhoc.py is this file
    #                   argparse_local.py is imported
    # @:adhoc_include:@ doc/Makefile
    # @:adhoc_unpack:@ !doc/Makefile
    RtAdHoc.unpack_(None, file_='doc/Makefile',
        mtime='2012-10-20T09:35:57', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        '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'
        'ORHh1PkHUfjTfNMaAAA=')
    # @:adhoc_unpack:@
    # @:adhoc_include:@ doc/_static/adhoc-logo-32.ico
    # @:adhoc_unpack:@ !doc/_static/adhoc-logo-32.ico
    RtAdHoc.unpack_(None, file_='doc/_static/adhoc-logo-32.ico',
        mtime='2012-10-17T06:52:15', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        'H4sIAESf8WEC/62Xe0hbVxzHT5IlsYZpqy4T3HzNYlbrY7Pq3GRJzWNqNiubcyn+k4HQ'
        'gZgOK8xlLSulo9tEqLRULJN2MKxVR0IowXQgPrrB2DRjJeBIMbGdpMQmMcYketX727lx'
        'KdKa5t6bnvBNbm7u/X3O/Z2T3wMhDn7l5iLqHQ3vR0iMEJJg4VNIhnbORwb+LU20o+gA'
        'AFoKh8MHLBaLtru7+3p9ff3vEonkYV5eHuTn5/vKysrut7S0/Nbb29tjs9mUJEkm07Ub'
        'Tw6Ho1qn0xkyMjLWqenGE4fDgaqqKvvo6GgXnsd+ttxQKJSJn/WmUCgEOty9VFNTY5+f'
        'n5die1wmbLvdLi0uLvaw5VI+4HK5kc+UlJQNg8FwBtvl02HPzc1pxWLxOlMmj8uD5vxm'
        'MNYYwVnnBK/KCy65C6bfmoZzknMw9fNUdzw/4OdWYPY2U3ZachqY3jWBV+GNKZfKRYYs'
        'oT7M2bcXOxgMvlJSUrLMlC14QQC3Zbefyd6t8Fj4BuYJnuTr9fobbNb6ROEJ2uyI8LoQ'
        'vxKf72b7/f5ckUhEsNlns4pZZnws34c+glwlC6N8k8nUxubZj2QeYcyOKvRj6If/+fz+'
        'y/3fs+H3vdnHmr+iWfHDFqQCCfuufXxtiSk768UsWFIuseZT2rRtfrT516bWprQBj8dj'
        'xL9adTUhduS/MBLuCfWHblLHxwuO02Y3v9YMXqU3YX6wN3hrtXN1njp2KBxwOONwXHZd'
        'Th0VSxJmUwqcDkzifbAe/U7NQVOgicTuJ7kioQj0xXpwq9xx7U4dnYLOok5Q56gj0kl0'
        'YJFanvJZ4KvAL75jvqfun5PPwfmS89Be3A66Ih1cqbgCDpUjLvee4h405TdF4kIs39kV'
        '9sfXr32zdsev9Xuehy9tchscPHAw7vodSj8ETqVzJwb0h0yBM4E/EmW7lC4ofamU9v7V'
        'Fmoj9xEzRCeOQ5cT5Z8qOsUsZ/EF4GxyEmSQzNz6Z+uTRNh35XchiZ/EOHaavzMbIrmY'
        'hGR/m/8hW/7J10+yqpGMRmN7NP+s31r/lg17+b1lyEzJZMW3Wq2qxzmYgCz/p8x9MPbO'
        'GCs2rts929vbwt01AN4Hx3zv+zZo83EsUbyqYMUfGho6vUcNxiX+JNo8H3gIOvxL1Zdi'
        'xplnSaPRWHFfkBSjBuU/mH3QYpaZN2Lll0eqR3Ch/ALjfEmpoqJieW1trSBeDW42mz+T'
        '5cjgYvlFmDk6A1aZFSalk9DzRg+UiktZ+byysnIZjxK6Pcj4+Hhbenp6mG0PsrtGbG1t'
        'ncX1dS7THmxxcbFarVb/zZadnZ3tGRkZOYvXW5BAD8qfmJhoxfOwCQQCMh6Tyt3l5eX/'
        'DgwMfI175pefVx+MJXS73UXDw8NfdHV1/dTY2HhHLpc7amtr7zc0NEx3dHQYBwcHv1xY'
        'WHgbX8ujbXcSX4rnvYWQFDd9OSsIpToREk4ixKN0FiEOJcRscKL3Re1QNrH9VMzJwU6U'
        'UkyK/R87YiMjvhAAAA==')
    # @:adhoc_unpack:@
    # @:adhoc_include:@ doc/adhoc-logo.svg
    # @:adhoc_unpack:@ !doc/adhoc-logo.svg
    RtAdHoc.unpack_(None, file_='doc/adhoc-logo.svg',
        mtime='2012-10-17T06:44:09', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        'H4sIAESf8WEC/+2cW3MbWXKt3/tX1OG8TMcBwH2/sCX5oSccMRGeF9snzjNFQhLcJMEA'
        'oZbUv97fyg2QFAXqNlK3w9Ht8IioKlTt2jtz5VqZufHkX95eXky/Ljc3q/XV0yO/cEfT'
        '8upsfb66evn06P/957/O29F0sz29Oj+9WF8tnx5drY/+5dkPT/7PfD79vFmebpfn05vV'
        '9tX096tfbs5Or5fTX19tt9cnx8dv3rxZrHYHF+vNy+Mfp/n82Q8/PLn59eUP0zTx3Kub'
        'k/Ozp0e7L1y/3lzYhednx8uL5eXyantz7Bf++Oju8rO7y8/09NWvy7P15eX66sa+eXXz'
        'l3sXb85f3F6t0byJdpHvvR+7cBzCnCvmN++utqdv5+9/lTEe+mpwzh1z7u7Kz7vq5O0F'
        'U/HoYOzs/acz/df8/+0X9gcWN+vXm7PlC765XFwtt8d/+8+/3Z6cu8X59vzebfaz/95z'
        '31uSq9PL5c316dny5nh/3L7/ZnW+ffX0KCRnH18tVy9fbe8+r86fHvF+wT7csx0/zu7u'
        'dHJ7xi1SW8SFnza9tWIX7Qd9cr4+0yieHp2ev1qfzS/WL9fzX8OcKVxoCp9x8ZPz5Ysb'
        'fWk8WZ/S0XRsp27vo5uc/7pavrm78PnpzXidabo+fYmhXKw3T4/+8sL+2514vt6cLzf7'
        'U8X+e+/UmulZbd8N19jde/+Cuuvt+YNnb16dnq/fMHMPT/62Xl8+PYqLHHP54OTZ26dH'
        'JSxKCzH6D05qLL4vcqi1PTzJbL6W48xfX622GOf12w++/nqz0QUXp++WvLL9s3/jm1fr'
        'Ny83mrrt5vXy/sHXq/PlzXuHb29o5+bPn6/fHj5/c3V6PX95sX5+evGRC67Wjz5g3IBh'
        'cf7F6cXN4Qu26/l+lAcvWj//r+XZdn59un312CVvVlcs1nxn/L778sgVe3/wzrdHLnl7'
        'wCB2p949fury9O3qcvXbkhXYr/uL1ZbDm5erK17x+u6r945fLF9sD57YjGEeOPN8vd3K'
        'AN29RR72/tgcc8F9gx4XPbOrntzZAqs0vjhN23dCnrfvdOxof1C2pQOht3x7cHl5LRCy'
        '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'
        'hvZEP+z87If/BprdwG+aZwAA')
    # @:adhoc_unpack:@
    # @:adhoc_include:@ doc/conf.py
    # @:adhoc_unpack:@ !doc/conf.py
    RtAdHoc.unpack_(None, file_='doc/conf.py',
        mtime='2013-08-24T06:03:38', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        'H4sIAESf8WEC/7VabW8bxxH+TvRHLCQERwbk2ZKDIGDjILZjxwbsOIiUJoFhMMvjktzq'
        'eHu53ZPEVP3vfWZmb3nUS6oqadHW5HF3ZuftmWfndKgmn05U4Ra2Wk1VG5aTL+jJ4HBw'
        'qHK1cEW7MVXQwbpKzVtbLrC2WtpV28izpS3NWBWN0cEs1HyLbb5e2+py8ltrizMfdBMU'
        '1p3ooE5MrdQX6ujz6WefTY8fq+PHR8c5azpdW8+iFP41l6agz8PRQl3YsFZhbVTRNg0O'
        'oha2MUVwzVZ5E1RwygZPRwraVjCBfheR37lgsBNqKxeULktVO+/tHDr2LTjXZWu80o1R'
        'dWM8KbEVdloPKboNbmUq07B5dCqR/gzybhWz1udGabUwS92W4e/dYz4IqSjchhwKYa4N'
        '5CzTYAPs8Gt3wZbGrflgYDe1g/f81o+V8wOsfrOEd4KpPDR6NXSN2rhFW5ICl4IlTqOT'
        '48mItcIgDTesTbNz4JjMWyxIpzfpsRVZ0JnXGmKwxeSkl4+WnI8wNaaE5XJ4/Ahp+9nS'
        'OBfGqoVsJ7JyPfcsExs2+gyngkvm3pVtQAqVFk/ICZXoHBx2Z8htBS+F4ePxdUnDLM9G'
        'o8HgXivzR/hvaeeP6m1Yu4o23m8fqzhUk4n6ljPheuQnD/lPjObWtc01v1XGLJCOaoOE'
        '3kDZCZeTOjcNRX2sUFKBfRfdxOtnUnTqqcqO8scZSX+G2Opq2+1PeRNTRlV6Q/kKIWOl'
        'PcQ2qB+foxbNVhUa5W56yQaBSF2qMM6uKHRIQhYqE+05luefZiOFvGTDitYHt0H5G58P'
        'eon7VH3ob4mpmo33BJ1bcwFcMtnHvjUUlFhOsepVMJsaqZiM2U9MZGpK23yQ1s44E+kg'
        's/RMNMF+5dvl0l4qt1QedhSGK58dlg/kySwugcPzxoes22kqwdJrez3ls2xMK7CV8Xbi'
        '7Srt32gfUKXBFaExJqVGPpAfZnhAG221MJe8qctJWy1ds5EU0nOAC1ds3bh/wvZ8ED9g'
        'b5s9W7yGtweFq7eNXa3lIcD4aMyQPFY/uXK50jjiSUEubdLpYhKyMgV9fR0U8qzZHRkm'
        'IrEKwLMmsICLC8PwhH0QdxVlXSGsC3WFoBntzRW2lN4RbCwItc51Y13rlWAXy6DoN65d'
        'raONkEWNKSTFvuspjCcA0J/zX7qT56R5Gr9MrwadQXDp4/xJfpzFjcsWAJ9KzlZF2XLM'
        'dFmv9aO5CfpRU6igUTCDePSejCikhAtbvTLsKcpWsn6/o8y7+szVD2bJgd+HA4ii3Rr4'
        '6AMnVVtTV8DeTjzZm1Q9ReOrTDwBokHoHy6ccnXg0iNhEgwy5wqFp7dXU2UsOXhMMYyN'
        'Fc+5EbgNebhy1WSJyBhpaGNyfEUghPKiWE0Hh7IFTiAfvsTSsUiZLTdpGaUCpYykarQM'
        'yLMMdoPeiC6dR0G8C8I+ea4+WYzVJ7+wV99GJ6B4UQyV3y/2WG+7Dic4AU3FWqqQco0a'
        '1X6zs6vKwU0XZFLp3Bl5ho62X7/mkpLAzDrdAh7MiXbA0ZiT066DowMCZodst9QKvLDR'
        'zVlbT9WvARj364jUU4tkTyDl+jkcxcxYzC6u1IsbCkE2HGVAY+wCUuu6NsCEBQmcLtuq'
        'QExDkYOZgfVMGsotAA/cRNA6OETjn9EqSgpYRNSKaAAZdQrhe3r69KvXO5JqsKadbjbC'
        '+KKxdUzftkKaBBvI/UPfIhRIgjxXnfrpdBQPJMJn0phuOYg3vAEVtCZ3ATZkR3wgUUUu'
        '+HQ04RNM5yiLgRh1G2KLY17EkecyTLTrkDbNRCYd4xWlfRdfNtwJG/p+u+JQwaotqvVS'
        'rQGmJQEqEmiEtN6WJsYX+BsXz+Tx067VSatO1d0dCD5FdzFSr9HpjPlIyobk45wbaiN4'
        'NCNOSWHkPZSWHyNfed8r+ten795GB6gH8hVyAAzfmH7WslyKBX94bcoa1UmgpMD3jdDG'
        'PX4j8L8DNAZvCRH313XYlDNRAy/FsHSYSt6PRjGy0ZOJr01hl7bgYwjnsL+Laipnfrw0'
        'piRtWvYQrLYNYR7O+WoPYJP8c21LTfcFMtPoYi1bKQ/NbYy3f/RZJ+Wp+ldWuLLUNd89'
        'vF2YuW6yKWf3v/8Ls4n8STxzD3Zz2DtAx28+7qVuwiECeRgbedwOdhSVG0HNmNA9ep9Q'
        'ElIOvoyt/it1/mXsel/t++AgHYIKvodaz6QXU4fjXzryUOlzu4rXS03B+CaCp5VO4enU'
        'AIyd0E4Dy7uhp1+k4LBg0CtBcDW823MMw0wulBbeFFxNeCGFHoPWKS7dyt1PI1FlyWxm'
        '7chQikoCfZi1hPmIdtQkGUVB2F2IYWaLWzdBvPoJ9e4uvOItoiLH5xF+pZ519Pnl0edE'
        'vp8cXz45hrAaEFJ6EIVmZWJ2dgpRWnqxdsWErJk8OSY52f3SMZoiDTUhuuCaXxsT/Ehy'
        'FdL+IFt3KAwiaokbLDk94KwOEvqaSBqIoRa75d5x0IF24f2BgL4DabtobDB7gvYWRk+I'
        '8N49QB5IL0cR0Nggw51Eq+wtuLdq6wVTNnSsTBFfwfpNTXkqt0eyICgD/VtGQDV3Ae6i'
        'c7eewkMHWsEX1Y7xCA9KiQU1s6gm8Z95n/+kVngCHhG232tqP12zY6IBPyNcOERQv7Uu'
        'COVRC43AxCoO29qtGo3CJ76Fq55rKCSKKHuwzCb5NBA386ymZjW7hvwi5oGUxe7+NQa7'
        'qf1uDiGNnCIfV6h4hYoFLPsZIzsktNzgy96djjNwVwQNMY1GDOU+E5WyxzuFZOWtKnXS'
        'MOPNSTUcy/R2jLDv91vEN9H1TszCbVAPMyywxXWqshNz935yrfx6B91KW31dEsmuAouz'
        '53bRwjty9tSWSkOMNLmVtiTxib0k+aWtznwc2ghfFZ4rHRUeEufyzS7eLjq8vZjJUhJx'
        '29EPXsQ5oCS8NJcDtqNHxIQpLJ2jQ/fxnuTta+uGGjc1DV+M1It0gc3z/E+o6V+Eb2gC'
        'pL8HvT0xuoGre9RWgKgrPmFWY642HjZyiOhXnpwIgGr1JbnuK7o4KubkDQMDTTEZ9OP1'
        'StoBjiosQm1QcKQk3nbpsvnjD7CtQRVeoI5lRLq0lUWZRybGPb453086B0u8WMIXtW70'
        'GpttgtZuAJIIXgR7k69ydZBfksCDUSeZftzNQ7q++F64JsvkIycCwhLXxBT59kSpS3Lo'
        'yYxW8kLifjSluMlk3+pT8/PDqexgQLhwOQN/EfoODIhtvNY1OpAn8jjMpKr4UUZNNdOf'
        'yReyO+OPtBJUbm/puOMESwS9k3X0uA403jo6wr8s7OgYn0SSQ3l3kmThNTD0Ab5NjEnM'
        'B9nXmzmzoaz7TAKwmQHt28a1ddd1EiLzTInRRKTI1TZdq0Nb4zt2D+PVV8b3MuMPxCIE'
        '1MdC4sZKbknjpKBAC/PqA4oquEcbXQGsPsJIcXgimdRuBwpukSkW/JIH/rfNUKh9Oglr'
        'lKKJFeuhlSI0G40HH/9augcJ1DboC1NKKmAerNDRr1E+ujAcyEkOdtwZjDmWLZVTk6Yk'
        'EF6CFpRIeU1DpPiuAZ5lUkM8o1jrGhnkk0IqVl5xK4TzuwLueOli7yN9QnBNQ0nDMJ/k'
        'Mc7RDmz4A5mEKugAjfE+SaS57V0S26bck/ZNCjGNAngkQdwQkZEvAIg4IxDv7cTF36Wd'
        'fvj4P/XkLr3uaMrX4EM0i/seACIMbRUNegMRPbMn8J6lJDXU6yVdJTGbYWlx1jGiwW+V'
        'yAqVzV7h3F00Sn1IdfNxrI5Gg48PjDcd4NZoX3PsqbnkufADkfk+qNWp+ItwCzsIFRS0'
        'tBLQa1EpkFkrQoxBEM1/BGL3AzD6H+UPvGv26ASNNeO0XnZl76wH1yp1ZVzrE+Q9pMa6'
        '0/+ZKtt54I46e00vMB0cCgaqt/u5hc5ETAxYZ8gBlcP/Uxu0Ffkh64nvZ9puzy3p9rJu'
        '539yoPXczkvbXYbUNy2+VWCV/MJ06fKBgYo0YUBsM3kS541Pd3GV5zUJ8PSi4sZPN961'
        'HI9Vt+D624I4deBJrXqzN4SRmVZa2I1Y6SJQSffp/Yz4UW/xhi6YfIreW4Is6fWFjNVk'
        'N+5kuAcuLXHm021Nd8S4QtrWm5Pn35E+RLeTGgX0ZbaV/a3tC9s3ijlnfMWoRWTVbuam'
        'EVv6L5XWbmNiK2ZlPZGdwmfX1RVp0LjTGbe3dtHbx7jR/+sBHnXTCCEyCR4o8nduF8RS'
        'dzfL3jvBwxjkcz7WkN8X93jztTtsmhfMzdLJFDPeF3Z/RxH/iiJPZJJfmFjfG1QK6l0/'
        'Ps8z6NzdsExSszEzOUtX973j+TuOtxvI/L9P53y4drzdSPymCymr6b2DLs74LWGsCxLV'
        '/YkGi+3e2OxLPuW/sahxji4neciLL/EVnecLpCvyqrjsROGr7Hmqngzk7z+AdgvYSNlG'
        'BLLgBmJ32UBb2rqHj1dTmopNr/BxilSdUNeZqpcbXXj15puX6h1dEd9RK5qo52D88P3X'
        'z3989erlD1/zH+O8m1yqXw1W8s4MaTZM39TB7wecdSR5ql68f/f9m7cvp/yGkjcPcUdR'
        'wyF6oVcH9PRgNFLDwm1qJsswHXYQqT0zanKmDhStHI1ukwmADzdl0tOHy0TOBc135Wti'
        '4w8Pl1yURlc35fLjh0slJLgpVK7F95N5+Dd6n+kIX/+hG0s56Kd4hBYMRbSe0paGnpWt'
        'J/tPJyv6RNeVpiX5ZkJdFE2W4vKyWkwH/wFpPLyL1yUAAA==')
    # @:adhoc_unpack:@
    #                   doc/index.rst is generated
    # @:adhoc_include:@ doc/make.bat
    # @:adhoc_unpack:@ !doc/make.bat
    RtAdHoc.unpack_(None, file_='doc/make.bat',
        mtime='2012-09-18T09:26:21', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        'H4sIAESf8WEC/7VXbU8bORD+TH7FKFKk9gSJkO7DiTanawsITimJINX1QwV1didZN7v2'
        'snZ46a+/8ctmX27jQ0CRIMF+ZuYZe/x4/NfJp7MpTE9Pe73Lk8/wSWYZEzEseYqwlAVc'
        '5QkXDxDLaJOh0ExzKXo9voT+4Gp2dn7x9eOX88nxoA/jMfT78Ka3p1BDbWqsrIeDxYan'
        'ce9tz0zbiePzy/GNGzVjHyYTZzWdza/GBzEMStRgRNF1gahgUEEGMLR254d/XNQMWwgi'
        'ejGdE9nZh9nJZZtmK+YxpEzjw03OcixuFP+JY28HgwZ04MxboYP2TeyAFsIt4mFJaSW1'
        'hATTvDlhRizfIzu3h1Eih7MUmULY0O/3jK0Rrt9rVqxQX//5He4TLOojwBVIgSCX3hog'
        '0VkK7oeCWg9K07az1ADP5p8ntgDU1iDmRWlTGlQoECzDGLiI8WFoYVwYC4y0LHjNi+Ji'
        'laJFlF6YH6SVI7aV061NzqM1Tdcj+6Emwx9KilZKf19NL1ooE9usY3cepvCZG7CgvJA/'
        'KImt9a32tgFrj2mbxnhX2u40PfaYti3mm0UrNSbs6BZi664JmbA5fnX+9+FRbiAiI1O1'
        'tiLH7Heg0+2+p6g1Fltn5Eq34tmh5lKSTEALRUMblkLOVjUcmXKxlHXc3A81Ha4MCxe5'
        'BM6mkKFS5I/Ya6rOVQWPEiYoTmtV5B0Wdxzv7Rdgaepx8YjFMf2NMae6pNWietWYVe5S'
        'LtZRgtHaunPfjDkxwkJQVgagrCRyoXFVcP1Y7S7pE6qSerER1tSPKsBsgSa6ORdUHk0x'
        'BTrtKNgixbi3Z0UARdyWh4gOvLAyYAiMSBwH3Hh7U4nkt9/ekmMoMjp5MLqFkTKg3l6M'
        'aflvDbs7lDkiNlJD3+Fg4VSjJYR1lTbzvT2TTlHIIsU7inxIC8g1jBZw6FfLf3w0wk8V'
        'ILhKMB7CPPEnwlYPMJIwyq/lfbibtleobualfAXIe8iv4+8DBFKo5LE7i5p8BhKpUL8u'
        'lypGIB0n092peAkPpOEQz0zhHQh5vxU90tOIVMQevfrdEeBubpNu5vaeCfA286/OurrJ'
        'huGDu+0WOg+vvV3+5wC7LuMV+BsVtEV0ZqL+I4u1SmQO91wnNqfr3jBJtpedazj/e+IN'
        'nUDO7rbtztjfxIF8HeLVsu3fRjJNKRlS9RUKLBj1P/1GxrdJFEzZMdqny8ZcuglXRz42'
        'tXFd3uua7my/2Rjeai7BXoYmul0ME7LmkinFTeOn4aByfmpodfhdJVFAfl3vskN+fWMT'
        'kl8Hea5k7SZm2qRuVratClByDdYLJNQGcJusWvtspgKkbTvXzdp1egHaFvDsmjaVUusc'
        'O7Tf+g9wNz1cN3Xb3QWYm/kXLXjVpXbwNpMB2hnbIfimzw2QpukXca73zB2saTq81qaR'
        '3rnctssOr7iBvCiBRjPfve5mPpCFb/y7syhfBe0HdKMkZcSe3Sv4bWg9M7oK30YJ5OFf'
        'JN15lM+VwG54yJPzMLy3751unfEuQ1JTvnt2yM32WRSSnBL0ZOoTsvCPrEhmOT1A8R2k'
        'Uq7tA4uJR+dFlS8mtqBEQW50vtF0j9pHWCeDkcMMdfCw+5fZjtvKP+ZCt5WDPH2nCEwt'
        'M8hl9Sj0mSm5KajP25bjvlsGpn3LUKDapLq9r97L7myPzOe/zV7QttwTAAA=')
    # @:adhoc_unpack:@
    # @:adhoc_include:@ doc/z-massage-index.sh
    # @:adhoc_unpack:@ !doc/z-massage-index.sh
    RtAdHoc.unpack_(None, file_='doc/z-massage-index.sh',
        mtime='2013-07-10T07:24:06', mode=int("100775", 8),
        zipped=True, flat=None, source64=
        'H4sIAESf8WEC/81Y/3PaOBb/nbk/4tXJ1fYW2033N5NwJcRJuBLCANlOB1IibIG1tSWP'
        'JUiyIf/7PdkEyC7ptr2bzjGZYOvpffR50vsm9l55E8Y9GVcqe/CHkxIpyYw6jEf0zpUx'
        'ONCIIpBqPp2CEnA+uGiDlQmpnMmcJVpCM1vrzrWevwtiOGUJBdd1ryt7ODG4I2mWUB8f'
        '9WeHwmEvaJxcBG6s0gTq5bB+1ss0RXafs1mswGra8O7twbsqfBTJdEb4DPphTHOaV+Hw'
        'achdDQFRMEvv3IjWCxKDmEkoeOF3RnIFYoqWxiJ0Ue4D7IEMc5YpiGmSPSlkuZjlJNU6'
        '05xSkGKqbklOa3Av5hASDjmNmFQ5m8wVQisgPPJEDqmI2PQeYXBojvbkoGIKiuap1Avr'
        'l7POFZxRTnOSQHc+SVgIbRZSLikQXFmPyJhGMNEwWuFUM+ivGMCpQFyimOA1oAzlOSxo'
        'LvEdfn1aYoVXBZEjhoVbgrRzEJlWs5HrPSREbTTdzVZtWb4xMALGC+BYZGhNjIBo3y1L'
        'EphQdAg6nSdVwJmI8rE1OL+8GkCj8wk+Nnq9RmfwqYZzVSzmCuiClkgMXYMhMNqUE67u'
        'kToqXwS95jlqNI5b7dbgE/KH09agE/T7cHrZgwZ0G71Bq3nVbvSge9XrXvYDF6BP6dPO'
        'IsYLezstTgc3MKKKsESWNn/C45TIDB08JguKxxpStkBeBEJ0wL8/M8QgiUCX1Bbi3M0W'
        'utCaAheqChL5HcZKZb7n3d7eujM+d0U+85ISQnr1KsIgv9ucoTdh9H2no6O2890fVFou'
        'l76koY/fcHrVaQ5al53+j4FVirQAll15qOhoL4NqrIPqyChfHP1iFFILjP2HrSmPBuw/'
        'HLwx9t8bj1r0Fgcw6OteRBcen6OfjQo95Ln/0A9OxuNu7/LMkTR6BIeD+WvV+zz8vHft'
        'PdRWD1Etqz2aK6xa5VHvkaVPhoOFroBuFzkJ4xQObEtylmFSkjRXDgYwBeOzjMdTl9x+'
        'GS9IPqYyJBkdS6rm2b4ByrYrE7ka3Vic5YyrKRj/lCNu6IV/QSN28DVldTTCP/w3MzUx'
        'LsbfCKdn7yK10dqDltL+hukmxdwNONuUGL0Y7FlOFUxI+EUmBBOMHoUbZwEIdrQgyZya'
        '1RVELG4xTtHpUlS3DmyIBE5HV17Jl/7J8Zm/hBUFTAWWwFTNOEkc1LB9GK4Nun5ZR0+F'
        'p8836sy2lb5Rh/+ATvonne0zKtXWk4+MbWHp342PH8a/NXrjoN9sdINx8zxofjjCMzxw'
        'zJFrPu6c1Av6V+0BzrLQZ7Ss9Bkkgj6+AIz68IvG2IWNnuY4YB4HZ60OPJS+U2rUAKNg'
        'O5AON492yUNRdJS7l5GPdglLttrDl9tb8fV9+EYTtXSNWeSDF5jZ/43ZbPq3lr/6qunl'
        '5sWUV54cZRWz9dfvnuLWpHkuch9mVLcIoijXZVC55lqN3qHLHRSvU6ZjfM3r4A3Gd3kE'
        '+ACvX2MeDAlWMy3DccYrzuhfSydeOkV2tcvurFZCvq3VKo4TiXC+GsfdwkqdbImpJOH/'
        'pHxcNFqdH6wc/+6Pj1uD46vmh2BwZB6u2jF1n9EjQ9E75f1OFqQcNeqHr1Cl3DbPK1pW'
        'AirHgs6wWhaZTddPXbOveu2qPmS09Cl/AeVFK3NTdJnmyDR11b3x9JO7QQ0SipUW86hI'
        '5rpjwh5QpHBCFiyCZkzSCXZNMGwoXE0ywq9XmriW9cqzRgX4cuTZ+56rT9JKRFg0bG5G'
        'VMxJSm0bHtanD/AXObw5As2pIFZbzXxcE3Sc+qFXbkjd1Ke39HVL4C9fqA7oLNt7jJ67'
        'K/qeHcOuIHyO8RR82+VK11nvcHgeXw8Dej1skOvhSXQ9/Fy//qXuwdbEZ4tpLXNT/yuV'
        'wjtL9yrtWqJle/9AQ30WUSelfO5DkJJQQuskgAuCR3qBg3iHOcbrC4bY++Or09Og9x5V'
        'XLhw7uCG4sxC0wRr/QzGH0Zxp9G4PvQ7ra4PZSMAl13dDUH78rJboOzoErBJmLjYVDuJ'
        'EJkBnCXYG2zBnQfttg+9OS+bwzIUS7BVJyKx58T7leZs4xuGcOKEIk3xNgFWKDj6hV4G'
        'DGxa8A7jaOdwuOARw0ZVifwerFLbWYvRt4zVUoZtf5XO6sbzM+gUrd+LdDwBJJ/Jn8Ll'
        'OYvm5UW31Q62tuVGA2/fS5f6Rov/FXbxmysqDuBNb2p+hTOyzfTFc832r8jZPV6LOLje'
        '91rxAh1w5pPjZ2s4/1f24nn9BFt1pmhjTk3gN5IzMkmo1D9C6KD1kQI+akeiXDlSkVz5'
        'YOwZfx505BeWacmbbVGIFSHlPrzVP2/wqEBNUyfUlQAXAUvnKx17oBMVauSMSrvyH7ie'
        'e7N8EQAA')
    # @:adhoc_unpack:@
    #                   docutils.conf is included above
    #                   namespace_dict.py is imported
    # @:adhoc_include:@ setup.py
    # @:adhoc_unpack:@ !setup.py
    RtAdHoc.unpack_(None, file_='setup.py',
        mtime='2013-08-24T05:47:21', mode=int("100664", 8),
        zipped=True, flat=None, source64=
        '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'
        'Oi/0euz+qev++XuiSt+z6t38D7p16b9oDwAA')
    # @:adhoc_unpack:@
    #                   stringformat_local.py is imported
    #                   use_case_00?_* is imported
    #                   adhoc_test is imported
    #                   dist/adhoc.py is generated

    # |:here:|

# (progn (forward-line 1) (snip-insert-mode "py.t.ide" t) (insert "\n"))
#
# :ide-menu: Emacs IDE Main Menu - Buffer @BUFFER@
# . M-x `eIDE-menu' (eIDE-menu "z")

# :ide: CSCOPE ON
# . (cscope-minor-mode)

# :ide: CSCOPE OFF
# . (cscope-minor-mode (quote ( nil )))

# :ide: TAGS: forced update
# . (compile (concat "cd /home/ws/project/ws-rfid && make -k FORCED=1 tags"))

# :ide: TAGS: update
# . (compile (concat "cd /home/ws/project/ws-rfid && make -k tags"))

# :ide: +-#+
# . Utilities ()

# :ide: TOC: Generate TOC with py-toc.py
# . (progn (save-buffer) (compile (concat "py-toc.py ./" (file-name-nondirectory (buffer-file-name)) " ")))

# :ide: CMD: Fold region with line continuation
# . (shell-command-on-region (region-beginning) (region-end) "fold --spaces -width 79 | sed 's, $,,;1!s,^, ,;$!s,$,\\\\,'" nil nil nil t)

# :ide: CMD: Fold region and replace with line continuation
# . (shell-command-on-region (region-beginning) (region-end) "fold --spaces --width 79 | sed 's, $,,;1!s,^, ,;$!s,$,\\\\,'" t nil nil t)

# :ide: +-#+
# . Fold ()

# :ide: CMD: Remove 8 spaces and add `>>> ' to region
# . (shell-command-on-region (region-beginning) (region-end) "sed 's,^        ,,;/^[ ]*##/d;/^[ ]*#/{;s,^ *# *,,p;d;};/^[ ]*$/!s,^,>>> ,'" nil nil nil t)

# :ide: CMD: Remove 4 spaces and add `>>> ' to region
# . (shell-command-on-region (region-beginning) (region-end) "sed 's,^    ,,;/^[ ]*##/d;/^[ ]*#/{;s,^ *# *,,p;d;};/^[ ]*$/!s,^,>>> ,'" nil nil nil t)

# :ide: +-#+
# . Doctest ()

# :ide: LINT: Check 80 column width ignoring IDE Menus
# . (let ((args " | /srv/ftp/pub/check-80-col.sh -")) (compile (concat "sed 's,^\\(\\|. \\|.. \\|... \\)\\(:ide\\|[.] \\).*,,;s,^ *. (progn (forward-line.*,,' " (buffer-file-name) " " args " | sed 's,^-," (buffer-file-name) ",'")))

# :ide: LINT: Check 80 column width
# . (let ((args "")) (compile (concat "/srv/ftp/pub/check-80-col.sh " (buffer-file-name) " " args)))

# :ide: +-#+
# . Lint Tools ()

# :ide: DELIM:     |: SYM :|         |:tag:|                standard symbol-tag!
# . (symbol-tag-normalize-delimiter (cons (cons nil "|:") (cons ":|" nil)) t)

# :ide: DELIM:     :: SYM ::         ::fillme::             future standard fill-me tag
# . (symbol-tag-normalize-delimiter (cons (cons nil "::") (cons "::" nil)) t)

# :ide: DELIM:     @: SYM :@         @:fillme:@             adhoc tag
# . (symbol-tag-normalize-delimiter (cons (cons nil "@:") (cons ":@" nil)) t)

# :ide: +-#+
# . Delimiters ()

# :ide: COMPILE: Run with --ap-help
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --ap-help")))

# :ide: COMPILE: Run with --help
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --help")))

# :ide: COMPILE: Run with --test
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --test")))

# :ide: COMPILE: Run with --test --verbose
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --test --verbose")))

# :ide: COMPILE: Run with --debug
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --debug")))

# :ide: +-#+
# . Compile with standard arguments ()

# :ide: OCCUR-OUTLINE: Python Source Code
# . (x-symbol-tag-occur-outline "sec" '("||:" ":||") (cons (cons "^\\([ \t\r]*\\(def\\|class\\)[ ]+\\|[A-Za-z_]?\\)" nil) (cons nil "\\([ \t\r]*(\\|[ \t]*=\\)")))

# :ide: MENU-OUTLINE: Python Source Code
# . (x-eIDE-menu-outline "sec" '("|||:" ":|||") (cons (cons "^\\([ \t\r]*\\(def\\|class\\)[ ]+\\|[A-Za-z_]?\\)" nil) (cons nil "\\([ \t\r]*(\\|[ \t]*=\\)")))

# :ide: +-#+
# . Outline ()

# :ide: INFO: SQLAlchemy - SQL Expression Language - Reference
# . (let ((ref-buffer "*sqa-expr-ref*")) (if (not (get-buffer ref-buffer)) (shell-command (concat "w3m -dump -cols " (number-to-string (1- (window-width))) " 'http://www.sqlalchemy.org/docs/05/reference/sqlalchemy/expressions.html'") ref-buffer) (display-buffer ref-buffer t)))

# :ide: INFO: SQLAlchemy - SQL Expression Language - Tutorial
# . (let ((ref-buffer "*sqa-expr-tutor*")) (if (not (get-buffer ref-buffer)) (shell-command (concat "w3m -dump -cols " (number-to-string (1- (window-width))) " 'http://www.sqlalchemy.org/docs/05/sqlexpression.html'") ref-buffer) (display-buffer ref-buffer t)))

# :ide: INFO: SQLAlchemy - Query
# . (let ((ref-buffer "*sqa-query*")) (if (not (get-buffer ref-buffer)) (shell-command (concat "w3m -dump -cols " (number-to-string (1- (window-width))) " 'http://www.sqlalchemy.org/docs/orm/query.html'") ref-buffer) (display-buffer ref-buffer t)))

# :ide: +-#+
# . SQLAlchemy Reference ()

# :ide: INFO: Python - argparse
# . (let ((ref-buffer "*python-argparse*")) (if (not (get-buffer ref-buffer)) (shell-command (concat "w3m -dump -cols " (number-to-string (1- (window-width))) " 'http://docs.python.org/library/argparse.html'") ref-buffer) (display-buffer ref-buffer t)))

# :ide: INFO: Python Documentation
# . (let ((ref-buffer "*w3m*")) (if (get-buffer ref-buffer) (display-buffer ref-buffer t)) (other-window 1) (w3m-goto-url "http://docs.python.org/index.html" nil nil))

# :ide: INFO: Python Reference
# . (let* ((ref-buffer "*python-ref*") (local "/home/ws/project/ws-util/python/reference/PQR2.7.html") (url (or (and (file-exists-p local) local) "'http://rgruet.free.fr/PQR27/PQR2.7.html'"))) (unless (get-buffer ref-buffer) (get-buffer-create ref-buffer) (with-current-buffer ref-buffer (shell-command (concat "snc txt.py.reference 2>/dev/null") ref-buffer) (goto-char (point-min)) (if (eobp) (shell-command (concat "w3m -dump -cols " (number-to-string (1- (window-width))) " " url) ref-buffer)))) (display-buffer ref-buffer t))

# :ide: +-#+
# . Python Reference ()

# :ide: COMPILE: Run with --decompile dist/xx_adhoc.py
# . (progn (save-buffer) (compile (concat "rm -rf __adhoc__; cp -p dist/adhoc.py dist/xx_adhoc.py; python ./" (file-name-nondirectory (buffer-file-name)) " --decompile dist/xx_adhoc.py")))

# :ide: COMPILE: Run with cat dist/adhoc.py | --decompile
# . (progn (save-buffer) (compile (concat "rm -rf __adhoc__; cat dist/adhoc.py | python ./" (file-name-nondirectory (buffer-file-name)) " --decompile")))

# :ide: COMPILE: Run with cat /dev/null | --decompile
# . (progn (save-buffer) (compile (concat "rm -rf __adhoc__; cat /dev/null | python ./" (file-name-nondirectory (buffer-file-name)) " --decompile")))

# :ide: COMPILE: Run with cat /dev/null | --compile
# . (progn (save-buffer) (compile (concat "cat /dev/null | python ./" (file-name-nondirectory (buffer-file-name)) " --compile")))

# :ide: COMPILE: Run with cat /dev/null |
# . (progn (save-buffer) (compile (concat "cat /dev/null | python ./" (file-name-nondirectory (buffer-file-name)) " ")))

# :ide: COMPILE: Run with --help
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --help")))

# :ide: COMPILE: Run with --template doc/index.rst
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --template doc/index.rst")))

# :ide: COMPILE: Run with --template test
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --template test")))

# :ide: COMPILE: Run with --template
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --template")))

# :ide: COMPILE: Run with python3 with --template list
# . (progn (save-buffer) (compile (concat "python3 ./" (file-name-nondirectory (buffer-file-name)) " --template list")))

# :ide: COMPILE: Run with --verbose --implode
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) "  --verbose --implode")))

# :ide: COMPILE: Run with --documentation
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --documentation")))

# :ide: COMPILE: make ftp
# . (progn (save-buffer) (compile (concat "make -k ftp")))

# :ide: COMPILE: Run with --verbose --extract
# . (progn (save-buffer) (shell-command "rm -f README.txt doc/index.rst") (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) "  --verbose --extract")))

# :ide: COMPILE: Run with --verbose --template README.txt
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --verbose --template README.txt")))

# :ide: COMPILE: Run with --template list
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --template list")))

# :ide: COMPILE: Run with --eide #
# . (progn (save-buffer) (shell-command (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --eide '#'") (concat "*templates: " (file-name-nondirectory (buffer-file-name)) "*")))

# :ide: COMPILE: Run with --expected
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --expected")))

# :ide: COMPILE: make doc
# . (progn (save-buffer) (compile (concat "make doc")))

# :ide: COMPILE: Run with --eide
# . (progn (save-buffer) (shell-command (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --eide") (concat "*templates: " (file-name-nondirectory (buffer-file-name)) "*")))

# :ide: COMPILE: Run with python3 with --test
# . (progn (save-buffer) (compile (concat "python3 ./" (file-name-nondirectory (buffer-file-name)) " --test")))

# :ide: COMPILE: Run with python3 w/o args
# . (progn (save-buffer) (compile (concat "python3 ./" (file-name-nondirectory (buffer-file-name)) " ")))

# :ide: COMPILE: Run with --test
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --test")))

# :ide: COMPILE: Run with --verbose
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --verbose")))

# :ide: +-#+
# . Compile ()

#
# Local Variables:
# mode: python
# comment-start: "#"
# comment-start-skip: "#+"
# comment-column: 0
# truncate-lines: t
# End:
