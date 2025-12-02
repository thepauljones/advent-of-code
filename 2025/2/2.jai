#import "Basic";
#import "String";
#import "File";


is_valid :: (str:string, length:int = 2) -> bool {
  if length > str.count / 2 {
    return false;
  }

  if (str.count % length > 0) {
    return is_valid(str, length + 1);
  }

  parts : [..]string;

  for 0..(str.count / length) - 1 {
    pos := it * length;
    array_add(*parts, slice(str, pos, length));
  }

  all_same := true;
  for parts {
    for inner: parts {
        if inner != it {
            all_same = false;
          }
      }
  }

  if all_same {
    return true;
  } else {
    return is_valid(str, length + 1);
  }

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
