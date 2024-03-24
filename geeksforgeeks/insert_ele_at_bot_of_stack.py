#You are given a stack st of n integers and an element x. You have to insert x at the bottom of
# the given stack. Note: Everywhere in this problem, the bottommost element of the stack is shown
# first while priniting the stack.
def insertAtBottom( st, x):
    i = len(st)
    st.append(0)
    while i >= 0:
        if i!=0:
            st[i] = st[i - 1]
            i -= 1
        else:
            st[i] = x
            i-=1
    return st
st=[4,3,2,1,8]
x=2
print(insertAtBottom(st,x))