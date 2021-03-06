import simplegui

# define global variables
interval = 100
t = 0
successful_stops = 0
total_stops = 0
stop = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    munites = int(t / 600)                        
    seconds = int(t % 600) / 10
    milliseconds = int(t % 600) - seconds * 10
    if seconds &lt; 10:
        return str(munites) + ":0" + str(seconds) + "." + str(milliseconds)   
    elif seconds &gt;= 10:
        return str(munites) + ":" + str(seconds) + "." + str(milliseconds) 

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global t, stop
    stop = False
    timer.start()
    
def stop():
    global t, successful_stops, total_stops, stop
    stop = True
    if t % 10 == 0 and t != 0:
        successful_stops += 1
        total_stops += 1
    elif t %10 != 0 and t != 0:
        total_stops +=1        
    timer.stop()
    
    
def reset():
    global t, successful_stops, total_stops, stop
    t = 0
    stop = True
    successful_stops = 0
    total_stops = 0
    timer.stop()


# define event handler for timer with 0.1 sec interval
def tick():
    print "tick"
    global t
    t += 1
    print t


# define draw handler
def draw(canvas):
    text = format(t)
    canvas.draw_text(text, (80, 120), 48, "white")
    canvas.draw_text(str(successful_stops) + "/" + str(total_stops), (250, 60), 18, "red")
  
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)


# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)


# start frame
frame.start()
#reset()
