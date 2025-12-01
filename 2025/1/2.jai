#import "Basic";
#import "String";
#import "File";
#import "Math";

main :: () {
  file := read_entire_file("input.dat");

  initial :: 50;

  ins := split(file, "\n");
  curr := initial;
  dist := 0;
  answer := 0;

  num_positions := 100;

  for ins {
    if it == "" {
      continue;
    }

    print("Curr %", curr);

    dist = string_to_int(slice(it, 1, it.count - 1));

    if (dist > num_positions - 1) {
      answer += cast(int)dist / num_positions;
    }

    dist = dist % num_positions;

    if it[0] == #char "L" {
      dist = -dist;
    } 

    if (curr + dist == 0 && curr != 0) {
      answer +=1;
    }

    curr += dist;


    if curr < 0 {
      curr = num_positions + curr;
      answer += 1;
    } else if curr > 99 {
      curr = curr - num_positions;
      answer += 1;
    }

    print(" -> % = ; count= % ; Dial position: %\n", it, answer, curr);
  }

  print("Answer %\n", answer);
}
