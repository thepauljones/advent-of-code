#import "Basic";
#import "String";
#import "File";
#import "Math";

main :: () {
  file := read_entire_file("input.dat");
  lines := split(file, "\n");

  answer := 0;
  for lines {
    num := 0;
    num2 := 0;

    division := 0;

    cells := split(it, "\t");
    for cell, i:cells {
      num = string_to_int(cell);
      for cell2, j: cells {
        if i == j continue;

        num2 = string_to_int(cell2);

        if num > num2 {
          if num % num2 == 0 {
              break cell2;
              answer += num / num2;
          }
        } else {
          if num2 % num == 0 {
              answer += num2 / num;
              break cell2;
          }
        }
      }
    }
  }
  print("Answer: %\n", answer);
}















