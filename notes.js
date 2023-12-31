
state = Calc.getState()

state.expressions.list.push(
    {
    type: "expression",
    latex:  "o"
    }
)

Calc.setState(state)


var resetText = "r_{eset}=T\\to0"

for (var i = 1; i < 90; i++) {
    resetText += ",o_{" + i + "}\\to-1000,L_{" + i + "}\\to0,A_{" + i + "}\\to1,p_{" + i + "}\\to0"
}

state.expressions.list.push(
{
    type: "expression",
    id: "18",
    color: "#388c46",
    latex: resetText
},
{
    type: "expression",
    id: "32",
    color: "#2d70b3",
    latex: "f_{ps}=25",
    slider: {
        hardMin: true,
        playDirection: -1,
        min: "0",
        max: "50",
        step: "1"
    }
},
{
    type: "expression",
    id: "52",
    color: "#c74440",
    latex: "D_{t}=\\frac{1000}{f_{ps}}",
    hidden: true
},
{
    type: "expression",
    id: "56",
    color: "#aaaaaa",
    latex: "T=0",
    slider: {
        hardMin: true,
        min: "0",
        max: "4460"
    }
},
{
    type: "expression",
    id: "63",
    color: "#2d70b3",
    latex: "u_{pdate}=T\\to T+\\frac{1000}{f_{ps}}"
},
{
    type: "expression",
    id: "59",
    color: "#388c46",
    latex: "s_{ounds}=\\left\\{T=1000:\\left(p_{lay49}\\left(300,1\\right),p_{lay53}\\left(300,1\\right)\\right),T=3000:\\left(p_{lay49}\\left(3000,2\\right),p_{lay53}\\left(3000,2\\right)\\right)\\right\\}"
},
{
    type: "expression",
    id: "4176",
    color: "#c74440",
    hidden: true,
    latex: "p_{artials}=\\left[\\left(1,0.7\\right),\\left(2,0.2\\right),\\left(3,0.1\\right),\\left(4,0.05\\right),\\left(5,0.03\\right),\\left(6,0.02\\right),\\left(7,0.015\\right),\\left(8,0.01\\right),\\left(9,0.008\\right),\\left(10,0.005\\right)\\right]"
},
{
    type: "folder",
    id: "4175",
    title: "Amplitudes",
    collapsed: true
},
)

for (var i = 1; i < 90; i++) {
    state.expressions.list.push({
        type: "expression",
        folderId: "4175",
        latex: "A_{" + i + "}=1"
    })

}

state.expressions.list.push(
{
    type: "folder",
    id: "4174",
    title: "Offsets",
    collapsed: true
}
)

for (var i = 1; i < 90; i++) {
    state.expressions.list.push({
        type: "expression",
        folderId: "4174",
        latex: "o_{" + i + "}=-1000"
    })
}

state.expressions.list.push(
    {
        type: "folder",
        id: "4170",
        title: "Tones",
        collapsed: true
    }
)

for (var i = 1; i < 90; i++) {
    state.expressions.list.push({
        type: "expression",
        folderId: "4170",
        latex: "t_{" + i + "}=\\operatorname{tone}\\left(p_{artials}.x\\cdot n_{otes}\\left[" + i + "\\right],A_{" + i + "}p_{artials}.y\\cdot\\frac{E\\left(T-o_{" + i + "},L_{" + i + "}\\right)}{p_{artials}.x}\\right)"
    })
}
state.expressions.list.push(
    {
        type: "folder",
        id: "4169",
        title: "Note lengths",
        collapsed: true
    }
)

for (var i = 1; i < 90; i++) {
    state.expressions.list.push({
        type: "expression",
        folderId: "4169",
        latex: "L_{" + i + "}=0"
    })
}

state = Calc.getState()


state.expressions.list.push(
{
    type: "folder",
    id: "4171",
    title: "Actions",
    collapsed: true
})
    

for (var i = 1; i < 90; i++) {
    state.expressions.list.push(
        {
            type: "expression",
            folderId: "4171",
            // latex: "p_{lay" + i + "}\\left(L,a\\right)=o_{" + i + "}\\to T,L_{" + i + "}\\to L,A_{" + i + "}\\to a"
            latex: "p_{lay" + i + "}\\left(L,a\\right)=o_{" + i + "}\\to T,L_{" + i + "}\\to L,A_{" + i + "}\\to a,p_{" + i + "}\\to-H"
            // \\left\\{T-o_{" + i + "}>L_{" + i + "}:p_{" + i + "}\\to0\\right\\}
        }
    )
}




Calc.setState(state)

state.expressions.list.push(
{
    type: "folder",
    id: "4172",
    title: "Key Positions",
    collapsed: true
})

for (var i = 1; i < 90; i++) {
    state.expressions.list.push(
        {
            type: "expression",
            folderId: "4172",
            latex: "p_{" + i + "}=0"
            // latex: "p_{" + i + "}=\\left\\{\\left(T-o_{" + i + "}\\right)<50:-\\frac{H}{50}\\left(T-o_{" + i + "}\\right),T-o_{" + i + "}<L_{" + i + "}-50:-H,T-o_{" + i + "}<L_{" + i + "}:\\frac{H}{50}\\left(T-o_{" + i + "}\\right)-\\frac{L_{" + i + "}H}{50},0\\right\\}"
        }
    )
}

// Calc.setState(state)


