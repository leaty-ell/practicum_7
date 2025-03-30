N = int(input())
volumes = []
edge = 1

while True:
    volume = edge ** 3
    if volume > N:
        break
    volumes.append(volume)
    edge += 1

print(' '.join(map(str, volumes)))
