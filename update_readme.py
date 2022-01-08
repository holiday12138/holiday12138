from typing import AsyncGenerator
import pathlib
import random
from datetime import datetime

print()
root = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    readme = root / "README.md"
    age = datetime.now().year - 1992

    sleep=random.randint(0,9)
    sport=random.randint(0,100)

    rewritten = f"""
### Hi there 👋


    我的名字叫凶良凶影，{age}岁。
    住在下北泽，未婚。
    我在龟仙屋连锁店服务。
    每天都要打电动到晚上8点才能回家。
    我不抽烟，酒仅止于浅尝。
    晚上12点睡，每天要睡足{sleep}个小时。
    睡前，我一定喝一杯高乐高，然后做{sport}分钟的柔软操，上了床，马上熟睡。
    一觉到天亮，决不把疲劳和压力，留到第二天。医生都说我很正常。
    """

    readme.open("w",encoding="UTF-8").write(rewritten)