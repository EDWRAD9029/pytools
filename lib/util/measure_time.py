# -*- coding: utf-8 -*-
"""

"""
import time

def print_process_time(f):
    """
    計測デコレータ
    経過時間を計測する
    
    使用例：
    import measure_time
    @measure_time.print_process_time
    def _sample():
        // 計測されるコード
    """
    def print_process_time_func(*args, **kwargs):
        # 引数表示
        print("時間を計測します...")
        print("args   :",args)
        print("kwargs :",kwargs)
        
        # 開始
        print("------------------------ 時間計測　開始 ------------------------")
        start_time = time.process_time()
 
        # 関数実行
        return_val = f(*args, **kwargs)
 
        # 終了
        end_time = time.process_time()
        print("------------------------ 時間計測　終了 ------------------------")
 
        # 関数名と経過時間を出力(秒)
        elapsed_time = end_time - start_time
        print("function     :", f.__name__)
        print("elapsed_time :", "{:.3f}".format(elapsed_time),"sec")
 
        # 戻り値を返す
        return return_val
 
    return print_process_time_func


def print_performance_time(f):
    """
    計測デコレータ
    CPU使用時間を計測する
    
    使用例：
    import measure_time
    @measure_time.print_performance_time
    def _sample():
        // 計測されるコード
    """
    def print_performance_time_func(*args, **kwargs):
        # 引数表示
        print("時間を計測します...")
        print("args   :",args)
        print("kwargs :",kwargs)
        
        # 開始
        print("------------------------ 時間計測　開始 ------------------------")
        start_time = time.perf_counter()
 
        # 関数実行
        return_val = f(*args, **kwargs)
 
        # 終了
        end_time = time.perf_counter()
        print("------------------------ 時間計測　終了 ------------------------")
 
        # 関数名と経過時間を出力(秒)
        elapsed_time = end_time - start_time
        print("function     :", f.__name__)
        print("elapsed_time :", "{:.3f}".format(elapsed_time),"sec")
 
        # 戻り値を返す
        return return_val
 
    return print_performance_time_func

class Timer():
    """
    複数行にまたがる処理時間を計測する
    """
    def __init__(self):
        self.time_start = None
        self.time_finish = None
        self.timer_mode = None
    
    def start(self):
        pass