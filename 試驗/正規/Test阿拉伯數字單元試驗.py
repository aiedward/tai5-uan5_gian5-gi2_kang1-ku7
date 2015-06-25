# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.正規.阿拉伯數字 import 阿拉伯數字


class 阿拉伯數字單元試驗(TestCase):
	def setUp(self):
		self.數字 = 阿拉伯數字()
		pass

	def tearDown(self):
		pass

	def test_判斷是數字無(self):
		self.assertEqual(self.數字.是數字無(''), False)
		self.assertEqual(self.數字.是數字無('0'), True)
		self.assertEqual(self.數字.是數字無('12312'), True)
		self.assertEqual(self.數字.是數字無('13３2312'), True)
		self.assertEqual(self.數字.是數字無('6'), True)
		self.assertEqual(self.數字.是數字無('013３2312三'), False)
		self.assertEqual(self.數字.是數字無('００13３27890'), True)
		self.assertEqual(self.數字.是數字無('000'), True)
		# 小數本來就會使拆開唸，予別的模組合起來
		self.assertEqual(self.數字.是數字無('00.30'), False)
		self.assertEqual(self.數字.是數字無('197.080'), False)
		self.assertEqual(self.數字.是數字無('197.08.0'), False)

	def test_轉號碼(self):
		問答 = [
			('2', '二'),
			('10', '一空'),
			('23', '二三'),
			('15', '一五'),
			('120', '一二空'),
			('230', '二三空'),
			('602', '六空二'),
			('1001', '一空空一'),
			('1020', '一空二空'),
			('1300', '一三空空'),
			('4512', '四五一二'),
			('5004', '五空空四'),
			('6070', '六空七空'),
			('9800', '九八空空'),  # 九千八百
			('10800', '一空八空空'),
			('400000800', '四空空空空空八空空'),
			('1230567890980654', '一二三空五六七八九空九八空六五四'),
			('1300130013', '一三空空一三空空一三'),
			('2000000022222', '二空空空空空空空二二二二二'),
			('10000000000000000', '一空空空空空空空空空空空空空空空空'),
			('0830', '空八三空'),
			]
		for 問, 答 in 問答:
			if 答 is None:
				self.assertEqual(self.數字.是號碼無(問), False)
				self.assertEqual(self.數字.轉號碼('空', 問), 問)
			else:
				self.assertEqual(self.數字.是號碼無(問), True)
				self.assertEqual(self.數字.轉號碼('空', 問), 答)
				self.assertEqual(self.數字.轉號碼('零', 問),
						答.replace('空', '零'))

	def test_轉數量(self):
		問答 = [
			('2', '兩'),
			('10', '十'),
			('23', '二十三'),
			('15', '十五'),
			('120', '一百二十'),  # 百二 一百二
			('230', '兩百三十'),  # 兩百三
			('602', '六百空二'),
			('1001', '一千空一'),
			('1020', '一千空二十'),
			('1200', '一千兩百'),
			('1300', '一千三百'),  # 千三 一千三
			('4512', '四千五百一十二'),
			('5004', '五千空四'),
			('6070', '六千空七十'),
			('9800', '九千八百'),  # 九千八
			('10800', '一萬空八百'),
			('400000800', '四億空八百'),
			('1230567890980654', '一千兩百三十兆五千六百七十八億九千空九十八萬空六百五十四'),
			('1300130013', '十三億空一十三萬空一十三'),
			('2000000022222', '兩兆空二萬兩千兩百二十二'),
			('2000000000000', '兩兆'),
			('7900000000', '七十九億'),
			('10000000000000000', None),
			('0830', None),
			]
		self.檢查數量(問答)
		
	def test_轉兩佮二的數量(self):
		問答 = [
			('12', '十二'),
			('120', '一百二十'),
			('3200', '三千兩百'),
			('42000', '四萬兩千'),
			('920000', '九十二萬'),
			('1200000', '一百二十萬'),
			('12000000', '一千兩百萬'),
			('32000000', '三千兩百萬'),
			('200000000', '兩億'),
			('820000000', '八億兩千萬'),
			]
		self.檢查數量(問答)

	def test_轉閩南語數量省一佮單位(self):
		問答 = [
			('兩百三十', '兩百三'),
			('六百空二', None),
			('一千空一', None),
			('一千空一十', '一千空十'),
			('一千空二十', None),
			('一千一百一十', '一千一百一'),
			('一千兩百', '千二'),
			('一千三百', '千三'),
			('一千三百一十三', '一千三百十三'),
			('四千五百一十二', '四千五百十二'),
			('五千空四', None),
			('六千空七十', None),
			('九千八百', '九千八'),
			('十三萬空一十三', '十三萬空十三'),
			('一兆空一十六萬七千', '一兆空十六萬七'),
			('七十九億', None),
			]
		self.檢查閩南語數量(問答)

	def test_轉閩南語兩佮二數量(self):
		問答 = [
			('十二', None),
			('一百二十', '百二'),
			('一千兩百', '千二'),
			('三千兩百', '三千二'),
			('四萬兩千', '四萬二'),
			('九十二萬', None),
			('八億兩千萬', None),
			('一百二十萬', '百二萬'),
			('一千兩百萬', '千二萬'),
			('三千兩百萬', None),
			('兩億', None),
			('一千兩百億', '千二億'),
			('三千兩百億', None),
			]
		self.檢查閩南語數量(問答)

	def test_轉客家話數量省單位(self):
		問答 = [
			('一百二十', '百二'),
			('兩百三十', '兩百三'),
			('六百零二', None),
			('一千零一', None),
			('一千零一十', None),
			('一千零二十', None),
			('一千一百一十', '一千一百一'),
			('一千兩百', '千二'),
			('一千三百', '千三'),
			('一千三百一十三', None),
			('四千五百一十二', None),
			('五千零四', None),
			('六千零七十', None),
			('九千八百', '九千八'),
			('十三億零一十三萬零一十三', None),
			('一兆零一十六萬七千', '一兆零一十六萬七'),
			('七十九億', None),
			]
		self.檢查客家話數量(問答)

	def test_轉官話數量省上尾單位(self):
		問答 = [
			('一百二十', '一百二'),
			('兩百三十', '兩百三'),
			('六百零二', None),
			('一千零一', None),
			('一千零一十', None),
			('一千零二十', None),
			('一千一百一十', '一千一百一'),
			('一千兩百', '一千二'),
			('一千三百', '一千三'),
			('一千三百一十三', None),
			('四千五百一十二', None),
			('五千零四', None),
			('六千零七十', None),
			('九千八百', '九千八'),
			('十三億零一十三萬零一十三', None),
			('一兆零一十六萬七千', '一兆零一十六萬七'),
			('七十九億', None),
			]
		self.檢查官話數量(問答)

	def test_轉官話兩佮二數量(self):
		問答 = [
			('十二', None),
			('一百二十', '一百二'),
			('一千兩百', '一千二'),
			('三千兩百', '三千二'),
			('四萬兩千', '四萬二'),
			('九十二萬', None),
			('八億兩千萬', None),
			('一百二十萬', None),
			('一千兩百萬', None),
			('三千兩百萬', None),
			('兩億', None),
			]
		self.檢查官話數量(問答)
		
	def 檢查數量(self, 問答):
		for 問, 答 in 問答:
			if 答 is None:
				self.assertEqual(self.數字.是數量無(問), False, 問)
				self.assertEqual(self.數字.轉數量('空', 問), 問)
			else:
				self.assertEqual(self.數字.是數量無(問), True)
				self.assertEqual(self.數字.轉數量('空', 問), 答, 問)
				self.assertEqual(self.數字.轉數量('零', 問),
						答.replace('空', '零'), 問)

	def 檢查閩南語數量(self, 問答):
		for 問, 答 in 問答:
			if 答 is None:
				self.assertEqual(self.數字.轉閩南語數量無(問), False, 問)
				self.assertEqual(self.數字.轉閩南語數量(問), 問)
			else:
				self.assertEqual(self.數字.轉閩南語數量無(問), True, 問)
				self.assertEqual(self.數字.轉閩南語數量(問), 答, 問)

	def 檢查客家話數量(self, 問答):
		for 問, 答 in 問答:
			if 答 is None:
				self.assertEqual(self.數字.轉客家話數量無(問), False, 問)
				self.assertEqual(self.數字.轉客家話數量(問), 問)
			else:
				self.assertEqual(self.數字.轉客家話數量無(問), True, 問)
				self.assertEqual(self.數字.轉客家話數量(問), 答, 問)

	def 檢查官話數量(self, 問答):
		for 問, 答 in 問答:
			if 答 is None:
				self.assertEqual(self.數字.轉官話數量無(問), False, 問)
				self.assertEqual(self.數字.轉官話數量(問), 問)
			else:
				self.assertEqual(self.數字.轉官話數量無(問), True, 問)
				self.assertEqual(self.數字.轉官話數量(問), 答, 問)
