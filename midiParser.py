import mido
mid = mido.MidiFile('midiTest3.mid')
mid = mido.MidiFile('midi1B.mid')
f = open("midi1.txt", "w")

messages = []

result = "s_{ounds}=\left\{"

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

totalTime = 0

for msg in messages:
    # f.write(str(msg)+"\n")
    msg["time"] = round(msg["time"]/10) * 10
    for d in range(len(durations)):
        if isOn[d]:
            durations[d] += msg["time"]
    totalTime += msg["time"]
    if msg["type"] == "note_on":
        print("creating note " + str(msg["note"]) + " at time " + str(totalTime))
        if totalTime in notes:
            notes[totalTime].append([msg["note"], durations[msg["note"]], msg["velocity"]])
        else:
            notes[totalTime] = [[msg["note"], durations[msg["note"]], msg["velocity"]]]
        durations[msg["note"]] = 0
        isOn[msg["note"]] = True
    else: # Note released
        print("releasing note " + str(msg["note"]) + " at time " + str(totalTime))
        isOn[msg["note"]] = False
        for note in notes[totalTime - durations[msg["note"]]]:
            if note[0] == msg["note"]:
                note[1] = durations[msg["note"]]
                break
    
# f.write(str(notes))
# for n in notes:
#     f.write(str(n) + "\n")

for n in notes:
    result += ("\left|T-" + str(n * 2)) + "\\right|\le20:\left("
    for note in notes[n]:
        result += "p_{lay" + str(note[0] - 20) + "}\left(" + str(note[1] / 2) + "," + str(note[2] / 100) + "\\right),"
    result = result[:-1]
    result += "\\right),"

result = result[:-1]
result += "\\right\}"

f.write(result)


f.close()

