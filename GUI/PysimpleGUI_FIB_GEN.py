from optparse import Values
import PySimpleGUI as sg


#sg.theme('BluePurple')

theme_list = ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 
'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 
'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']

layout = [
        [sg.Text('Show:'), sg.Combo(["All Values", "Result"], key = "drop_down")],
        [sg.Text('Enter the Fib sequence you would like to see')],
        [sg.Input("", key = "Fib_Input"), sg.Button("Calculate", key = "-Calculate_Button-")],
        [sg.Combo(theme_list)],
        [sg.Button("Update_Theme")]
        #sg.Cancel()]
    ]

window = sg.Window('Fibonacci Generator', layout)

def fib(sequence, return_option):

    counter = 0
    fib_numbers = []

    while counter < sequence:
        if len(fib_numbers) < 2:
            fib_numbers.append(counter)
        else:
            n1 = counter - 1
            n2 = counter - 2
            fib_numbers.append(fib_numbers[n1] + fib_numbers[n2])

        counter += 1

    if return_option == 1:
        return (f'The Fibbonaci Sequence is: {fib_numbers}')
    elif return_option == 2:
        return (f'The Fibbonaci Number for the {sequence} iteration is: {fib_numbers[-1]}')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-Calculate_Button-":
        print(values)
        #print(values["drop_down"])
        #print(values["Fib_Input"])

        drop_down_Value = values["drop_down"]
        fib_seq = values["Fib_Input"]

        # if fib_seq.isnumeric():
        #     print(drop_down_Value, fib_seq)
        # if drop_down_Value == "All Values":
        #      fib(fib_seq, 1)
        # if drop_down_Value == "Result":
        #      fib(fib_seq, 2)
        
        #fib(values["Fib_Input"], values["drop_down"]) 

 

window.close()