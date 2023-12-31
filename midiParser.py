import mido
mid = mido.MidiFile('midiTest5.mid')
mid = mido.MidiFile('midi3.mid')
f = open("midi1.txt", "w")
f2 = open("midi2.txt", "w")

fps = 20
frame = 1000/fps

messages = []

result = "s_{ounds}=\left\{"
result2 = "k_{eys}=\left\{"

# "s_{ounds}=\left\{T=0:\left(p_{lay57}\left(2000,1\right),p_{lay60}\left(2000,1\right)\right),
# \left|T-170\right|\le20:\left(p_{lay69}\left(600,1.5\right),p_{lay72}\left(600,1.5\right)\right),
# \left|T-670\right|\le20:\left(p_{lay65}\left(500,0.5\right),p_{lay69}\left(500,0.5\right)\right)\right\}"


# \left|T-500\right|\le20:\left(p_{lay1})
def parseMsg(msg):
    result = {}
    if msg.type == "note_on" or msg.type == "note_off":
        result["type"] = msg.type
        result["note"] = msg.note
        result["velocity"] = msg.velocity
        result["time"] = msg.time
        return result



track = mid.tracks[0]
for msg in track:
    if parseMsg(msg):
        messages.append(parseMsg(msg))
    # messages.append(msg)
    # f.write(str(msg)+"\n")
    # f.write(str(parseMsg(msg)) + "\n")
        
isOn = [False] * 121
durations = [0] * 121
velocities = [0] * 121
notes = {}
keyRelease = {}

totalTime = 0

for msg in messages:
    # msg["time"] *= 1.5
    # msg["time"] = msg["time"] + frame / 2
    # msg["time"] = (msg["time"] - (msg["time"] % frame))
    msg["time"] = int(msg["time"] * 1 / 10) * 10
    for d in range(len(durations)):
        if isOn[d]:
            durations[d] += msg["time"]
    totalTime += msg["time"]
    if msg["type"] == "note_on":
        # print("creating note " + str(msg["note"]) + " at time " + str(totalTime))
        if totalTime in notes:
            flag = True
            # Check if note is already bieng played at totalTime. If so, don't play it and raise an alert
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
    else: # Note released
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
            

        # result2 += "\left|T-" + str(totalTime) + "\\right|\le20:p_{" + str((msg["note"] - 20)) + "}\\to 0,"
        # print("releasing note " + str(msg["note"]) + " at time " + str(totalTime))
        isOn[msg["note"]] = False
        for note in notes[totalTime - durations[msg["note"]]]:
            if note[0] == msg["note"]:
                note[1] = durations[msg["note"]]
                break
    
# f.write(str(notes))
# for n in notes:
#     f.write(str(notes[n]) + "\n")

for n in notes:
    result += ("\left|T-" + str(n * 2)) + "\\right|\le20:\left("
    for note in notes[n]:
        result += "p_{lay" + str(note[0] - 20) + "}\left(" + str(note[1] * 1) + "," + str(note[2] / 100) + "\\right),"
    result = result[:-1]
    result += "\\right),"


for n in keyRelease:
    result2 += ("\left|T-" + str(n * 2)) + "\\right|\le20:\left("
    for key in keyRelease[n]:
        result2 += "p_{" + str(key - 20) + "}\\to 0,"
    result2 = result2[:-1]
    result2 += "\\right),"

result = result[:-1]
result += "\\right\}"


result2 = result2[:-1]
result2 += "\\right\}"

f.write(result)
f2.write(result2)

f.close()
f2.close()

