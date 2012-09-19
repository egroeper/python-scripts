#!/usr/bin/python
'''
 * Copyright (C) 2012, Enno Groeper
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2, or (at your option)
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street - Fifth Floor, Boston, MA 02110-1301, USA.
'''

import poppler
import sys
import urllib
import os

def main():
  input_filename = sys.argv[1]
	# http://blog.hartwork.org/?p=612
  document = poppler.document_new_from_file('file://%s' % \
    urllib.pathname2url(os.path.abspath(input_filename)), None)
  n_pages = document.get_n_pages()
  all_annots = 0

  for i in range(n_pages):
		page = document.get_page(i)
		annot_mappings = page.get_annot_mapping ()
		num_annots = len(annot_mappings)
		if num_annots > 0:
			for annot_mapping in annot_mappings:
				if  annot_mapping.annot.get_annot_type().value_name != 'POPPLER_ANNOT_LINK':
					all_annots += 1
					print 'page: {0:3}, {1:10}, type: {2:10}, content: {3}'.format(i+1, annot_mapping.annot.get_modified(), annot_mapping.annot.get_annot_type().value_nick, annot_mapping.annot.get_contents())
	
  if all_annots > 0:
    print str(all_annots) + " annotation(s) found"
  else:
    print "no annotations found"

if __name__ == "__main__":
    main()
