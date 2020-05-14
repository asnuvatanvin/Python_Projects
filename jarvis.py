import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')

import wolframalpha
client = wolframalpha.Client("5J4UJ4-8837G33QXP")

import PySimpleGUI as sg

import speech_recognition as sr

sg.theme('DarkBlue')
# All the stuff inside your window.
layout = [[sg.Text('                                       Hi I am your Virtual Assistant')],
          [sg.Text('Enter a command:'), sg.InputText()],
          [sg.Button('Search'),    sg.Button('Calculate'),     sg.Button('Exit')]]

# Create the Window
window = sg.Window('JARVIS', layout)
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event in ('Calculate'):
        res = client.query(values[0])
        sg.Popup(next(res.results).text)
    else:
        res=values[0]
        res=res.lower()
        l=res.split()
        if l[0]=="what" or l[0]=='who' or l[0]=="which" or l[0]=="where" or l[0]=="when":
            res=" ".join(l[2:]) 
        try:
            page_py = wiki_wiki.page(res)
            ans=page_py.summary
            ans=ans.split('\n')
            if(len(ans[0])<50):
                res = client.query(values[0])
                cnt=0
                count=len(res)
                for pod in res.pods:
                    cnt=cnt+1
                    if cnt==count-1:
                        sg.Popup(pod.text)
            else:
                sg.Popup(ans[0])
        except:
            res = client.query(values[0])
            cnt=0
            count=len(res)
            for pod in res.pods:
                cnt=cnt+1
                if cnt==count-1:
                    sg.Popup(pod.text)
                  
window.close()
