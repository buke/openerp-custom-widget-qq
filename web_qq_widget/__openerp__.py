# -*- coding: utf-8 -*-
##############################################################################
#
#    Custom Module For Rundex
#    Copyright 2013 wangbuke <wangbuke@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'web_qq_widget',
    'version': '0.1',
    'category': 'Tools',
    'description': """
Web QQ Custom Widget

功能：自定义QQ Widget

如果您觉得好用，请进入下面的网址，付费支持作者 ~

http://me.alipay.com/wangbuke

谢谢！

""",
    'author': 'wangbuke@gmail.com',
    'website': 'http://buke.github.io',
    'depends': ['web'],
    'js': [
        'static/src/js/*.js'
    ],
    'css': [
    ],
    'qweb' : [
        'static/src/xml/*.xml',
    ],
    'installable': True,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
