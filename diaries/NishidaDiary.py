from diaries.AbstractDiary import AbstractDiary
class NishidaDiary(AbstractDiary):
  def get_date(self):
    return "2025-10-16"
  def get_summary(self):
    return "最近は雨が続いていて気分が少し滅入る。"
  def get_author(self):
    return "Nishida"