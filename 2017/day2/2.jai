#import "Basic";
#import "String";
#import "File";
#import "Math";

main :: () {
  file := read_entire_file("input.dat");
  lines := split(file, "\n");

  answer := 0;
  for lines {
    max := 0;
    min := 99999999999999;
    num := 0;

    diff := 0;

    cells := split(it, "\t");
    for cell:cells {

      num = string_to_int(cell);

      if num > max {
        max = num;
      }

      if num < min {
        min = num;
      }

    }

    answer += abs(max - min);
  }
  print("Answer: %\n", answer);
}
