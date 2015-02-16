#!/usr/bin/python2
# -*- coding: utf-8 -*-

#	dump_from_binstream.py - dump content from a binary stream
#	Copyright (C) 2015  Tim Blazytko
#
#	This program is free software; you can redistribute it and/or
#	modify it under the terms of the GNU General Public License
#	as published by the Free Software Foundation; either version 2
#	of the License, or (at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program; if not, write to the Free Software
#	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import sys

if (len(sys.argv) < 5):
	print "[*] Too few parameters!"
	print "[*] Syntax: <source> <offset> <destination> <size>"
	sys.exit()

sfile = sys.argv[1]
offset = int(sys.argv[2],16)
dfile = sys.argv[3]
size = int(sys.argv[4])

s = open(sfile)
s.seek(offset)

with open(dfile,"w+") as d:
	d.write(s.read(size))
