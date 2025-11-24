#import "Basic";
#import "String";
#import "File";

main :: () {
  file := read_entire_file("input.dat");

  answer := 0;
  num := 0;
  next := 0;
  value := "";
  looped_index := 0;

  print("\n");
  print("%\n", file);

  for 0..file.count - 1 {
    num = string_to_int(slice(file, it, 1));

    // (file.count - 1) this was the part I was missing, it's fine to 
    // add half the total list, but you have to mod by the actual length, file.count -1
    looped_index = (it + file.count / 2) % (file.count - 1);
    value = slice(file, looped_index, 1);

    print("looped_index:%, \n", looped_index, value);

    next = string_to_int(value);
    if num == next {
      print("Match %\n", num);
      answer += num;
    }

  }

  print("Answer %\n", answer);
}
