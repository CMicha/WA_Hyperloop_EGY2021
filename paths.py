# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:04:01 2018

@author: bec
"""
import WA_Hyperloop
import os

def get_path(name):
    install_path = os.path.dirname(WA_Hyperloop.__file__)
    paths = {
             'sheet1_svg':  os.path.join(install_path, "svg\sheet_1_v2.svg"),
             'sheet2_svg':  os.path.join(install_path, "svg\sheet_2.svg"),
             'sheet3_svg': os.path.join(install_path, "svg\sheet_3_national.svg"),
             'sheet4_1_svg':  os.path.join(install_path, "svg\sheet_4_part1.svg"),
             'sheet4_2_svg':  os.path.join(install_path, "svg\sheet_4_part2.svg"),
             'sheet6_svg':    os.path.join(install_path, "svg\sheet_6.svg"),
             'sheet5_svg':    os.path.join(install_path, "svg\sheet_5.svg"),
             'sheet7m_svg':  os.path.join(install_path, "svg\sheet7_month.svg"),
             'sheet7y_svg':  os.path.join(install_path, "svg\sheet7_yearly.svg"),
             }
    
    return paths[name]