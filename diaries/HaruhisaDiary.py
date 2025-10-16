from diaries.AbstractDiary import AbstractDiary
class HaruhisaDiary(AbstractDiary):
  def get_date(self):
    return "2025-10-16"
  def get_summary(self):
    return "今日はオブジェクト指向プログラミング演習2のグループワーク演習だった。Git難しかった"
  def get_author(self):
    return "Haruhisa"