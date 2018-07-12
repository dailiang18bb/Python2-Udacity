import webbrowser
import time

print "Program start at " + time.ctime() + "!"
count = 0
while count < 3:
    time.sleep(5)
    webbrowser.open_new("https://www.youtube.com/watch?v=dLG4as6BNYo&list=RDdLG4as6BNYo&start_radio=1")
    count = count + 1
    print count, "times"

print "Program finished"
