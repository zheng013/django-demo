class A:
    def __init__(self):
        print("__init__ ")
        super(A, self).__init__()

    def __new__(cls):
        print("__new__ ")
        return super(A, cls).__new__(cls)

    def __call__(self):  # 可以定义任意参数
        print('__call__ ')


# class A(type):
#     """自定义单例元类"""

#     def __init__(cls, *args, **kwargs):
#         print("__init__ ")
#         super().__init__(*args, **kwargs)

   
#     def __call__(cls, *args, **kwargs):
#         print('__call__ ')

a=A()