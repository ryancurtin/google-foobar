def answer(numbers):
  visited = {}
  pirates_visited = []
  current_pirate = 0

  while True:
    next_pirate = numbers[current_pirate]
    pirates_visited.append(current_pirate)

    if (visited.has_key(str(next_pirate))):
      loop_length = len(pirates_visited) - pirates_visited.index(next_pirate)
      break
    else:
      visited[str(current_pirate)] = 1
      current_pirate = next_pirate

  return loop_length
