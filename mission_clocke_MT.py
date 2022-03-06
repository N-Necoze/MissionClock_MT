# --- library ----
# Tkinter
import tkinter as tk
import datetime

# =========== 期限入力(変更部分) ===========
kigen_name_1 = '学士梗概集提出期限'
text_1 = "Deadline For Submitting Bachelor's Abstracts"
kigen_time_1 = '2022/1/27,16:30'

kigen_name_2 = '学士論文提出期限'
text_2 = "Deadline For Submission Of Bachelor's Papers"
kigen_time_2 = '2022/2/7,16:30'
# ========================================

kigen_1 = kigen_time_1.split(',')[0]
time_1 = kigen_time_1.split(',')[1]
year_1 = int(kigen_1.split('/')[0])
month_1 = int(kigen_1.split('/')[1])
day_1 = int(kigen_1.split('/')[2])
hour_1 = int(time_1.split(':')[0])
min_1 = int(time_1.split(':')[1])

kigen_2 = kigen_time_2.split(',')[0]
time_2 = kigen_time_2.split(',')[1]
year_2 = int(kigen_2.split('/')[0])
month_2 = int(kigen_2.split('/')[1])
day_2 = int(kigen_2.split('/')[2])
hour_2 = int(time_2.split(':')[0])
min_2 = int(time_2.split(':')[1])

target1_1 = datetime.datetime(year_1, month_1, day_1, hour_1, min_1)
date1_t1 = target1_1.strftime("%Y/%m/%d")
date1_t2 = target1_1.strftime("%Y/%m/%d %H:%M:%S")

