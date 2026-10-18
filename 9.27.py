names = ['mao zedong','deng xiaoping','jiang jieshi','xi jinping']
print(names)
#增加嘉宾
print(f"zun jing de {names[2].title()} bu neng lai le.")
names[2] = 'max'
names.insert(0,'engs')
names.insert(2,'sidaling')
names.append('lie ning')
print("I got a new bigger table ,everyone can go there , and I invite another people")
print(f"zun jing de {names[0].title()} xi wang ni neng lai fu yue")
print(f"zun jing de {names[1].title()} xi wang ni neng lai fu yue")
print(f"zun jing de {names[2].title()} xi wang ni neng lai fu yue")
print(f"zun jing de {names[3].title()} xi wang ni neng lai fu yue")
print(f"zun jing de {names[4].title()} xi wang ni neng lai fu yue")
print(f"zun jing de {names[5].title()} xi wang ni neng lai fu yue")
print("because of some ranson I only can invit teo people ,sorry")
print(names)
print(f"I will invite {len(names)} people to dinner")