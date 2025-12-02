#import "Basic";
#import "String";
#import "File";

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

      if num.count % 2 == 0 {

        if slice(num, 0, num.count / 2) == slice(num, num.count / 2, num.count -1) {
          answer += string_to_int(num);
        }
      }
    }
  }
  print("Answer %\n", answer);
}