target2_2 = datetime.datetime(year_2, month_2, day_2, hour_2, min_2)
date2_t1 = target2_2.strftime("%Y/%m/%d")
date2_t2 = target2_2.strftime("%Y/%m/%d %H:%M:%S")


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # メインウィンドウサイズ
        master.geometry("1850x640")
        master.title("〇〇作戦アプリ")
        Label = tk.Label
        self.pack()
        # Countdown_1
        self.Countdown_1 = Label(self,
                                 bg="black",
                                 font=("", 50),
                                 text="Countdown",
                                 fg="#FF9933")
        self.Countdown_1.grid(row=0, column=1, padx=(0, 200), sticky="news")
        # [期限名1]
        self.Countdown_time_1 = Label(self,
                                      bg="black",
                                      font=(('ToppanBunkyuMidashi'
                                             'MinchoStdN-ExtraBold'),
                                            60,
                                            "bold"),
                                      text=kigen_name_1,
                                      fg="#FF9933")
        self.Countdown_time_1.grid(row=1, column=0, sticky="news")
        # [期限日付表示_1]
        self.wt1 = Label(self,
                         bg="black",
                         font=("DSEG7 Classic", 80, "bold"),
                         fg="#FF9933")
        self.wt1.grid(row=1, column=1, sticky="news")
        # [期限時刻表示_1]
        self.wt1_1 = Label(self,
                           bg="black",
                           font=("DSEG7 Classic", 80, "bold"),
                           fg="#FF9933")
        self.wt1_1.grid(row=1, column=2, padx=(0, 300), sticky="news")
        # [英語表記]
        self.Countdown_UN_1 = Label(self,
                                    bg="black",
                                    font=("", 30),
                                    text=text_1,
                                    fg="#FF9933")
        self.Countdown_UN_1.grid(row=2, column=0, sticky="news")
        # [ラベル(Day)]
        self.Countdown_UN_1 = Label(self,
                                    bg="black",
                                    font=("", 30),
                                    text="Day",
                                    fg="#FF9933")
        self.Countdown_UN_1.grid(row=2, column=1, sticky="news")
        # [ラベル(Time)]
        self.Countdown_UN_1 = Label(self,
                                    bg="black",
                                    font=("", 30),
                                    text="Time",
                                    fg="#FF9933")
        self.Countdown_UN_1.grid(row=2, column=2, sticky="news")

        # Countdown_2
        self.Countdown_2 = Label(self,
                                 bg="black",
                                 font=("", 50),
                                 text="Countdown",
                                 fg="#FF9933")
        self.Countdown_2.grid(row=3, column=1, padx=(0, 200), sticky="news")
        # [期限名2]
        self.Countdown_time_2 = Label(self,
                                      bg="black",
                                      font=(('ToppanBunkyuMidashi'
                                             'MinchoStdN-ExtraBold'),
                                            60,
                                            "bold"),
                                      text=kigen_name_2,
                                      fg="#FF9933")
        self.Countdown_time_2.grid(row=4,
                                   column=0,
                                   padx=(0, 50),
                                   sticky="news")
        # [期限日付表示_2]
        self.wt2 = Label(self,
                         bg="black",
                         font=("DSEG7 Classic", 80, "bold"),
                         fg="#FF9933")
        self.wt2.grid(row=4, column=1, sticky="news")
        # [期限時刻表示_2]
        self.wt2_1 = Label(self,
                           bg="black",
                           font=("DSEG7 Classic", 80, "bold"),
                           fg="#FF9933")
        self.wt2_1.grid(row=4, column=2, padx=(0, 300), sticky="news")
        # [英語表記]
        self.Countdown_UN_2 = Label(self,
                                    bg="black",
                                    font=("", 30),
                                    text=text_2,
                                    fg="#FF9933")
        self.Countdown_UN_2.grid(row=5, column=0, sticky="news")
        # [ラベル(Day)]
        self.Countdown_UN_2 = Label(self,
                                    bg="black",
                                    font=("", 30),
                                    text="Day",
                                    fg="#FF9933")
        self.Countdown_UN_2.grid(row=5, column=1, sticky="news")
        # [ラベル(Time)]
        self.Countdown_UN_2 = Label(self,
                                    bg="black",
                                    font=("", 30), text="Time", fg="#FF9933")
        self.Countdown_UN_2.grid(row=5, column=2, sticky="news")

        # --- 日本標準時 ---
        self.Countdown_3 = Label(self,
                                 bg="black",
                                 font=("", 50),
                                 text="Live",
                                 fg="#FF9933")
        self.Countdown_3.grid(row=9, column=1, padx=(0, 350), sticky="news")
        # [日本標準時]
        self.Countdown_time_3 = Label(self,
                                      bg="black",
                                      font=(('ToppanBunkyuMidashi'
                                             'MinchoStdN-ExtraBold'),
                                            60,
                                            "bold"),
                                      text="日本標準時",
                                      fg="#FF9933")
        self.Countdown_time_3.grid(row=10,
                                   column=0,
                                   padx=(0, 120),
                                   sticky="news")
        # [期限時刻表示]
        self.wt3 = Label(self,
                         bg="black",
                         font=("DSEG7 Classic", 80, "bold"),
                         fg="#FF9933")
        self.wt3.grid(row=10, column=1)
        self.wt3_1 = Label(self,
                           bg="black",
                           font=("DSEG7 Classic", 80, "bold"),
                           fg="#FF9933")
        self.wt3_1.grid(row=10, padx=(0, 300), column=2)
        # [英語表記]
        self.Countdown_UN_3 = Label(self,
                                    bg="black",
                                    font=("", 30),
                                    text="Japan Standard Time",
                                    fg="#FF9933")
        self.Countdown_UN_3.grid(row=11,
                                 column=0,
                                 padx=(0, 120),
                                 sticky="news")
        master.after(50, self.update)

    def update(self):
        # Countdown_setup
        today = datetime.datetime.now()
        # Target_Time
        target_day_1 = (datetime.datetime.
                        strptime(date1_t2, '%Y/%m/%d %H:%M:%S'))
        target_time_1 = (datetime.datetime.
                         strptime(date1_t2, '%Y/%m/%d %H:%M:%S'))
        if today > target_day_1:
            self.wt1.configure(text=("%s" % 0))
            self.wt1_1.configure(text=("%s:%s:%s" % (0, 0, 0)))
        else:
            days_Abstracts_days = target_day_1 - today
            days_Abstracts_time = target_time_1 - today
            secs_time_1 = days_Abstracts_time.seconds+1
            # Days
            self.wt1.configure(text=days_Abstracts_days.days)
            # Time
            second_1 = int((secs_time_1 % 60))
            minut_1 = int((secs_time_1 / 60) % 60)
            hour_1 = int((secs_time_1 / 3600))
            (self.wt1_1.
             configure(text=("%s:%s:%s" % (hour_1, minut_1, second_1))))
        # Target_Time
        target_day_2 = (datetime.datetime.
                        strptime(date2_t2, '%Y/%m/%d %H:%M:%S'))
        target_time_2 = (datetime.datetime.
                         strptime(date2_t2, '%Y/%m/%d %H:%M:%S'))
        if today > target_day_2:
            self.wt2.configure(text=("%s" % 0))
            self.wt2_1.configure(text=("%s:%s:%s" % (0, 0, 0)))
        else:
            days_Papers_days = target_day_2 - today
            days_Papers_time = target_time_2 - today
            secs_time_2 = days_Papers_time.seconds+1
            # Days
            self.wt2.configure(text=days_Papers_days.days)
            # Time
            second_2 = int((secs_time_2 % 60))
            minut_2 = int((secs_time_2 / 60) % 60)
            hour_2 = int((secs_time_2 / 3600))
            (self.wt2_1.
             configure(text=("%s:%s:%s" % (hour_2, minut_2, second_2))))
        # Live
        self.wt3.configure(text=today.strftime("%m-%d"))
        self.wt3_1.configure(text=today.strftime("%H:%M:%S"))
        # 1秒後に再表示
        self.master.after(1000, self.update)


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.config(bg="black")
    app.mainloop()


if __name__ == "__main__":
    main()
