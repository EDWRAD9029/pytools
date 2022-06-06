# -*- coding: utf-8 -*-
"""

"""
import time,timeit
import numpy as np
import math

def print_time_time(f):
    """
    計測デコレータ
    経過時間を計測する
    
    詳細：
    time.time関数を用いて時間を計測し、小数3桁まで表示する
    
    使用例：
    import measure_time
    @measure_time.print_time_time
    def _sample():
        // 計測されるコード
    """
    def print_time_time_func(*args, **kwargs):
        # 引数表示
        print("経過時間を計測します...")
        print("args   :",args)
        print("kwargs :",kwargs)
        
        # 開始
        print("------------------------ 時間計測　開始 ------------------------")
        start_time = time.time()
 
        # 関数実行
        return_val = f(*args, **kwargs)
 
        # 終了
        end_time = time.time()
        print("------------------------ 時間計測　終了 ------------------------")
 
        # 関数名と経過時間を出力(秒)
        elapsed_time = end_time - start_time
        print("function     :", f.__name__)
        print("elapsed_time :", "{:.3f}".format(elapsed_time),"sec")
 
        # 戻り値を返す
        return return_val
 
    return print_time_time_func



def print_process_time(f):
    """
    計測デコレータ
    CPU使用時間を計測する
    
    詳細：
    time.process_time関数を用いて時間を計測し、小数3桁まで表示する
    
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
    
    詳細：
    time.process_time関数を用いて時間を計測する。
    1回の実行で、time_maxを超える場合はその実行時間小数3桁まで表示する。
    超えない場合はtime_maxを実行時間で割った回数、実行し平均・最大・最小・標準偏差を表示する。
    
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
    
    詳細：
    time.perf_counter関数を用いて時間を計測し、小数3桁まで表示する
    
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



def print_performance_time_detail(f):
    """
    計測デコレータ
    経過時間を精密に計測する
    
    詳細：
    time.perf_counter関数を用いて時間を計測する。
    1回の実行で、time_maxを超える場合はその実行時間小数3桁まで表示する。
    超えない場合はtime_maxを実行時間で割った回数、実行し平均・最大・最小・標準偏差を表示する。
    
    使用例：
    import measure_time
    @measure_time.print_performance_time_detail
    def _sample():
        // 計測されるコード
    """
    def print_performance_time_detail_func(*args, **kwargs):
        # 設定
        time_max = 10 # 合計の時間(秒)
        loops_max = 1000000 # 繰り返し計算する場合の最大ループ回数
        
        # 引数表示
        print("経過時間を精密に計測します...")
        print("args   :",args)
        print("kwargs :",kwargs)
        
        # 開始
        print("------------------------ 時間計測　開始 ------------------------")
        start_time = time.perf_counter()
 
        # 関数実行
        return_val = f(*args, **kwargs)
 
        # 終了
        end_time = time.perf_counter()
 
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
                tmp = time.perf_counter()
                return_val = f(*args, **kwargs)
                times.append(time.perf_counter() - tmp)
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
 
    return print_performance_time_detail_func



class Timer():
    """
    時間を計測するクラス。
    複数行にまたがる処理時間を計測できる。
    
    パラメータ
    ----------
    times : list
    time_start : float
    time_finish : float
    timer_func : function
    
    メソッド
    ----------
    set_timer_mode : 時間計測を行う関数を設定する。
    start : 時間計測を開始する。
    finish : 時間計測を終了する。
    lap : 経過時間を記録する。
    print_times : 記録された経過時間をlapタイムごとに表示する。
    clear : 記録された経過時間を削除する。
    
    """
    def __init__(self):
        self.clear()
        self.set_timer_mode()
    
    
    
    def set_timer_mode(self,func=time.perf_counter):
        """
        時間計測を行う関数を設定する。

        パラメータ
        ----------
        func : function
            計測に使用する関数。
            デフォルトはtime.perf_counter。

        返り値
        -------
        なし。

        """
        self.timer_func = func
        print("計測関数は",self.timer_func,"です")
    
    
    
    def start(self):
        """
        時間計測を開始する。
        lapタイムとしてもtimesに記録する。
        
        パラメータ
        ----------
        なし

        返り値
        -------
        なし

        """
        print("------------------------ 時間計測　開始 ------------------------")
        self.time_start = self.timer_func()
        self.times.append(self.time_start)
    
    
    
    def finish(self):
        """
        時間計測を終了する。開始から終了までの時間を小数3桁で表示する。
        lapタイムとしてもtimesに記録する。
        
        パラメータ
        ----------
        なし

        返り値
        -------
        elapsed_time : flaot
            開始から終了までの時間[sec]

        """
        self.time_finish = self.timer_func()
        self.times.append(self.time_finish)
        elapsed_time = self.time_finish - self.time_start
        print("------------------------ 時間計測　終了 ------------------------")
        print("elapsed_time :", "{:.3f}".format(elapsed_time),"sec")
        return elapsed_time
    
    
    
    def lap(self):
        """
        lapタイムとしてtimesに記録する。
        
        パラメータ
        ----------
        なし

        返り値
        -------
        なし

        """
        self.times.append(self.timer_func())
    
    
    
    def print_times(self):
        """
        lapタイムとしてtimesに記録された時間を表示する。
        timesに3回記録されていた場合にはtimes[0]からtimes[1]までの時間とtimes[1]からtimes[2]までの時間が表示される。
        
        パラメータ
        ----------
        なし

        返り値
        -------
        times_diff : list
            timesに記録された時刻の差が含まれたリスト。
            timesに3回記録されていた場合にはtimes[0]からtimes[1]までの時間とtimes[1]からtimes[2]までの時間が含まれる。

        """
        print(type(self.time_start))
        for i,j in enumerate(np.diff(np.array(self.times))):
            print("time"+str(i),"-","time"+str(i+1),":","{:.3f}".format(j),"sec")
        return [np.diff(np.array(self.times))]
    
    
    
    def clear(self):
        self.times = []
        self.time_start = None
        self.time_finish = None