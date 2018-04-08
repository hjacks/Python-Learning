from die import Die
import  pygal

# 创建一个D6
# die = Die()

# 创建两个D6骰子
die_1 = Die()
die_2 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(100):
    # result = die.roll()
    result = die_1.roll()+die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
#print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

# hist.title = "Result of rolling one D6 100 times"
hist.title = "Result of rolling two D6 100 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# hist.add("D6",frequencies)
hist.add("D6+D6",frequencies)
hist.render_to_file('die_visual2.svg')