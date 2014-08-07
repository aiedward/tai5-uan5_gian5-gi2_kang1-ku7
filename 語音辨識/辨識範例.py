import os
from 語音辨識.模型訓練 import 模型訓練
from 語音辨識.辨識模型 import 辨識模型

if __name__ == '__main__':
	訓練 = 模型訓練()
	這馬目錄 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	資料目錄 = os.path.join(這馬目錄, 'data')
	音檔目錄 = os.path.join(這馬目錄, 'wav')
	標仔目錄 = os.path.join(這馬目錄, 'labels')
	音節聲韻對照檔 = os.path.join(這馬目錄, 'Syl2Monophone.dic.ok')
	執行檔路徑 = ''
	(原本聲韻類檔, 原本模型檔),\
	(加短恬聲韻類檔, 加短恬模型檔),\
	(三連音聲韻類檔, 三連音模型檔) = 訓練.訓練(
		音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄,
		算特徵=True, 執行檔路徑=執行檔路徑)
	模型 = 辨識模型()
	特徵檔, 音節檔, 聲韻檔 = 模型.處理試驗語料(音檔目錄, 資料目錄, 標仔目錄, 音節聲韻對照檔, 執行檔路徑=執行檔路徑)
	
	原本目錄 = os.path.join(資料目錄, '原本')
	os.makedirs(原本目錄, exist_ok=True)
	對齊聲韻結果檔 = 模型.對齊聲韻(原本聲韻類檔, 原本模型檔, 聲韻檔, 特徵檔, 原本目錄, 執行檔路徑=執行檔路徑)
	對齊音節結果檔 = 模型.對齊音節(音節聲韻對照檔, 原本聲韻類檔, 原本模型檔, 音節檔, 特徵檔, 原本目錄, 執行檔路徑=執行檔路徑)
	模型.辨識聲韻(原本聲韻類檔, 原本模型檔, 特徵檔, 原本目錄, 3, 執行檔路徑=執行檔路徑)
	模型.辨識音節(音節聲韻對照檔, 原本聲韻類檔, 原本模型檔, 特徵檔, 原本目錄, 3, 執行檔路徑=執行檔路徑)
	
	加短恬目錄 = os.path.join(資料目錄, '加短恬')
	os.makedirs(加短恬目錄, exist_ok=True)
	對齊聲韻結果檔 = 模型.對齊聲韻(加短恬聲韻類檔, 加短恬模型檔, 聲韻檔, 特徵檔, 加短恬目錄, 執行檔路徑=執行檔路徑)
	對齊音節結果檔 = 模型.對齊音節(音節聲韻對照檔, 加短恬聲韻類檔, 加短恬模型檔, 音節檔, 特徵檔, 加短恬目錄, 執行檔路徑=執行檔路徑)
	模型.辨識聲韻(加短恬聲韻類檔, 加短恬模型檔, 特徵檔, 加短恬目錄, 3, 執行檔路徑=執行檔路徑)
	模型.辨識音節(音節聲韻對照檔, 加短恬聲韻類檔, 加短恬模型檔, 特徵檔, 加短恬目錄, 3, 執行檔路徑=執行檔路徑)
	
	三連音目錄 = os.path.join(資料目錄, '三連音')
	os.makedirs(三連音目錄, exist_ok=True)
	對齊聲韻結果檔 = 模型.對齊聲韻(三連音聲韻類檔, 三連音模型檔, 聲韻檔, 特徵檔, 三連音目錄, 執行檔路徑=執行檔路徑)
	對齊音節結果檔 = 模型.對齊音節(音節聲韻對照檔, 三連音聲韻類檔, 三連音模型檔, 音節檔, 特徵檔, 三連音目錄, 執行檔路徑=執行檔路徑)
	'若愛辨識聲韻，聲韻類檔會傷大，所以無支援'
# 	模型.辨識聲韻(三連音聲韻類檔, 三連音模型檔, 特徵檔, 三連音目錄, 3, 執行檔路徑=執行檔路徑)
	模型.辨識音節(音節聲韻對照檔, 三連音聲韻類檔, 三連音模型檔, 特徵檔, 三連音目錄, 3, 執行檔路徑=執行檔路徑)
