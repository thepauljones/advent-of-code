#import "Basic";
#import "String";
#import "File";
#import "Math";
#import "Hash_Table";

V2 :: struct {
    x: s64;
    y: s64;
}

main :: () {
  file := read_entire_file("input.dat");
  lines := split(trim(file), "\n");

  grid : [..][]u8;

  for lines {
    arr := string_to_chars(it);
    array_add(*grid, arr);
  }

  adjs : [..]V2;
  answer := 0;
  rolls := 0;

  triggers: Table(string, bool, null, LOAD_FACTOR_PERCENT=70);

  for y, j:grid {
    for x, i: y {
      if x != 64 continue;

      adjs = get_adjacents(grid, .{j, i});
      rolls = 0;

      for a:adjs {
        if grid[a.y][a.x] == 64 {
          rolls += 1;
        }
      }

      if rolls < 4 {
        table_add(*triggers, sprint("%-%", j, i), true);
        answer += 1;
      } 
    }
  }

  print_grid := true;

  if print_grid {
    for y, j:grid {
      for x, i: y {
        found, val := table_find_new(*triggers, sprint("%-%", j, i));
        if val {
          print("x");
        } else {
          print_character(grid[j][i]);
        }
      }

      print("\n");
    }
  }

  print("\nAnswer: %\n", answer);
}

get_adjacents :: (grid :[][]u8, pos:V2) -> [..]V2 {
  result : [..]V2;

  directions :[8]V2 = .[.{-1, 0},.{0, -1},.{1, 0},.{0, 1},.{1, -1},.{-1, 1},.{-1, -1},.{1, 1}];

  for directions {
    i:= it.x + pos.x;
    j:= it.y + pos.y;
    if i > -1 && i < grid[0].count && j > -1 && j < grid.count {
      array_add(*result, .{j, i});
    }
  }

  return result;
}

string_to_chars :: (s: string) -> []u8 {
  l:[..]u8;
  for s {
    array_add(*l, it);
  }
  return l;
}

