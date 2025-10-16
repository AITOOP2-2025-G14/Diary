from diaries.AbstractDiary import AbstractDiary
class MizunoDiary(AbstractDiary):
  def get_date(self):
    return "2021-12-01"
  def get_summary(self):
    return "今日はgithubの使い方を勉強しました!!"
  def get_author(self):
    return "Mizuno"