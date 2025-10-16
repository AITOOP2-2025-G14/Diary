from diaries.AbstractDiary import AbstractDiary
class OishiDiary(AbstractDiary):
  def get_date(self):
    return "2025-10-25"
  def get_summary(self):
    return "なにもない一日だった"
  def get_author(self):
    return "Taiga Oishi"