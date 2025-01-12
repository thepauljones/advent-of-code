extends SceneTree

var dirs = {
  "U": Vector2(0, 1),
  "D": Vector2(0, -1),
  "L": Vector2(-1, 0),
  "R": Vector2(1, 0)
}

func mapWire(wire):
  var positions = {}
  var pos = Vector2(0, 0)

  var moves = wire.split(",")
  var total_dist = 0
  for i in moves:
    var dir = i[0]
    var dist = int(i.substr(1, len(i)))

    var count = 0
    while count < dist:
      pos = pos + dirs[dir]
      total_dist += 1
      positions[pos] = total_dist
      count += 1

  return positions


func mdistance(a: Vector2, b: Vector2):
  var result = abs(a.x - b.x) + abs(a.y - b.y)
  return result


func _init():
  var file = FileAccess.open("res://3-input.txt", FileAccess.READ)

  if file:
      var content = file.get_as_text()
      file.close()
      var wires = content.trim_suffix("\n").split('\n')

      var one = mapWire(wires[0])
      var two = mapWire(wires[1])

      var intersections = {}
      for k in one.keys():
        if two.has(k):
          intersections[k] = mdistance(Vector2(0, 0), k)

      # Part 1
      print("Part 1: ", intersections.values().min())

      # Part 2
      var distances = []
      for x in intersections.keys():
        distances.append(one[x] + two[x])

      print("Part 2: ", distances.min())
        
      quit()


