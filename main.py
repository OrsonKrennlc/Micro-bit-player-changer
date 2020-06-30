from microbit import * #导入库
while True: #主循环
    if button_a.is_pressed() or button_b.is_pressed(): #按任意键激活程序
        a=0 #重置球员号码
        b=0 #重置球员号码
        display.scroll("A starting",a) #展示当前号码A已重置
        while counting==True: #号码A主循环
            if button_a.is_pressed(): #当左键按下时
                a+=1 #A号码+1
                display.scroll(a) #显示当前号码A的值
                sleep(700) #等待下次输入反应间隙
            counting=False #若0.7秒没有再次输入则认为结束输入
        counting=True #重置运行状态函数
        display.scroll("A finished=",a) #显示号码A的输入值
        display.scroll("B starting",b) #显示当前号码B已重置
        while counting==Ture: #号码B主循环
            if button_b.is_pressed(): #当右键按下时
                b+=1 #B号码+1
                display.scroll(b) #显示当前号码B的值
                sleep(700) #等待下次输入反应间隙
            counting=False #若0.7秒没有再次输入则认为结束输入
        counting=True #重置运行状态函数
        display.scroll("B finished=",b) #显示号码B的输入值
        display.scroll("CHANGING",a,"TO",b) #完整显示换人信息
