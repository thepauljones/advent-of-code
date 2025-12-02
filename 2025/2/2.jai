#import "Basic";
#import "String";
#import "File";
#import "Hash_Table";

table: Table(string, int, null, LOAD_FACTOR_PERCENT=70);

is_valid :: (str:string, length:int = 2) -> bool {
  key := sprint("%,%", str, length);

  // Can't be more than two sets, so longer than half
  if length > str.count / 2 {
    return false;
  }

  // Has to be equally divisible
  if (str.count % length > 0) {
    return is_valid(str, length + 1);
  }

  // Check cache
  found, value := table_find_new(*table, key);

  if (found) {
    table_add(*table, key, 1);
    return true;
  }

  all_same := true;

  base := slice(str, 0, length);

  for 0..str.count / length - 1 {
    check := slice(str, it * length + length, length);
    if check == "" continue;

    // print("Checking % against %\n", base, check);

    if base != check {
      all_same = false;
      break;
    }
  }

  if all_same {
    table_add(*table, key, 1);
    return true;
  } else {
    return is_valid(str, length + 1);
  }

  table_add(*table, key, -1);
  return false;
}

main :: () {
  file := read_entire_file("input.dat");
  pairs := split(file, ",");

  answer := 0;

  nums :[]string;
  start :int;
  end: int;
  num: string;

  for pairs {
    if it == "" continue;

    nums = split(it, "-");
    start = string_to_int(nums[0]);
    end = string_to_int(nums[1]);

    for start..end {
      num = sprint("%", it);

      if is_valid(num, 1) {
        answer += it;
      }
    }
  }
  print("Answer %\n", answer);
}
