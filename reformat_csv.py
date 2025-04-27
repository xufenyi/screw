import os


files = [f for f in os.listdir(os.getcwd()) if f.endswith('.csv')]
for file in files:
    lines = ['x,y,action']
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                lines.append(line.strip())
    assert len(lines) > 2
    lines[1] = lines[1] + ',jump'
    for i in range(2, len(lines)):
        lines[i] = lines[i] + ',mark'
    with open(file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
