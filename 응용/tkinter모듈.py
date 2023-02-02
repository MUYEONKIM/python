from tkinter import *
#라벨 만들기
"""
root = Tk()
label = Label(root, text='hello world') #창에 표시 되어 있는 hello world는 Label(창에 포함되는 컴포넌트, 글자)
label.pack() # label의 객체를 창에 표시하는 역할

root.mainloop() # root창을 이벤트 루프에 들어가도록 함, mainroop()에 의해 root창은 종료되지 않고 버튼 클릭 등의 이벤트를 수신하거나, 사용자의 입력을 처리하는 등의 일을 계속 수행
"""

"""
root.title : 윈도우 창의 제목을 설정
ListBox : 블로그의 목록을 보여준다
Label : 라벨을 표시한다
Entry : 제목을 보여주고 입력할 수 있다
Text : 내용을 보여주고 입력할 수 있다
Button : 버튼 추가
"""

#리스트 박스 만들기 = 블로그 목록처럼 정해진 순서가 있는 여러 개의 데이터를 표시하는 컴포넌트
"""
root = Tk()
listbox = Listbox(root)
listbox.pack()

a = ['one', 'two', 'three','four']
for i in a :
    listbox.insert(END, i) #listbox.insert(index,'항목') 여기서 index자리에 end를 넣었다는 건 마지막으로 들어간 문장 아래에 리스트를 추가한다

def event_for_listbox(event):
    prtin(19+1)

listbox.bind('<<ListBoxSelect>>', event_for_listbox) #bind()를 통해서 컴포넌트에 이벤트 연결, 이 함수를 이용해 리스트박스를 선택했을 때 발생하는 이벤트 <<listboxselect>>와 호출할 함수 event_for_listbox()를 연결했다

root.mainloop()
"""

# 엔트리 만들기 - 엔트리는 텍스트를 입력하거나 보여주고자 사용하는 컴포넌트, 주로 한 줄로 구성된 문자열을 처리, 여러 줄의 문자열은 text컴포넌트 사용
"""
root = Tk()
entry = Entry(root)
entry.pack()

entry.insert(0,"Hello")

root.mainloop()
"""

# 텍스트 만들기 - 여러 줄의 문자열을 처리할 수 있다는 점 이외에는 엔트리 컴포넌트와 거의 같다
"""
root = Tk()
text = Text(root)
text.pack()

data = '''life is too short
so you must use python
Do not this behavior you must die'''

text.insert(1.0, data) #앞의 소수점을 기준으로 왼쪽은 행, 오른쪽은 열을 뜻한다, 행은 1부터 시작이지만 열은 0부터 시작
# 따라서 2행2열이면 2,1


root.mainloop()
"""

#버튼 만들기 - 클릭했을 때 특정함수를 실행하고자 사용하는 컴포넌트
"""
root = Tk()
b1 = Button(root, text='테스트 버튼')
b1.pack()

def btn_click(event):
    print("버튼이 클릭되었습니다")

b1.bind('<Button-1>', btn_click)

root.mainloop()
"""

