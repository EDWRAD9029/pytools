# -*- coding: utf-8 -*-
"""

"""
import os
import pickle

def _make_path_config(root):
    pytools_config = {}
    pytools_config["path_setup"] = os.path.join(root,"lib","setup")
    pytools_config["path_config"] = os.path.join(pytools_config["path_setup"],"setting",'config.bin')
    return pytools_config

def _set_pytools_config(root):
    pytools_config =  _make_path_config(root)
    with open(pytools_config["path_config"], 'wb') as p:
        pickle.dump(pytools_config, p)

def set_config_root(pytools_config):
    if type(pytools_config)==dict:
        _set_pytools_config(pytools_config["root"])
        
    elif type(pytools_config)==str:
        _set_pytools_config(pytools_config)
        
    else:
        import traceback
        import inspect
        try:
            raise Exception("\n"
                "=========================================================\n"
                "    問題が発生しました !\n"
                "=========================================================\n"
                "モジュール : "+__name__+"\n"+
                "メソッド : "+inspect.currentframe().f_code.co_name+"\n"+
                "詳細 : ""引数pytools_configは "+type(pytools_config)+" に対応していません\n"
                )
        except:
            traceback.print_exc()