def disp(n):
    print("iam the one fun")
    n()
def one():
    print("iam first nested")
def two():
    print("iam second nested") 
disp(one)
disp(two)           