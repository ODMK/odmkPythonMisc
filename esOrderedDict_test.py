# -*- coding: utf-8 -*-
# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header begin-----------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************
#
# __::((esOrderedDict_test.py))::__
#
# Test script using for processing Nissan Dictionary data
# CSV read & write -> parse
# Manipulating Python Dictionaries, ordering/sorting dictionaries
# Python Regular Expressions, 're' library.
#
#
# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header end-------------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************

import pprint
import matplotlib.pyplot as plt

import collections

nested_dict={}

# original un-ordered nested dict:
nested_dict["and"] = {"small": {"characters": "gnomes&ghouls", "max_distance": "56K"},
                        "big": {"characters": "trolls&phantoms", "max_distance": "418K", "brain_hemisphere_separator": "astralplane"}}

# init - build ordered dict:

#gt_sm_keyList = ["characters", "max_distance"]
#gt_sm_dataList = ["gnomes&ghouls", "56K"]
#gt_sm_zip = zip(gt_sm_keyList, gt_sm_dataList)
#
#gt_bg_keyList = ["characters", "max_distance", "brain_hemisphere_separator"]
#gt_bg_dataList = ["trolls&phantoms", "418K", "astralplane"]
#gt_bg_zip = zip(gt_bg_keyList, gt_bg_dataList)
#
#gt_keyList = ["small", "big"]
#gt_dataList = [gt_sm_zip, gt_bg_zip]
#gt_zip = zip(gt_keyList, gt_dataList)

# // *---------------------------------------------------------------------* //
nested_OD = collections.OrderedDict()

smdict = collections.OrderedDict()
smdict['characters'] = "gnomes&ghouls"
smdict['max_distance'] = "56K"

bgdict = collections.OrderedDict()
bgdict['characters'] = "trolls&phantoms"
bgdict['max_distance'] = "418K"
bgdict['brain_hemisphere_separator'] = "astralplane"

ghostdict = collections.OrderedDict()
ghostdict['small'] = smdict
ghostdict['big'] = bgdict

nested_OD['and'] = ghostdict


# // *---------------------------------------------------------------------* //
smdict = collections.OrderedDict([('characters', 'gnomes&ghouls'), ('max_distance', '56K')])
bgdict = collections.OrderedDict([('characters', 'trolls&phantoms'), ('max_distance', '418K'), ('brain_hemisphere_separator', 'astralplane')])
ghostdict = collections.OrderedDict([('small', smdict), ('big', bgdict)])

nested_OD2 = collections.OrderedDict([('and', ghostdict)])


# // *---------------------------------------------------------------------* //
# check dictionary output

print('\n// *------------------------------------------------------------* //')

print('\nOriginal dict "and" = ')
print(nested_dict['and'])

print('\nOrdered dict "and" = ')
print(nested_OD2['and'])


print('\n// *------------------------------------------------------------* //')

print('\nOriginal dict "[and][big]" = ')
print(nested_dict['and']['big'])

print('\nOrdered dict "[and][big]" = ')
print(nested_OD2['and']['big'])

print('\n// *------------------------------------------------------------* //')

print('\nOriginal dict "[and][big][max_distance]" = ')
print(nested_dict['and']['big']['max_distance'])

print('\nOriginal dict "[and][big][max_distance]" = ')
print(nested_OD2['and']['big']['max_distance'])

print('\n// *------------------------------------------------------------* //')

print('\nOriginal dict "[and][small][characters]" = ')
print(nested_dict['and']['small']['characters'])

print('\nOriginal dict "[and][small][characters]" = ')
print(nested_OD2['and']['small']['characters'])

print('\n// *------------------------------------------------------------* //')
