from diaries.DiarySample import DiarySample
from diaries.OishiDiary import OishiDiary
from diaries.MizunoDiary import MizunoDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), MizunoDiary(),OishiDiary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
