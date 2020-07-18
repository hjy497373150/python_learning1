# 常用于封装数据
import pickle
# my_list = [123, 3.14, '胡晋源', ['another list']]
# pickle_file = open('my_list.pkl', 'wb')
# pickle.dump(my_list, pickle_file)
# pickle_file.close()
pickle_file = open('my_list.pkl', 'rb')
my_list1 = pickle.load(pickle_file)
print(my_list1)