state.expressions.list.push(
{
    type: "folder",
    id: "43",
    title: "unused",
    collapsed: true
},
{
    type: "expression",
    id: "3",
    folderId: "43",
    color: "#388c46",
    latex: ".E\\left(t\\right)=\\left\\{0\\le t<a_{ttack}:1-\\frac{t}{a_{ttack}},t\\le a_{ttack}+s_{us}:s_{us},t\\le a_{ttack}+s_{us}+r_{elease}:s_{us}-\\frac{t-a_{ttack}-s_{us}}{r_{elease}},0\\right\\}"
},
{
    type: "expression",
    id: "35",
    folderId: "43",
    color: "#aaaaaa",
    latex: ".E\\left(t\\right)=\\left\\{0\\le t<t_{attack}:1-e^{-\\frac{t}{a_{ttack}}},t<t_{attack}+r_{elease}:1,2\\right\\}"
},
{
    type: "expression",
    id: "36",
    folderId: "43",
    color: "#c74440",
    latex: ".E\\left(t\\right)=\\left\\{t<t_{attack}:1-e^{-\\frac{t}{t_{attack}}},t<t_{attack}:1+\\left(0.1-1\\right)e^{-\\frac{t}{t_{decay}}},t<r_{elease}:0.1,0\\right\\}"
},
{
    type: "expression",
    id: "38",
    folderId: "43",
    color: "#388c46",
    latex: ".E\\left(t\\right)=\\left\\{t<t_{attack}:\\frac{t}{t_{attack}},t<t_{attack}+t_{decay}:s_{us}+\\left(1-s_{us}\\right)e^{\\frac{-t+t_{attack}}{t_{decay}}},t<t_{attack}+t_{decay}+t_{release}:s_{us},0\\right\\}"
},
{
    type: "expression",
    id: "41",
    folderId: "43",
    color: "#c74440",
    latex: ".E\\left(t,L\\right)=\\left\\{t<t_{attack}:2^{\\frac{t}{t_{attack}}}-1,t<t_{attack}+t_{decay}:\\frac{s_{us}-1}{t_{decay}}\\left(t-t_{attack}\\right)+1,t<L:s_{us},-\\frac{s_{us}}{t_{decay}}\\left(t-L-t_{decay}\\right)\\right\\}"
},
{
    type: "expression",
    id: "8",
    folderId: "43",
    color: "#388c46",
    latex: ".u_{pdate}=t_{master}\\to t_{master}+\\frac{1000}{f_{ps}},t_{imes}\\to\\left\\{t_{imes}>2000:0,t_{imes}>0:t_{imes}+\\frac{1000}{f_{ps}},0\\right\\}"
},
{
    type: "expression",
    id: "22",
    folderId: "43",
    color: "#2d70b3",
    latex: ".p_{artials}=\\left[\\left(1,0.7\\right),\\left(2,0.2\\right),\\left(3,0.1\\right),\\left(4,0.05\\right),\\left(5,0.03\\right),\\left(6,0.02\\right),\\left(7,0.015\\right),\\left(8,0.01\\right),\\left(9,0.008\\right),\\left(10,0.005\\right),\\left(11,0.004\\right),\\left(12,0.003\\right),\\left(13,0.002\\right),\\left(14,0.0015\\right),\\left(15,0.001\\right),\\left(16,0.001\\right),\\left(17,0.001\\right),\\left(18,0.001\\right),\\left(19,0.001\\right),\\left(20,0.001\\right),\\left(21,0.001\\right)\\right]"
},
{
    type: "expression",
    id: "23",
    folderId: "43",
    color: "#388c46",
    latex: "t_{one}\\left(n\\right)=\\operatorname{tone}\\left(p_{artials}.x\\cdot n_{otes}\\left[n\\right],p_{artials}.y\\cdot\\frac{E\\left(t_{imes}\\left[n\\right],1000\\right)}{p_{artials}.x}\\right)"
},
{
    type: "expression",
    id: "15",
    folderId: "43",
    color: "#aaaaaa",
    latex: "p_{lay}\\left(n\\right)=t_{imes}\\to\\operatorname{join}\\left(t_{imes}\\left[1...n-1\\right],\\left[\\frac{1000}{f_{ps}}\\right],t_{imes}\\left[n+1...\\right]\\right)"
},
{
    type: "folder",
    id: "4168",
    title: "Envelope",
    collapsed: true
},
{
    type: "expression",
    id: "46",
    folderId: "4168",
    color: "#aaaaaa",
    latex: "E\\left(t,L\\right)=\\left\\{t<A:2^{\\frac{t}{A}}-1,t<A+D:\\frac{S-1}{D}\\left(t-A\\right)+1,t<L:-.0002\\left(t-A-D\\right)+S,S-0.001\\left(t-L\\right)-0.0002\\left(L-A-D\\right)\\right\\}"
},
{
    type: "expression",
    id: "40",
    folderId: "4168",
    color: "#aaaaaa",
    latex: "S=0.5"
},
{
    type: "expression",
    id: "6",
    folderId: "4168",
    color: "#c74440",
    latex: "A=10",
    slider: {
        hardMin: true,
        min: "0",
        max: "10"
    }
},
{
    type: "expression",
    id: "42",
    folderId: "4168",
    color: "#2d70b3",
    latex: "D=250"
},
{
    type: "expression",
    id: "16",
    color: "#c74440",
    latex: "n_{otes}=\\left[27.5\\cdot2^{\\frac{i}{12}}\\operatorname{for}i=\\left[0...87\\right]\\right]"
}
    
)

Calc.setState(state)