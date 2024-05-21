import mido
mid = mido.MidiFile('midiFiles/midi9.mid')
f = open("output/midi1.txt", "w")
f2 = open("output/midi2.txt", "w")

fps = 40
frame = 1000/fps

messages = []

result = "s_{ounds}=\left\{"
result2 = "k_{eys}=\left\{"

usedNotes = []

def parseMsg(msg):
    result = {}
    if msg.type == "note_on" or msg.type == "note_off":
        result["type"] = msg.type
        result["note"] = msg.note
        result["velocity"] = msg.velocity
        result["time"] = msg.time
        return result
    if msg.type == "control_change" and msg.control == 64:
        result["type"] = msg.type
        result["value"] = 1 if msg.value > 0 else 0
        result["time"] = msg.time
        return result

track = mid.tracks[0]
for msg in track:
    if parseMsg(msg):
        messages.append(parseMsg(msg))
        
isOn = [False] * 121
durations = [0] * 121
velocities = [0] * 121
notes = {}
keyRelease = {}

totalTime = 0

for msg in messages:
    # Round to the nearest multiple of 12
    msg["time"] = msg["time"] + 12 / 2
    msg["time"] = (msg["time"] - (msg["time"] % 12))
    # msg["time"] = int(msg["time"] * 1 / 10) * 10
    for d in range(len(durations)):
        if isOn[d]:
            durations[d] += msg["time"]
    totalTime += msg["time"]
    if msg["type"] == "note_on":
        if (msg["note"] - 20) not in usedNotes:
            usedNotes.append(msg["note"] - 20)
        # print("creating note " + str(msg["note"]) + " at time " + str(totalTime))
        if totalTime in notes:
            flag = True
            # Check if note is already being played at totalTime. If so, don't play it and raise an alert
            for note in notes[totalTime]:
                if note[0] == msg["note"]:
                    print("WARNING: note " + str(msg["note"]) + " is already being played at time " + str(totalTime))
                    flag = False
                    break
            if flag:
                notes[totalTime].append([msg["note"], durations[msg["note"]], msg["velocity"]])
        else:
            notes[totalTime] = [[msg["note"], durations[msg["note"]], msg["velocity"]]]
        durations[msg["note"]] = 0
        isOn[msg["note"]] = True
    elif msg["type"] == "note_off": # Note released
        if totalTime in keyRelease:
            flag = True
            for key in keyRelease[totalTime]:
                if key == msg["note"]:
                    print("WARNING: note " + str(msg["note"]) + " is already being released at time " + str(totalTime))
                    flag = False
                    break
            if flag:
                keyRelease[totalTime].append(msg["note"])
        else:
            keyRelease[totalTime] = [msg["note"]]
        # str(totalTime) + "\\right|\le10:p_{" + str((msg["note"] - 20)) + "}\\to 0," # CHANGED
        str(totalTime) + "\\right|\le10:p_{" + str((msg["note"] - 20)) + "}\\to 0,"
        # print("releasing note " + str(msg["note"]) + " at time " + str(totalTime))
        isOn[msg["note"]] = False
        for note in notes[totalTime - durations[msg["note"]]]:
            if note[0] == msg["note"]:
                note[1] = durations[msg["note"]]
                break
    else: # Sustain pedal
        if msg["value"] == 1: # Pedal is pressed
            # If pedalUp at same time, then replace with pedalDown
            if totalTime in notes and "pedalUp" in notes[totalTime]:
                notes[totalTime].remove("pedalUp")
                notes[totalTime].append("pedalDown")
            # Else, add pedalDown
            elif totalTime in notes and "pedalDown" not in notes[totalTime]:
                notes[totalTime].append("pedalDown")
            else:
                notes[totalTime] = ["pedalDown"]
        elif msg["value"] == 0: # Pedal is released
            # If pedalDown at same time, then replace with pedalUp
            if totalTime in notes and "pedalDown" in notes[totalTime]:
                notes[totalTime].remove("pedalDown")
                notes[totalTime].append("pedalUp")
            elif totalTime in notes and "pedalUp" not in notes[totalTime]:
                notes[totalTime].append("pedalUp")
            else:
                notes[totalTime] = ["pedalUp"]

toAdd = {}
for n in keyRelease:
    if n not in notes:
        notes[n] = []
    elif n in notes: # Check if key is being played at the same time it is being released. If so, release after 50 ms
        for key in keyRelease[n]:
            for note in notes[n]:
                if (not isinstance(note, str)) and note[0] == key:
                    # toAdd[n + 49] = key
                    print("FIXED: removed note " + str(note) + " from time " + str(n) + " = " + str(n/384))
                    notes[n].remove(note)
                    keyRelease[n].remove(key)
                    break

f2.write(str(notes))
for n in notes:
    # Change BPM
    # result += ("\left|T-" + str(n * 1)) + "\\right|\le10:\left(" # CHANGED
    result += ("T=" + str(n * 2)) + ":\left("
    if n in keyRelease: # released at time n
        for key in keyRelease[n]:
            result += "p_{" + str(key - 20) + "}\\to 1," # CHANGED to 0
    for note in notes[n]: # played at time n
        if not isinstance(note, str): # If not pedalUp or pedalDown
            # note = [note, duration, velocity]
            result += "p_{lay" + str(note[0] - 20) + "}\left(" + str(round(note[1] * 1.75)) + "," + str(round((note[2] / 100) ** 2, 2)) + "\\right),"
        else: # If pedalUp or pedalDown
            if note == "pedalDown": # 0 = pedal down, 1 = pedal up
                result += "p_{edal}\\to 0,"
            else:
                result += "p_{edal}\\to 1,"
    result = result[:-1]
    result += "\\right),"

for n in keyRelease:
    result2 += ("\left|T-" + str(n * 2)) + "\\right|\le10:\left("
    for key in keyRelease[n]:
        result2 += "p_{" + str(key - 20) + "}\\to 0,"
    result2 = result2[:-1]
    result2 += "\\right),"

result = result[:-1]
result += "\\right\}"

result2 = result2[:-1]
result2 += "\\right\}"

f.write(result)
f2.write("usedNotes = " + str(usedNotes))

f.close()
f2.close()
