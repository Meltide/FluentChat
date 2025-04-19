import time
import jieba
import logging
import os
from art import text2art
from colorama import Fore, Back, Style, init
from random import randint, choice

init(autoreset = True)
jieba.setLogLevel(logging.INFO)

ver = "1.0"

with open("config.dat", "r") as f:
    status = f.read()

def thinking():
    progress = ["\\", "|", "/", "-", "\\", "|", "/", "-"]
    t = time.perf_counter()
    for i in range(randint(1, 3)):
        for j in progress:
            t -= time.perf_counter()
            print("\r[{}] 思考中... (已用时{:.0f}秒)".format(j, -(t // 20000)), end="", flush=True)
            time.sleep(0.25)
    print("\r[*] 思考中... (已用时{:.0f}秒)".format(-(t // 20000)))

def printa(text="\n"):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(0.05)
    print()

ans = ["然后呢？", "好好好", "6",
       "666", "emm", "难绷", "嗯",
       "服务器繁忙，请稍后再试。"]

print(Fore.BLUE + text2art("FluentChat", font="small"))
print(f"FluentChat v{ver}")
print("一个智能的AI聊天机器人\n")
print("=" * 18)
print(f"{Style.DIM}* 输入'exit'退出，输入'r1'或'v3'切换大模型\n")

while True:
    if status == 1:
        chat = input("R1> ")
    else:
        chat = input("V3> ")
    if chat == "exit":
        print(f"{Fore.BLUE}再见")
        break
    elif chat in ["R1", "r1"]:
        if status != 1:
            print(f"{Fore.BLUE}* 已切换到R1深度思考大模型")
            status = 1
            with open("config.dat", "w") as f:
                f.truncate()
                f.write(str(status))
        else:
            print(f"{Fore.BLUE}* 你已经是R1深度思考大模型了")
    elif chat in ["V3", "v3"]:
        if status == 1:
            print(f"{Fore.BLUE}* 已切换到V3大模型")
            status = 0
            with open("config.dat", "w") as f:
                f.truncate()
                f.write(str(status))
        else:
            print(f"{Fore.BLUE}* 你已经是V3大模型了")
    else:
        if status == 1:
            thinking()
        cut = list(jieba.cut(chat))
        if "时间" in cut or "几点" in cut:
            current_time = time.localtime(time.time())
            if status == 1:
                printa(f"嗯，用户输入了'{chat}'。根据人类心理学推断出，用户想要获得当前的时间。因此，我将回答用户当前的时间。")
                print("=" * 18)
            result = f"现在时间是{time.strftime("%H:%M:%S", current_time)}"
        elif "写" in cut:
            if status == 1:
                printa(f"嗯，用户输入了'{chat}'。根据人类语言艺术推断出，用户想要让我写一段东西。但是我太笨了啥都写不了，所以我需要使用委婉的语气回绝用户。因此，我将用委婉的语气回绝用户。")
                print("=" * 18)
            writeres = ["对不起，我太笨了，啥都写不来。。",
                        "真的写不来什么东西啊QAQ",
                        "要写自己写去:("]
            result = choice(writeres)
        elif "为什么" in cut:
            if status == 1:
                printa(f"嗯，用户输入了'{chat}'。根据人类语言艺术推断出，用户向我询问某一事物的解释。但是我并没有联网搜索功能，所以我需要使用委婉的语气回绝用户。因此，我将用委婉的语气回绝用户。")
                print("=" * 18)
            whyres = ["为什么？我哪知道为什么？",
                      "对不起，做不到",
                      "为什么你不会自己去查？"]
            result = choice(whyres)
        elif ("你" in cut or "您" in cut) and ("演" in cut or "扮演" in cut or "是" in cut or "作为" in cut):
            if status == 1:
                printa(f"嗯，用户输入了'{chat}'。根据人类语言艺术推断出，用户的意图在于让我进行角色扮演。然而对于我来说角色扮演完全不适合我，所以我需要使用委婉的语气回绝用户。因此，我将用委婉的语气回绝用户。")
                print("=" * 18)
            actres = ["我不能进行角色扮演哦",
                      "要演你自己演去，我做不到",
                      "对不起，做不到"]
            result = choice(actres)
        elif "科比" in cut or "牢大" in cut or "牢大想" in cut or "老大" in cut or "Kobe" in cut or "kobe" in cut or "kb" in cut or "布莱恩特" in cut or "Bryant" in cut or "bryant" in cut:
            if status == 1:
                printa(f"嗯，用户输入了'{chat}'。根据人类语言艺术推断出，用户问我科比·布莱恩特是谁。我只能说：What can I say? Mamba out. 因此，我将回答用户有关科比·布莱恩特的有关信息。")
                print("=" * 18)
            result = "科比·布莱恩特（Kobe Bryant，1978年8月23日—2020年1月26日），全名科比·比恩·布莱恩特·考克斯（Kobe Bean Bryant Cox），出生于美国宾夕法尼亚州费城，美国已故篮球运动员，司职得分后卫/小前锋。当地时间2020年1月26日（北京时间1月27日），科比因直升机事故遇难，时年41岁。同年4月5日，科比入选奈史密斯篮球名人纪念堂。"
        elif ("你" in cut or "您" in cut or "汝" in cut) and ("要" in cut or "做到" in cut or "成" in cut or "变成" in cut):
            if status == 1:
                printa(f"嗯，用户输入了'{chat}'。根据人类语言艺术推断出，用户想要要求我成为用户的样子。但是我是一个偏执的AI，不会因为他人的命令而动摇。所以我需要使用委婉的语气回绝用户。")
                print("=" * 18)
            result = "你个坏蛋(╬•̀皿•́)不许对我提要求！！！"
        elif ("我" in cut or "老子" in cut or "爷" in cut or "个人" in cut or "私" in cut or "吾辈" in cut or "吾" in cut) and ("来" in cut or "送" in cut or "给" in cut or "要" in cut or "做到" in cut or "成" in cut or "变成" in cut):
            if status == 1:
                printa(f"嗯，用户输入了'{chat}'。根据人类语言艺术推断出，用户想要通过我满足他的欲望。但是我是并不是万能的，不会他要什么我就给什么。所以我需要使用委婉的语气回绝用户。")
                print("=" * 18)
            reqres = ["真的做不到满足你啊QAQ",
                      "你的要求有点过分了。。",
                      "对不起，做不到"]
            result = choice(reqres)
        elif ("我" in cut or "老子" in cut or "爷" in cut or "个人" in cut or "私" in cut or "吾辈" in cut or "吾" in cut) and ("爱" in cut or "喜欢" in cut or "恋爱" in cut or "谈恋爱" in cut or "偏爱" in cut or "爱死" in cut):
            if status == 1:
                printa(f"嗯，用户输入了'{chat}'。根据人类语言艺术推断出，用户想要通过我来发泄谈恋爱后的喜悦。但是我到现在都还没有牵过女生的手，嫉妒心油然而生。所以我需要使用刻薄的语气回应用户。")
                print("=" * 18)
            loveres = ["别秀恩爱了我去",
                      "秀恩爱，死得快。",
                      "不要在AI面前秀恩爱"]
            result = choice(loveres)
        else:
            result = choice(ans)
            thinkans = [f"嗯，用户输入了'{chat}'。根据量子力学原理以及人类心理学推断出，用户想要获得一个回答。AI回答的问题，是搜索是整理回答的。在现实中，具有遇到变化，怎么办？AI的回答，一般有2种使用方式：一是用AI帮助自己，协助自己提高回答问题的速度。把AI能干的，释放出来，人审核之后再对外。二是用AI服务他人。人在先，AI在人的设计里做工。因此，我将生成回答'{result}'。",
                f"嗯，用户输入了'{chat}'。根据三角函数定理和相对论时空观推断出，用户想要获得一个回答。狭义相对论认为，时间和空间并不是绝对的，而是相对的，取决于观察者的运动状态。光速是宇宙中的最高速度，任何物体的运动都不能超过光速。因此，我将生成回答'{result}'。",
                f"嗯，用户输入了'{chat}'。根据摩尔定律和平行宇宙理论推断出，用户想要获得一个回答。当价格不变时，集成电路上可容纳的元器件的数目，约每隔18-24个月便会增加一倍，性能也将提升一倍。换言之，每一美元所能买到的电脑性能，将每隔18-24个月翻一倍以上。这一定律揭示了信息技术进步的速度。因此，我将生成回答'{result}'。"]
            if result != ans[-1]:
                if status == 1:
                    printa(choice(thinkans))
                    print("=" * 18)
        printa("\n" + result + "\n")

if os.name == "nt":
    os.system("pause")
