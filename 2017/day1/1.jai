#import "Basic";
#import "String";
#import "File";

main :: () {
  file := read_entire_file("input.dat");

  answer := 0;
  num := 0;
  next := 0;

  for 0..file.count - 1 {
    num = string_to_int(slice(file, it, 1));

    if it < file.count - 2 {
      next = string_to_int(slice(file, it + 1, 1));
      if num == next {
        answer += num;
      }
    } else {
      first := string_to_int(slice(file, 0, 1));
      if num == first {
        answer += num;
      }
    }

  }

  print("Answer %\n", answer);
}
