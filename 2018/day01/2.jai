#import "Basic";
#import "File_Utilities";
#import "String";
#import "Hash_Table";
#import "File";

main :: () {
  file := read_entire_file("input.dat");
  bits := split(file, "\n");
  count := 0;

  nums : [..] int;

  for bits {
    array_add(*nums, to_integer(it));
  }

  table: Table(s64, bool, null, LOAD_FACTOR_PERCENT=70);

  i := 0;
  loop := true;
  it : int;
  is_plus := true;
  value := 0;

  loopCount := 1;
  while loop {
    it = nums[i];

    value = it;

    if value == 0 continue;

    count += value;

    if table_find_new(*table, count) {
      print("First repeated value is %\n", count);
      loop = false;
    }

    i += 1;
    if i == nums.count - 1 {
      i = 0;
    }

    loopCount += 1;

    table_add(*table, count, true);
  }
  exit(1);
}
