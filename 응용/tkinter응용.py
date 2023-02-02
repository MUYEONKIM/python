"""
grid() 함수의 row는 행, column은 열을 뜻함
columnspan은 열을 병합할 때 사용하므로, columnspan=3은 3개의 열을 병합한다는 뜻
rowspan 은 행을 병합할 때 사용
sticky는 컴포넌트가 차지하는 열 또는 행의 크기에 맞게 확장할 때 사용
e 오른쪽 w 왼쪽, n위쪽, s아래쪽   함께 쓰기 가능 ew면 좌우로 확장하라는 뜻
"""

from tkinter import *
from tkinter.messagebox import * #메세지 박스 쓰기 위함

showerror("오류", "오류가 발생했습니다") # (제목, 내용) 이렇게 하면 오류창 나타남


root = Tk()

listbox = Listbox(root)
label= Label(root, text = '제목')
entry = Entry(root)
text = Text(root)
b1 = Button(root, text = '생성')
b2 = Button(root, text = '수정')
b3 = Button(root, text = '삭제')
listbox.grid(row=0, column=0, columnspan=3, sticky='ew')
label.grid(row=1, column=0)
entry.grid(row=1, column=1, columnspan=2, sticky='ew')
text.grid(row=2, column=0, columnspan=3)
b1.grid(row=3, column=0, sticky='ew')
b2.grid(row=3, column=1, sticky='ew')
b3.grid(row=3, column=2, sticky='ew')


root.mainloop()

# 추가적인건 https://wikidocs.net/132610