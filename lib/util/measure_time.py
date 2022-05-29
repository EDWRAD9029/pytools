# -*- coding: utf-8 -*-
"""

"""
import time,timeit
import numpy as np
import math

def print_process_time(f):
    """
    計測デコレータ
    CPU使用時間を計測する
    
    使用例：
    import measure_time
    @measure_time.print_process_time
    def _sample():
        // 計測されるコード
    """
    def print_process_time_func(*args, **kwargs):
        # 引数表示
        print("CPU使用時間を計測します...")
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

def print_process_time_detail(f):
    """
    計測デコレータ
    CPU使用時間を精密に計測する
    
    使用例：
    import measure_time
    @measure_time.print_process_time_detail
    def _sample():
        // 計測されるコード
    """
    def print_process_time_detail_func(*args, **kwargs):
        # 設定
        time_max = 10 # 合計の時間(秒)
        loops_max = 1000000 # 繰り返し計算する場合の最大ループ回数
        
        # 引数表示
        print("CPU使用時間を精密に計測します...")
        print("args   :",args)
        print("kwargs :",kwargs)
        
        # 開始
        print("------------------------ 時間計測　開始 ------------------------")
        start_time = time.process_time()
 
        # 関数実行
        return_val = f(*args, **kwargs)
 
        # 終了
        end_time = time.process_time()
 
        # 関数名と経過時間を出力(秒)
        elapsed_time = end_time - start_time
        print("function     :", f.__name__)
        if time_max < elapsed_time:
            print("elapsed_time :", "{:.3f}".format(elapsed_time),"sec")
            print("loop = 1")
        else:
            try:
                N = math.ceil(time_max / elapsed_time)
                if N > loops_max:
                    N = loops_max
            except ZeroDivisionError:
                N = loops_max
            times = []
            for i in range(N):
                tmp = time.process_time()
                return_val = f(*args, **kwargs)
                times.append(time.process_time() - tmp)
            elapsed_time = np.average(times)
            print("elapsed_time :")
            print("\t loop :",N)
            print("\t average :", "{}".format(np.average(times)),"sec")
            print("\t std :", "{}".format(np.std(times)),"sec")
            print("\t min :", "{}".format(np.min(times)),"sec")
            print("\t max :", "{}".format(np.max(times)),"sec")
        
        print("------------------------ 時間計測　終了 ------------------------")
        
        # 戻り値を返す
        return return_val
 
    return print_process_time_detail_func


def print_performance_time(f):
    """
    計測デコレータ
    経過時間を計測する
    
    使用例：
    import measure_time
    @measure_time.print_performance_time
    def _sample():
        // 計測されるコード
    """
    def print_performance_time_func(*args, **kwargs):
        # 引数表示
        print("経過時間を計測します...")
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
        self.clear()
        self.set_timer_mode()
    
    def set_timer_mode(self,func=time.perf_counter):
        self.timer_func = func
        print("計測関数は",self.timer_func,"です")
    
    def start(self):
        print("------------------------ 時間計測　開始 ------------------------")
        self.time_start = self.timer_func()
        self.times.append(self.time_start)
    
    def finish(self):
        self.time_finish = self.timer_func()
        self.times.append(self.time_finish)
        elapsed_time = self.time_finish - self.time_start
        print("------------------------ 時間計測　終了 ------------------------")
        print("elapsed_time :", "{:.3f}".format(elapsed_time),"sec")
        return elapsed_time
    
    def lap(self):
        self.times.append(self.timer_func())
    
    def print_times(self):
        for i,j in enumerate(np.diff(np.array(self.times))):
            print("time"+str(i),"-","time"+str(i+1),":","{:.3f}".format(j),"sec")
        return [np.diff(np.array(self.times))]
    
    def clear(self):
        self.times = []
        self.time_start = None
        self.time_finish = None