#import "Basic";
#import "File";
#import "Hash_Table";
#import "String";
#import "Math";

main :: () {
  file := read_entire_file("test.dat");
  lines := split(file, "\n");

  parts: []string;
  id: string;
  posX: int;
  posY: int;
  width: int;
  height: int;
  posBits: []string;
  sizeBits: []string;

  table: Table(string, [..]string, null, LOAD_FACTOR_PERCENT=70);

  for lines {
      // Why does jai always have this, the file ends without a space
      if it == "" {
          continue;
      }

      parts = split(it, " ");

      id = slice(it, 1, parts[0].count - 1);

      posBits = split(parts[2], ",");
      posX = string_to_int(posBits[0]);
      posY = string_to_int(posBits[1]);

      sizeBits = split(parts[3], "x");
      width = string_to_int(sizeBits[0]);
      height = string_to_int(sizeBits[1]);

      for posX..posX + width  - 1 {
          for itY: posY..posY + height - 1 {
            ida : [..]string;
            key := sprint("%,%", it, itY);
            found, found_ids := table_find_new(*table, key);

            if found {
              array_add(*found_ids, id);
              table_set(*table, key, found_ids);
            } else {
              array_add(*ida, id);
              table_add(*table, key, ida);
            }
          }
      }
    }
    count := 0;
    for table {
      if it.count > 1 {
        count += 1;
      }
      print("% %\n", it_index, it);
    }

    print("Answer: %\n", count);
}
