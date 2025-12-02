#import "Basic";
#import "String";
#import "File";

main :: () {
  file := read_entire_file("input.dat");

  initial :: 50;

  ins := split(file, "\n");
  curr := initial;
  dist := 0;
  answer := 0;

  for ins {
    if it == "" {
      continue;
    }

    dist = string_to_int(slice(it, 1, it.count - 1));

    for move: 0..dist - 1 {
      if it[0] == #char "L" {
        curr += 1;
      } else {
        curr -= 1;
      }

      if curr < 0 {
        curr = 100 + curr;
      } else if curr > 99 {
        curr = curr - 100;
      } 

      if curr == 0 {
        answer += 1;
      }
    }

    print("Curr %\n", curr);
  }

  print("Answer %\n", answer);
}
