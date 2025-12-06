#import "Basic";
#import "File";
#import "String";

main :: () {
  file := read_entire_file("input.dat");
  lines := split(trim(file), "\n");

  char :u8;
  char = 32;

  rows :[..][..]int;
  signs:[..]string;
  for lines {
    if it_index == lines.count - 1 {
      t_row := split(it, char);
      row:[..]string;
      for r:t_row {
        if r == "" continue;
        array_add(*signs, r);
      }
      break;
    }
    t_row := split(it, char);
    row:[..]int;
    for r:t_row {
      if r == "" continue;
      array_add(*row, string_to_int(r));
    }
    array_add(*rows, row);
  }

  sign :string;
  answer := 0;
  res:= 0;
  for column, col_index:rows[0] {
    sign = signs[col_index];
    res = ifx sign == "*" then 1 else 0;
    for rows {
      value := rows[it_index][col_index];

      if sign == "+" {
        res += value;
      }
      if sign == "*" {
        res *= value;
      }
    }

    answer += res;
  }

  print("Answer: %\n", answer);
}
